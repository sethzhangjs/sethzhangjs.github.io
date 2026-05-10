## Honors & Awards

<ul class="honors-list">
{% for item in site.data.honors.main %}
  <li>
    <b>{{ item.title }}</b> &nbsp;·&nbsp; {{ item.org }}, {{ item.year }}
    {% if item.detail %}<br><span class="honors-detail">{{ item.detail }}</span>{% endif %}
  </li>
{% endfor %}
</ul>
