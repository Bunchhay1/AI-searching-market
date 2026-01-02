with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    content = f.read()

old_block = """    cheap_prices = [it["priceUsd"] for it in cheap_items if it.get("priceUsd", 0) > 0] or [min_p]
    fair_prices = [it["priceUsd"] for it in fair_items if it.get("priceUsd", 0) > 0] or [avg_p]
    exp_prices = [it["priceUsd"] for it in exp_items if it.get("priceUsd", 0) > 0] or [max_p]"""

new_block = """    # Filter out high-risk bait scams to present clean, realistic market prices to buyers
    cheap_clean = [it for it in cheap_items if it.get("scamRiskLevel") != "HIGH"] or cheap_items
    fair_clean = [it for it in fair_items if it.get("scamRiskLevel") != "HIGH"] or fair_items
    exp_clean = [it for it in exp_items if it.get("scamRiskLevel") != "HIGH"] or exp_items

    cheap_prices = [it["priceUsd"] for it in cheap_clean if it.get("priceUsd", 0) > 0] or [min_p]
    fair_prices = [it["priceUsd"] for it in fair_clean if it.get("priceUsd", 0) > 0] or [avg_p]
    exp_prices = [it["priceUsd"] for it in exp_clean if it.get("priceUsd", 0) > 0] or [max_p]"""

old_summary = '''        "summaryKhmer": f"ទីផ្សារមានចម្រុះតាំងពីជម្រើសធូរថ្លៃ (${min(cheap_prices):,} - ${max(cheap_prices):,}) ដល់ជម្រើសកម្រិតខ្ពស់ (${min(exp_prices):,} - ${max(exp_prices):,})។"'''

new_summary = '''        "summaryKhmer": (
            f"🔍 វិភាគឆ្លាតវៃចម្រុះស៊េរី & តម្លៃ៖ ទីផ្សារមានជម្រើសចាប់ពីកម្រិតធូរថ្លៃ ${min(cheap_prices):,} - ${max(cheap_prices):,} "
            f"(សន្សំប្រាក់ច្រើន សម្រាប់ស៊េរីដើម ឬ Option មធ្យម), ជម្រើសកណ្តាលតម្លៃទីផ្សារសមរម្យ ${min(fair_prices):,} - ${max(fair_prices):,} (ពេញនិយមបំផុត), "
            f"ដល់ជម្រើសកម្រិតខ្ពស់ ${min(exp_prices):,} - ${max(exp_prices):,} (ស៊េរីឆ្នាំចុងក្រោយ ឬ Top Option ថ្មីកេះ)។"
        )'''

if old_block in content:
    content = content.replace(old_block, new_block, 1)
    print("Updated clean pricing logic")
else:
    print("Warning: old_block not found")

if old_summary in content:
    content = content.replace(old_summary, new_summary, 1)
    print("Updated summaryKhmer")
else:
    print("Warning: old_summary not found")

with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Finished patching scrapers/ai_search_service.py for clean prices")
