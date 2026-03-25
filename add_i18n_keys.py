#!/usr/bin/env python3
"""Properly insert new i18n keys into js/i18n.js - section-based approach."""
WD = "/Users/carson/ai-workspace/snowl-w/"
fpath = WD + "js/i18n.js"

with open(fpath, encoding="utf-8") as f:
    raw = f.read()

# Split off the exec code at the end
exec_code_start = raw.find('// Auto-apply i18n update')
assert exec_code_start > 0, "Could not find exec code marker"
i18n_content = raw[:exec_code_start].rstrip()
exec_code = raw[exec_code_start:]

# Split i18n_content into lines
lines = i18n_content.split('\n')

# Find language block boundaries
# Each lang block starts with "  en: {" (indented)
lang_start = {}
lang_end = {}
current_lang = None

for i, line in enumerate(lines):
    stripped = line.strip()
    # Detect start of a language block: "  en: {" or "  'en': {"
    for lang in ["en", "zh", "de", "fr", "ru", "pt", "es"]:
        if stripped == f'{lang}: {{' or stripped == f"'{lang}': {{" or stripped == f'"{lang}": {{':
            lang_start[lang] = i
            current_lang = lang
        # Detect end of block: "  }," (closing brace at same indent level as lang start)
        if current_lang and stripped == '},':
            lang_end[current_lang] = i

print("Lang starts:", lang_start)
print("Lang ends:", lang_end)

# New keys for each language (to insert after vid_placeholder_title in each block)
NEW_KEYS = {
    "en": [
        '    about_hero_title: "30+ Years of Marine Excellence", about_hero_title2: "Marine Excellence",',
        '    about_hero_desc: "Founded in 1995, SNOWL Hong Kong Limited has grown into a globally trusted name in marine hardware -- serving boat builders and yacht manufacturers across Europe and America.",',
        '    about_why_title: "Our Competitive Advantages",',
        '    about_facility_header: "Our Facilities", about_facility_area: "20,000 m2",',
        '    about_facility_title: "State-of-the-Art Manufacturing",',
        '    about_facility_desc1: "Our modern production facility in Foshan, Guangdong spans over 20,000 square meters with automated manufacturing lines, rigorous quality control labs, and professional R&D centers.",',
        '    about_facility_desc2: "Every product undergoes multiple quality checks from raw material inspection to final packaging, ensuring that every fastener that leaves our facility meets the highest international standards.",',
        '    about_quick_title: "Ready to Partner?",',
        '    about_quick_desc: "Whether you\'re a boat manufacturer, yacht builder, or maritime supplier, we\'d love to hear from you.",',
        '    about_quick_btn: "Get in Touch",',
        '    contact_page_title: "Contact SNOWL",',
        '    contact_hero_desc: "Whether you need a custom marine solution or standard product -- we\'re here to help. Fill out the form or reach us directly.",',
        '    contact_info_tag: "Contact Info", contact_info_title: "Let\'s Talk",',
        '    contact_addr: "Aoying Business Center 2414, Xinan Street, Sanshui District, Foshan City, Guangdong, China",',
        '    contact_hours: "Mon-Sat 9:00-18:00 (UTC+8)",',
        '    prod_hero_title: "Our Products", prod_hero_title2: "Marine-Grade Fastener Solutions",',
        '    prod_hero_desc: "From ocean-rated snap kits to deck hardware -- engineered for durability in the harshest marine environments. Over 30 years of precision manufacturing.",',
        '    prod_sec_title: "All Marine Hardware Categories",',
        '    prod_sec_desc: "Complete range of precision marine fasteners and hardware for the global yacht and boat industry.",',
        '    prod_owoz_title: "OWOZ Fastener", prod_owoz_desc: "All-copper marine snap button bases with silver, chrome, and black chrome finishes.",',
        '    prod_snap_title: "Snap Fastener", prod_snap_desc: "Heavy-duty stainless steel snap fasteners for demanding marine canvas applications.",',
        '    prod_turn_title: "Turn Button", prod_turn_desc: "Precision turn buttons for secure and quick-release canvas fastening on vessels.",',
        '    prod_nylon_title: "Nylon Button", prod_nylon_desc: "Lightweight nylon buttons for sailboat canvas with zero corrosion performance.",',
        '    prod_tool_title: "Installation Tools", prod_tool_desc: "Professional installation tools and accessories for marine fastener assembly.",',
        '    prod_deck_title: "Deck Fasteners", prod_deck_desc: "Marine panel clips for boat decks and cabin interiors. Corrosion-resistant.",',
        '    prod_cta_title: "Need a Custom Solution?",',
        '    prod_cta_desc: "We offer OEM and custom manufacturing for boat manufacturers worldwide. Contact us to discuss your requirements.",',
        '    news_hero_title: "News & Industry Updates", news_hero_title2: "Industry Updates",',
        '    news_hero_desc: "Stay informed about SNOWL, marine industry trends, trade shows, and product innovations.",',
        '    news_metstrade_title: "METSTRADE Amsterdam 2026 - Marine Equipment Trade Show",',
        '    news_metstrade_desc: "SNOWL showcased its full product range at METSTRADE 2026 in Amsterdam, connecting with over 250 marine industry professionals from across Europe and beyond.",',
        '    news_ss316_title: "New SS316 Marine Snap Fastener Series Launches",',
        '    news_ss316_desc: "We\'re excited to introduce our new SS316 snap fastener series, featuring enhanced corrosion resistance for prolonged saltwater exposure.",',
        '    news_miami_title: "Miami International Boat Show 2026 Highlights",',
        '    news_miami_desc: "Our team had an outstanding show in Miami, presenting our latest marine hardware innovations to North American boat builders.",',
        '    news_corrosion_title: "Innovation in Marine Hardware: Corrosion Resistance",',
        '    news_corrosion_desc: "A deep dive into the materials science behind our proprietary corrosion-resistant coatings and ocean performance.",',
        '    news_europe_title: "SNOWL Expands European Distribution Network",',
        '    news_europe_desc: "New distribution partnerships across Northern Europe and the Mediterranean strengthen our global presence.",',
        '    news_sustainable_title: "Sustainable Marine Fittings: Industry Trends 2025",',
        '    news_sustainable_desc: "How the marine hardware industry is evolving toward sustainable materials and eco-friendly manufacturing.",',
        '    vid_hero_title: "Product Videos", vid_hero_title2: "Videos",',
        '    vid_hero_desc: "Watch our product demonstrations and factory tour footage to learn about SNOWL marine hardware.",',
        '    vid_sec_title: "See SNOWL in Action",',
        '    vid_hibur_title: "Installation Guide - Hibur & Snap Fastener",',
        '    vid_youtube_note: "Click to watch on YouTube",',
        '    vid_hibur_desc: "Learn the correct installation method for Hibur and Snap Fastener products in marine and outdoor applications.",',
        '    vid_4000c1_title: "Installation Guide - 4000C1 Shock Cord Cover Clip",',
        '    vid_4000c1_desc: "Official installation tutorial for the 4000C1 Shock Cord Cover Clip series. Ideal for marine canvas, bimini tops, and deck enclosure applications.",',
        '    vid_4000r2_title: "Installation Guide - 4000R2 Fastener",',
        '    vid_4000r2_desc: "Official installation tutorial for the 4000R2 marine snap fastener series. Designed for reliable performance in marine canvas and deck hardware applications.",',
        '    vid_4000d8_title: "Installation Guide - 4000D8 Fastener",',
        '    vid_4000d8_desc: "Official installation tutorial for the 4000D8 marine snap fastener series. Reliable performance for bimini tops, pontoon rails, and marine canvas installations.",',
        '    vid_owoz_title: "Installation Guide - OWOZ Fastener",',
        '    vid_owoz_desc: "Step-by-step guide for installing OWOZ marine snap fasteners on deck hardware, life vests, and marine canvas.",',
        '    footer_brand_desc: "SNOWL Hong Kong Limited - precision marine fastener manufacturer since 1995. Trusted by boat builders and yacht manufacturers worldwide.",',
    ],
}

# ZH translations
NEW_KEYS["zh"] = [
    '    about_hero_title: "30年船舶五金卓越品质", about_hero_title2: "船舶五金卓越品质",',
    '    about_hero_desc: "SNOWL香港有限公司创立于1995年，已发展成为全球船舶五金领域受信赖的品牌——为欧洲和美洲的船舶制造商及游艇建造商提供服务。",',
    '    about_why_title: "我们的竞争优势",',
    '    about_facility_header: "我们的设施", about_facility_area: "20,000 平方米",',
    '    about_facility_title: "现代化生产制造",',
    '    about_facility_desc1: "位于佛山广东的现代化生产基地占地超过20,000平方米，配备自动化生产线、严格的质量控制实验室和专业研发中心。",',
    '    about_facility_desc2: "每件产品从原材料检验到最终包装都经过多重质量检查，确保每件离开我们工厂的紧固件都达到最高国际标准。",',
    '    about_quick_title: "期待与您合作？",',
    '    about_quick_desc: "无论您是船舶制造商、游艇建造商还是海事供应商，我们期待您的垂询。",',
    '    about_quick_btn: "联系我们",',
    '    contact_page_title: "联系SNOWL",',
    '    contact_hero_desc: "无论您需要定制船舶解决方案还是标准产品——我们随时为您服务。请填写表单或直接联系我们。",',
    '    contact_info_tag: "联系方式", contact_info_title: "洽谈合作",',
    '    contact_addr: "中国广东省佛山市三水区西南街道奥盈商务中心2414室",',
    '    contact_hours: "周一至周六 9:00-18:00（北京时间）",',
    '    prod_hero_title: "我们的产品", prod_hero_title2: "船用级紧固件解决方案",',
    '    prod_hero_desc: "从海洋级按扣套装到甲板五金——专为最恶劣的海洋环境设计，经久耐用。超过30年的精密制造经验。",',
    '    prod_sec_title: "所有船舶五金类别",',
    '    prod_sec_desc: "面向全球游艇和船舶行业的精密船舶紧固件及五金全套解决方案。",',
    '    prod_owoz_title: "OWOZ紧固件", prod_owoz_desc: "全铜船用按扣底座，提供镍银、镀铬、黑色镀铬三种高端表面处理。",',
    '    prod_snap_title: "按扣", prod_snap_desc: "重型不锈钢按扣，专为严苛船用帆布应用设计。",',
    '    prod_turn_title: "旋钮", prod_turn_desc: "精密旋钮，适用于安全快速释放的帆布紧固。",',
    '    prod_nylon_title: "尼龙扣", prod_nylon_desc: "轻量化尼龙按钮，专为帆船帆布设计，零腐蚀。",',
    '    prod_tool_title: "安装工具", prod_tool_desc: "船舶五金专业安装工具及配件。",',
    '    prod_deck_title: "甲板紧固件", prod_deck_desc: "船舶面板夹，适用于船用甲板和船舱内部，防腐耐用。",',
    '    prod_cta_title: "需要定制解决方案？",',
    '    prod_cta_desc: "我们为全球船舶制造商提供OEM和定制生产服务。联系我们讨论您的需求。",',
    '    news_hero_title: "新闻与行业动态", news_hero_title2: "行业动态",',
    '    news_hero_desc: "了解SNOWL动态、海事行业趋势、贸易展会和产品创新。",',
    '    news_metstrade_title: "2026年阿姆斯特丹METSTRADE船舶设备展",',
    '    news_metstrade_desc: "SNOWL在阿姆斯特丹METSTRADE 2026展示了全系列产品，与来自欧洲及世界各地的250多位海事行业专业人士进行了深入交流。",',
    '    news_ss316_title: "全新SS316船用按扣系列发布",',
    '    news_ss316_desc: "我们激动地推出全新SS316按扣系列，增强耐腐蚀性，适用于长时间盐水浸泡。",',
    '    news_miami_title: "2026年迈阿密国际船展回顾",',
    '    news_miami_desc: "我们的团队在迈阿密表现出色，向北美船舶制造商展示了最新的船舶五金创新产品。",',
    '    news_corrosion_title: "船舶五金创新：耐腐蚀技术",',
    '    news_corrosion_desc: "深入探讨我们专有耐腐蚀涂层和海洋性能背后的材料科学。",',
    '    news_europe_title: "SNOWL拓展欧洲分销网络",',
    '    news_europe_desc: "北欧和地中海地区新的分销合作伙伴关系加强了我们的全球布局。",',
    '    news_sustainable_title: "可持续船舶配件：2025行业趋势",',
    '    news_sustainable_desc: "船舶五金行业如何向可持续材料和环保制造方向发展。",',
    '    vid_hero_title: "产品视频", vid_hero_title2: "视频",',
    '    vid_hero_desc: "观看我们的产品演示和工厂参观视频，了解SNOWL船舶五金。",',
    '    vid_sec_title: "了解SNOWL",',
    '    vid_hibur_title: "安装教程 - Hibur和按扣",',
    '    vid_youtube_note: "点击在YouTube观看",',
    '    vid_hibur_desc: "了解Hibur和按扣产品在海洋及户外应用中的正确安装方法。",',
    '    vid_4000c1_title: "安装教程 - 4000C1弹力绳盖夹",',
    '    vid_4000c1_desc: "4000C1弹力绳盖夹系列官方安装教程。适用于船用帆布、双体船顶棚和甲板围栏应用。",',
    '    vid_4000r2_title: "安装教程 - 4000R2紧固件",',
    '    vid_4000r2_desc: "4000R2船用按扣系列官方安装教程。专为船用帆布和甲板五金应用中的可靠性能而设计。",',
    '    vid_4000d8_title: "安装教程 - 4000D8紧固件",',
    '    vid_4000d8_desc: "4000D8船用按扣系列官方安装教程。双体船顶棚、pontoon轨道和船用帆布安装的可靠性能。",',
    '    vid_owoz_title: "安装教程 - OWOZ紧固件",',
    '    vid_owoz_desc: "OWOZ船用按扣在甲板五金、救生衣和船用帆布上的分步安装指南。",',
    '    footer_brand_desc: "SNOWL香港有限公司——自1995年以来的精密船用紧固件制造商。深受全球船舶制造商和游艇建造商信赖。",',
]

# For DE/FR/RU/PT/ES, copy EN keys as placeholders
for lang in ["de", "fr", "ru", "pt", "es"]:
    NEW_KEYS[lang] = NEW_KEYS["en"].copy()

# Find vid_placeholder_title line in each block and insert after it
for lang in ["en", "zh", "de", "fr", "ru", "pt", "es"]:
    start = lang_start.get(lang)
    end = lang_end.get(lang)
    if start is None or end is None:
        print(f"SKIP {lang}: no block found")
        continue
    
    # Find vid_placeholder_title in this block
    placeholder_line = None
    for i in range(start, end + 1):
        if 'vid_placeholder_title' in lines[i]:
            placeholder_line = i
            break
    
    if placeholder_line is None:
        print(f"SKIP {lang}: no vid_placeholder_title found")
        continue
    
    # Get the indent of placeholder line
    indent = len(lines[placeholder_line]) - len(lines[placeholder_line].lstrip())
    indent_str = ' ' * indent
    
    # Prepare new keys with same indent
    new_lines = []
    for key in NEW_KEYS[lang]:
        new_lines.append(key)
    
    # Insert new lines after placeholder
    lines = lines[:placeholder_line + 1] + new_lines + lines[placeholder_line + 1:]
    # Adjust end positions for subsequent blocks
    insert_count = len(new_lines)
    for lang2 in ["en", "zh", "de", "fr", "ru", "pt", "es"]:
        if lang_start.get(lang2, 999999) > placeholder_line:
            lang_start[lang2] += insert_count
        if lang_end.get(lang2, 999999) > placeholder_line:
            lang_end[lang2] += insert_count
    
    print(f"Inserted {len(new_lines)} keys for {lang} after line {placeholder_line + 1}")

# Reconstruct the file
result = '\n'.join(lines) + '\n' + exec_code

with open(fpath, "w", encoding="utf-8") as f:
    f.write(result)

print("\ni18n.js updated!")
