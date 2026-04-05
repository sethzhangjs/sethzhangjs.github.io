## News

<div class="news-timeline">
  {% assign default_count = 3 %}
  {% assign news_items = site.data.news.main %}
  {% assign total = news_items | size %}

  {% for item in news_items %}
  <div class="news-item{% if forloop.index > default_count %} news-hidden{% endif %}" data-news-index="{{ forloop.index }}">
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

  {% if total > default_count %}
  <div class="news-more-node" id="news-more-node"
       onclick="toggleNews(this)"
       title="Show more"
       data-stage="0"
       data-default="{{ default_count }}"
       data-total="{{ total }}">
    <span class="news-more-label" id="news-more-label">+</span>
  </div>
  {% endif %}
</div>

{% if total > default_count %}
<script>
(function() {
  document.querySelectorAll('.news-hidden').forEach(function(el) {
    el.style.display = 'none';
  });

  window.toggleNews = function(node) {
    var defaultCount = parseInt(node.getAttribute('data-default'));
    var expandedCount = defaultCount * 2;
    var total = parseInt(node.getAttribute('data-total'));
    var stage = parseInt(node.getAttribute('data-stage'));
    var label = document.getElementById('news-more-label');
    var items = document.querySelectorAll('.news-item');

    if (stage === 0) {
      items.forEach(function(el) {
        var idx = parseInt(el.getAttribute('data-news-index'));
        el.style.display = (idx <= expandedCount) ? '' : 'none';
      });
      if (total <= expandedCount) {
        node.setAttribute('data-stage', '2');
        label.textContent = '−';
      } else {
        node.setAttribute('data-stage', '1');
      }
    } else if (stage === 1) {
      items.forEach(function(el) {
        el.style.display = '';
      });
      node.setAttribute('data-stage', '2');
      label.textContent = '−';
    } else {
      items.forEach(function(el) {
        var idx = parseInt(el.getAttribute('data-news-index'));
        el.style.display = (idx <= defaultCount) ? '' : 'none';
      });
      node.setAttribute('data-stage', '0');
      label.textContent = '+';
    }
  };
})();
</script>
{% endif %}
