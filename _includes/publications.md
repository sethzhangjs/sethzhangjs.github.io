<h2 id="publications" style="margin: 2px 0px -15px;">Publications</h2>

<div class="publications">
<ol class="bibliography">

{% for link in site.data.publications.main %}
<li>
<div style="display:flex; align-items:flex-start; margin-bottom:1.5rem;">

  <!-- Image box: strictly fixed size -->
  <div style="width:200px; min-width:200px; height:130px; overflow:hidden; position:relative; margin-right:16px; border-radius:4px; border: 1px solid rgba(0,0,0,0.05);">
    {% if link.conference_short %}
    <abbr class="badge" style="position:absolute; top:6px; left:6px; z-index:1; background-color:#002D72; color:#fff;">{{ link.conference_short }}</abbr>
    {% endif %}
    {% if link.image %}
    <img src="{{ link.image }}" style="width:200px; height:130px; object-fit:contain; display:block;">
    {% endif %}
  </div>

  <!-- Text -->
  <div style="flex:1; min-width:0;">
    <div class="title">{% if link.doi %}<a href="{{ link.doi }}" target="_blank" rel="noopener">{{ link.title }}</a>{% else %}{{ link.title }}{% endif %}</div>
    <div class="author">{{ link.authors | replace: "Jiashuo Zhang", "<strong style='font-weight:550;'>Jiashuo Zhang</strong>" }}</div>
    <div class="periodical"><em>{{ link.conference }}</em></div>
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
</div>
