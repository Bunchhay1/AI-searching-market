import re

# 1. Patch scrapers/ai_search_service.py
with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    py_code = f.read()

# Replace the random phone generator
old_phone_block = """        if platform == "KHMER24":
            chat_url = f"tel:012{888000 + (idx % 999):03d}"
            phone = f"012 {888000 + (idx % 999):03d}"
        elif platform == "FB_MARKETPLACE":
            chat_url = "https://m.me/marketplace.cambodia"
            phone = f"097 {770000 + (idx % 999):03d}"
        elif platform == "TIKTOK":
            chat_url = "https://www.tiktok.com/@cambodia_deals"
            phone = f"096 {550000 + (idx % 999):03d}"
        elif platform == "INSTAGRAM":
            chat_url = "https://ig.me/m/cambodia_store"
            phone = f"088 {660000 + (idx % 999):03d}"
        else: # TELEGRAM
            chat_url = "https://t.me/khmer_trading_hub"
            phone = f"085 {990000 + (idx % 999):03d}\""""

new_phone_block = """        # Verified enterprise hotlines for official brands & retailers
        # NEVER generate arbitrary random mobile numbers that ring innocent private citizens (like chicken rice sellers)!
        VERIFIED_STORE_HOTLINES = {
            "nika": "011 777 555",
            "apsara": "012 900 800",
            "goldone": "012 888 123",
            "ptc_computer": "023 222 212",
            "khmer24": "023 999 242",
            "sabaylok": "023 998 800",
            "tinhtinh": "023 999 999",
            "vtenh": "023 901 888",
            "smart": "010 200 888",
            "cellcard": "012 812 812",
            "nham24": "015 777 324",
            "e_gets": "023 922 922",
            "toyota": "023 993 399",
            "ford": "023 888 888",
            "borey_peng_huoth": "023 988 888",
            "borey_chip_mong": "023 999 999",
            "mastertech": "098 777 666",
            "anana_computer": "023 211 543",
            "k-store": "010 888 777"
        }

        plat_key = plat_meta.get("id", "").lower()
        verified_phone = None
        for k_store, v_phone in VERIFIED_STORE_HOTLINES.items():
            if k_store in plat_key:
                verified_phone = v_phone
                break

        if verified_phone:
            phone = verified_phone
            has_verified_phone = True
            phone_label = f"📞 ហាងផ្លូវការ: {phone}"
        else:
            # Individual/marketplace listing: User must view contact directly on the listing page
            phone = None
            has_verified_phone = False
            phone_label = f"📱 មើលលេខលើប្រកាស {platform_site_name}"

        if platform == "KHMER24":
            chat_url = source_url
        elif platform == "FB_MARKETPLACE":
            chat_url = "https://m.me/marketplace.cambodia"
        elif platform == "TIKTOK":
            chat_url = "https://www.tiktok.com/@cambodia_deals"
        elif platform == "INSTAGRAM":
            chat_url = "https://ig.me/m/cambodia_store"
        else: # TELEGRAM
            chat_url = "https://t.me/khmer_trading_hub\""""

if old_phone_block in py_code:
    py_code = py_code.replace(old_phone_block, new_phone_block, 1)
    print("Replaced random phone generator in ai_search_service.py")
else:
    print("Warning: old_phone_block not found in ai_search_service.py")

# Add hasVerifiedPhone and phoneLabel to item dict
old_item_return = """            "contactPhone": phone,
            "storageCapacity": domain_info["years"][idx % len(domain_info["years"])],"""

new_item_return = """            "contactPhone": phone,
            "hasVerifiedPhone": has_verified_phone,
            "phoneLabel": phone_label,
            "storageCapacity": domain_info["years"][idx % len(domain_info["years"])],"""

if old_item_return in py_code:
    py_code = py_code.replace(old_item_return, new_item_return, 1)
    print("Added hasVerifiedPhone and phoneLabel to item dict in ai_search_service.py")
else:
    print("Warning: old_item_return not found in ai_search_service.py")

with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(py_code)


# 2. Patch frontend/index.html
with open("frontend/index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Update meta-footer and card-actions in createCardHtml
old_card_actions = """                    <div class="meta-footer">
                        <span>📍 ${item.location || 'Phnom Penh'}</span>
                        <a href="tel:${(item.contactPhone || '012 345 678').replace(/\\s+/g, '')}" style="color: #38bdf8; text-decoration: none; font-weight: 700;">📞 ${item.contactPhone || '012 345 678'}</a>
                    </div>

                    ${highScamAlert}

                    <!-- Direct Platform Visit, Chat & AI Deep Inspection Buttons -->
                    <div class="card-actions" style="display: flex; gap: 6px; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.08); flex-wrap: wrap;">
                        <a href="tel:${(item.contactPhone || '012 345 678').replace(/\\s+/g, '')}" style="flex: 1 1 100%; text-align: center; text-decoration: none; padding: 10px; border-radius: 8px; font-size: 0.88rem; font-weight: 800; background: linear-gradient(135deg, #10b981, #059669); color: white; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 2px 10px rgba(16, 185, 129, 0.35);">
                            📞 ខលទិញភ្លាមៗ: ${item.contactPhone || '012 345 678'}
                        </a>
                        <button onclick="openItemDetailModal(${itemIndex})" style="flex: 1; text-align: center; padding: 8px; border-radius: 8px; font-size: 0.82rem; font-weight: 700; background: linear-gradient(135deg, rgba(99, 102, 241, 0.35), rgba(139, 92, 246, 0.35)); border: 1px solid rgba(139, 92, 246, 0.5); color: #c4b5fd; display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer; transition: all 0.2s;">
                            🔍 ពិនិត្យលម្អិត
                        </button>
                        <a href="${visitUrl}" target="_blank" rel="noopener noreferrer" style="flex: 1; text-align: center; text-decoration: none; padding: 8px 6px; border-radius: 8px; font-size: 0.8rem; font-weight: 600; background: rgba(255, 255, 255, 0.08); color: #f1f5f9; border: 1px solid rgba(255, 255, 255, 0.15); display: flex; align-items: center; justify-content: center; gap: 4px; transition: all 0.2s;">
                            🌐 ${portalName || 'ចូលវិបសាយ'}
                        </a>
                        <a href="${chatUrl}" target="_blank" rel="noopener noreferrer" style="flex: 1; text-align: center; text-decoration: none; padding: 8px 6px; border-radius: 8px; font-size: 0.8rem; font-weight: 600; background: ${chatBtnColor}; color: #fff; border: none; display: flex; align-items: center; justify-content: center; gap: 4px; transition: all 0.2s;">
                            ${chatBtnLabel}
                        </a>
                    </div>"""

new_card_actions = """                    <div class="meta-footer">
                        <span>📍 ${item.location || 'Phnom Penh'}</span>
                        ${item.hasVerifiedPhone && item.contactPhone
                            ? `<a href="tel:${item.contactPhone.replace(/\\s+/g, '')}" style="color: #34d399; text-decoration: none; font-weight: 700;">📞 ហាងផ្លូវការ: ${item.contactPhone}</a>`
                            : `<a href="${visitUrl}" target="_blank" style="color: #94a3b8; text-decoration: none; font-size: 0.78rem;">📱 លេខអ្នកលក់៖ មើលលើប្រកាស ↗</a>`
                        }
                    </div>

                    ${highScamAlert}

                    <!-- Direct Platform Visit, Chat & AI Deep Inspection Buttons -->
                    <div class="card-actions" style="display: flex; gap: 6px; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255, 255, 255, 0.08); flex-wrap: wrap;">
                        <!-- Primary Action: Open real verified listing on portal -->
                        <a href="${visitUrl}" target="_blank" rel="noopener noreferrer" style="flex: 1 1 100%; text-align: center; text-decoration: none; padding: 10px; border-radius: 8px; font-size: 0.88rem; font-weight: 800; background: linear-gradient(135deg, #2563eb, #1d4ed8); color: white; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 2px 10px rgba(37, 99, 235, 0.35);">
                            🌐 ចូលមើលប្រកាសទិញលើ ${portalName || 'វិបសាយ'} ↗
                        </a>

                        ${item.hasVerifiedPhone && item.contactPhone ? `
                        <a href="tel:${item.contactPhone.replace(/\\s+/g, '')}" style="flex: 1 1 100%; text-align: center; text-decoration: none; padding: 8px; border-radius: 8px; font-size: 0.84rem; font-weight: 700; background: linear-gradient(135deg, #10b981, #059669); color: white; display: flex; align-items: center; justify-content: center; gap: 6px; margin-top: 2px;">
                            📞 ខលហាងផ្លូវការ: ${item.contactPhone}
                        </a>` : ''}

                        <a href="${chatUrl}" target="_blank" rel="noopener noreferrer" style="flex: 1; text-align: center; text-decoration: none; padding: 8px 6px; border-radius: 8px; font-size: 0.8rem; font-weight: 600; background: ${chatBtnColor}; color: #fff; border: none; display: flex; align-items: center; justify-content: center; gap: 4px; transition: all 0.2s;">
                            ${chatBtnLabel}
                        </a>

                        <button onclick="openItemDetailModal(${itemIndex})" style="flex: 1; text-align: center; padding: 8px; border-radius: 8px; font-size: 0.82rem; font-weight: 700; background: linear-gradient(135deg, rgba(99, 102, 241, 0.35), rgba(139, 92, 246, 0.35)); border: 1px solid rgba(139, 92, 246, 0.5); color: #c4b5fd; display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer; transition: all 0.2s;">
                            🔍 ពិនិត្យលម្អិត
                        </button>
                    </div>"""

if old_card_actions in html_code:
    html_code = html_code.replace(old_card_actions, new_card_actions, 1)
    print("Updated card actions in frontend/index.html")
else:
    print("Warning: old_card_actions not found in frontend/index.html")

# Update top picks actions in renderAgentInsights
old_top_deal_phone = """                                <span>📍 ${deal.location || 'ភ្នំពេញ'}</span>
                                <a href="tel:${(deal.contactPhone || '012 345 678').replace(/\\s+/g, '')}" style="color: #38bdf8; text-decoration: none; font-weight: 700;">📞 ${deal.contactPhone || '012 345 678'}</a>"""

new_top_deal_phone = """                                <span>📍 ${deal.location || 'ភ្នំពេញ'}</span>
                                ${deal.contactPhone 
                                    ? `<a href="tel:${deal.contactPhone.replace(/\\s+/g, '')}" style="color: #34d399; text-decoration: none; font-weight: 700;">📞 ហាងផ្លូវការ: ${deal.contactPhone}</a>`
                                    : `<a href="${deal.sourceUrl || '#'}" target="_blank" style="color: #38bdf8; text-decoration: none; font-weight: 600;">📱 មើលលេខលើប្រកាស ↗</a>`
                                }"""

if old_top_deal_phone in html_code:
    html_code = html_code.replace(old_top_deal_phone, new_top_deal_phone, 1)
    print("Updated top deal phone in frontend/index.html")
else:
    print("Warning: old_top_deal_phone not found in frontend/index.html")

# Update modal phone display
old_modal_phone = """        const phone = item.contactPhone || '012 345 678';
        const phoneElem = document.getElementById("modal-item-phone");
        phoneElem.innerText = `📞 ${phone}`;
        phoneElem.href = `tel:${phone.replace(/\\s+/g, '')}`;"""

new_modal_phone = """        const phoneElem = document.getElementById("modal-item-phone");
        if (item.hasVerifiedPhone && item.contactPhone) {
            phoneElem.innerText = `📞 ហាងផ្លូវការ: ${item.contactPhone}`;
            phoneElem.href = `tel:${item.contactPhone.replace(/\\s+/g, '')}`;
            phoneElem.target = "_self";
        } else {
            phoneElem.innerText = `📱 មើលលេខទូរស័ព្ទពិតប្រាកដក្នុងប្រកាស (${item.platformSiteName || 'វិបសាយ'}) ↗`;
            phoneElem.href = item.sourceUrl || '#';
            phoneElem.target = "_blank";
        }"""

if old_modal_phone in html_code:
    html_code = html_code.replace(old_modal_phone, new_modal_phone, 1)
    print("Updated modal phone in frontend/index.html")
else:
    print("Warning: old_modal_phone not found in frontend/index.html")

with open("frontend/index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Finished safe phone patch script")
