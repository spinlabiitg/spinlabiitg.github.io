---
title: "SPIN Lab - Showcase"
layout: textlay
excerpt: "Interactive sites, visualizations and open datasets from SPIN Lab"
sitemap: false
permalink: /showcase/
---

<h1>{% include t.html k="showcase_title" %}</h1>

<p class="page-intro">{% include t.html k="showcase_intro" %}</p>

<div class="showcase-grid" markdown="0">
{% for s in site.data.showcase %}{% include showcase_card.html s=s %}{% endfor %}
</div>

<h2>{% include t.html k="datasets" %}</h2>

<div class="dataset-list" markdown="0">
{% for d in site.data.datasets %}
  <div class="dataset">
    <h4>{{ d.title }}</h4>
    <p>{% include bi.html en=d.blurb hi=d.blurb_hi %}</p>
    <div class="tags">{% for k in d.tags %}<span>{{ k }}</span>{% endfor %}</div>
    <a href="{{ d.url }}" target="_blank" rel="noopener">{% include bi.html en=d.link_text hi=d.link_text_hi %} &rarr;</a>{% if d.data_url %} &nbsp; <a href="{{ d.data_url }}" target="_blank" rel="noopener">{% include t.html k="get_data" %}</a>{% endif %}
  </div>
{% endfor %}
</div>
