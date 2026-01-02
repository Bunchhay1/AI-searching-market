#!/usr/bin/env python3
import sys

def apply_updates():
    with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update PTC Computer phone number to direct mobile sales hotline
    old_ptc = '''    {
        "id": "ptc_computer",
        "name": "PTC Computer",
        "phone": "023 222 212",'''
    new_ptc = '''    {
        "id": "ptc_computer",
        "name": "PTC Computer",
        "phone": "012 220 152",'''
    assert old_ptc in content, "Could not find old_ptc"
    content = content.replace(old_ptc, new_ptc, 1)

    old_ptc_reg = '''    "ptc_computer": {
        "phone": "023 222 212",'''
    new_ptc_reg = '''    "ptc_computer": {
        "phone": "012 220 152",'''
    assert old_ptc_reg in content, "Could not find old_ptc_reg"
    content = content.replace(old_ptc_reg, new_ptc_reg, 1)

    # 2. Update MacBook logic in classify_intent_and_specs
    old_macbook = '''        if "macbook" in q:
            brand = "Apple"
            if "pro" in q:
                model = "MacBook Pro"
                trims = [("14-inch M3 Pro 18GB/512GB ថ្មីកេះ", 1850), ("16-inch M3 Max 36GB/1TB ថ្មីកេះ", 2950), ("14-inch M2 Pro ស្អាត 99%", 1450)]
                years = ["M3 Pro", "M3 Max", "M2 Pro"]
                core_specs = ["បន្ទះឈីប Apple M3 Pro / Max", "អេក្រង់ Liquid Retina XDR 120Hz ProMotion", "ថ្មកាន់បានរហូតដល់ 22 ម៉ោង"]
            else:
                model = "MacBook Air"
                trims = [("13-inch M3 8GB/256GB ថ្មីកេះ", 1050), ("13-inch M2 8GB/256GB ស្អាត 99%", 850), ("15-inch M3 16GB/512GB ថ្មីកេះ", 1450)]
                years = ["M3 (2024)", "M2 (2022)"]
                core_specs = ["បន្ទះឈីប Apple M3 / M2", "កម្រាស់ស្តើងស្រាល គ្មានកង្ហារស្ងាត់ល្អ", "ថ្មកាន់បាន 18 ម៉ោង"]
            colors = ["Space Gray", "Silver", "Midnight", "Starlight"]'''

    new_macbook = '''        if "macbook" in q:
            brand = "Apple"
            if "max" in q or "m3 max" in q or "m4 max" in q:
                model = "MacBook Pro (M3 Max)"
                trims = [
                    ("14-inch M3 Max (14-Core CPU, 30-Core GPU) 36GB / 1TB SSD ថ្មីកេះ", 2790),
                    ("16-inch M3 Max (14-Core CPU, 30-Core GPU) 36GB / 1TB SSD ថ្មីកេះ", 2990),
                    ("16-inch M3 Max (16-Core CPU, 40-Core GPU) 48GB / 1TB SSD ថ្មីកេះ", 3450),
                    ("16-inch M3 Max (16-Core CPU, 40-Core GPU) 64GB / 2TB SSD ស្អាត 99%", 3890)
                ]
                years = ["2024 (M3 Max)", "ឆ្នាំ 2024"]
                core_specs = ["បន្ទះឈីប Apple M3 Max (Up to 16-Core CPU, 40-Core GPU)", "អេក្រង់ 14/16 Liquid Retina XDR 120Hz ProMotion", "អង្គចងចាំ 36GB - 64GB Unified Memory"]
                colors = ["Space Black (ខ្មៅរលើប)", "Silver (ប្រាក់)"]
            elif "m3 pro" in q or ("pro" in q and "m3" in q):
                model = "MacBook Pro (M3 Pro)"
                trims = [
                    ("14-inch M3 Pro (11-Core CPU, 14-Core GPU) 18GB / 512GB SSD ថ្មីកេះ", 1790),
                    ("14-inch M3 Pro (12-Core CPU, 18-Core GPU) 18GB / 1TB SSD ថ្មីកេះ", 2150),
                    ("16-inch M3 Pro (12-Core CPU, 18-Core GPU) 18GB / 512GB SSD ថ្មីកេះ", 2290),
                    ("16-inch M3 Pro (12-Core CPU, 18-Core GPU) 36GB / 512GB SSD ថ្មីកេះ", 2650)
                ]
                years = ["2024 (M3 Pro)", "ឆ្នាំ 2024"]
                core_specs = ["បន្ទះឈីប Apple M3 Pro", "អេក្រង់ Liquid Retina XDR 120Hz ProMotion", "ថ្មកាន់បានរហូតដល់ 22 ម៉ោង"]
                colors = ["Space Black (ខ្មៅរលើប)", "Silver (ប្រាក់)"]
            elif "pro" in q:
                model = "MacBook Pro"
                trims = [
                    ("14-inch M3 Pro 18GB / 512GB SSD ថ្មីកេះ", 1790),
                    ("16-inch M3 Pro 18GB / 512GB SSD ថ្មីកេះ", 2290),
                    ("16-inch M3 Max 36GB / 1TB SSD ថ្មីកេះ", 2990)
                ]
                years = ["2024", "ឆ្នាំ 2024"]
                core_specs = ["បន្ទះឈីប Apple M3 Pro / Max", "អេក្រង់ Liquid Retina XDR 120Hz ProMotion", "ថ្មកាន់បានរហូតដល់ 22 ម៉ោង"]
                colors = ["Space Black (ខ្មៅរលើប)", "Silver (ប្រាក់)"]
            else:
                model = "MacBook Air"
                trims = [("13-inch M3 8GB/256GB ថ្មីកេះ", 1050), ("13-inch M2 8GB/256GB ស្អាត 99%", 850), ("15-inch M3 16GB/512GB ថ្មីកេះ", 1450)]
                years = ["2024 (M3)", "2023 (M2)"]
                core_specs = ["បន្ទះឈីប Apple M3 / M2", "កម្រាស់ស្តើងស្រាល គ្មានកង្ហារស្ងាត់ល្អ", "ថ្មកាន់បាន 18 ម៉ោង"]
                colors = ["Midnight (ខៀវចាស់)", "Starlight (មាសស្រាល)", "Space Gray (ប្រផេះ)", "Silver (ប្រាក់)"]'''

    assert old_macbook in content, "Could not find old_macbook"
    content = content.replace(old_macbook, new_macbook, 1)

    # 3. Clean computer title construction (remove conflicting redundant year chips like (M2 Pro))
    old_comp_title = '''        elif is_computer:
            if seller_type == "STORE":
                title = f"{item_full_name} ({year}) {trim_name} ({color}) - ថ្មីកេះ 100% ធានាក្រុមហ៊ុន"
                desc = (
                    f"លក់កុំព្យូទ័រ {item_full_name} ថ្មីកេះ 100% ធានាក្រុមហ៊ុនផ្លូវការពី {platform_site_name}។\\n"
                    f"• ម៉ាស៊ីនថ្មីកេះ ប្រអប់បិទជិត គ្រឿងហ្ស៊ីនរោងចក្រ 100% មានការធានាផ្លូវការ។\\n"
                    f"• តម្លៃស្តង់ដារក្រុមហ៊ុន៖ ${item_price:,}។\\n"
                    + (f"• ទំនាក់ទំនងផ្នែកលក់ផ្ទាល់ខលលេខ {phone}!" if phone else f"• ព័ត៌មានបន្ថែម៖ {platform_home}")
                )
            else:
                title = f"{item_full_name} ({year}) {trim_name} ({color})"'''

    new_comp_title = '''        elif is_computer:
            if seller_type == "STORE":
                title = f"{item_full_name} {trim_name} ({color}) - ថ្មីកេះ 100% ធានាក្រុមហ៊ុន"
                desc = (
                    f"លក់កុំព្យូទ័រ {item_full_name} ថ្មីកេះ 100% ធានាក្រុមហ៊ុនផ្លូវការពី {platform_site_name}។\\n"
                    f"• ម៉ាស៊ីនថ្មីកេះ ប្រអប់បិទជិត គ្រឿងហ្ស៊ីនរោងចក្រ 100% មានការធានាផ្លូវការ។\\n"
                    f"• តម្លៃស្តង់ដារក្រុមហ៊ុន៖ ${item_price:,}។\\n"
                    + (f"• ទំនាក់ទំនងផ្នែកលក់ផ្ទាល់ខលលេខ {phone}!" if phone else f"• ព័ត៌មានបន្ថែម៖ {platform_home}")
                )
            else:
                title = f"{item_full_name} {trim_name} ({color}) - ស្អាត 99%"'''

    assert old_comp_title in content, "Could not find old_comp_title"
    content = content.replace(old_comp_title, new_comp_title, 1)

    with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
        f.write(content)

    print("Successfully patched MacBook and PTC Computer contacts.")

if __name__ == "__main__":
    apply_updates()
