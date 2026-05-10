<h2 id="presentations" class="pub-section-heading">Presentations & Talks</h2>

<div class="publications">
<ol class="bibliography">

{% assign pres_per_page = 3 %}
{% assign pres_items = site.data.presentations.main %}
{% assign pres_total = pres_items | size %}

{% for item in pres_items %}
<li data-pres-index="{{ forloop.index }}">
<div class="pres-item">

  <div>
    <div class="title">{% if item.link %}<a href="{{ item.link }}" target="_blank">{{ item.title }}</a>{% else %}<span class="pres-title-plain">{{ item.title }}</span>{% endif %}</div>
    <div class="author">{% include author-highlight.html authors=item.authors %}</div>
    <div class="periodical"><em>{% if item.venue_url %}<a href="{{ item.venue_url }}" target="_blank">{{ item.venue }}</a>{% else %}{{ item.venue }}{% endif %}</em>{% if item.location %} &middot; {{ item.location }}{% endif %}{% if item.date %} &middot; {{ item.date }}{% endif %}</div>
    <div class="links pub-links">
      {% if item.poster_url %}
      <a href="{{ item.poster_url }}" class="btn btn-sm z-depth-0" role="button" target="_blank">POSTER</a>
      {% endif %}
      {% if item.pdf %}
      <a href="{{ item.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank">PDF</a>
      {% endif %}
    </div>
  </div>

</div>
</li>
{% endfor %}

</ol>

{% if pres_total > pres_per_page %}
<div class="pub-pagination" id="pres-pagination"></div>
{% endif %}
</div>

{% if pres_total > pres_per_page %}
<script>
(function() {
  var perPage = {{ pres_per_page }};
  var total = {{ pres_total }};
  var totalPages = Math.ceil(total / perPage);
  var currentPage = 1;

  function showPage(page) {
    currentPage = page;
    var items = document.querySelectorAll('[data-pres-index]');
    items.forEach(function(el) {
      var idx = parseInt(el.getAttribute('data-pres-index'));
      var inPage = idx > (page - 1) * perPage && idx <= page * perPage;
      el.style.display = inPage ? '' : 'none';
    });
    renderPagination();
  }

  function renderPagination() {
    var container = document.getElementById('pres-pagination');
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
    document.getElementById('pres-pagination').style.display = 'none';
  }
  showPage(1);
})();
</script>
{% endif %}
