---
title: "SPIN Lab - Research"
layout: textlay
excerpt: "SPIN -- Research"
sitemap: false
permalink: /research/
---

<h1>{% include t.html k="nav_research" %}</h1>

<div class="lead-row">
<img class="lead-img" src="{{ site.url }}{{ site.baseurl }}/images/respic/signal_data_AI.png" alt="Signals, data and AI" />
<p>{% include t.html k="research_intro" %}</p>
</div>

<div class="theme-nav" markdown="0">
{% for t in site.data.research %}<a href="#{{ t.id }}">{% include bi.html en=t.title hi=t.title_hi %}</a>{% endfor %}
</div>

{% for t in site.data.research %}
<div class="theme-card" id="{{ t.id }}" markdown="0">
  <div class="theme-img"><img src="{{ site.url }}{{ site.baseurl }}/images/{{ t.image }}" alt="{{ t.title }}" loading="lazy" /></div>
  <div class="theme-text">
    <h3>{% include bi.html en=t.title hi=t.title_hi %}</h3>
    {% if t.short_hi %}<p class="theme-lead-hi" data-l="hi" lang="hi">{{ t.short_hi }}</p>{% endif %}
    {{ t.body | markdownify }}
    <div class="tags">{% for k in t.keywords %}<span>{{ k }}</span>{% endfor %}</div>
    {% if t.refs.size > 0 %}
    <div class="refs"><b>{% include t.html k="key_papers" %}</b>
      <ul>{% for r in t.refs %}<li>{% if r.url %}<a href="{{ r.url }}" target="_blank" rel="noopener">{{ r.title }}</a>{% else %}{{ r.title }}{% endif %}</li>{% endfor %}</ul>
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}

<h2>{% include t.html k="funding" %}</h2>

<div class="funding-list" markdown="0">
{% for f in site.data.funding %}
  <div class="funding">
    <span class="news-date">{{ f.years }}</span>
    <b>{{ f.title }}</b>
    <p>{{ f.agency }} &middot; {{ f.role }}</p>
  </div>
{% endfor %}
</div>
