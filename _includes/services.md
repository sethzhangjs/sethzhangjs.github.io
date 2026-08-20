## Services

<ul class="honors-list">
{% for item in site.data.services.main %}
  <li>
    <b>{{ item.role }}</b>{% if item.venue %} &nbsp;·&nbsp; {{ item.venue }}{% endif %}
    {% if item.detail %}<br><span class="honors-detail">{{ item.detail }}</span>{% endif %}
  </li>
{% endfor %}
</ul>
