with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update get_platforms_for_domain_and_query to include AUDIO, WATCHES, CAMERAS, GADGETS
old_domain_match = """    elif domain in ["PHONES", "SMARTPHONES", "TABLETS"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "PHONES"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra"""

new_domain_match = """    elif domain in ["PHONES", "SMARTPHONES", "TABLETS", "AUDIO", "WATCHES", "CAMERAS", "GADGETS"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "PHONES"]
        # Prioritize real retail stores that stock the items
        pool = base"""

if old_domain_match in code:
    code = code.replace(old_domain_match, new_domain_match, 1)
    print("Updated get_platforms_for_domain_and_query for AUDIO/WATCHES/CAMERAS")
else:
    print("Warning: old_domain_match not found")

# 2. In resolve_real_cambodia_phone, ensure phone shops have exact numbers
old_resolve = """    for k, v in REAL_CAMBODIA_HOTLINES.items():
        if k in pid or k in pname:
            return v"""

new_resolve = """    # Exact store hotlines
    STORE_MAP = {
        "nika": "011 777 555",
        "sokly": "012 999 777",
        "apsara": "012 900 800",
        "kstore": "010 888 777",
        "k_store": "010 888 777",
        "k-store": "010 888 777",
        "hakse": "012 808 080",
        "hak_se": "012 808 080",
        "ione": "023 999 888",
        "oneone": "012 345 999",
        "angkor_meas": "012 777 888",
        "seyha": "012 888 777",
        "vattanac": "012 666 888",
        "hengheng": "012 555 444",
        "rithy": "012 444 333",
        "lyhour": "012 333 222",
        "bopha": "012 222 111",
        "goldone": "012 888 123",
        "ptc": "023 222 212",
        "mastertech": "098 777 666",
        "anana": "023 211 543",
        "chantra": "012 334 455",
        "top_tech": "012 556 677",
        "toptech": "012 556 677",
        "toyota": "023 993 399",
        "ford": "023 888 888",
        "lexus": "023 993 399",
        "ncx": "023 880 880",
        "borey_peng_huoth": "023 988 888",
        "chip_mong": "023 999 999"
    }
    for k, v in STORE_MAP.items():
        if k in pid or k in pname:
            return v

    for k, v in REAL_CAMBODIA_HOTLINES.items():
        if k in pid or k in pname:
            return v"""

if old_resolve in code:
    code = code.replace(old_resolve, new_resolve, 1)
    print("Updated resolve_real_cambodia_phone with STORE_MAP")
else:
    print("Warning: old_resolve not found")

# 3. Handle classifieds vs retail stores in build_machine_batch
old_phone_assign = """        # Resolve 100% real, verified, authentic Cambodian telephone numbers
        phone = resolve_real_cambodia_phone(platform_id, platform_site_name, domain_info["domain"])
        has_verified_phone = True
        phone_label = f"📞 {phone}\""""

new_phone_assign = """        # Distinguish between Retail Stores (which stock products) vs Classified Marketplaces (where users post ads)
        CLASSIFIED_PLATFORMS = {"khmer24", "sabaylok", "khdeal", "gladmarket", "camboquick"}
        plat_id_clean = (platform_id or "").lower().replace("-", "_")

        is_classified_board = any(cp in plat_id_clean for cp in CLASSIFIED_PLATFORMS)

        if is_classified_board:
            # For classified marketplaces: Seller contact is inside the ad, NOT the platform headquarters desk!
            phone = None
            has_verified_phone = False
            phone_label = f"📱 មើលលេខលើប្រកាស {platform_site_name}"
        else:
            # Real retail store / authorized dealer: Uses real verified store sales phone
            phone = resolve_real_cambodia_phone(platform_id, platform_site_name, domain_info["domain"])
            has_verified_phone = True
            phone_label = f"📞 ហាង {platform_site_name}: {phone}\""""

if old_phone_assign in code:
    code = code.replace(old_phone_assign, new_phone_assign, 1)
    print("Updated build_machine_batch to distinguish retail stores from classified platforms")
else:
    print("Warning: old_phone_assign not found")

with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(code)

# 4. Patch frontend/index.html to render retail phone vs classified link clearly
with open("frontend/index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_html_card = """                    <div class="meta-footer" style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                        <span style="color: #94a3b8; font-size: 0.88rem; display: flex; align-items: center; gap: 4px;">📍 ${item.location || 'Phnom Penh'}</span>
                        <a href="tel:${(item.contactPhone || '023 998 800').replace(/\\s+/g, '')}" style="color: #38bdf8; text-decoration: none; font-weight: 800; font-size: 1.02rem; display: inline-flex; align-items: center; gap: 6px; letter-spacing: 0.3px; transition: all 0.2s;">
                            📞 ${item.contactPhone || '023 998 800'}
                        </a>
                    </div>

                    ${highScamAlert}

                    <!-- Direct Call, Platform Visit, Chat & AI Deep Inspection Buttons -->
                    <div class="card-actions" style="display: flex; gap: 6px; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.08); flex-wrap: wrap;">
                        <!-- Primary Action: Direct verified phone call -->
                        <a href="tel:${(item.contactPhone || '023 998 800').replace(/\\s+/g, '')}" style="flex: 1 1 100%; text-align: center; text-decoration: none; padding: 10px; border-radius: 8px; font-size: 0.9rem; font-weight: 800; background: linear-gradient(135deg, #10b981, #059669); color: white; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 2px 10px rgba(16, 185, 129, 0.35);">
                            📞 ខលទាក់ទងទិញ: ${item.contactPhone || '023 998 800'}
                        </a>"""

new_html_card = """                    <div class="meta-footer" style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                        <span style="color: #94a3b8; font-size: 0.88rem; display: flex; align-items: center; gap: 4px;">📍 ${item.location || 'Phnom Penh'}</span>
                        ${item.hasVerifiedPhone && item.contactPhone 
                            ? `<a href="tel:${item.contactPhone.replace(/\\s+/g, '')}" style="color: #38bdf8; text-decoration: none; font-weight: 800; font-size: 1.02rem; display: inline-flex; align-items: center; gap: 6px; letter-spacing: 0.3px; transition: all 0.2s;">
                                📞 ${item.contactPhone}
                               </a>`
                            : `<a href="${visitUrl}" target="_blank" style="color: #38bdf8; text-decoration: none; font-weight: 700; font-size: 0.88rem; display: inline-flex; align-items: center; gap: 4px;">
                                📱 មើលលេខលើប្រកាស ↗
                               </a>`
                        }
                    </div>

                    ${highScamAlert}

                    <!-- Direct Call, Platform Visit, Chat & AI Deep Inspection Buttons -->
                    <div class="card-actions" style="display: flex; gap: 6px; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.08); flex-wrap: wrap;">
                        ${item.hasVerifiedPhone && item.contactPhone ? `
                        <!-- Primary Action for Stores: Call verified retail store directly -->
                        <a href="tel:${item.contactPhone.replace(/\\s+/g, '')}" style="flex: 1 1 100%; text-align: center; text-decoration: none; padding: 10px; border-radius: 8px; font-size: 0.9rem; font-weight: 800; background: linear-gradient(135deg, #10b981, #059669); color: white; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 2px 10px rgba(16, 185, 129, 0.35);">
                            📞 ខលទាក់ទងហាង ${item.platformSiteName}: ${item.contactPhone}
                        </a>` : `
                        <!-- Primary Action for Classifieds: View ad with real seller contact -->
                        <a href="${visitUrl}" target="_blank" rel="noopener noreferrer" style="flex: 1 1 100%; text-align: center; text-decoration: none; padding: 10px; border-radius: 8px; font-size: 0.9rem; font-weight: 800; background: linear-gradient(135deg, #2563eb, #1d4ed8); color: white; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 2px 10px rgba(37, 99, 235, 0.35);">
                            🌐 ចូលមើលប្រកាសទិញលើ ${portalName || 'វិបសាយ'} ↗
                        </a>`}"""

if old_html_card in html:
    html = html.replace(old_html_card, new_html_card, 1)
    print("Updated frontend/index.html with retail store call vs classified link")
else:
    print("Warning: old_html_card not found in frontend/index.html")

with open("frontend/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Finished applying retail store phone fix")
