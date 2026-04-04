## News

<div class="news-timeline">
  {% assign news_items = site.data.news.main %}
  {% assign total = news_items | size %}

  {% for item in news_items %}
  <div class="news-item{% if forloop.index > 4 %} news-hidden{% endif %}">
    <div class="news-dot{% if item.detail %} news-dot-expandable{% endif %}"></div>
    <div class="news-content{% if item.detail %} news-has-detail{% endif %}">
      <span class="news-date">{{ item.date }}</span>
      <span class="news-short">{{ item.short }}</span>
      {% if item.detail %}
      <div class="news-detail">{{ item.detail }}</div>
      {% endif %}
    </div>
  </div>
  {% endfor %}

  {% if total > 4 %}
  {% assign remaining = total | minus: 4 %}
  <div class="news-more-node" id="news-more-node" onclick="toggleNews(this)" title="Show more">
    <span class="news-more-label" id="news-more-label">+</span>
  </div>
  {% endif %}
</div>

{% if site.data.news.main.size > 4 %}
<script>
function toggleNews(node) {
  var hidden = document.querySelectorAll('.news-hidden');
  var expanded = node.getAttribute('data-expanded') === 'true';
  var label = document.getElementById('news-more-label');
  hidden.forEach(function(el) {
    el.style.display = expanded ? 'none' : 'block';
  });
  node.setAttribute('data-expanded', expanded ? 'false' : 'true');
  label.textContent = expanded ? '+' : '−';
}
document.querySelectorAll('.news-hidden').forEach(function(el){ el.style.display='none'; });
</script>
{% endif %}
