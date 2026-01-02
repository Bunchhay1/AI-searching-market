import re

def classify_test(query: str):
    q = query.lower().strip()
    
    # 0. Year Extractor
    year_match = re.search(r'\b(199\d|20[0-2]\d)\b', q)
    ext_year = int(year_match.group(1)) if year_match else None

    # Brand maps
    car_brands_map = {
        "toyota": "Toyota", "lexus": "Lexus", "ford": "Ford", "honda": "Honda",
        "hyundai": "Hyundai", "kia": "Kia", "mazda": "Mazda", "nissan": "Nissan",
        "mitsubishi": "Mitsubishi", "isuzu": "Isuzu", "suzuki": "Suzuki", "subaru": "Subaru",
        "byd": "BYD", "tank": "GWM Tank", "haval": "Haval", "gwm": "GWM", "geely": "Geely",
        "changan": "Changan", "jetour": "Jetour", "chery": "Chery", "deepal": "Deepal",
        "zeekr": "Zeekr", "mg": "MG", "wuling": "Wuling", "gac": "GAC", "vinfast": "VinFast",
        "mercedes": "Mercedes-Benz", "benz": "Mercedes-Benz", "bmw": "BMW", "audi": "Audi",
        "porsche": "Porsche", "land rover": "Land Rover", "range rover": "Land Rover",
        "defender": "Land Rover Defender", "discovery": "Land Rover Discovery", "jaguar": "Jaguar",
        "volvo": "Volvo", "volkswagen": "Volkswagen", "jeep": "Jeep", "chevrolet": "Chevrolet",
        "chevy": "Chevrolet", "gmc": "GMC", "ram": "RAM", "dodge": "Dodge", "tesla": "Tesla"
    }

    model_to_brand = {
        "corolla cross": "Toyota", "corolla": "Toyota", "yaris cross": "Toyota", "yaris": "Toyota",
        "camry": "Toyota", "prius": "Toyota", "raize": "Toyota", "rush": "Toyota",
        "fortuner": "Toyota", "hilux": "Toyota", "revo": "Toyota", "vigo": "Toyota",
        "land cruiser": "Toyota", "landcruiser": "Toyota", "cruiser": "Toyota", "prado": "Toyota",
        "alphard": "Toyota", "vellfire": "Toyota", "highlander": "Toyota", "harrier": "Toyota",
        "rav4": "Toyota", "tundra": "Toyota", "tacoma": "Toyota", "sienna": "Toyota",
        "sequoia": "Toyota", "crown": "Toyota", "avanza": "Toyota", "veloz": "Toyota",
        "wigo": "Toyota", "supra": "Toyota", "innova": "Toyota",
        "lx570": "Lexus", "lx600": "Lexus", "lx470": "Lexus", "rx350": "Lexus", "rx330": "Lexus", "rx300": "Lexus",
        "rx450": "Lexus", "gx460": "Lexus", "gx550": "Lexus", "gx470": "Lexus", "nx200": "Lexus",
        "nx350": "Lexus", "tx500": "Lexus", "es350": "Lexus", "es300": "Lexus", "is250": "Lexus",
        "is300": "Lexus", "ls460": "Lexus", "ls500": "Lexus",
        "ranger": "Ford", "raptor": "Ford", "wildtrak": "Ford", "everest": "Ford",
        "explorer": "Ford", "f150": "Ford", "f-150": "Ford", "territory": "Ford", "mustang": "Ford",
        "crv": "Honda", "cr-v": "Honda", "hrv": "Honda", "hr-v": "Honda", "civic": "Honda",
        "city": "Honda", "accord": "Honda", "brv": "Honda", "br-v": "Honda",
        "starex": "Hyundai", "staria": "Hyundai", "santa fe": "Hyundai", "santafe": "Hyundai",
        "tucson": "Hyundai", "creta": "Hyundai", "palisade": "Hyundai",
        "carnival": "Kia", "sorento": "Kia", "sportage": "Kia", "seltos": "Kia", "sonet": "Kia",
        "morning": "Kia", "picanto": "Kia", "bongo": "Kia",
        "atto 3": "BYD", "atto": "BYD", "seal": "BYD", "dolphin": "BYD",
        "tank 300": "GWM Tank", "tank 500": "GWM Tank",
        "monjaro": "Geely", "coolray": "Geely", "okavango": "Geely",
        "pajero": "Mitsubishi", "xpander": "Mitsubishi", "triton": "Mitsubishi",
        "d-max": "Isuzu", "dmax": "Isuzu", "mu-x": "Isuzu", "mux": "Isuzu",
        "navara": "Nissan", "terra": "Nissan", "kicks": "Nissan", "x-trail": "Nissan",
        "cx-5": "Mazda", "cx5": "Mazda", "cx-30": "Mazda", "cx30": "Mazda", "bt-50": "Mazda",
        "cayenne": "Porsche", "macan": "Porsche", "panamera": "Porsche",
        "defender": "Land Rover Defender", "wrangler": "Jeep", "rubicon": "Jeep"
    }

    vehicle_keywords = [
        "cross", "crossover", "suv", "sedan", "pickup", "truck", "coupe", "hatchback",
        "wagon", "van", "minivan", "mpv", "ev", "hybrid", "hev", "phev", "4x4", "4wd",
        "awd", "turbo", "v6", "v8", "v12", "twin turbo", "car", "cars", "auto", "automobile",
        "vehicle", "motor", "ឡាន", "រថយន្ត", "ឡានលក់", "ឡានជួល", "ក្រដាសពន្ធ", "ស្លាកលេខ",
        "ម្ចាស់ដើម", "បាឡែន", "ឆ្លាម", "គូទហើម", "ចង្កៀងពេជ្រ"
    ]

    is_car = any(b in q for b in car_brands_map) or any(m in q for m in model_to_brand) or any(v in q for v in vehicle_keywords)

    moto_cues = ["dream", "scoopy", "click", "pcx", "adv", "wave", "beat", "zoomer", "forza", "vespa", "fino", "aerox", "nvx", "xsr", "125cc", "150cc", "160cc", "ម៉ូតូ"]
    if any(m in q for m in moto_cues) and not any(ck in q for ck in ["cross", "crv", "hrv", "civic", "city", "accord", "suv", "sedan", "ឡាន", "រថយន្ត", "car"]):
        is_car = False

    phone_cues = ["iphone", "galaxy s", "redmi", "pixel", "pro max", "promax", "fold", "flip", "ទូរស័ព្ទ", "airpod", "watch", "macbook", "ipad"]
    if any(p in q for p in phone_cues) and not any(ck in q for ck in ["cross", "suv", "car", "ឡាន", "sedan", "hybrid", "4x4"]):
        is_car = False

    if is_car:
        brand = "Automotive"
        for m_key, b_val in model_to_brand.items():
            if m_key in q:
                brand = b_val
                break
        if brand == "Automotive":
            for b_key, b_val in car_brands_map.items():
                if b_key in q:
                    brand = b_val
                    break

        clean_model = query.strip()
        for prefix in ["ឡាន", "រថយន្ត", "car", "auto"]:
            if clean_model.lower().startswith(prefix + " "):
                clean_model = clean_model[len(prefix)+1:].strip()
        for b_word in ["toyota", "lexus", "ford", "honda", "hyundai", "kia", "mazda", "nissan", "mitsubishi", "isuzu", "byd", "geely", "gwm"]:
            if clean_model.lower().startswith(b_word + " "):
                clean_model = clean_model[len(b_word)+1:].strip()
                break
        model_name = clean_model.title() if clean_model else query.title()

        # Specific Car Models with Realistic Cambodia Market Pricing
        if "prius" in q:
            brand = "Toyota"
            model_name = "Prius"
            if (ext_year and ext_year <= 2009) or any(y in q for y in ["2004", "2005", "2006", "2007", "2008", "2009"]):
                y_str = str(ext_year) if ext_year else "2007"
                model_name = f"Prius {y_str} (Gen 2)"
                trims = [
                    ("Option 4 ប៊ូតុង ស្អាតទឹកថ្នាំហ្ស៊ីន ក្រដាសពន្ធ", 8200),
                    ("Option 7 ប៊ូតុង Smart Key កាមេរ៉ា JBL", 9800),
                    ("Full Option បើកដំបូល ពូកស្បែក", 10900),
                    ("Touring Edition ស្លាកលេខភ្នំពេញ ម្ចាស់ដើម", 8900)
                ]
                years = [str(ext_year)] if ext_year else ["2005", "2006", "2007", "2008", "2009"]
                core_specs = ["ម៉ាស៊ីន 1.5L Hybrid ស៊ីសាំងតិច 4.5L/100km", "ជម្រើស Option 4 ឬ 7 ប៊ូតុង", "ប្រព័ន្ធ Smart Key & JBL Sound", "ស៊េរីឆ្នាំពេញនិយម 2004-2009"]
            elif (ext_year and 2010 <= ext_year <= 2015) or any(y in q for y in ["2010", "2011", "2012", "2013", "2014", "2015", "gen 3"]):
                y_str = str(ext_year) if ext_year else "2010"
                model_name = f"Prius {y_str} (Gen 3)"
                trims = [
                    ("Option 3 1.8L Hybrid Solar Roof ស្លាកលេខភ្នំពេញ", 13800),
                    ("Option 4 កៅអីស្បែក Head-Up Display JBL", 15200),
                    ("Option 5 / Persona Series កំពូល", 16500),
                    ("1.8L Hybrid ក្រដាសពន្ធថ្មី អត់បុក", 14500)
                ]
                years = [str(ext_year)] if ext_year else ["2010", "2011", "2012", "2013", "2014"]
                core_specs = ["ម៉ាស៊ីន 1.8L Hybrid ជំនាន់ទី 3 (Gen 3)", "ជម្រើស Solar Roof ដំបូលសូឡា", "Head-Up Display & កៅអីចុច", "ស៊េរីឆ្នាំ 2010-2015"]
            elif (ext_year and 2016 <= ext_year <= 2022) or any(y in q for y in ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]):
                model_name = "Prius (Gen 4)"
                trims = [
                    ("1.8L Hybrid TNGA TSS-P ស្លាកលេខវែង", 21500),
                    ("Two-Tone Leather Seats ស៊ីសាំងតិច 3.8L/100km", 23800),
                    ("Four Touring Edition ក្រដាសពន្ធ", 25500)
                ]
                years = [str(ext_year)] if ext_year else ["2016", "2017", "2018", "2019", "2020"]
                core_specs = ["គ្រោងឆ្អឹង TNGA ប្រព័ន្ធសុវត្ថិភាព TSS-P", "ស៊ីសាំងតិចបំផុត 3.8L/100km", "ស៊េរីឆ្នាំ 2016-2022", "រូបរាងស្ព័រទំនើប"]
            else:
                model_name = "Prius 2023+ (Gen 5)"
                trims = [
                    ("2.0L Hybrid LE / XLE New Body Shape 2023+", 38500),
                    ("2.0L PHEV Prime Plug-In Hybrid", 43500)
                ]
                years = ["2024", "2023"]
                core_specs = ["ម៉ាស៊ីន 2.0L Hybrid ជំនាន់ថ្មី Gen 5", "កម្លាំង 196HP បង្កើនល្បឿនស្ទុះ", "រចនាបថទំនើបបែប Coupe", "TSS 3.0 Full System"]

        elif "camry" in q:
            brand = "Toyota"
            if (ext_year and ext_year <= 2006) or "បាឡែន" in q or any(y in q for y in ["2002", "2003", "2004", "2005", "2006"]):
                model_name = "Camry បាឡែន"
                trims = [
                    ("2.4L LE បាឡែន ស្លាកលេខភ្នំពេញ ទឹកថ្នាំហ្ស៊ីន", 9200),
                    ("2.4L XLE ពូកស្បែក កៅអីចុច បើកដំបូល", 11500),
                    ("2.4L LE ក្រដាសពន្ធថ្មី ម៉ាស៊ីនស្ងាត់", 10200)
                ]
                years = [str(ext_year)] if ext_year else ["2002", "2003", "2004", "2005", "2006"]
                core_specs = ["ម៉ាស៊ីន 2.4L VVT-i ធន់ស្វិត", "ពូកស្បែក កៅអីចុច បើកដំបូល (XLE)", "រថយន្តពេញនិយមស៊េរីបាឡែន", "ស៊េរីឆ្នាំ 2002-2006"]
            elif (ext_year and 2007 <= ext_year <= 2011) or "គូទហើម" in q or any(y in q for y in ["2007", "2008", "2009", "2010", "2011"]):
                model_name = "Camry គូទហើម"
                trims = [
                    ("2.4L Hybrid គូទហើម សន្សំសំចៃសាំង ស្លាកលេខ 2A-2B", 13500),
                    ("2.4L LE ពូកស្បែក កៅអីចុច ម៉ាស៊ីនស្អាត", 12800),
                    ("2.4L XLE Full Option ដំបូលបើក Smart Key", 15800)
                ]
                years = [str(ext_year)] if ext_year else ["2007", "2008", "2009", "2010", "2011"]
                core_specs = ["ម៉ាស៊ីន 2.4L Hybrid / Gasoline គូទហើម", "Smart Key & Start/Stop Engine", "កៅអីចុចសងខាង ដំបូលបើក", "ស៊េរីឆ្នាំ 2007-2011"]
            elif ext_year and 2012 <= ext_year <= 2017:
                model_name = "Camry (2012-2017)"
                trims = [
                    ("2.5L Hybrid XLE Smart Key ស្លាកលេខភ្នំពេញ", 19500),
                    ("2.5L LE មួយទឹកស្អាត ឯកសារគ្រប់", 17500),
                    ("2.5L XLE Full Option កៅអីចុចសងខាង", 22800)
                ]
                years = [str(ext_year)] if ext_year else ["2012", "2013", "2014", "2015"]
                core_specs = ["ម៉ាស៊ីន 2.5L Hybrid / Gasoline", "រាងកណ្តុរស្ព័រ ខាងក្នុងធំទូលាយ", "Smart Key & Reverse Camera", "ស៊េរីឆ្នាំ 2012-2017"]
            else:
                model_name = "Camry (2018+)"
                trims = [
                    ("2.5L Hybrid TNGA Dynamic Force ស្អាត 99%", 34500),
                    ("2.5L XLE Sunroof Head-Up Display", 37800),
                    ("2.0L / 2.5L ក្រដាសពន្ធថ្មី ធានាមជ្ឈមណ្ឌល", 39800)
                ]
                years = ["2024", "2023", "2022", "2020"]
                core_specs = ["គ្រោងឆ្អឹង TNGA ម៉ាស៊ីន Dynamic Force", "កញ្ចក់មើលផ្លូវ HUD & Panoramic Sunroof", "Toyota Safety Sense (TSS)", "ស៊េរីឆ្នាំ 2018-2024"]

        elif "highlander" in q:
            brand = "Toyota"
            if (ext_year and ext_year <= 2007) or any(y in q for y in ["2001", "2002", "2003", "2004", "2005", "2006", "2007"]):
                y_str = str(ext_year) if ext_year else "2003"
                model_name = f"Highlander {y_str}"
                trims = [
                    ("V6 3.0L / 3.3L Limited 4WD ប៉ុង 2 បើកដំបូល", 12800),
                    ("2.4L Base Option ប៉ុង 1 ស្លាកលេខភ្នំពេញ", 10200),
                    ("V6 3.3L Hybrid Limited 7-Seats", 13900)
                ]
                years = [str(ext_year)] if ext_year else ["2001", "2002", "2003", "2004", "2005"]
                core_specs = ["ម៉ាស៊ីន V6 3.0L / 3.3L / 2.4L 4WD", "ប៉ុង 1 ឬ ប៉ុង 2 ដំបូលបើក", "ពូកស្បែក កៅអី 2-3 ជួរ", "ស៊េរីឆ្នាំ 2001-2007"]
            elif (ext_year and 2008 <= ext_year <= 2013) or any(y in q for y in ["2008", "2009", "2010", "2011", "2012", "2013"]):
                model_name = "Highlander (2008-2013)"
                trims = [
                    ("2.7L Base Option កៅអី 3 ជួរ ស្លាកលេខ 2x", 19500),
                    ("3.5L V6 Limited Full Option ដំបូលបើក JBL", 24500)
                ]
                years = [str(ext_year)] if ext_year else ["2008", "2010", "2012"]
                core_specs = ["ម៉ាស៊ីន 2.7L / 3.5L V6 កៅអី 3 ជួរ", "ដំបូលបើក Sunroof & Smart Key", "JBL Premium Audio", "ស៊េរីឆ្នាំ 2008-2013"]
            else:
                model_name = "Highlander (New Gen)"
                trims = [
                    ("3.5L V6 XLE Captain Seats 7-Seats", 33500),
                    ("2.5L Hybrid Platinum / Limited AWD", 58000)
                ]
                years = ["2024", "2023", "2021", "2018"]
                core_specs = ["ម៉ាស៊ីន V6 / 2.5L Hybrid 7-Seats", "Captain Chairs & Panoramic Roof", "Toyota Safety Sense (TSS)", "ស៊េរីឆ្នាំ 2018-2024"]

        elif "rx" in q and ("lexus" in q or "rx300" in q or "rx330" in q or "rx350" in q):
            brand = "Lexus"
            if "rx300" in q or "rx 300" in q:
                model_name = "RX300"
                trims = [("3.0L V6 AWD ប៉ុង 2 ស្លាកលេខភ្នំពេញ ទឹកថ្នាំស្អាត", 9800), ("3.0L V6 Base Option ឯកសារគ្រប់", 8800)]
                years = ["2001", "2002", "2003"]
                core_specs = ["ម៉ាស៊ីន 3.0L V6 AWD ប៉ុង 2", "ពូកស្បែក ដំបូលបើក", "ស៊េរីឆ្នាំ 1999-2003"]
            elif "rx330" in q or "rx 330" in q:
                model_name = "RX330"
                trims = [
                    ("3.3L V6 AWD Base Option ប៉ុង 2 បើកដំបូល", 17500),
                    ("3.3L V6 Full Option Laser Cruise កាមេរ៉ា", 21500),
                    ("3.3L Half Full ប៉ុង 1 ស្លាកលេខវែង", 18500)
                ]
                years = ["2004", "2005", "2006"]
                core_specs = ["ម៉ាស៊ីន 3.3L V6 AWD", "Option Laser Cruise Control & កាមេរ៉ាក្រោយ", "បើកដំបូល ពូកស្បែក ចង្កៀងគុជ", "ស៊េរីឆ្នាំ 2004-2006"]
            else: # RX350
                model_name = "RX350"
                if (ext_year and ext_year <= 2009) or any(y in q for y in ["2007", "2008", "2009"]):
                    trims = [("3.5L V6 AWD Full Option បើកដំបូល ពូកស្បែក", 23500), ("3.5L V6 Touring ស្លាកលេខភ្នំពេញ", 21500)]
                    years = ["2007", "2008", "2009"]
                    core_specs = ["ម៉ាស៊ីន 3.5L V6 Dual VVT-i AWD", "កាមេរ៉ាក្រោយ & Smart Key", "ស៊េរីឆ្នាំ 2007-2009"]
                elif (ext_year and ext_year <= 2015) or any(y in q for y in ["2010", "2011", "2012", "2013", "2014", "2015"]):
                    trims = [("3.5L V6 AWD F-Sport Mouse Control Head-Up Display", 34500), ("3.5L V6 Base Option ស្អាត 99%", 29800)]
                    years = ["2010", "2011", "2012", "2013"]
                    core_specs = ["ម៉ាស៊ីន 3.5L V6 F-Sport AWD", "កណ្តុរបញ្ជា Remote Touch & HUD", "ស៊េរីឆ្នាំ 2010-2015"]
                elif (ext_year and ext_year <= 2022) or any(y in q for y in ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]):
                    trims = [("3.5L V6 F-Sport Triple Beam LED Panoramic Roof", 68000), ("3.5L V6 AWD Premium ក្រដាសពន្ធថ្មី", 62000)]
                    years = ["2016", "2017", "2018", "2020"]
                    core_specs = ["ចង្កៀងមុខ Triple Beam LED & ដំបូលកញ្ចក់", "កៅអីត្រជាក់-ក្តៅ & 360 Camera", "ស៊េរីឆ្នាំ 2016-2022"]
                else:
                    trims = [("2.4L Turbo AWD F-Sport Performance 2023+", 115000), ("350h Hybrid Luxury 2024", 125000)]
                    years = ["2024", "2023"]
                    core_specs = ["ម៉ាស៊ីន 2.4L Turbo / 2.5L Hybrid F-Sport", "អេក្រង់ 14-inch Touchscreen", "ស៊េរីឆ្នាំ 2023-2024"]

        elif "land cruiser" in q or "cruiser" in q:
            brand = "Toyota"
            model_name = "Land Cruiser"
            if (ext_year and ext_year <= 2015) or any(y in q for y in ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]):
                trims = [("V8 4.6L GXR Full Option 7-Seats", 49000), ("V8 5.7L VXR Arabian Spec", 68000)]
                years = ["2008", "2010", "2012", "2014"]
                core_specs = ["ម៉ាស៊ីន V8 4.6L / 5.7L 4WD", "ពូកស្បែក 7 កៅអី ទូរទឹកកក", "ស៊េរីឆ្នាំ 2008-2015 (LC200)"]
            elif (ext_year and ext_year <= 2021) or any(y in q for y in ["2016", "2017", "2018", "2019", "2020", "2021"]):
                trims = [("V8 5.7L VXR Super Sport / Executive Lounge", 108000), ("V8 4.6L GXR Upgrade VXR ស្អាត", 84000)]
                years = ["2016", "2017", "2018", "2020"]
                core_specs = ["ម៉ាស៊ីន V8 5.7L VXR Super Sport", "ទូរទឹកកក បូមខ្យល់ កាមេរ៉ា 360", "ស៊េរីឆ្នាំ 2016-2021 (LC200 Facelift)"]
            else: # LC300
                trims = [("3.5L V6 Twin-Turbo ZX Option កំពូល", 168000), ("3.5L Twin-Turbo GR-Sport 4x4", 152000)]
                years = ["2024", "2023", "2022"]
                core_specs = ["ម៉ាស៊ីន 3.5L V6 Twin-Turbo (LC300)", "Option កំពូល ZX & GR-Sport", "កៅអី 7-Seats Full Luxury VIP", "ស៊េរីឆ្នាំ 2022-2024"]

        elif "cross" in q or "corolla cross" in q:
            brand = "Toyota"
            model_name = "Corolla Cross"
            trims = [
                ("1.8L Hybrid (HEV) ស៊ីសាំងតិច 3.9L/100km Full Option", 41500),
                ("1.8L Gasoline Premium Auto ក្រដាសពន្ធថ្មី", 37800),
                ("GR-Sport Package 5-Seats Sunroof Smart Key", 43500),
                ("1.8L Smart Edition ស្លាកលេខភ្នំពេញ ម្ចាស់ដើម 99%", 34900)
            ]
            years = ["2024", "2023", "2022", "2021"]
            core_specs = ["ម៉ាស៊ីន 1.8L Hybrid HEV / 1.8L Gasoline", "ស៊ីសាំងតិច 3.9L/100km (HEV)", "Toyota Safety Sense (TSS)", "ស៊េរីឆ្នាំ 2021-2024"]

        elif "monjaro" in q:
            brand = "Geely"
            model_name = "Monjaro"
            trims = [
                ("2.0L Turbo Flagship AWD CMA Platform", 41500),
                ("2.0L Turbo Luxury 3-Screens Interior", 38500)
            ]
            years = ["2024", "2023"]
            core_specs = ["ម៉ាស៊ីន 2.0L Turbo Volvo CMA Platform", "អេក្រង់ 3 ផ្ទាំង Panoramic Interior", "ប្រព័ន្ធបើកបរ AWD & Smart Driving", "ស៊េរីឆ្នាំ 2023-2024"]

        elif "atto" in q:
            brand = "BYD"
            model_name = "Atto 3"
            trims = [
                ("Extended Range 510km Blade Battery Ultra", 35500),
                ("Standard Range 410km Smart Auto", 32500)
            ]
            years = ["2024", "2023"]
            core_specs = ["អាគុយ Blade Battery សុវត្ថិភាពខ្ពស់", "ចម្ងាយរត់ 480-510km ក្នុងមួយសាកពេញ", "អេក្រង់បង្វិល 15.6-inch", "ស៊េរីឆ្នាំ 2023-2024"]

        else: # Generic Car
            trims = [
                ("Full Option Sunroof Leather Seats Smart Auto", 32500),
                ("Hybrid Full Option ស៊ីសាំងតិច ម្ចាស់ដើម", 27800),
                ("Half Full Option ស្លាកលេខភ្នំពេញ ស្អាត 99%", 21500)
            ]
            years = ["2024", "2023", "2022", "2021"]
            core_specs = [f"ម៉ូដែល {model_name} Full Option", "កៅអីស្បែក & ប្រព័ន្ធសុវត្ថិភាព", "រថយន្តពេញនិយមនៅកម្ពុជា", "ស៊េរីឆ្នាំ 2021-2024"]

        return {
            "domain": "CARS", "category": "CARS", "category_label": "រថយន្ត / Cars",
            "brand": brand, "model": model_name, "years": years, "trims": trims,
            "core_specs": core_specs, "is_vehicle": True
        }

    # Motos
    if any(k in q for k in ["dream", "scoopy", "click", "pcx", "adv", "wave", "beat", "ម៉ូតូ"]):
        if "dream" in q:
            brand = "Honda"
            model_name = "Dream 125"
            if (ext_year and ext_year >= 2024) or "2024" in q:
                trims = [("NCX Cambodia 125cc PGM-FI ថ្មីកេះ 100%", 2350), ("ស៊េរីឆ្នាំ 2024 តែមមាស ស្លាកលេខភ្នំពេញ", 2200)]
                years = ["2024"]
                core_specs = ["ម៉ាស៊ីន 125cc PGM-FI សន្សំសំចៃសាំង", "តែមមាស Gold Emblem & ចង្កៀង LED", "ផលិតផល NCX Cambodia ថ្មីកេះ", "ស៊េរីឆ្នាំ 2024"]
            elif (ext_year and ext_year >= 2020) or any(y in q for y in ["2020", "2021", "2022", "2023"]):
                trims = [("125cc NCX ស្លាកលេខភ្នំពេញ ម្ចាស់ដើម", 1850), ("Dream ស៊េរីឆ្នាំស្អាត ម៉ាស៊ីនហ្ស៊ីន", 1650)]
                years = [str(ext_year)] if ext_year else ["2020", "2021", "2022", "2023"]
                core_specs = ["ម៉ាស៊ីន 125cc សំណុំហ្ស៊ីន", "កាតគ្រីត្រឹមត្រូវ ម្ចាស់ដើម", "ស៊េរីឆ្នាំ 2020-2023"]
            else:
                trims = [("សេ១២៥ ស៊េរីចាស់ ស្លាកលេខភ្នំពេញ", 1150), ("125cc កាតគ្រីគ្រប់ ម៉ាស៊ីនស្ងាត់", 950)]
                years = ["2018", "2016", "2014"]
                core_specs = ["ម៉ូតូ Honda Dream សេ១២៥", "ម៉ាស៊ីនស្ងាត់ ធន់ស្វិត", "តម្លៃសមរម្យ"]
        elif "scoopy" in q:
            brand = "Honda"
            model_name = "Scoopy-i"
            if (ext_year and ext_year >= 2024) or "2024" in q:
                trims = [("Club12 Smart Key កង់រង្វង់ 12 ថ្មីកេះ", 2280), ("Prestige LED 110cc PGM-FI ថ្មីកេះ", 2150)]
                years = ["2024"]
                core_specs = ["ម៉ាស៊ីន 110cc eSP PGM-FI", "Smart Key បញ្ឆេះដោយមិនបាច់ប្រើសោ", "កង់រង្វង់ 12 Club12 Sport", "ស៊េរីឆ្នាំ 2024"]
            else:
                trims = [("Smart Key ស្លាកលេខភ្នំពេញ ស្អាត 99%", 1650), ("Prestige 110cc ម្ចាស់ដើម", 1450)]
                years = ["2023", "2022", "2021"]
                core_specs = ["ម៉ាស៊ីន 110cc eSP ស៊ីសាំងតិច", "Smart Key ប្រព័ន្ធសុវត្ថិភាព", "ស៊េរីឆ្នាំ 2020-2023"]
        elif "pcx" in q:
            brand = "Honda"
            model_name = "PCX 160"
            trims = [("eSP+ 160cc 4-Valve ABS Smart Key ថ្មីកេះ", 3950), ("HSTC System ស្លាកលេខភ្នំពេញ ស្អាត 99%", 3650)]
            years = ["2024", "2023"]
            core_specs = ["ម៉ាស៊ីន eSP+ 160cc 4-Valve", "ប្រព័ន្ធហ្វ្រាំង ABS & HSTC", "ឃ្លុបក្រោមកៅអីធំទូលាយ 30L", "ស៊េរីឆ្នាំ 2023-2024"]
        elif "adv" in q:
            brand = "Honda"
            model_name = "ADV 160"
            trims = [("160cc Adventure Scooter Showa Subtank ថ្មីកេះ", 4350), ("ABS Smart Key ស្លាកលេខវែង", 4050)]
            years = ["2024", "2023"]
            core_specs = ["ម៉ាស៊ីន 160cc eSP+ 4-Valve", "បូម Showa Sub-tank ខាងក្រោយ", "Adventure Touring Design", "ស៊េរីឆ្នាំ 2023-2024"]
        else:
            brand = "Honda"
            model_name = query.title()
            trims = [("125cc / 160cc ថ្មីកេះ 100%", 2450), ("ស្អាត 99% ស្លាកលេខភ្នំពេញ", 2150)]
            years = ["2024", "2023"]
            core_specs = ["ម៉ាស៊ីន PGM-FI សន្សំសំចៃសាំង", "Smart Key & ប្រព័ន្ធសុវត្ថិភាព", "ម៉ូតូពេញនិយមនៅកម្ពុជា"]

        return {
            "domain": "MOTOS", "category": "MOTOS", "category_label": "ម៉ូតូ / Motorcycles",
            "brand": brand, "model": model_name, "years": years, "trims": trims,
            "core_specs": core_specs, "is_vehicle": True
        }

    # Phones / Audio / Electronics
    is_promax = ("pro max" in q or "promax" in q)
    is_pro = ("pro" in q and not is_promax)
    is_plus = ("plus" in q)
    is_mini = ("mini" in q)

    if "airpod" in q:
        brand = "Apple"
        if "max" in q:
            model_name = "AirPods Max"
            trims = [("Smart Case Space Gray / Silver ស្អាត 99%", 390), ("New in Box ថ្មីកេះ ធានាមជ្ឈមណ្ឌល", 460)]
            years = ["Over-Ear"]
            core_specs = ["កាសគ្របត្រចៀក Over-Ear Hi-Fi Audio", "ប្រព័ន្ធកាត់សម្លេងរំខាន ANC កម្រិតខ្ពស់", "តួខ្លួន Aluminum & Memory Foam", "ថាមពលថ្មប្រើបាន 20 ម៉ោង"]
        elif "pro 2" in q or "pro2" in q or ("pro" in q and ("usb" in q or "type-c" in q or "c" in q or "2" in q)):
            model_name = "AirPods Pro 2"
            trims = [("USB-C MagSafe Case ANC 2x ថ្មីកេះ 100%", 210), ("Type-C ស្អាត 99% សំណុំហ្ស៊ីន ធានា", 185)]
            years = ["USB-C Case"]
            core_specs = ["បន្ទះឈីប Apple H2 Chip ជំនាន់ថ្មី", "ប្រព័ន្ធកាត់សម្លេង ANC ខ្លាំងជាងមុន 2 ដង", "រន្ធសាកថ្ម USB-C & MagSafe Case", "Adaptive Audio & Transparency Mode"]
        elif "pro" in q:
            model_name = "AirPods Pro"
            trims = [("Active Noise Cancelling (ANC) Full Box ថ្មីកេះ", 165), ("MagSafe Charging Case ស្អាត 99%", 135)]
            years = ["MagSafe Case"]
            core_specs = ["ប្រព័ន្ធកាត់សម្លេង Active Noise Cancelling", "MagSafe Wireless Charging Case", "Transparency Mode ស្តាប់សម្លេងជុំវិញ", "កៅស៊ូញាត់ត្រចៀក 3 ទំហំ"]
        elif "4" in q:
            model_name = "AirPods 4"
            trims = [("ANC Edition USB-C ថ្មីកេះ 100%", 169), ("Standard Edition H2 Chip", 139)]
            years = ["USB-C Case"]
            core_specs = ["រចនាបថថ្មី Open-Ear ពាក់មិនឈឺត្រជៀក", "បន្ទះឈីប H2 Chip សម្លេងច្បាស់", "ជម្រើសមាន ANC Active Noise Cancelling", "រន្ធសាកថ្ម USB-C"]
        elif "2" in q:
            model_name = "AirPods 2"
            trims = [("Wireless Charging Case ស្អាត 99%", 85), ("Charging Case ថ្មីកេះ 100%", 95)]
            years = ["Charging Case"]
            core_specs = ["បន្ទះឈីប Apple H1 Chip", "ទម្ងន់ស្រាល ពាក់ស្រួលត្រចៀក", "ថ្មកាន់បាន 5 ម៉ោង (សរុប 24 ម៉ោង)", "តម្លៃសមរម្យបំផុត"]
        else:
            model_name = "AirPods 3"
            trims = [("MagSafe Charging Case ស្អាត 99%", 125), ("Lightning Case ថ្មីកេះ", 140)]
            years = ["MagSafe Case"]
            core_specs = ["Spatial Audio សម្លេងជុំទិស 3D", "រចនាបថថ្មីទ្រវែងខ្លី មិនជ្រុះ", "ធន់នឹងទឹក និងញើស IPX4", "ថ្មកាន់បាន 6 ម៉ោង"]

        return {
            "domain": "ELECTRONICS", "category": "ELECTRONICS", "category_label": "គ្រឿងអេឡិចត្រូនិក / Electronics",
            "brand": brand, "model": model_name, "years": years, "trims": trims,
            "core_specs": core_specs, "is_vehicle": False
        }

    if "watch" in q and ("apple" in q or "iwatch" in q or "series" in q or "ultra" in q):
        brand = "Apple"
        if "ultra 2" in q or "ultra2" in q:
            model_name = "Apple Watch Ultra 2"
            trims = [("Titanium Case 49mm Trail Loop ថ្មីកេះ 100%", 740), ("Titanium Case 49mm Ocean Band ស្អាត 99%", 670)]
            core_specs = ["តួខ្លួន Titanium 49mm អេក្រង់ 3000 nits", "បន្ទះឈីប S9 SiP & កាយវិការ Double Tap", "ថាមពលថ្ម 36-72 ម៉ោង", "ធន់នឹងទឹកជម្រៅ 100m"]
        elif "ultra" in q:
            model_name = "Apple Watch Ultra"
            trims = [("Titanium 49mm Alpine Loop ស្អាត 99%", 520), ("Full Box សំណុំហ្ស៊ីន ថ្ម 98%", 480)]
            core_specs = ["តួខ្លួន Titanium 49mm អេក្រង់ Sapphire", "ប៊ូតុង Action Button ពណ៌ទឹកក្រូច", "Dual-Frequency GPS ត្រឹមត្រូវខ្ពស់", "ស៊េរីឆ្នាំ Ultra 1"]
        elif "9" in q or "series 9" in q:
            model_name = "Apple Watch Series 9"
            trims = [("45mm GPS Midnight Aluminum ថ្មីកេះ 100%", 340), ("41mm Starlight ស្អាត 99%", 295)]
            core_specs = ["បន្ទះឈីប S9 SiP & កាយវិការ Double Tap", "អេក្រង់ភ្លឺ 2000 nits", "ឆែកសុខភាពបេះដូង & ECG", "ស៊េរីឆ្នាំ 2023-2024"]
        elif "8" in q or "series 8" in q:
            model_name = "Apple Watch Series 8"
            trims = [("45mm GPS Midnight ស្អាត 99%", 260), ("41mm Silver Aluminum", 230)]
            core_specs = ["សេនស័រវាស់កម្តៅ Temperature Sensor", "ប្រព័ន្ធចាប់ការបុកទង្គិច Crash Detection", "ECG & Blood Oxygen", "ស៊េរីឆ្នាំ 2022-2023"]
        elif "se" in q:
            model_name = "Apple Watch SE 2"
            trims = [("44mm GPS ស្អាត 99%", 195), ("40mm Starlight ស្អាត 99%", 165)]
            core_specs = ["បន្ទះឈីប S8 SiP ល្បឿនលឿន", "អេក្រង់ Retina Display", "តម្លៃសមរម្យសម្រាប់កីឡា និងសុខភាព", "ស៊េរីឆ្នាំ SE Gen 2"]
        else:
            model_name = "Apple Watch"
            trims = [("GPS + Cellular Aluminum Case ស្អាត 99%", 250), ("Sport Band Full Box", 210)]
            core_specs = ["អេក្រង់ OLED Retina Display", "តាមដានចង្វាក់បេះដូង និងជំហានដើរ", "ភ្ជាប់ជាមួយ iPhone យ៉ាងរលូន"]
        years = ["45mm", "49mm Ultra", "41mm", "44mm"]
        return {
            "domain": "WATCHES", "category": "WATCHES", "category_label": "នាឡិកាដៃ / Watches",
            "brand": brand, "model": model_name, "years": years, "trims": trims,
            "core_specs": core_specs, "is_vehicle": False
        }

    if "macbook" in q:
        brand = "Apple"
        if "pro" in q:
            if "m3" in q:
                model_name = "MacBook Pro M3"
                trims = [("14-inch M3 16GB RAM 512GB SSD Space Gray ថ្មីកេះ", 1580), ("16-inch M3 Pro 18GB RAM 512GB SSD", 2150)]
                core_specs = ["បន្ទះឈីប Apple M3 / M3 Pro (3nm)", "អេក្រង់ Liquid Retina XDR 120Hz ProMotion", "អង្គចងចាំ 16GB-18GB Unified Memory", "ថ្មកាន់បានរហូតដល់ 22 ម៉ោង"]
            elif "m2" in q:
                model_name = "MacBook Pro M2"
                trims = [("14-inch M2 Pro 16GB RAM 512GB SSD ស្អាត 99%", 1350), ("13-inch M2 8GB 256GB", 980)]
                core_specs = ["បន្ទះឈីប Apple M2 / M2 Pro", "អេក្រង់ Liquid Retina XDR 120Hz", "16GB RAM 512GB SSD", "ថ្មកាន់បាន 18 ម៉ោង"]
            elif "m1" in q:
                model_name = "MacBook Pro M1"
                trims = [("14-inch M1 Pro 16GB RAM 512GB SSD ស្អាត 99%", 1050), ("13-inch M1 8GB 256GB ថ្ម 90%+", 750)]
                core_specs = ["បន្ទះឈីប Apple M1 / M1 Pro", "អេក្រង់ Liquid Retina XDR", "ល្បឿនកាត់តវីដេអូ 4K ស្មូត", "ស៊េរីពេញនិយម"]
            else:
                model_name = "MacBook Pro"
                trims = [("14-inch Apple Silicon 16GB RAM 512GB SSD", 1450), ("Retina Display ស្អាត 99% សំណុំហ្ស៊ីន", 1150)]
                core_specs = ["បន្ទះឈីប Apple Silicon", "អេក្រង់ Liquid Retina XDR", "អង្គចងចាំ 16GB RAM 512GB SSD"]
        else: # MacBook Air
            if "m3" in q:
                model_name = "MacBook Air M3"
                trims = [("13.6-inch M3 8GB 256GB Midnight ថ្មីកេះ 100%", 980), ("15.3-inch M3 16GB 512GB Starlight", 1350)]
                core_specs = ["បន្ទះឈីប Apple M3 (3nm) ជំនាន់ថ្មី", "អេក្រង់ Liquid Retina 13.6\" / 15.3\"", "តួខ្លួនស្តើងស្រាល គ្មានកង្ហារស្ងាត់ល្អ", "ថ្មកាន់បាន 18 ម៉ោង"]
            elif "m2" in q:
                model_name = "MacBook Air M2"
                trims = [("13.6-inch M2 8GB 256GB Midnight ស្អាត 99%", 790), ("15.3-inch M2 16GB 512GB", 1050)]
                core_specs = ["បន្ទះឈីប Apple M2 ជំនាន់ទី 2", "រចនាបថរាងជ្រុងស្អាត MagSafe 3", "អេក្រង់ Liquid Retina 13.6\"", "ពណ៌ Midnight & Starlight"]
            else: # M1 Air
                model_name = "MacBook Air M1"
                trims = [("13.3-inch M1 8GB 256GB Space Gray ស្អាត 99%", 580), ("13.3-inch M1 16GB 512GB ស្អាត", 720)]
                core_specs = ["បន្ទះឈីប Apple M1 8-Core CPU", "ទម្ងន់ស្រាល 1.29kg គ្មានកង្ហារស្ងាត់", "អង្គចងចាំ 8GB RAM 256GB SSD", "ថ្មកាន់បាន 15-18 ម៉ោង តម្លៃធូរដាច់គេ"]
        years = ["16GB / 512GB", "8GB / 256GB", "16GB / 1TB"]
        return {
            "domain": "COMPUTERS", "category": "COMPUTERS", "category_label": "កុំព្យូទ័រ / Computers",
            "brand": brand, "model": model_name, "years": years, "trims": trims,
            "core_specs": core_specs, "is_vehicle": False
        }

    # iPhones
    brand = "Apple" if ("iphone" in q or "apple" in q or "pro max" in q) else "Samsung"
    if "17" in q and ("iphone" in q or "apple" in q or "pro" in q or "max" in q):
        if is_promax:
            model_name = "iPhone 17 Pro Max"
            trims = [("256GB Concept Pre-Order VIP Spec", 1750), ("512GB A19 Pro Bionic 12GB RAM Next-Gen", 1950), ("1TB Extreme Titanium Edition Pre-Order", 2150)]
            core_specs = ["បន្ទះឈីប A19 Pro Bionic (2nm)", "អង្គចងចាំ 12GB RAM Next-Gen AI", "Pre-Order VIP Spec 256GB - 2TB", "ពណ៌ Cosmic Titanium", "Camera 48MP Periscope 10x"]
        elif is_pro:
            model_name = "iPhone 17 Pro"
            trims = [("128GB A19 Pro Bionic 12GB RAM", 1450), ("256GB Pro Edition Pre-Order", 1620)]
            core_specs = ["បន្ទះឈីប A19 Pro (2nm) 12GB RAM", "អេក្រង់ 6.3\" ProMotion 120Hz", "Pre-Order VIP Edition", "រចនាបថ Titanium ស្តើង"]
        elif "slim" in q or "air" in q:
            model_name = "iPhone 17 Air"
            trims = [("256GB Ultra Slim Design A19", 1180), ("512GB Ultra Thin Body", 1350)]
            core_specs = ["តួខ្លួនស្តើងបំផុត Ultra-Slim Design", "បន្ទះឈីប A19 Bionic", "អេក្រង់ 6.6\" OLED 120Hz"]
        else:
            model_name = "iPhone 17"
            trims = [("128GB A19 Bionic ថ្មីកេះ 100%", 950), ("256GB Dual Camera Next-Gen", 1080)]
            core_specs = ["បន្ទះឈីប Apple A19 Bionic", "អេក្រង់ OLED 120Hz ProMotion", "កាមេរ៉ាភ្លោះ 48MP Dual Camera"]
        years = ["256GB", "512GB", "1TB"]

    elif "16" in q and ("iphone" in q or "apple" in q or "pro" in q or "max" in q):
        if is_promax:
            model_name = "iPhone 16 Pro Max"
            trims = [("256GB Desert Titanium ថ្មីកេះ 100% LL/A-ZA/A", 1320), ("512GB A18 Pro Camera Control ស្អាត 99%", 1490), ("1TB Full Box ធានាមជ្ឈមណ្ឌល", 1690), ("256GB សំណុំហ្ស៊ីន ថ្ម 100% ម្ចាស់ដើម", 1260)]
            core_specs = ["បន្ទះឈីប A18 Pro (3nm)", "ប៊ូតុង Camera Control ថ្មី", "ទំហំ 256GB, 512GB, 1TB", "ពណ៌ Desert Titanium", "Camera 48MP Telephoto 5x"]
            years = ["256GB", "512GB", "1TB"]
        elif is_pro:
            model_name = "iPhone 16 Pro"
            trims = [("128GB Desert Titanium ថ្មីកេះ 100%", 1120), ("256GB A18 Pro Camera Control ស្អាត 99%", 1220), ("512GB Full Box ធានាមជ្ឈមណ្ឌល", 1380)]
            core_specs = ["បន្ទះឈីប A18 Pro (3nm)", "អេក្រង់ 6.3\" ProMotion 120Hz", "ប៊ូតុង Camera Control & Action Button", "Camera 48MP Telephoto 5x"]
            years = ["128GB", "256GB", "512GB"]
        elif is_plus:
            model_name = "iPhone 16 Plus"
            trims = [("128GB Ultramarine ថ្មីកេះ 100%", 920), ("256GB Teal Dual Camera A18", 1020)]
            core_specs = ["អេក្រង់ធំ 6.7\" Dynamic Island", "បន្ទះឈីប A18 Bionic", "ប៊ូតុង Camera Control", "ពណ៌ Ultramarine & Teal"]
            years = ["128GB", "256GB"]
        else:
            model_name = "iPhone 16"
            trims = [("128GB Ultramarine ថ្មីកេះ 100%", 799), ("256GB Dual Camera A18 ថ្មីប្រអប់", 899), ("512GB Full Option ធានា 1 ឆ្នាំ", 1099)]
            core_specs = ["បន្ទះឈីប A18 Bionic (3nm)", "ប៊ូតុង Camera Control ថ្មី", "កាមេរ៉ា 48MP Fusion Camera", "ពណ៌ស្រស់ស្អាត Ultramarine/Pink"]
            years = ["128GB", "256GB", "512GB"]

    elif "15" in q and ("iphone" in q or "apple" in q or "pro" in q or "max" in q):
        if is_promax:
            model_name = "iPhone 15 Pro Max"
            trims = [("256GB Natural Titanium ស្អាត 99% សំណុំហ្ស៊ីន", 940), ("512GB A17 Pro Action Button ថ្ម 95%", 1080), ("1TB Full Box ធានាមជ្ឈមណ្ឌល", 1220), ("256GB ពណ៌ Blue Titanium ស្អាត", 890)]
            core_specs = ["បន្ទះឈីប A17 Pro (3nm)", "តួខ្លួន Titanium ស្រាលធន់", "ប៊ូតុង Action Button ថ្មី", "Camera 5x Optical Zoom"]
            years = ["256GB", "512GB", "1TB"]
        elif is_pro:
            model_name = "iPhone 15 Pro"
            trims = [("128GB Natural Titanium ស្អាត 99%", 790), ("256GB A17 Pro Action Button", 880), ("512GB Full Box", 990)]
            core_specs = ["បន្ទះឈីប A17 Pro (3nm)", "តួខ្លួន Titanium អេក្រង់ 6.1\" 120Hz", "ប៊ូតុង Action Button", "Camera 3x Optical Zoom"]
            years = ["128GB", "256GB", "512GB"]
        elif is_plus:
            model_name = "iPhone 15 Plus"
            trims = [("128GB Dynamic Island ថ្មី 99%", 660), ("256GB Type-C 48MP Camera", 740)]
            core_specs = ["អេក្រង់ធំ 6.7\" Dynamic Island", "រន្ធសាក USB-C ថ្មី", "ថ្មកាន់បានយូរដាច់គេ"]
            years = ["128GB", "256GB"]
        else:
            model_name = "iPhone 15"
            trims = [("128GB Dynamic Island ថ្មី 99%", 560), ("256GB Type-C 48MP Camera", 650)]
            core_specs = ["Dynamic Island & រន្ធសាក USB-C", "កាមេរ៉ាមេ 48MP Main Camera", "បន្ទះឈីប A16 Bionic"]
            years = ["128GB", "256GB"]

    elif "14" in q and ("iphone" in q or "apple" in q or "pro" in q or "max" in q):
        if is_promax:
            model_name = "iPhone 14 Pro Max"
            trims = [("128GB Deep Purple ស្អាត 99% ថ្ម 90%", 690), ("256GB Dynamic Island A16 Bionic", 780), ("512GB Full Box", 880)]
            core_specs = ["Dynamic Island ដំបូងគេ", "បន្ទះឈីប A16 Bionic", "Camera 48MP Pro System", "ពណ៌ Deep Purple ពេញនិយម"]
        elif is_pro:
            model_name = "iPhone 14 Pro"
            trims = [("128GB Deep Purple ស្អាត 99%", 590), ("256GB Dynamic Island A16", 670), ("512GB ស្អាត", 750)]
            core_specs = ["Dynamic Island & Always-On Display", "អេក្រង់ 6.1\" ProMotion 120Hz", "បន្ទះឈីប A16 Bionic"]
        else:
            model_name = "iPhone 14"
            trims = [("128GB Midnight ស្អាត 99%", 430), ("256GB ស្អាត", 490)]
            core_specs = ["បន្ទះឈីប A15 Bionic 5-Core GPU", "កាមេរ៉ា Dual Camera", "តម្លៃសមរម្យ"]
        years = ["128GB", "256GB", "512GB"]

    elif "13" in q and ("iphone" in q or "apple" in q or "pro" in q or "max" in q):
        if is_promax:
            model_name = "iPhone 13 Pro Max"
            trims = [("128GB Sierra Blue ស្អាត 98% ថ្ម 85%", 490), ("256GB 3-Camera ProMotion 120Hz", 560), ("512GB Graphite", 630)]
            core_specs = ["អេក្រង់ 6.7\" ProMotion 120Hz", "បន្ទះឈីប A15 Bionic", "ពណ៌ Sierra Blue & Alpine Green", "ថាមពលថ្មកាន់បានយូរ"]
        elif is_pro:
            model_name = "iPhone 13 Pro"
            trims = [("128GB Sierra Blue ស្អាត 98%", 430), ("256GB ProMotion 120Hz", 490)]
            core_specs = ["អេក្រង់ 6.1\" ProMotion 120Hz", "កាមេរ៉ា 3 គ្រាប់ Pro System", "បន្ទះឈីប A15 Bionic"]
        elif is_mini:
            model_name = "iPhone 13 Mini"
            trims = [("128GB Pink / Starlight ស្អាត 98%", 310), ("256GB ស្អាត", 360)]
            core_specs = ["តូចច្រឡឹង 5.4\" ងាយស្រួលកាន់ដៃមួយ", "បន្ទះឈីប A15 Bionic", "ទម្ងន់ស្រាល"]
        else:
            model_name = "iPhone 13"
            trims = [("128GB Midnight ស្អាត 99% ថ្ម 90%", 360), ("256GB ស្អាត", 420)]
            core_specs = ["កាមេរ៉ាបញ្ឆិត Dual Camera", "បន្ទះឈីប A15 Bionic", "អេក្រង់ Super Retina XDR OLED"]
        years = ["128GB", "256GB", "512GB"]

    elif "12" in q and ("iphone" in q or "apple" in q):
        if is_promax:
            model_name = "iPhone 12 Pro Max"
            trims = [("128GB Pacific Blue ស្អាត 98%", 390), ("256GB ស្អាត", 450)]
            core_specs = ["អេក្រង់ធំ 6.7\" OLED", "LiDAR Scanner & 3 Cameras", "ពណ៌ Pacific Blue"]
        elif is_pro:
            model_name = "iPhone 12 Pro"
            trims = [("128GB Pacific Blue ស្អាត 98%", 330), ("256GB ស្អាត", 380)]
            core_specs = ["អេក្រង់ 6.1\" OLED", "តួខ្លួនដែក Stainless Steel", "LiDAR Scanner"]
        else:
            model_name = "iPhone 12"
            trims = [("64GB Black / White ស្អាត 98%", 250), ("128GB ស្អាត 99%", 290)]
            core_specs = ["តួខ្លួនរាងជ្រុង OLED Display", "បន្ទះឈីប A14 Bionic", "ទ្រទ្រង់ប្រព័ន្ធ 5G ដំបូងគេ"]
        years = ["64GB", "128GB", "256GB"]

    elif "11" in q and ("iphone" in q or "apple" in q):
        if is_promax:
            model_name = "iPhone 11 Pro Max"
            trims = [("64GB Midnight Green ស្អាត 98%", 280), ("256GB ស្អាត 99%", 330)]
            core_specs = ["អេក្រង់ 6.5\" Super Retina XDR", "កាមេរ៉ា 3 គ្រាប់ ពណ៌ Midnight Green", "ថ្មកាន់បានល្អ"]
        elif is_pro:
            model_name = "iPhone 11 Pro"
            trims = [("64GB Midnight Green ស្អាត 98%", 230), ("256GB ស្អាត 99%", 270)]
            core_specs = ["អេក្រង់ 5.8\" OLED តូចល្មមដៃ", "កាមេរ៉ា 3 គ្រាប់", "បន្ទះឈីប A13 Bionic"]
        else:
            model_name = "iPhone 11"
            trims = [("64GB Purple / Black ស្អាត 98%", 185), ("128GB ស្អាត 99% ថ្ម 85%+", 225)]
            core_specs = ["កាមេរ៉ាភ្លោះ Dual Camera", "បន្ទះឈីប A13 Bionic", "ពណ៌ Purple & Green ពេញនិយម", "តម្លៃធូរថ្លៃបំផុត"]
        years = ["64GB", "128GB"]

    elif any(x in q for x in ["iphone x", "iphone xs", "iphone xr", "iphonex"]):
        if "max" in q or "xs max" in q:
            model_name = "iPhone XS Max"
            trims = [("64GB Gold ស្អាត 98%", 170), ("256GB ស្អាត 98%", 205)]
            core_specs = ["អេក្រង់ធំ 6.5\" OLED", "បន្ទះឈីប A12 Bionic", "ពណ៌ Gold ទឹកមាស"]
        elif "xr" in q:
            model_name = "iPhone XR"
            trims = [("64GB Coral / Black ស្អាត 98%", 135), ("128GB ស្អាត 98%", 160)]
            core_specs = ["អេក្រង់ 6.1\" Liquid Retina", "ថ្មកាន់បានយូរ", "ពណ៌ស្រស់ឆើតឆាយ"]
        elif "xs" in q:
            model_name = "iPhone XS"
            trims = [("64GB Space Gray ស្អាត 98%", 140), ("256GB ស្អាត 98%", 165)]
            core_specs = ["អេក្រង់ 5.8\" OLED", "កាមេរ៉ាភ្លោះ Dual Camera", "Stainless Steel Frame"]
        else:
            model_name = "iPhone X"
            trims = [("64GB Silver / Space Gray ស្អាត 98%", 125), ("256GB ស្អាត", 145)]
            core_specs = ["អេក្រង់លាត Face ID ដំបូងគេ", "បន្ទះឈីប A11 Bionic", "តម្លៃសមរម្យ"]
        years = ["64GB", "256GB"]

    else:
        model_name = query.title()
        trims = [("128GB ស្អាត 99% សំណុំហ្ស៊ីន", 420), ("256GB Full Option ថ្មីកេះ", 520)]
        years = ["128GB", "256GB"]
        core_specs = [f"ម៉ូដែល {model_name}", "គុណភាពស្តង់ដារ 100% ហ្ស៊ីន", "តម្លៃទីផ្សារកម្ពុជា"]

    return {
        "domain": "PHONES", "category": "PHONES", "category_label": "ទូរស័ព្ទ / Smartphones",
        "brand": brand, "model": model_name, "years": years, "trims": trims,
        "core_specs": core_specs, "is_vehicle": False
    }

# Run tests
test_queries = [
    "COROLLA CROSS",
    "iPhone 16 Pro Max",
    "iPhone 16 Pro",
    "iPhone 16",
    "iPhone 15 Pro Max",
    "iPhone 15 Pro",
    "iPhone 12",
    "iPhone 11",
    "AirPods 2",
    "AirPods Pro",
    "AirPods 4",
    "Apple Watch Ultra",
    "Apple Watch Series 8",
    "MacBook Air M1",
    "MacBook Pro M3",
    "Prius 2010",
    "Prius 2007",
    "Camry 2007",
    "Lexus RX330",
    "Highlander 2003",
    "Land Cruiser 2018",
    "Land Cruiser 2023",
    "Honda Dream 2024",
    "Scoopy 2024",
    "Geely Monjaro",
    "BYD Atto 3"
]

for q in test_queries:
    res = classify_test(q)
    print(f"{q:<22} -> [{res['domain']:<10}] {res['brand']} {res['model']:<25} | ${res['trims'][0][1]:<7} | {res['trims'][0][0][:35]}")
