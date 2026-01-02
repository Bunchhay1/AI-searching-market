# scratch/enrich_domain_map.py
import re
import sys
sys.path.append("scratch")
from generate_platforms import raw_categories

with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    code = f.read()

# Build comprehensive domain map entries
map_lines = []
for c in raw_categories:
    cat = c["cat_id"]
    map_lines.append(f"    # ── {c['cat_name_en']} ({len(c['items'])}) ──")
    for item in c["items"]:
        p_id, p_name, p_dom = item[0], item[1], item[2]
        clean_dom = p_dom.replace("https://", "").replace("http://", "").split("/")[0].lower()
        clean_name = p_name.lower().strip()
        map_lines.append(f'    "{clean_dom}": "{cat}", "{clean_name}": "{cat}",')
        if p_id != clean_name:
            map_lines.append(f'    "{p_id}": "{cat}",')

# Keyword aliases
keyword_aliases = [
    # REAL ESTATE
    '"borey": "REAL_ESTATE", "villa": "REAL_ESTATE", "condo": "REAL_ESTATE", "house": "REAL_ESTATE",',
    '"apartment": "REAL_ESTATE", "shophouse": "REAL_ESTATE", "land": "REAL_ESTATE", "plot": "REAL_ESTATE",',
    '"ផ្ទះ": "REAL_ESTATE", "ដី": "REAL_ESTATE", "បុរី": "REAL_ESTATE", "វីឡា": "REAL_ESTATE",',
    '"ខុនដូ": "REAL_ESTATE", "បន្ទប់ជួល": "REAL_ESTATE", "លក់ផ្ទះ": "REAL_ESTATE", "លក់ដី": "REAL_ESTATE",',
    '"ផ្ទះជួល": "REAL_ESTATE", "ផ្ទះអាជីវកម្ម": "REAL_ESTATE", "ផ្ទះល្វែង": "REAL_ESTATE",',
    # BEAUTY
    '"skincare": "BEAUTY", "serum": "BEAUTY", "lotion": "BEAUTY", "sunscreen": "BEAUTY", "cosmetics": "BEAUTY",',
    '"cream": "BEAUTY", "lipstick": "BEAUTY", "perfume": "BEAUTY", "pharmacy": "BEAUTY", "ក្រែម": "BEAUTY", "ឡេ": "BEAUTY",',
    # FURNITURE
    '"furniture": "FURNITURE", "sofa": "FURNITURE", "mattress": "FURNITURE", "bed": "FURNITURE", "table": "FURNITURE",',
    '"dining table": "FURNITURE", "kitchenware": "FURNITURE", "cookware": "FURNITURE", "សាឡុង": "FURNITURE", "ពូក": "FURNITURE", "គ្រែ": "FURNITURE",',
    # GROCERIES
    '"supermarket": "GROCERIES", "grocery": "GROCERIES", "groceries": "GROCERIES", "organic": "GROCERIES",',
    '"veggies": "GROCERIES", "vegetables": "GROCERIES", "fruits": "GROCERIES", "beef": "GROCERIES", "wine": "GROCERIES",',
    '"ផ្សារទំនើប": "GROCERIES", "បន្លែ": "GROCERIES", "សាច់គោ": "GROCERIES", "ស្រា": "GROCERIES",',
    # SERVICES
    '"bookmebus": "SERVICES", "camboticket": "SERVICES", "vireak buntham": "SERVICES", "vet airbus": "SERVICES",',
    '"larryta": "SERVICES", "cinema": "SERVICES", "movie": "SERVICES", "ticket": "SERVICES", "express": "SERVICES",',
    '"logistics": "SERVICES", "courier": "SERVICES", "parcel": "SERVICES", "សំបុត្រឡាន": "SERVICES", "ដឹកទំនិញ": "SERVICES",'
]

all_map_entries = "\n".join(map_lines) + "\n\n    # ── General Keyword Aliases ──\n    " + "\n    ".join(keyword_aliases)
new_map_str = "WEBSITE_DOMAIN_MAP = {\n" + all_map_entries + "\n}"

# Replace in code
old_map_pattern = r"WEBSITE_DOMAIN_MAP = \{.*?\n\}"
code = re.sub(old_map_pattern, new_map_str, code, flags=re.DOTALL)

# Add intent handlers for BEAUTY, FURNITURE, GROCERIES, SERVICES in classify_intent_and_specs
# Insert before # 10. SMARTPHONES
new_intents = """    # 9.1 BEAUTY & HEALTHCARE DOMAIN
    if any(k in q for k in ["beauty", "skincare", "serum", "lotion", "sunscreen", "cosmetics", "cream", "lipstick", "watsons", "guardian", "innisfree", "cerave", "pharmacy", "ក្រែម", "ឡេ", "ថែស្បែក"]):
        brand = "Innisfree" if "innisfree" in q else ("CeraVe" if "cerave" in q else ("Watsons" if "watsons" in q else ("Laneige" if "laneige" in q else "Beauty Care")))
        model = query.title()
        trims = [
            ("ផលិតផលសុទ្ធ 100% នាំចូលផ្ទាល់ មានធានាស្តង់ដារ", 28),
            ("ឈុត Skincare Set Promotion បញ្ចុះតម្លៃពិសេស", 45),
            ("សេរ៉ូម / ឡេការពារកម្តៅថ្ងៃ គុណភាពខ្ពស់", 19)
        ]
        years = ["Original Import", "Certified Safe"]
        core_specs = ["រូបមន្តផ្សំធម្មជាតិ គ្មានសារធាតុគ្រោះថ្នាក់", "ស្តង់ដារវេជ្ជសាស្ត្រ និងការអនុញ្ញាតត្រឹមត្រូវ", "នាំចូលពីកូរ៉េ ជប៉ុន និងបារាំង"]
        return {
            "domain": "BEAUTY", "category": "BEAUTY", "category_label": "សម្រស់ & សុខភាព / Beauty",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1571781926291-c477ebfd024b?auto=format&fit=crop&w=800&q=80"],
            "colors": ["Natural", "Original"], "core_specs": core_specs, "is_vehicle": False
        }

    # 9.2 FURNITURE & HOME LIVING DOMAIN
    if any(k in q for k in ["furniture", "sofa", "mattress", "bed", "dining", "desk", "table", "chair", "home decor", "kitchen", "dyson", "air fryer", "សាឡុង", "ពូក", "គ្រែ", "តុ", "កៅអី"]):
        brand = "Index Living" if "index" in q else ("Ashley" if "ashley" in q else ("Dyson" if "dyson" in q else ("SB Furniture" if "sb" in q else "Home Living")))
        model = query.title()
        trims = [
            ("ឈុតគ្រឿងសង្ហារិមថ្មីកេះ គុណភាព Premium", 450),
            ("ម៉ូដ Minimalist ទាន់សម័យ ធន់រឹងមាំ", 280),
            ("ទំនិញស្អាត 99% ស្តង់ដារនាំចូល", 190)
        ]
        years = ["Modern Living", "Solid Wood", "Standard"]
        core_specs = ["រចនាបទស្អាត សន្សំទំហំក្នុងបន្ទប់", "សម្ភារៈធន់ រឹងមាំ ប្រើប្រាស់បានយូរឆ្នាំ", "សេវាកម្មដំឡើង និងដឹកជញ្ជូនដល់ផ្ទះ"]
        return {
            "domain": "FURNITURE", "category": "FURNITURE", "category_label": "គ្រឿងសង្ហារិម & ផ្ទះ / Furniture",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=800&q=80"],
            "colors": ["Oak Wood", "Walnut", "Modern Gray", "Cream White"], "core_specs": core_specs, "is_vehicle": False
        }

    # 9.3 SUPERMARKET & GROCERIES DOMAIN
    if any(k in q for k in ["supermarket", "grocery", "groceries", "makro", "lucky", "organic", "veggies", "meat", "beef", "wine", "snack", "cheese", "ផ្សារទំនើប", "បន្លែ", "សាច់គោ", "ស្រា"]):
        brand = "AEON" if "aeon" in q else ("Makro" if "makro" in q else ("Lucky" if "lucky" in q else "Fresh Market"))
        model = query.title()
        trims = [
            ("ទំនិញស្រស់គុណភាពខ្ពស់ ដឹកជញ្ជូនរហ័ស 30 នាទី", 15),
            ("កញ្ចប់គ្រួសារ Family Pack តម្លៃបោះដុំសន្សំសំចៃ", 35),
            ("ទំនិញនាំចូល Original Import ស្តង់ដារអន្តរជាតិ", 25)
        ]
        years = ["Daily Fresh", "Weekly Stock"]
        core_specs = ["បន្លែ ផ្លែឈើ និងសាច់ស្រស់ប្រចាំថ្ងៃ", "ត្រួតពិនិត្យស្តង់ដារអនាម័យ និងសុវត្ថិភាពម្ហូបអាហារ", "ដឹកជញ្ជូនរហ័សដល់មាត់ទ្វារ"]
        return {
            "domain": "GROCERIES", "category": "GROCERIES", "category_label": "ផ្សារទំនើប & គ្រឿងទេស / Groceries",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=800&q=80"],
            "colors": ["Fresh"], "core_specs": core_specs, "is_vehicle": False
        }

    # 9.4 BOOKS, TRAVEL & LOGISTICS DOMAIN
    if any(k in q for k in ["bookmebus", "camboticket", "vireak buntham", "vet airbus", "larryta", "cinema", "movie", "legend", "major cineplex", "express", "courier", "parcel", "j&t", "zto", "kerry", "cambodia post", "សំបុត្រ", "ដឹកជញ្ជូន"]):
        brand = "BookMeBus" if "bus" in q else ("Vireak Buntham" if "vireak" in q else ("Legend Cinema" if "cinema" in q or "legend" in q else "Express Logistics"))
        model = query.title()
        trims = [
            ("សេវាកម្មកក់សំបុត្រ VIP Express រហ័សទាន់ចិត្ត", 18),
            ("សេវាដឹកជញ្ជូនបញ្ញើអីវ៉ាន់ទូទាំង ២៥ ខេត្ត-ក្រុង", 5),
            ("សំបុត្រកុន 2D/3D/IMAX Promotion ពិសេស", 7)
        ]
        years = ["VIP Service", "Standard Service"]
        core_specs = ["ប្រព័ន្ធកក់អនឡាញ 24/7 និងទូទាត់រហ័ស", "សុវត្ថិភាព ទំនុកចិត្ត និងតាមដានទំនិញបាន (Tracking)", "គ្របដណ្តប់ទូទាំងប្រទេសកម្ពុជា"]
        return {
            "domain": "SERVICES", "category": "SERVICES", "category_label": "សៀវភៅ & ដឹកជញ្ជូន / Services",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=800&q=80"],
            "colors": ["Standard"], "core_specs": core_specs, "is_vehicle": False
        }

    # 10. SMARTPHONES (IPHONES & ANDROIDS)"""

code = code.replace("    # 10. SMARTPHONES (IPHONES & ANDROIDS)", new_intents)

with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Enriched WEBSITE_DOMAIN_MAP and intent classification successfully!")
