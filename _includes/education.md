## Education

<table class="entry-table">
{% for item in site.data.education.main %}
{% include entry-card.html item=item type="education" %}
{% endfor %}
</table>
