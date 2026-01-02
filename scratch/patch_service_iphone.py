with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update iPhone generic handling
old_iphone_logic = """    # 10. SMARTPHONES (IPHONES & ANDROIDS)
    is_iphone = "iphone" in q or "apple" in q
    if is_iphone:
        brand = "Apple"
        gen_match = re.search(r'\\b(17|16|15|14|13|12|11|xs|xr|x|se)\\b', q)
        gen = gen_match.group(1) if gen_match else "16"
        is_pro_max = "pro max" in q
        is_pro = "pro" in q and not is_pro_max
        is_plus = "plus" in q"""

new_iphone_logic = """    # 10. SMARTPHONES (IPHONES & ANDROIDS)
    is_iphone = "iphone" in q or "apple" in q
    if is_iphone:
        brand = "Apple"
        gen_match = re.search(r'\\b(17|16|15|14|13|12|11|xs|xr|x|se)\\b', q)
        is_pro_max = "pro max" in q
        is_pro = "pro" in q and not is_pro_max
        is_plus = "plus" in q

        if not gen_match:
            # Multi-generation iPhone spectrum (Budget to Flagship)
            model = "iPhone Series (ចម្រុះគ្រប់ស៊េរី)"
            trims = [
                ("iPhone 11 64GB/128GB ស្អាត 99% សំណុំហ្ស៊ីន (ស៊េរីធូរថ្លៃ)", 210),
                ("iPhone 12 Pro 128GB ស្អាត 99% ធានាហាង (ស៊េរីធូរថ្លៃ)", 360),
                ("iPhone 13 128GB ស្អាត 99% សំណុំហ្ស៊ីន", 460),
                ("iPhone 14 Pro Max 128GB ស្អាត 99% Deep Purple", 710),
                ("iPhone 15 Pro 128GB/256GB Natural Titanium", 820),
                ("iPhone 16 Pro Max 256GB Desert Titanium ថ្មីកេះ 100%", 1320),
                ("iPhone 16 Pro Max 512GB/1TB ZA/LL ថ្មីកេះ ប្រអប់បិទជិត", 1490)
            ]
            years = ["iPhone 11", "iPhone 12 Pro", "iPhone 13", "iPhone 14 Pro Max", "iPhone 15 Pro", "iPhone 16 Pro Max"]
            core_specs = ["គ្រប់ជំនាន់ iPhone ពីស៊េរីធូរថ្លៃ ដល់ថ្មីកេះ", "មានការធានាម៉ាស៊ីន និងគុណភាពហ្ស៊ីន 100%", "ជម្រើសទំហំ 64GB - 1TB"]
            colors = ["Natural Titanium", "Desert Titanium", "Deep Purple", "Midnight", "Starlight"]
            return {
                "domain": "PHONES", "category": "PHONES", "category_label": "ទូរស័ព្ទ / Smartphones",
                "brand": brand, "model": model, "years": years, "trims": trims,
                "images": ["https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=800&q=80"],
                "colors": colors, "core_specs": core_specs, "is_vehicle": False
            }

        gen = gen_match.group(1)"""

if old_iphone_logic in content:
    content = content.replace(old_iphone_logic, new_iphone_logic, 1)
    print("Updated iPhone generic multi-gen handling")
else:
    print("Warning: old_iphone_logic not found")

# 2. Fix year sorting for non-numeric arrays
old_year_sort = """        num_years_list = [y for y in avail_years if str(y).strip().isdigit() and len(str(y).strip()) == 4]
        if num_years_list:
            s_years = sorted(num_years_list, key=lambda y: int(y))
            y_earliest = s_years[0]
            y_latest = s_years[-1]
            y_mid = s_years[len(s_years)//2]
        else:
            y_earliest = avail_years[-1] if len(avail_years) > 1 else avail_years[0]
            y_latest = avail_years[0]
            y_mid = avail_years[len(avail_years)//2]"""

new_year_sort = """        num_years_list = [y for y in avail_years if str(y).strip().isdigit() and len(str(y).strip()) == 4]
        if num_years_list:
            s_years = sorted(num_years_list, key=lambda y: int(y))
            y_earliest = s_years[0]
            y_latest = s_years[-1]
            y_mid = s_years[len(s_years)//2]
        else:
            y_earliest = avail_years[0]
            y_latest = avail_years[-1]
            y_mid = avail_years[len(avail_years)//2]"""

if old_year_sort in content:
    content = content.replace(old_year_sort, new_year_sort, 1)
    print("Updated year sort for non-numeric arrays")
else:
    print("Warning: old_year_sort not found")

with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Finished patching scrapers/ai_search_service.py")
