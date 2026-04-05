<h2 id="publications" style="margin: 2px 0px -15px;"><a href="https://scholar.google.com/citations?user=ao8Tf0gAAAAJ&hl=en" target="_blank" rel="noopener" style="color:inherit; text-decoration:none;">Publications</a></h2>

<div class="publications">
<ol class="bibliography">

{% assign per_page = 5 %}
{% assign pub_items = site.data.publications.main %}
{% assign pub_total = pub_items | size %}

{% for link in pub_items %}
<li data-pub-index="{{ forloop.index }}">
<div style="display:flex; align-items:flex-start; margin-bottom:1.5rem;">

  <!-- Image box: strictly fixed size -->
  <div style="width:200px; min-width:200px; height:130px; overflow:hidden; position:relative; margin-right:16px; box-shadow: 0 0 0 1px rgba(0,0,0,0.04), 2px 3px 8px rgba(0,0,0,0.14); transition:transform 0.2s ease, box-shadow 0.2s ease;" onmouseover="this.style.transform='scale(1.06)';this.style.boxShadow='0 0 0 1px rgba(0,0,0,0.06), 4px 6px 16px rgba(0,0,0,0.22)'" onmouseout="this.style.transform='scale(1)';this.style.boxShadow='0 0 0 1px rgba(0,0,0,0.04), 2px 3px 8px rgba(0,0,0,0.14)'">
    {% if link.conference_short %}
    <abbr class="badge" style="position:absolute; top:6px; left:6px; z-index:1; background-color:#002D72; color:#fff;">{{ link.conference_short }}</abbr>
    {% endif %}
    {% if link.image %}
    <img src="{{ link.image }}" style="width:200px; height:130px; object-fit:contain; display:block; cursor:zoom-in;" onclick="openLightbox(this.src)">
    {% endif %}
  </div>

  <!-- Text -->
  <div style="flex:1; min-width:0;">
    <div class="title">{% if link.doi %}<a href="{{ link.doi }}" target="_blank" rel="noopener">{{ link.title }}</a>{% else %}{{ link.title }}{% endif %}</div>
    <div class="author">{{ link.authors | replace: "Jiashuo Zhang", "<strong style='font-weight:550;'>Jiashuo Zhang</strong>" }}</div>
    <div class="periodical"><em>{{ link.conference | split: " · " | first }}</em>{% assign _year = link.conference | split: " · " | last %}{% if _year != link.conference %} · {{ _year }}{% endif %}</div>
    <div class="links" style="margin-top:4px;">
      {% if link.pdf %}
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">PDF</a>
      {% endif %}
      {% if link.code %}
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Code</a>
      {% endif %}
      {% if link.page %}
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Project Page</a>
      {% endif %}
      {% if link.bibtex %}
      <a href="{{ link.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">BibTex</a>
      {% endif %}
      {% if link.notes %}
      <strong><i style="color:#e74d3c">{{ link.notes }}</i></strong>
      {% endif %}
    </div>
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

    // Prev button
    var prev = document.createElement('button');
    prev.className = 'pub-page-btn';
    prev.textContent = '‹';
    prev.disabled = currentPage === 1;
    prev.onclick = function() { showPage(currentPage - 1); };
    container.appendChild(prev);

    // Page number buttons
    for (var i = 1; i <= totalPages; i++) {
      (function(p) {
        var btn = document.createElement('button');
        btn.className = 'pub-page-btn' + (p === currentPage ? ' pub-page-active' : '');
        btn.textContent = p;
        btn.onclick = function() { showPage(p); };
        container.appendChild(btn);
      })(i);
    }

    // Next button
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
