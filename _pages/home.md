---
title: "SPIN Lab - Home"
layout: homelay
excerpt: "SPIN at IIT Guwahati"
sitemap: false
permalink: /
---

<div data-l="en" markdown="1">
We are a research group exploring **sensory interactions** across modalities: speech and audio, images and video, text, and physiological signals such as breathing and EEG. We want to understand how humans **perceive** the world, and to build **intelligence** that is multimodal, grounded in signals, and humane. We converse in the language of signal processing and machine (deep) learning, and enrich our understanding using any scientific discipline the problem requires us to venture into.
</div>
<div data-l="hi" lang="hi" markdown="1">
हम एक शोध समूह हैं जो विभिन्न माध्यमों में **संवेदी अंतःक्रियाओं** का अध्ययन करता है: वाणी और ऑडियो, चित्र और वीडियो, पाठ (टेक्स्ट), तथा साँस और ईईजी जैसे शारीरिक संकेत। हम समझना चाहते हैं कि मनुष्य दुनिया को कैसे **अनुभव** करते हैं, और ऐसी **बुद्धिमत्ता** बनाना चाहते हैं जो बहु-माध्यमी (मल्टीमोडल) हो, संकेतों पर आधारित हो, और मानवीय हो। हम सिग्नल प्रोसेसिंग और मशीन (डीप) लर्निंग की भाषा में सोचते हैं, और समस्या हमें जिस भी वैज्ञानिक विषय में ले जाए, उसकी मदद से अपनी समझ को समृद्ध करते हैं।
</div>

<h2>{% include t.html k="what_we_do" %}</h2>

<div class="spin-cards" markdown="0">
  <div class="spin-card">
    <div class="spin-letter">S</div>
    <h4>{% include t.html k="sensing" %}</h4>
    <p data-l="en">We are immersed in signals, and our eyes, ears, skin and nose turn them into data for the brain. Understanding how a continuous signal becomes a discrete sequence of samples in the sensory periphery can inspire efficient sampling strategies.</p>
    <p data-l="hi" lang="hi">हम संकेतों से घिरे हैं, और हमारी आँखें, कान, त्वचा और नाक उन्हें मस्तिष्क के लिए डेटा में बदलती हैं। संवेदी तंत्र में एक सतत संकेत कैसे असतत नमूनों में बदलता है, यह समझना कुशल सैंपलिंग विधियों की प्रेरणा बन सकता है।</p>
  </div>
  <div class="spin-card">
    <div class="spin-letter">P</div>
    <h4>{% include t.html k="perception" %}</h4>
    <p data-l="en">The brain turns sensed signals into estimates such as loudness, pitch, timbre and location. Perception is a bit like feature extraction in machine learning, and predicting what humans perceive is a challenging (and rewarding) problem in AI.</p>
    <p data-l="hi" lang="hi">मस्तिष्क संवेदित संकेतों से प्रबलता, तारत्व (पिच), ध्वनि-गुण (टिम्बर) और स्थान जैसे गुणों का अनुमान लगाता है। बोध कुछ हद तक मशीन लर्निंग में फ़ीचर निकालने जैसा है, और मनुष्य क्या अनुभव करेंगे इसका पूर्वानुमान लगाना एआई की एक चुनौतीपूर्ण (और रोचक) समस्या है।</p>
  </div>
  <div class="spin-card">
    <div class="spin-letter">IN</div>
    <h4>{% include t.html k="intelligence" %}</h4>
    <p data-l="en">Perceived attributes feed a mental model of the world: cognition, whose output is behavior. Understanding cognition is critical to designing machines that interact with humans.</p>
    <p data-l="hi" lang="hi">अनुभव किए गए गुण दुनिया का एक मानसिक मॉडल बनाते हैं: यही संज्ञान है, जिसका परिणाम व्यवहार है। मनुष्यों से संवाद करने वाली मशीनें बनाने के लिए संज्ञान को समझना आवश्यक है।</p>
  </div>
</div>

<p data-l="en">Through our work, we aim to unify these three concepts and build solutions. Frankly, this is very interesting work, with lots of open questions.</p>
<p data-l="hi" lang="hi">अपने काम के ज़रिए हम इन तीनों अवधारणाओं को जोड़कर समाधान बनाना चाहते हैं। सच कहें तो यह बेहद रोचक काम है, जिसमें बहुत से अनसुलझे प्रश्न हैं।</p>

<h2>{% include t.html k="modalities" %}</h2>

<div class="modality-strip" markdown="0">
{% for m in site.data.modalities %}
  <div class="modality">
    <span class="modality-icon" aria-hidden="true">{{ m.icon }}</span>
    <b>{% include bi.html en=m.name hi=m.name_hi %}</b>
    <span>{% include bi.html en=m.examples hi=m.examples_hi %}</span>
  </div>
{% endfor %}
</div>

<h2>{% include t.html k="research_themes" %}</h2>

<div class="theme-tiles" markdown="0">
{% for t in site.data.research %}
  <a class="theme-tile" href="{{ site.url }}{{ site.baseurl }}/research/#{{ t.id }}">
    <img src="{{ site.url }}{{ site.baseurl }}/images/{{ t.image }}" alt="" loading="lazy" />
    <b>{% include bi.html en=t.title hi=t.title_hi %}</b>
    <span>{% include bi.html en=t.short hi=t.short_hi %}</span>
  </a>
{% endfor %}
</div>

<h2>{% include t.html k="explore" %}</h2>

<div class="showcase-grid compact" markdown="0">
{% for s in site.data.showcase %}{% if s.home %}{% include showcase_card.html s=s compact=true %}{% endif %}{% endfor %}
</div>
<p><a href="{{ site.url }}{{ site.baseurl }}/showcase/">{% include t.html k="explore_all" %}</a></p>

<p data-l="en">See also our <a href="{{ site.url }}{{ site.baseurl }}/publications/">publications</a>. We are part of the <a href="https://www.iitg.ac.in/dsai/">Mehta Family School of Data Science and AI</a> and the <a href="https://www.iitg.ac.in/clst/index.php">Centre for Linguistic Science and Technology</a>.</p>
<p data-l="hi" lang="hi">हमारे <a href="{{ site.url }}{{ site.baseurl }}/publications/">प्रकाशन</a> भी देखें। हम <a href="https://www.iitg.ac.in/dsai/">मेहता फ़ैमिली स्कूल ऑफ़ डेटा साइंस एंड एआई</a> और <a href="https://www.iitg.ac.in/clst/index.php">भाषाई विज्ञान एवं प्रौद्योगिकी केंद्र (CLST)</a> का हिस्सा हैं।</p>

<div class="join-band say-hey" markdown="0" data-audio="{{ site.url }}{{ site.baseurl }}/audio/welcome_web.wav">
  <div class="hey-viz">
    <canvas class="hey-canvas" role="img" aria-label="Live waveform and spectrogram"></canvas>
    <div class="hey-buttons">
      <button type="button" class="btn btn-primary btn-sm js-mic" aria-pressed="false">&#127908; {% include t.html k="say_hey_btn" %}</button>
      <button type="button" class="btn btn-default btn-sm js-play">&#9654; {% include t.html k="play_hello" %}</button>
    </div>
    <p class="hey-status" aria-live="polite"></p>
    <p class="hey-privacy">{% include t.html k="hey_privacy" %}</p>
  </div>
  <div>
    <h3>{% include t.html k="say_hey" %}</h3>
    <p data-l="en">Does this relate to your interests? Drop an <a href="mailto:neerajs@iitg.ac.in">email</a> to <a href="{{ site.url }}{{ site.baseurl }}/team/">Neeraj</a>. We are happy to learn about the challenges you are tackling and discuss ways to collaborate. Students can <a href="{{ site.url }}{{ site.baseurl }}/vacancies">join the team</a>, and organisations can sponsor the lab.</p>
    <p data-l="hi" lang="hi">क्या यह आपकी रुचि से मेल खाता है? <a href="{{ site.url }}{{ site.baseurl }}/team/">नीरज</a> को <a href="mailto:neerajs@iitg.ac.in">ईमेल</a> भेजें। हम आपकी चुनौतियों के बारे में जानने और साथ काम करने के तरीकों पर बात करने को उत्सुक हैं। विद्यार्थी <a href="{{ site.url }}{{ site.baseurl }}/vacancies">टीम से जुड़ सकते हैं</a>, और संस्थाएँ लैब को प्रायोजित कर सकती हैं।</p>
  </div>
</div>

<p data-l="en">We are located at IIT Guwahati. Our campus is calm and vibrant, bio-diverse, and fondly known in India as (most!) heavenly (see <a href="{{ site.url }}{{ site.baseurl }}/pictures/">Pictures</a>).</p>
<p data-l="hi" lang="hi">हम आईआईटी गुवाहाटी में हैं। हमारा परिसर शांत और जीवंत है, जैव-विविधता से भरपूर है, और भारत में (सबसे!) स्वर्गिक परिसरों में गिना जाता है (<a href="{{ site.url }}{{ site.baseurl }}/pictures/">तस्वीरें</a> देखें)।</p>

<h2>The Curious Case of Sound</h2>

<p data-l="en">A TEDx IIT Guwahati talk by Neeraj (Feb 2023).</p>
<p data-l="hi" lang="hi">नीरज की TEDx आईआईटी गुवाहाटी वार्ता (फ़रवरी 2023), अंग्रेज़ी में।</p>

<div class="embed-responsive embed-responsive-16by9" markdown="0">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/CYMMLLeGrVs?si=WupHSq82_LRLGOI7" title="TEDx talk by Neeraj Sharma" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen loading="lazy"></iframe>
</div>
