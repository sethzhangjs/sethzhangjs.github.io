<h2 id="publications" style="margin: 2px 0px -15px;"><a href="https://scholar.google.com/citations?user=ao8Tf0gAAAAJ&hl=en" target="_blank" rel="noopener" style="color:inherit; text-decoration:none;">Publications</a></h2>

<div class="publications">
<ol class="bibliography">

{% for link in site.data.publications.main %}
<li>
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
</div>
