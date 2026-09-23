#!/usr/bin/env python3
"""
Fetch TLDR summaries from Semantic Scholar and write them back to publications.yml.

Rules:
- If a paper already has `tldr` WITHOUT `tldr_source`, it's a custom TLDR — skip it.
- If a paper has `tldr_source: semantic_scholar`, re-fetch to refresh it.
- If a paper has no `tldr`, try to fetch one and mark it with `tldr_source: semantic_scholar`.

An existing TLDR is never cleared: if a fetch fails or Semantic Scholar has no
TLDR for the paper, whatever is already in the YAML stays put.

Set SEMANTIC_SCHOLAR_API_KEY to raise the rate limit; without it the anonymous
pool is shared and HTTP 429 is common, so requests are spaced further apart.

Run whenever you add new papers:
    python scripts/fetch_tldr.py
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import yaml  # pip install pyyaml

YAML_PATH = "_data/publications.yml"
API_BASE = "https://api.semanticscholar.org/graph/v1/paper"

API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "").strip()
# Anonymous requests share one small pool, so space them out more.
REQUEST_SPACING = 1.0 if API_KEY else 3.0
MAX_ATTEMPTS = 4
BACKOFF_SECONDS = [2, 5, 15]
RETRY_STATUSES = {429, 500, 502, 503, 504}

# Fetch outcomes. OK and NO_TLDR are final answers from the API; NOT_FOUND means
# the paper is not indexed yet; FAILED means we never got an answer and the
# paper should be retried on a later run.
OK, NO_TLDR, NOT_FOUND, FAILED = "ok", "no_tldr", "not_found", "failed"


def extract_paper_id(doi_url: str) -> str | None:
    if not doi_url:
        return None
    m = re.search(r"arxiv\.org/abs/([^\s/?#]+)", doi_url, re.I)
    if m:
        return f"arXiv:{m.group(1)}"
    m = re.search(r"pubs\.acs\.org/doi/(.+)", doi_url, re.I)
    if m:
        return f"DOI:{m.group(1)}"
    m = re.search(r"doi\.org/(.+)", doi_url, re.I)
    if m:
        return f"DOI:{m.group(1)}"
    return None


def retry_delay(attempt: int, error: urllib.error.HTTPError | None) -> float:
    """Honour Retry-After when the server sends it, else exponential backoff."""
    if error is not None:
        header = error.headers.get("Retry-After") if error.headers else None
        if header:
            try:
                return max(float(header), 1.0)
            except ValueError:
                pass
    return BACKOFF_SECONDS[min(attempt, len(BACKOFF_SECONDS) - 1)]


def fetch_tldr(paper_id: str) -> tuple[str, str | None, str | None]:
    """Return (outcome, tldr_text, semantic_scholar_url).

    Retries transient failures (rate limiting, 5xx, network errors) and reports
    them as FAILED rather than pretending the paper has no TLDR.
    """
    url = f"{API_BASE}/{urllib.parse.quote(paper_id)}?fields=tldr,url"
    request = urllib.request.Request(url)
    if API_KEY:
        request.add_header("x-api-key", API_KEY)

    last_reason = "unknown error"
    for attempt in range(MAX_ATTEMPTS):
        try:
            with urllib.request.urlopen(request, timeout=15) as resp:
                data = json.loads(resp.read())
            tldr = data.get("tldr")
            if tldr and tldr.get("text"):
                return OK, tldr["text"], data.get("url")
            return NO_TLDR, None, data.get("url")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return NOT_FOUND, None, None
            if e.code not in RETRY_STATUSES:
                print(f"  ! HTTP {e.code} (not retryable)")
                return FAILED, None, None
            last_reason = f"HTTP {e.code}"
            error: urllib.error.HTTPError | None = e
        except Exception as e:  # network error, timeout, bad JSON
            last_reason = f"{type(e).__name__}: {e}"
            error = None

        if attempt < MAX_ATTEMPTS - 1:
            delay = retry_delay(attempt, error)
            print(f"  .. {last_reason}, retrying in {delay:g}s "
                  f"({attempt + 2}/{MAX_ATTEMPTS})")
            time.sleep(delay)

    print(f"  ! gave up after {MAX_ATTEMPTS} attempts ({last_reason})")
    return FAILED, None, None


def warn(message: str) -> None:
    """Emit a GitHub Actions annotation when running in CI, else a plain line."""
    prefix = "::warning::" if os.environ.get("GITHUB_ACTIONS") == "true" else "WARNING: "
    print(f"{prefix}{message}")


with open(YAML_PATH, "r") as f:
    original_text = f.read()
data = yaml.safe_load(original_text)

counts = {OK: 0, NO_TLDR: 0, NOT_FOUND: 0, FAILED: 0}
failed_papers: list[str] = []
missing_papers: list[str] = []

if not API_KEY:
    print("No SEMANTIC_SCHOLAR_API_KEY set — using the anonymous rate limit.\n")

for item in data.get("main", []):
    title = item.get("title", "")[:60]

    has_tldr = bool(item.get("tldr"))
    if has_tldr and not item.get("tldr_source"):
        print(f"skip (custom):   {title}")
        continue

    paper_id = extract_paper_id(item.get("doi", ""))
    if not paper_id:
        print(f"skip (no id):    {title}")
        continue

    print(f"fetching:        {title} [{paper_id}]")
    outcome, tldr, ss_url = fetch_tldr(paper_id)
    counts[outcome] += 1

    if outcome == OK:
        item["tldr"] = tldr
        item["tldr_source"] = "semantic_scholar"
        if ss_url:
            item["tldr_url"] = ss_url
        print(f"  -> {tldr[:80]}...")
    elif outcome == NO_TLDR:
        print("  -> indexed, but Semantic Scholar has no TLDR for it")
    elif outcome == NOT_FOUND:
        missing_papers.append(f"{title} [{paper_id}]")
        print("  -> not indexed by Semantic Scholar yet")
    else:
        failed_papers.append(f"{title} [{paper_id}]")
        kept = "existing TLDR kept" if has_tldr else "still has no TLDR"
        print(f"  -> fetch failed, {kept}")

    time.sleep(REQUEST_SPACING)

new_text = yaml.dump(data, allow_unicode=True, sort_keys=False)
if new_text != original_text:
    with open(YAML_PATH, "w") as f:
        f.write(new_text)
    print(f"\nDone — publications.yml updated ({counts[OK]} TLDR(s) written).")
else:
    print("\nNo changes — publications.yml left untouched.")

print(f"summary: {counts[OK]} fetched, {counts[NO_TLDR]} no TLDR upstream, "
      f"{counts[NOT_FOUND]} not indexed, {counts[FAILED]} failed")

for paper in missing_papers:
    print(f"  not indexed yet: {paper}")

if failed_papers:
    warn(f"{len(failed_papers)} paper(s) could not be checked "
         f"(rate limit or network); re-run to retry: "
         f"{'; '.join(failed_papers)}")
    # Exit non-zero only if every attempted fetch failed, which points at a
    # systemic problem rather than one flaky request.
    if counts[OK] == counts[NO_TLDR] == counts[NOT_FOUND] == 0:
        print("every fetch failed — treating this as an error")
        sys.exit(1)
