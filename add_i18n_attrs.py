#!/usr/bin/env python3
"""Add data-i18n attributes to all text elements in SNOWL HTML pages."""

WD = "/Users/carson/ai-workspace/snowl-w/"

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ============================================================
# about.html
# ============================================================
content = read(WD + "about.html")

# navbar nav links
content = content.replace('<a href="index.html">Home</a>', '<a href="index.html" data-i18n="nav_home">Home</a>')
content = content.replace('<a href="products.html" class="dropdown-trigger">Products <span class="dropdown-arrow">▼</span></a>', '<a href="products.html" class="dropdown-trigger" data-i18n="nav_products">Products <span class="dropdown-arrow">▼</span></a>')
content = content.replace('<a href="about.html" class="active">About</a>', '<a href="about.html" class="active" data-i18n="nav_about">About</a>')
content = content.replace('<a href="news.html">News</a>', '<a href="news.html" data-i18n="nav_news">News</a>')
content = content.replace('<a href="videos.html">Videos</a>', '<a href="videos.html" data-i18n="nav_videos">Videos</a>')
content = content.replace('<a href="contact.html">Contact</a>', '<a href="contact.html" data-i18n="nav_contact">Contact</a>')

# mobile menu links
content = content.replace('<a href="index.html">Home</a><a href="products.html">Products</a><a href="about.html">About</a><a href="news.html">News</a><a href="videos.html">Videos</a><a href="contact.html">Contact</a>',
    '<a href="index.html" data-i18n="nav_home">Home</a><a href="products.html" data-i18n="nav_products">Products</a><a href="about.html" data-i18n="nav_about">About</a><a href="news.html" data-i18n="nav_news">News</a><a href="videos.html" data-i18n="nav_videos">Videos</a><a href="contact.html" data-i18n="nav_contact">Contact</a>')

# hero h1 - split: "30+ Years of<br><span>Marine Excellence</span>"
content = content.replace(
    '<h1>30+ Years of<br><span>Marine Excellence</span></h1>',
    '<h1 data-i18n="about_hero_title">30+ Years of<br><span data-i18n="about_hero_title2">Marine Excellence</span></h1>'
)
# hero desc
content = content.replace(
    '<p class="hero-desc">Founded in 1995, SNOWL Hong Kong Limited has grown into a globally trusted name in marine hardware — serving boat builders and yacht manufacturers across Europe and America.</p>',
    '<p class="hero-desc" data-i18n="about_hero_desc">Founded in 1995, SNOWL Hong Kong Limited has grown into a globally trusted name in marine hardware — serving boat builders and yacht manufacturers across Europe and America.</p>'
)

# story section h2 "Founded in 1995"
content = content.replace(
    '<h2 style="font-size:var(--text-3xl);font-weight:900;color:var(--c-primary);margin-bottom:var(--sp-3)">Founded in 1995</h2>',
    '<h2 style="font-size:var(--text-3xl);font-weight:900;color:var(--c-primary);margin-bottom:var(--sp-3)" data-i18n="about_story_title">Founded in 1995</h2>'
)
# story p1 (Greek mythology)
content = content.replace(
    '<p style="color:var(--c-muted);margin-bottom:var(--sp-2);line-height:1.8">In Greek mythology, the owl was the archetype of the goddess Athena — a symbol of wisdom and navigation. SNOWL Hong Kong Limited chose the owl as its trademark, representing the crystallization of human wisdom in every product.</p>',
    '<p style="color:var(--c-muted);margin-bottom:var(--sp-2);line-height:1.8" data-i18n="about_story_p1">In Greek mythology, the owl was the archetype of the goddess Athena — a symbol of wisdom and navigation. SNOWL Hong Kong Limited chose the owl as its trademark, representing the crystallization of human wisdom in every product.</p>'
)
# story p2 (OWOZ specialize)
content = content.replace(
    '<p style="color:var(--c-muted);line-height:1.8">We specialize in OWOZ series marine fasteners, deck hardware, and maritime accessories. Headquartered in Hong Kong with production facilities in Guangdong, China, our products are trusted by boat manufacturers, yacht builders, and maritime suppliers worldwide.</p>',
    '<p style="color:var(--c-muted);line-height:1.8" data-i18n="about_story_p2">We specialize in OWOZ series marine fasteners, deck hardware, and maritime accessories. Headquartered in Hong Kong with production facilities in Guangdong, China, our products are trusted by boat manufacturers, yacht builders, and maritime suppliers worldwide.</p>'
)

# advantages section header
content = content.replace(
    '<h2 class="section-title">Our Competitive Advantages</h2>',
    '<h2 class="section-title" data-i18n="about_why_title">Our Competitive Advantages</h2>'
)
# advantage cards
content = content.replace('<h3>Marine-Grade</h3><p>Every product tested for salt water, UV, and harsh marine conditions.</p>',
    '<h3 data-i18n="adv_quality_title">Marine-Grade</h3><p data-i18n="adv_quality_desc">Every product tested for salt water, UV, and harsh marine conditions.</p>')
content = content.replace('<h3>80+ Patents</h3><p>Continuous innovation with proprietary OWOZ technology.</p>',
    '<h3 data-i18n="adv_patent_title">80+ Patents</h3><p data-i18n="adv_patent_desc">Continuous innovation with proprietary OWOZ technology.</p>')
content = content.replace('<h3>Global Shipping</h3><p>Worldwide delivery to ports across Europe and America.</p>',
    '<h3 data-i18n="adv_delivery_title">Global Shipping</h3><p data-i18n="adv_delivery_desc">Worldwide delivery to ports across Europe and America.</p>')
content = content.replace('<h3>24/7 Support</h3><p>Dedicated team for product selection and technical support.</p>',
    '<h3 data-i18n="adv_support_title">24/7 Support</h3><p data-i18n="adv_support_desc">Dedicated team for product selection and technical support.</p>')

# facilities section header h2 "Our Facilities"
content = content.replace(
    '<h2 class="section-title">Our Facilities</h2>',
    '<h2 class="section-title" data-i18n="about_facility_header">Our Facilities</h2>'
)
# facilities area tag
content = content.replace(
    '<div class="section-tag" style="text-align:left">20,000 m²</div>',
    '<div class="section-tag" style="text-align:left" data-i18n="about_facility_area">20,000 m²</div>'
)
# facilities h2 "State-of-the-Art Manufacturing"
content = content.replace(
    '<h2 style="font-size:var(--text-3xl);font-weight:900;color:var(--c-primary);margin-bottom:var(--sp-3)">State-of-the-Art Manufacturing</h2>',
    '<h2 style="font-size:var(--text-3xl);font-weight:900;color:var(--c-primary);margin-bottom:var(--sp-3)" data-i18n="about_facility_title">State-of-the-Art Manufacturing</h2>'
)
# facilities p1 (modern production facility)
content = content.replace(
    '<p style="color:var(--c-muted);margin-bottom:var(--sp-2);line-height:1.8">Our modern production facility in Foshan, Guangdong spans over 20,000 square meters with automated manufacturing lines, rigorous quality control labs, and professional R&D centers.</p>',
    '<p style="color:var(--c-muted);margin-bottom:var(--sp-2);line-height:1.8" data-i18n="about_facility_desc1">Our modern production facility in Foshan, Guangdong spans over 20,000 square meters with automated manufacturing lines, rigorous quality control labs, and professional R&D centers.</p>'
)
# facilities p2 (every product)
content = content.replace(
    '<p style="color:var(--c-muted);line-height:1.8">Every product undergoes multiple quality checks from raw material inspection to final packaging, ensuring that every fastener that leaves our facility meets the highest international standards.</p>',
    '<p style="color:var(--c-muted);line-height:1.8" data-i18n="about_facility_desc2">Every product undergoes multiple quality checks from raw material inspection to final packaging, ensuring that every fastener that leaves our facility meets the highest international standards.</p>'
)

# contact section
content = content.replace('<h2 class="section-title">Ready to Partner?</h2>',
    '<h2 class="section-title" data-i18n="about_quick_title">Ready to Partner?</h2>')
content = content.replace('<p class="section-desc">Whether you\'re a boat manufacturer, yacht builder, or maritime supplier, we\'d love to hear from you.</p>',
    '<p class="section-desc" data-i18n="about_quick_desc">Whether you\'re a boat manufacturer, yacht builder, or maritime supplier, we\'d love to hear from you.</p>')
content = content.replace('<a href="contact.html" class="btn btn-primary" style="display:inline-flex;margin:0 auto">Get in Touch →</a>',
    '<a href="contact.html" class="btn btn-primary" style="display:inline-flex;margin:0 auto" data-i18n="about_quick_btn">Get in Touch →</a>')

# footer brand p
content = content.replace(
    '<p>SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>',
    '<p data-i18n="footer_brand_desc">SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>'
)

write(WD + "about.html", content)
print("about.html data-i18n done")

# ============================================================
# contact.html
# ============================================================
content = read(WD + "contact.html")

# navbar
content = content.replace('<a href="index.html">Home</a>', '<a href="index.html" data-i18n="nav_home">Home</a>')
content = content.replace('<a href="products.html" class="dropdown-trigger">Products <span class="dropdown-arrow">▼</span></a>', '<a href="products.html" class="dropdown-trigger" data-i18n="nav_products">Products <span class="dropdown-arrow">▼</span></a>')
content = content.replace('<a href="about.html">About</a>', '<a href="about.html" data-i18n="nav_about">About</a>')
content = content.replace('<a href="news.html" class="active">News</a>', '<a href="news.html" class="active" data-i18n="nav_news">News</a>')
content = content.replace('<a href="videos.html">Videos</a>', '<a href="videos.html" data-i18n="nav_videos">Videos</a>')
content = content.replace('<a href="contact.html">Contact</a>', '<a href="contact.html" data-i18n="nav_contact">Contact</a>')

# mobile menu
content = content.replace('<a href="index.html">Home</a><a href="products.html">Products</a><a href="about.html">About</a><a href="news.html">News</a><a href="videos.html">Videos</a><a href="contact.html">Contact</a>',
    '<a href="index.html" data-i18n="nav_home">Home</a><a href="products.html" data-i18n="nav_products">Products</a><a href="about.html" data-i18n="nav_about">About</a><a href="news.html" data-i18n="nav_news">News</a><a href="videos.html" data-i18n="nav_videos">Videos</a><a href="contact.html" data-i18n="nav_contact">Contact</a>')

# hero
content = content.replace('<h1>Contact<br><span>SNOWL</span></h1>',
    '<h1 data-i18n="contact_page_title">Contact<br><span>SNOWL</span></h1>')
content = content.replace('<p class="hero-desc">Whether you need a custom marine solution or standard product — we\'re here to help. Fill out the form or reach us directly.</p>',
    '<p class="hero-desc" data-i18n="contact_hero_desc">Whether you need a custom marine solution or standard product — we\'re here to help. Fill out the form or reach us directly.</p>')

# contact info section
content = content.replace('<div class="section-tag" style="text-align:left">Contact Info</div>',
    '<div class="section-tag" style="text-align:left" data-i18n="contact_info_tag">Contact Info</div>')
content = content.replace('<h2 style="font-size:var(--text-3xl);font-weight:900;color:var(--c-primary);margin-bottom:var(--sp-3)">Let\'s Talk</h2>',
    '<h2 style="font-size:var(--text-3xl);font-weight:900;color:var(--c-primary);margin-bottom:var(--sp-3)" data-i18n="contact_info_title">Let\'s Talk</h2>')

# contact labels
content = content.replace('<div class="label">Address</div>',
    '<div class="label" data-i18n="addr_label">Address</div>')
content = content.replace('<div class="value">Aoying Business Center 2414, Xinan Street, Sanshui District, Foshan City, Guangdong, China</div>',
    '<div class="value" data-i18n="contact_addr">Aoying Business Center 2414, Xinan Street, Sanshui District, Foshan City, Guangdong, China</div>')
content = content.replace('<div class="label">Email</div>',
    '<div class="label" data-i18n="email_label">Email</div>')
content = content.replace('<div class="value">owoz@snowl.top</div>',
    '<div class="value" data-i18n="email_value">owoz@snowl.top</div>')
content = content.replace('<div class="label">Phone</div>',
    '<div class="label" data-i18n="phone_label">Phone</div>')
content = content.replace('<div class="value">+86-757-87768348</div>',
    '<div class="value" data-i18n="phone_value">+86-757-87768348</div>')
content = content.replace('<div class="label">Hours</div>',
    '<div class="label" data-i18n="hours_label">Hours</div>')
content = content.replace('<div class="value">Mon–Sat 9:00–18:00 (UTC+8)</div>',
    '<div class="value" data-i18n="contact_hours">Mon–Sat 9:00–18:00 (UTC+8)</div>')

# form title
content = content.replace('<h3 class="form-title">Send Us a Message</h3>',
    '<h3 class="form-title" data-i18n="form_title">Send Us a Message</h3>')
# form labels
content = content.replace('<label>Your Name</label>',
    '<label data-i18n="form_name">Your Name</label>')
content = content.replace('<label>Email Address</label>',
    '<label data-i18n="form_email">Email Address</label>')
content = content.replace('<label>Company Name</label>',
    '<label data-i18n="form_company">Company Name</label>')
content = content.replace('<label>Country</label>',
    '<label data-i18n="form_country">Country</label>')
content = content.replace('<label>Product Interest</label>',
    '<label data-i18n="form_product">Product Interest</label>')
content = content.replace('<label>Your Message</label>',
    '<label data-i18n="form_message">Your Message</label>')
# select placeholder
content = content.replace('<option value="">Select a product</option>',
    '<option value="" data-i18n="form_select">Select a product</option>')
# textarea placeholder
content = content.replace('<textarea name="message" rows="4" placeholder="Tell us about your boat model, requirements, quantity..."></textarea>',
    '<textarea name="message" rows="4" data-i18n-placeholder="form_msg_plh" placeholder="Tell us about your boat model, requirements, quantity..."></textarea>')
# submit button
content = content.replace('<button type="submit" class="btn btn-primary form-submit">Send Inquiry</button>',
    '<button type="submit" class="btn btn-primary form-submit" data-i18n="form_submit">Send Inquiry</button>')
# success message
content = content.replace('<div class="success-message" id="formSuccess">Thank you! We\'ll respond within 24 hours.</div>',
    '<div class="success-message" id="formSuccess" data-i18n="form_success">Thank you! We\'ll respond within 24 hours.</div>')

# footer brand p
content = content.replace(
    '<p>SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>',
    '<p data-i18n="footer_brand_desc">SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>'
)

write(WD + "contact.html", content)
print("contact.html data-i18n done")

# ============================================================
# products.html
# ============================================================
content = read(WD + "products.html")

# navbar
content = content.replace('<a href="index.html">Home</a>', '<a href="index.html" data-i18n="nav_home">Home</a>')
content = content.replace('<a href="products.html" class="dropdown-trigger active">Products <span class="dropdown-arrow">▼</span></a>',
    '<a href="products.html" class="dropdown-trigger active" data-i18n="nav_products">Products <span class="dropdown-arrow">▼</span></a>')
content = content.replace('<a href="about.html">About</a>', '<a href="about.html" data-i18n="nav_about">About</a>')
content = content.replace('<a href="news.html">News</a>', '<a href="news.html" data-i18n="nav_news">News</a>')
content = content.replace('<a href="videos.html">Videos</a>', '<a href="videos.html" data-i18n="nav_videos">Videos</a>')
content = content.replace('<a href="contact.html">Contact</a>', '<a href="contact.html" data-i18n="nav_contact">Contact</a>')

# mobile menu
content = content.replace('<a href="index.html">Home</a>\n  <a href="products.html">Products</a>\n  <a href="about.html">About</a>\n  <a href="news.html">News</a>\n  <a href="videos.html">Videos</a>\n  <a href="contact.html">Contact</a>',
    '<a href="index.html" data-i18n="nav_home">Home</a>\n  <a href="products.html" data-i18n="nav_products">Products</a>\n  <a href="about.html" data-i18n="nav_about">About</a>\n  <a href="news.html" data-i18n="nav_news">News</a>\n  <a href="videos.html" data-i18n="nav_videos">Videos</a>\n  <a href="contact.html" data-i18n="nav_contact">Contact</a>')

# hero h1
content = content.replace('<h1>Our Products<br><span>Marine-Grade Fastener Solutions</span></h1>',
    '<h1 data-i18n="prod_hero_title">Our Products<br><span data-i18n="prod_hero_title2">Marine-Grade Fastener Solutions</span></h1>')
# hero desc
content = content.replace('<p class="hero-desc">From ocean-rated snap kits to deck hardware — engineered for durability in the harshest marine environments. Over 30 years of precision manufacturing.</p>',
    '<p class="hero-desc" data-i18n="prod_hero_desc">From ocean-rated snap kits to deck hardware — engineered for durability in the harshest marine environments. Over 30 years of precision manufacturing.</p>')
# hero btn
content = content.replace('<a href="contact.html" class="btn btn-primary">Request a Quote</a>',
    '<a href="contact.html" class="btn btn-primary" data-i18n="request_quote">Request a Quote</a>')

# section header
content = content.replace('<h2 class="section-title">All Marine Hardware Categories</h2>',
    '<h2 class="section-title" data-i18n="prod_sec_title">All Marine Hardware Categories</h2>')
content = content.replace('<p class="section-desc">Complete range of precision marine fasteners and hardware for the global yacht and boat industry.</p>',
    '<p class="section-desc" data-i18n="prod_sec_desc">Complete range of precision marine fasteners and hardware for the global yacht and boat industry.</p>')

# product cards - h3 and p
content = content.replace('<h3>OWOZ Fastener</h3><p>All-copper marine snap button bases with silver, chrome, and black chrome finishes.</p>',
    '<h3 data-i18n="prod_owoz_title">OWOZ Fastener</h3><p data-i18n="prod_owoz_desc">All-copper marine snap button bases with silver, chrome, and black chrome finishes.</p>')
content = content.replace('<h3>Snap Fastener</h3><p>Heavy-duty stainless steel snap fasteners for demanding marine canvas applications.</p>',
    '<h3 data-i18n="prod_snap_title">Snap Fastener</h3><p data-i18n="prod_snap_desc">Heavy-duty stainless steel snap fasteners for demanding marine canvas applications.</p>')
content = content.replace('<h3>Turn Button</h3><p>Precision turn buttons for secure and quick-release canvas fastening on vessels.</p>',
    '<h3 data-i18n="prod_turn_title">Turn Button</h3><p data-i18n="prod_turn_desc">Precision turn buttons for secure and quick-release canvas fastening on vessels.</p>')
content = content.replace('<h3>Nylon Button</h3><p>Lightweight nylon buttons for sailboat canvas with zero corrosion performance.</p>',
    '<h3 data-i18n="prod_nylon_title">Nylon Button</h3><p data-i18n="prod_nylon_desc">Lightweight nylon buttons for sailboat canvas with zero corrosion performance.</p>')
content = content.replace('<h3>Installation Tools</h3><p>Professional installation tools and accessories for marine fastener assembly.</p>',
    '<h3 data-i18n="prod_tool_title">Installation Tools</h3><p data-i18n="prod_tool_desc">Professional installation tools and accessories for marine fastener assembly.</p>')
content = content.replace('<h3>Deck Fasteners</h3><p>Marine panel clips for boat decks and cabin interiors. Corrosion-resistant.</p>',
    '<h3 data-i18n="prod_deck_title">Deck Fasteners</h3><p data-i18n="prod_deck_desc">Marine panel clips for boat decks and cabin interiors. Corrosion-resistant.</p>')

# process section
content = content.replace('<h2 class="section-title">Simple 4-Step Process</h2>',
    '<h2 class="section-title" data-i18n="proc_title">Simple 4-Step Process</h2>')
content = content.replace('<p class="section-desc">From inquiry to delivery — we make it seamless for marine suppliers worldwide.</p>',
    '<p class="section-desc" data-i18n="proc_desc">From inquiry to delivery — we make it seamless for marine suppliers worldwide.</p>')
content = content.replace('<h3>Send Inquiry</h3><p>Contact us with your boat model and fastener requirements</p>',
    '<h3 data-i18n="step1">Send Inquiry</h3><p data-i18n="step1d">Contact us with your boat model and fastener requirements</p>')
content = content.replace('<h3>Get Quote</h3><p>We provide competitive pricing within 24 hours</p>',
    '<h3 data-i18n="step2">Get Quote</h3><p data-i18n="step2d">We provide competitive pricing within 24 hours</p>')
content = content.replace('<h3>Sample Test</h3><p>Request samples for quality testing before bulk orders</p>',
    '<h3 data-i18n="step3">Sample Test</h3><p data-i18n="step3d">Request samples for quality testing before bulk orders</p>')
content = content.replace('<h3>Ship Worldwide</h3><p>Fast production and international shipping to your port</p>',
    '<h3 data-i18n="step4">Ship Worldwide</h3><p data-i18n="step4d">Fast production and international shipping to your port</p>')

# CTA section
content = content.replace('<h2 class="section-title">Need a Custom Solution?</h2>',
    '<h2 class="section-title" data-i18n="prod_cta_title">Need a Custom Solution?</h2>')
content = content.replace('<p class="section-desc">We offer OEM and custom manufacturing for boat manufacturers worldwide. Contact us to discuss your requirements.</p>',
    '<p class="section-desc" data-i18n="prod_cta_desc">We offer OEM and custom manufacturing for boat manufacturers worldwide. Contact us to discuss your requirements.</p>')
content = content.replace('<a href="contact.html" class="btn btn-primary" style="display:inline-flex;margin-top:1rem">Contact Us →</a>',
    '<a href="contact.html" class="btn btn-primary" style="display:inline-flex;margin-top:1rem" data-i18n="send_inquiry">Contact Us →</a>')

# footer brand p
content = content.replace(
    '<p>SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>',
    '<p data-i18n="footer_brand_desc">SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>'
)

write(WD + "products.html", content)
print("products.html data-i18n done")

# ============================================================
# news.html
# ============================================================
content = read(WD + "news.html")

# navbar
content = content.replace('<a href="index.html">Home</a>', '<a href="index.html" data-i18n="nav_home">Home</a>')
content = content.replace('<a href="products.html" class="dropdown-trigger">Products <span class="dropdown-arrow">▼</span></a>',
    '<a href="products.html" class="dropdown-trigger" data-i18n="nav_products">Products <span class="dropdown-arrow">▼</span></a>')
content = content.replace('<a href="about.html">About</a>', '<a href="about.html" data-i18n="nav_about">About</a>')
content = content.replace('<a href="news.html" class="active">News</a>', '<a href="news.html" class="active" data-i18n="nav_news">News</a>')
content = content.replace('<a href="videos.html">Videos</a>', '<a href="videos.html" data-i18n="nav_videos">Videos</a>')
content = content.replace('<a href="contact.html">Contact</a>', '<a href="contact.html" data-i18n="nav_contact">Contact</a>')

# mobile menu
content = content.replace('<a href="index.html">Home</a><a href="products.html">Products</a><a href="about.html">About</a><a href="news.html">News</a><a href="videos.html">Videos</a><a href="contact.html">Contact</a>',
    '<a href="index.html" data-i18n="nav_home">Home</a><a href="products.html" data-i18n="nav_products">Products</a><a href="about.html" data-i18n="nav_about">About</a><a href="news.html" data-i18n="nav_news">News</a><a href="videos.html" data-i18n="nav_videos">Videos</a><a href="contact.html" data-i18n="nav_contact">Contact</a>')

# hero h1
content = content.replace('<h1>News &<br><span>Industry Updates</span></h1>',
    '<h1 data-i18n="news_hero_title">News &<br><span data-i18n="news_hero_title2">Industry Updates</span></h1>')
# hero desc
content = content.replace('<p class="hero-desc">Stay informed about SNOWL, marine industry trends, trade shows, and product innovations.</p>',
    '<p class="hero-desc" data-i18n="news_hero_desc">Stay informed about SNOWL, marine industry trends, trade shows, and product innovations.</p>')

# news cards - h3 and p (use sequential keys)
news_titles = [
    ('METSTRADE Amsterdam 2026', 'news_metstrade_title', 'news_metstrade_desc'),
    ('New SS316 Marine Snap Fastener Series Launches', 'news_ss316_title', 'news_ss316_desc'),
    ('Miami International Boat Show 2026 Highlights', 'news_miami_title', 'news_miami_desc'),
    ('Innovation in Marine Hardware: Corrosion Resistance', 'news_corrosion_title', 'news_corrosion_desc'),
    ('SNOWL Expands European Distribution Network', 'news_europe_title', 'news_europe_desc'),
    ('Sustainable Marine Fittings: Industry Trends 2025', 'news_sustainable_title', 'news_sustainable_desc'),
]
news_texts = [
    ('SNOWL showcased its full product range at METSTRADE 2026 in Amsterdam, connecting with over 250 marine industry professionals from across Europe and beyond.', 'news_metstrade'),
    ('We\'re excited to introduce our new SS316 snap fastener series, featuring enhanced corrosion resistance for prolonged saltwater exposure.', 'news_ss316'),
    ('Our team had an outstanding show in Miami, presenting our latest marine hardware innovations to North American boat builders.', 'news_miami'),
    ('A deep dive into the materials science behind our proprietary corrosion-resistant coatings and ocean performance.', 'news_corrosion'),
    ('New distribution partnerships across Northern Europe and the Mediterranean strengthen our global presence.', 'news_europe'),
    ('How the marine hardware industry is evolving toward sustainable materials and eco-friendly manufacturing.', 'news_sustainable'),
]

# News card h3 and p replacements
content = content.replace(
    '<h3>METSTRADE Amsterdam 2026 — Marine Equipment Trade Show</h3><p>SNOWL showcased its full product range at METSTRADE 2026 in Amsterdam, connecting with over 250 marine industry professionals from across Europe and beyond.</p>',
    '<h3 data-i18n="news_metstrade_title">METSTRADE Amsterdam 2026 — Marine Equipment Trade Show</h3><p data-i18n="news_metstrade_desc">SNOWL showcased its full product range at METSTRADE 2026 in Amsterdam, connecting with over 250 marine industry professionals from across Europe and beyond.</p>'
)
content = content.replace(
    '<h3>New SS316 Marine Snap Fastener Series Launches</h3><p>We\'re excited to introduce our new SS316 snap fastener series, featuring enhanced corrosion resistance for prolonged saltwater exposure.</p>',
    '<h3 data-i18n="news_ss316_title">New SS316 Marine Snap Fastener Series Launches</h3><p data-i18n="news_ss316_desc">We\'re excited to introduce our new SS316 snap fastener series, featuring enhanced corrosion resistance for prolonged saltwater exposure.</p>'
)
content = content.replace(
    '<h3>Miami International Boat Show 2026 Highlights</h3><p>Our team had an outstanding show in Miami, presenting our latest marine hardware innovations to North American boat builders.</p>',
    '<h3 data-i18n="news_miami_title">Miami International Boat Show 2026 Highlights</h3><p data-i18n="news_miami_desc">Our team had an outstanding show in Miami, presenting our latest marine hardware innovations to North American boat builders.</p>'
)
content = content.replace(
    '<h3>Innovation in Marine Hardware: Corrosion Resistance</h3><p>A deep dive into the materials science behind our proprietary corrosion-resistant coatings and ocean performance.</p>',
    '<h3 data-i18n="news_corrosion_title">Innovation in Marine Hardware: Corrosion Resistance</h3><p data-i18n="news_corrosion_desc">A deep dive into the materials science behind our proprietary corrosion-resistant coatings and ocean performance.</p>'
)
content = content.replace(
    '<h3>SNOWL Expands European Distribution Network</h3><p>New distribution partnerships across Northern Europe and the Mediterranean strengthen our global presence.</p>',
    '<h3 data-i18n="news_europe_title">SNOWL Expands European Distribution Network</h3><p data-i18n="news_europe_desc">New distribution partnerships across Northern Europe and the Mediterranean strengthen our global presence.</p>'
)
content = content.replace(
    '<h3>Sustainable Marine Fittings: Industry Trends 2025</h3><p>How the marine hardware industry is evolving toward sustainable materials and eco-friendly manufacturing.</p>',
    '<h3 data-i18n="news_sustainable_title">Sustainable Marine Fittings: Industry Trends 2025</h3><p data-i18n="news_sustainable_desc">How the marine hardware industry is evolving toward sustainable materials and eco-friendly manufacturing.</p>'
)

# footer brand p
content = content.replace(
    '<p>SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>',
    '<p data-i18n="footer_brand_desc">SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>'
)

write(WD + "news.html", content)
print("news.html data-i18n done")

# ============================================================
# videos.html
# ============================================================
content = read(WD + "videos.html")

# navbar
content = content.replace('<a href="index.html">Home</a>', '<a href="index.html" data-i18n="nav_home">Home</a>')
content = content.replace('<a href="products.html" class="dropdown-trigger">Products <span class="dropdown-arrow">▼</span></a>',
    '<a href="products.html" class="dropdown-trigger" data-i18n="nav_products">Products <span class="dropdown-arrow">▼</span></a>')
content = content.replace('<a href="about.html">About</a>', '<a href="about.html" data-i18n="nav_about">About</a>')
content = content.replace('<a href="news.html">News</a>', '<a href="news.html" data-i18n="nav_news">News</a>')
content = content.replace('<a href="videos.html" class="active">Videos</a>', '<a href="videos.html" class="active" data-i18n="nav_videos">Videos</a>')
content = content.replace('<a href="contact.html">Contact</a>', '<a href="contact.html" data-i18n="nav_contact">Contact</a>')

# mobile menu
content = content.replace('<a href="index.html">Home</a><a href="products.html">Products</a><a href="about.html">About</a><a href="news.html">News</a><a href="videos.html" class="active">Videos</a><a href="contact.html">Contact</a>',
    '<a href="index.html" data-i18n="nav_home">Home</a><a href="products.html" data-i18n="nav_products">Products</a><a href="about.html" data-i18n="nav_about">About</a><a href="news.html" data-i18n="nav_news">News</a><a href="videos.html" class="active" data-i18n="nav_videos">Videos</a><a href="contact.html" data-i18n="nav_contact">Contact</a>')

# hero
content = content.replace('<h1>Product<br><span>Videos</span></h1>',
    '<h1 data-i18n="vid_hero_title">Product<br><span data-i18n="vid_hero_title2">Videos</span></h1>')
content = content.replace('<p class="hero-desc">Watch our product demonstrations and factory tour footage to learn about SNOWL marine hardware.</p>',
    '<p class="hero-desc" data-i18n="vid_hero_desc">Watch our product demonstrations and factory tour footage to learn about SNOWL marine hardware.</p>')

# section header
content = content.replace('<h2 class="section-title">See SNOWL in Action</h2>',
    '<h2 class="section-title" data-i18n="vid_sec_title">See SNOWL in Action</h2>')

# video cards h3 and p
content = content.replace(
    '<h3>Installation Guide — Hibur &amp; Snap Fastener</h3>\n<p style="font-size:12px;color:var(--c-muted);margin:4px 0 0">Click to watch on YouTube</p>\n<p>Learn the correct installation method for Hibur and Snap Fastener products in marine and outdoor applications.</p>',
    '<h3 data-i18n="vid_hibur_title">Installation Guide — Hibur &amp; Snap Fastener</h3>\n<p style="font-size:12px;color:var(--c-muted);margin:4px 0 0" data-i18n="vid_youtube_note">Click to watch on YouTube</p>\n<p data-i18n="vid_hibur_desc">Learn the correct installation method for Hibur and Snap Fastener products in marine and outdoor applications.</p>'
)
content = content.replace(
    '<h3>Installation Guide — 4000C1 Shock Cord Cover Clip</h3>\n<p>Official installation tutorial for the 4000C1 Shock Cord Cover Clip series. Ideal for marine canvas, bimini tops, and deck enclosure applications.</p>',
    '<h3 data-i18n="vid_4000c1_title">Installation Guide — 4000C1 Shock Cord Cover Clip</h3>\n<p data-i18n="vid_4000c1_desc">Official installation tutorial for the 4000C1 Shock Cord Cover Clip series. Ideal for marine canvas, bimini tops, and deck enclosure applications.</p>'
)
content = content.replace(
    '<h3>Installation Guide — 4000R2 Fastener</h3>\n<p>Official installation tutorial for the 4000R2 marine snap fastener series. Designed for reliable performance in marine canvas and deck hardware applications.</p>',
    '<h3 data-i18n="vid_4000r2_title">Installation Guide — 4000R2 Fastener</h3>\n<p data-i18n="vid_4000r2_desc">Official installation tutorial for the 4000R2 marine snap fastener series. Designed for reliable performance in marine canvas and deck hardware applications.</p>'
)
content = content.replace(
    '<h3>Installation Guide — 4000D8 Fastener</h3>\n<p>Official installation tutorial for the 4000D8 marine snap fastener series. Reliable performance for bimini tops, pontoon rails, and marine canvas installations.</p>',
    '<h3 data-i18n="vid_4000d8_title">Installation Guide — 4000D8 Fastener</h3>\n<p data-i18n="vid_4000d8_desc">Official installation tutorial for the 4000D8 marine snap fastener series. Reliable performance for bimini tops, pontoon rails, and marine canvas installations.</p>'
)
content = content.replace(
    '<h3>Installation Guide — OWOZ Fastener</h3>\n<p>Step-by-step guide for installing OWOZ marine snap fasteners on deck hardware, life vests, and marine canvas.</p>',
    '<h3 data-i18n="vid_owoz_title">Installation Guide — OWOZ Fastener</h3>\n<p data-i18n="vid_owoz_desc">Step-by-step guide for installing OWOZ marine snap fasteners on deck hardware, life vests, and marine canvas.</p>'
)

# footer brand p
content = content.replace(
    '<p>SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>',
    '<p data-i18n="footer_brand_desc">SNOWL Hong Kong Limited — precision marine fastener manufacturer since 1995.</p>'
)

write(WD + "videos.html", content)
print("videos.html data-i18n done")
print("\nAll HTML data-i18n attributes added!")