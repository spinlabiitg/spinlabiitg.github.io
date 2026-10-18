---
title: "SPIN Lab - Team"
layout: gridlay
excerpt: "SPIN Lab: Team members"
sitemap: false
permalink: /team/
---

<h1>{% include t.html k="team_title" %}</h1>

<p class="callout">{% include t.html k="team_callout" %} <a href="{{ site.url }}{{ site.baseurl }}/vacancies">{% include t.html k="see_openings" %}</a></p>

{% for pi in site.data.team_members %}
<div class="pi-card" markdown="0">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ pi.photo }}" alt="{{ pi.name | strip_html }}" />
  <div>
    <h3>{{ pi.name }}</h3>
    <p class="member-info">{% include bi.html en=pi.info hi=pi.info_hi %}</p>
    <p class="member-links pi-links">
      {% if pi.email %}<a href="mailto:{{ pi.email }}">{% include t.html k="email" %}</a>{% endif %}
      {% if pi.scholar %}<a href="{{ pi.scholar }}" target="_blank" rel="noopener">{% include t.html k="scholar" %}</a>{% endif %}
      {% if pi.website %}<a href="{{ pi.website }}" target="_blank" rel="noopener">{% include t.html k="website" %}</a>{% endif %}
    </p>
    {% if pi.highlights %}<div class="tags pi-roles">{% for h in pi.highlights %}<span>{{ h }}</span>{% endfor %}</div>{% endif %}
    <ul>
    {% for i in (1..5) %}{% assign key = 'education' | append: i %}{% if pi[key] %}<li>{{ pi[key] }}</li>{% endif %}{% endfor %}
    </ul>
  </div>
</div>
{% endfor %}

{% assign groups = "phd|phd_scholars;mtech|masts;btech|bachs" | split: ';' %}
{% for g in groups %}
{% assign parts = g | split: '|' %}
{% assign key = parts[1] %}{% assign people = site.data[key] %}
{% if people.size > 0 %}
<h2>{% assign gk = parts[0] %}{% include t.html k=gk %}</h2>
<div class="member-grid" markdown="0">
{% for m in people %}{% include member_card.html m=m %}{% endfor %}
</div>
{% endif %}
{% endfor %}

<h2>{% include t.html k="former" %}</h2>

<table class="table alumni-table" markdown="0">
  <thead><tr><th>{% include t.html k="col_name" %}</th><th>{% include t.html k="col_role" %}</th><th>{% include t.html k="col_now" %}</th></tr></thead>
  {% assign alumni_groups = "postdocs|alumni_visitors;masters|alumni_msc;bachelors|alumni_bsc" | split: ';' %}
  {% for g in alumni_groups %}
  {% assign parts = g | split: '|' %}
  <tbody>
    <tr class="alumni-group"><td colspan="3">{% assign gk = parts[0] %}{% include t.html k=gk %}</td></tr>
    {% assign key = parts[1] %}{% for m in site.data[key] %}
    <tr><td>{{ m.name }}{% if m.thesis %}<span class="alumni-thesis">{{ m.thesis }}</span>{% endif %}</td><td>{{ m.info }}</td><td>{{ m.work }}</td></tr>
    {% endfor %}
  </tbody>
  {% endfor %}
</table>
