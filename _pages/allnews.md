---
title: "News"
layout: textlay
excerpt: "SPIN Lab at IIT Guwahati"
sitemap: false
permalink: /allnews.html
---

# News
<div markdown="0">
{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline | markdownify}}</em></p>
{% endfor %}
</div>