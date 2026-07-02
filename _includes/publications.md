<h2 id="publications" class="pub-section-heading"><a href="https://scholar.google.com/citations?user=ao8Tf0gAAAAJ&hl=en" target="_blank" rel="noopener">Publications & Preprints</a></h2>

<div class="publications">
<ol class="bibliography">

{% assign per_page = 5 %}
{% assign pub_items = site.data.publications.main %}
{% assign pub_total = pub_items | size %}

{% for link in pub_items %}
<li data-pub-index="{{ forloop.index }}">
<div class="pub-item-row">

  <div class="pub-image-box">
    {% if link.venue_short %}
    <abbr class="badge pub-badge">{{ link.venue_short }}</abbr>
    {% endif %}
    {% if link.image %}
    <img src="{{ link.image }}" class="pub-image" onclick="openLightbox(this.src)">
    {% endif %}
  </div>

  <div class="pub-text">
    <div class="title">{% if link.doi %}<a href="{{ link.doi }}" target="_blank" rel="noopener">{{ link.title }}</a>{% else %}{{ link.title }}{% endif %}{% if link.tags %}<span class="pub-tags">{% for tag in link.tags %}{% assign tag_color = site.data.pub_tags[tag] | default: "default" %}<span class="pub-tag pub-tag-{{ tag_color }}">{{ tag }}</span>{% endfor %}</span>{% endif %}</div>
    <div class="author">{% include author-highlight.html authors=link.authors %}</div>
    <div class="periodical"><em>{{ link.venue }}</em>{% if link.year %} · {{ link.year }}{% endif %}</div>
    <div class="links pub-links">
      {% if link.tldr %}
      <a href="javascript:void(0)" class="btn btn-sm z-depth-0 pub-tldr-btn" onclick="toggleTldr(this)">TLDR</a>
      {% endif %}
      {% if link.poster %}
      <a href="{{ link.poster }}" class="btn btn-sm z-depth-0" role="button" target="_blank">POSTER</a>
      {% endif %}
      {% if link.pdf %}
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank">PDF</a>
      {% endif %}
      {% if link.code %}
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank">CODE</a>
      {% endif %}
      {% if link.page %}
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank">Project Page</a>
      {% endif %}
      {% if link.bibtex %}
      <a href="{{ link.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank">BibTex</a>
      {% endif %}
      {% if link.notes %}
      <strong><i class="pub-note">{{ link.notes }}</i></strong>
      {% endif %}
    </div>
    {% if link.tldr %}
    <div class="pub-tldr-body">
      <div class="pub-tldr-content">
        {% if link.tldr_source == "semantic_scholar" %}<div class="pub-tldr-source">{% if link.tldr_url %}<a href="{{ link.tldr_url }}" target="_blank" rel="noopener">Powered by Semantic Scholar <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:9px;"></i></a>{% else %}Powered by Semantic Scholar{% endif %}</div>{% endif %}
        {{ link.tldr }}
      </div>
    </div>
    {% endif %}
  </div>

</div>
</li>
{% endfor %}

</ol>

{% if pub_total > per_page %}
<div class="pub-pagination" id="pub-pagination"></div>
{% endif %}
</div>

{% if pub_total > per_page %}
<script>
(function() {
  var perPage = {{ per_page }};
  var total = {{ pub_total }};
  var totalPages = Math.ceil(total / perPage);
  var currentPage = 1;

  function showPage(page) {
    currentPage = page;
    var items = document.querySelectorAll('[data-pub-index]');
    items.forEach(function(el) {
      var idx = parseInt(el.getAttribute('data-pub-index'));
      var inPage = idx > (page - 1) * perPage && idx <= page * perPage;
      el.style.display = inPage ? '' : 'none';
    });
    renderPagination();
  }

  function renderPagination() {
    var container = document.getElementById('pub-pagination');
    container.innerHTML = '';

    var prev = document.createElement('button');
    prev.className = 'pub-page-btn';
    prev.textContent = '‹';
    prev.disabled = currentPage === 1;
    prev.onclick = function() { showPage(currentPage - 1); };
    container.appendChild(prev);

    for (var i = 1; i <= totalPages; i++) {
      (function(p) {
        var btn = document.createElement('button');
        btn.className = 'pub-page-btn' + (p === currentPage ? ' pub-page-active' : '');
        btn.textContent = p;
        btn.onclick = function() { showPage(p); };
        container.appendChild(btn);
      })(i);
    }

    var next = document.createElement('button');
    next.className = 'pub-page-btn';
    next.textContent = '›';
    next.disabled = currentPage === totalPages;
    next.onclick = function() { showPage(currentPage + 1); };
    container.appendChild(next);
  }

  if (totalPages <= 1) {
    document.getElementById('pub-pagination').style.display = 'none';
  }
  showPage(1);
})();
</script>
{% endif %}

<script>
function toggleTldr(btn) {
  var body = btn.closest('.links').nextElementSibling;
  var isOpen = body.classList.contains('pub-tldr-open');
  body.classList.toggle('pub-tldr-open', !isOpen);
  btn.classList.toggle('pub-tldr-btn-active', !isOpen);
}
</script>
