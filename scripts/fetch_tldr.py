#!/usr/bin/env python3
"""
Fetch TLDR summaries from Semantic Scholar and write them back to publications.yml.

Rules:
- If a paper already has `tldr` WITHOUT `tldr_source`, it's a custom TLDR — skip it.
- If a paper has `tldr_source: semantic_scholar`, re-fetch to refresh it.
- If a paper has no `tldr`, try to fetch one and mark it with `tldr_source: semantic_scholar`.

Run whenever you add new papers:
    python scripts/fetch_tldr.py
"""

import re
import time
import urllib.request
import urllib.error
import urllib.parse
import json
import yaml  # pip install pyyaml

YAML_PATH = "_data/publications.yml"
API_BASE = "https://api.semanticscholar.org/graph/v1/paper"


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


def fetch_tldr(paper_id: str) -> tuple[str | None, str | None]:
    url = f"{API_BASE}/{urllib.parse.quote(paper_id)}?fields=tldr,url"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
            tldr = data.get("tldr")
            return (tldr["text"] if tldr else None), data.get("url")
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} for {paper_id}")
    except Exception as e:
        print(f"  Error for {paper_id}: {e}")
    return None, None


with open(YAML_PATH, "r") as f:
    data = yaml.safe_load(f)

changed = False
for item in data.get("main", []):
    title = item.get("title", "")[:60]

    has_tldr = bool(item.get("tldr"))
    is_custom = has_tldr and not item.get("tldr_source")

    if is_custom:
        print(f"skip (custom):   {title}")
        continue

    paper_id = extract_paper_id(item.get("doi", ""))
    if not paper_id:
        print(f"skip (no id):    {title}")
        continue

    print(f"fetching:        {title} [{paper_id}]")
    tldr, ss_url = fetch_tldr(paper_id)
    if tldr:
        item["tldr"] = tldr
        item["tldr_source"] = "semantic_scholar"
        if ss_url:
            item["tldr_url"] = ss_url
        changed = True
        print(f"  -> {tldr[:80]}...")
    else:
        print(f"  -> no tldr found")
    time.sleep(1.5)

if changed:
    with open(YAML_PATH, "w") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
    print("\nDone — publications.yml updated.")
else:
    print("\nNo changes.")
