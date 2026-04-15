<h2 id="presentations" style="margin: 2px 0px -15px;">Presentations & Talks</h2>

<div class="publications">
<ol class="bibliography">

{% for item in site.data.presentations.main %}
<li>
<div style="margin-bottom:1.5rem;">

  <div>
    <div class="title">{% if item.link %}<a href="{{ item.link }}" target="_blank">{{ item.title }}</a>{% else %}<span style="color:#39c;">{{ item.title }}</span>{% endif %}</div>
    <div class="author">{{ item.authors | replace: "Jiashuo Zhang", "<strong style='font-weight:550;'>Jiashuo Zhang</strong>" }}</div>
    <div class="periodical"><em>{% if item.venue_url %}<a href="{{ item.venue_url }}" target="_blank" style="color:inherit;text-decoration:none;">{{ item.venue }}</a>{% else %}{{ item.venue }}{% endif %}</em>{% if item.location %} &middot; {{ item.location }}{% endif %}{% if item.date %} &middot; {{ item.date }}{% endif %}</div>
    <div class="links" style="margin-top:4px;">
      {% if item.poster_url %}
      <a href="{{ item.poster_url }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">POSTER</a>
      {% endif %}
      {% if item.pdf %}
      <a href="{{ item.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">PDF</a>
      {% endif %}
    </div>
  </div>

</div>
</li>
{% endfor %}

</ol>
</div>
