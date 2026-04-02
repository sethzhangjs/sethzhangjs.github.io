<h2 id="presentations" style="margin: 2px 0px -15px;">Presentations & Talks</h2>

<div class="publications">
<ol class="bibliography">

{% for item in site.data.presentations.main %}
<li>
<div style="margin-bottom:1.5rem;">

  <!-- Text -->
  <div style="flex:1; min-width:0;">
    <div class="title">{% if item.poster_url %}<a href="{{ item.poster_url }}" target="_blank">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}</div>
    <div class="author">{{ item.authors | replace: "Jiashuo Zhang", "<strong style='font-weight:550;'>Jiashuo Zhang</strong>" }}</div>
    <div class="periodical"><em>{{ item.venue }}</em>{% if item.type %} &middot; {{ item.type }}{% endif %}</div>
    <div class="periodical">{{ item.date }}{% if item.location %} · {{ item.location }}{% endif %}</div>
    {% if item.pdf %}
    <div class="links" style="margin-top:4px;">
      <a href="{{ item.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">PDF</a>
    </div>
    {% endif %}
  </div>

</div>
</li>
{% endfor %}

</ol>
</div>
