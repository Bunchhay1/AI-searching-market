import sys

with open('scrapers/ai_search_service.py', 'r', encoding='utf-8') as f:
    content = f.read()

target = "    # 6. COMPUTERS, LAPTOPS & PC HARDWARE DOMAIN (PTC, Gold One, Mastertech, Top Tech, CAC, Chantra, Anana, IT Zone, etc.)"
if target not in content:
    raise ValueError("Target anchor not found!")

new_classifiers = '''    # 5.1 AUDIO, GADGETS & SOUND DOMAIN (Marshall, Bose, JBL, Sony Audio, Sennheiser, DJI, GoPro, Shure, Rode)
    audio_keywords = [
        "marshall", "bose", "jbl", "sennheiser", "shure", "rode", "boya", "harman kardon",
        "audio-technica", "edifier", "soundbar", "speaker", "headphone", "earbuds", "wireless audio",
        "dji", "gopro", "insta360", "drone", "action camera", "gimbal", "mic", "microphone",
        "baseus", "anker", "ugreen", "joyroom", "hoco", "ldnio", "tronsmart", "sound system", "បាស", "កាស"
    ]
    if any(k in q for k in audio_keywords):
        if "marshall" in q:
            brand = "Marshall"
            model = query.title() if any(x in q for x in ["stanmore", "acton", "woburn", "emberton", "willen"]) else "Marshall Stanmore III"
            trims = [
                ("Marshall Stanmore III Bluetooth 5.2 សំឡេងកន្ត្រាក់បេះដូង ថ្មីកេះ ធានា 1 ឆ្នាំ", 360),
                ("Marshall Acton III Bluetooth Speaker ថ្មីកេះ 100%", 275),
                ("Marshall Emberton II Portable Waterproof ថ្មីកេះ", 165),
                ("Marshall Major IV Wireless Bluetooth Headphones ថ្មីកេះ", 135)
            ]
            years = ["Stanmore III", "Acton III", "Emberton II", "Major IV"]
            core_specs = ["សំឡេងស្តង់ដារ Marshall Signature Sound សំឡេងបាសកន្ត្រាក់", "Bluetooth 5.2 & App Control បញ្ជាតាមទូរស័ព្ទ", "ទំនិញសុទ្ធ 100% ធានាផ្លូវការ 1 ឆ្នាំពេញ"]
            colors = ["Black & Brass", "Cream Vintage", "Brown"]
        elif "bose" in q:
            brand = "Bose"
            model = query.title() if "quietcomfort" in q else "Bose QuietComfort Ultra"
            trims = [
                ("Bose QuietComfort Ultra Headphones Noise Cancelling ថ្មីកេះ", 380),
                ("Bose QuietComfort Ultra Earbuds ថ្មីកេះ 100%", 285),
                ("Bose SoundLink Flex Bluetooth Speaker ថ្មីកេះ", 145)
            ]
            years = ["QC Ultra", "QC 45", "SoundLink"]
            core_specs = ["កំពូលបច្ចេកវិទ្យាកាត់បន្ថយសំឡេងរំខាន World-Class Noise Cancelling", "CustomTune Technology កែតម្រូវសំឡេងតាមទម្រង់ត្រចៀក", "ថ្មកាន់រហូតដល់ 24 ម៉ោង"]
            colors = ["Black", "White Smoke", "Sandstone"]
        elif "jbl" in q:
            brand = "JBL"
            model = query.title() if any(x in q for x in ["partybox", "flip", "charge", "boombox"]) else "JBL PartyBox Stage 320"
            trims = [
                ("JBL PartyBox Stage 320 Bluetooth Party Speaker ថ្មីកេះ", 520),
                ("JBL Boombox 3 Wi-Fi & Bluetooth ថ្មីកេះ", 420),
                ("JBL Charge 5 Portable Waterproof ថ្មីកេះ", 155),
                ("JBL Flip 6 Portable Bluetooth ថ្មីកេះ", 115)
            ]
            years = ["PartyBox 320", "Boombox 3", "Charge 5", "Flip 6"]
            core_specs = ["JBL Pro Sound សំឡេងបាសធ្ងន់ និងភ្លើង LED Party Lights", "ការពារទឹក និងធូលីកម្រិត IP67", "ថ្មកាន់បានដល់ 18 ម៉ោង គាំទ្រ Auracast"]
            colors = ["Midnight Black", "Squad Camo", "Blue"]
        elif any(d in q for d in ["dji", "drone", "gopro", "insta360"]):
            brand = "DJI" if "dji" in q else ("GoPro" if "gopro" in q else "Insta360")
            model = query.title() if any(x in q for x in ["mini", "air", "mavic", "osmo", "hero", "x4", "x3"]) else "DJI Mini 4 Pro Fly More Combo"
            trims = [
                ("DJI Mini 4 Pro Fly More Combo Plus (DJI RC 2) ថ្មីកេះ 100%", 950),
                ("DJI Mini 4 Pro (DJI RC-N2) ថ្មីកេះ", 750),
                ("GoPro HERO 12 / 13 Black 5.3K Action Cam ថ្មីកេះ", 395),
                ("Insta360 X4 8K 360-Degree Action Camera ថ្មីកេះ", 495)
            ]
            years = ["4K/60fps HDR", "5.3K 60fps", "8K 360"]
            core_specs = ["ប្រព័ន្ធទប់លំនឹង 3-Axis Gimbal & Obstacle Sensing ជុំទិស", "កាមេរ៉ាថតវីដេអូ 4K/60fps HDR True Vertical Shooting", "ចម្ងាយហោះហើរ 20km ជាមួយបច្ចេកវិទ្យា O4 Video Transmission"]
            colors = ["Standard Gray", "Black Edition"]
        else:
            brand = "Audio & Pro Sound"
            model = query.title()
            trims = [
                ("ឧបករណ៍សំឡេង & Accessories សុទ្ធ 100% ធានាក្រុមហ៊ុន", 195),
                ("ស៊េរីពេញនិយម Original Box ថ្មីកេះ", 125),
                ("ទំនិញស្អាត 99% សំណុំហ្ស៊ីន គុណភាពខ្ពស់", 85)
            ]
            years = ["Pro Audio", "Hi-Res Wireless", "Standard"]
            core_specs = ["គុណភាពសំឡេង Hi-Res Audio ភ្លេងពិរោះរណ្តំ", "ធានាផលិតផលសុទ្ធ 100% ពីតំណាងចែកចាយផ្លូវការនៅកម្ពុជា", "ផ្គត់ផ្គង់ដោយ Rithy Tech, Phnom Penh Audio, Gadget Store KH"]
            colors = ["Black", "Silver", "White"]

        return {
            "domain": "PHONES", "category": "PHONES", "category_label": "ឧបករណ៍សំឡេង & Gadgets / Audio",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=800&q=80"],
            "colors": colors, "core_specs": core_specs, "is_vehicle": False
        }

    # 5.2 KEYBOARDS, GAMING ACCESSORIES & PC COMPONENTS (Keychron, Akko, Royal Kludge, NZXT, Corsair, Lian Li, Noctua, ZOTAC)
    keyboard_pc_keywords = [
        "keychron", "akko", "royal kludge", "rk", "redragon", "fantech", "dareu", "glorious",
        "mechanical keyboard", "keyboard", "gaming mouse", "mousepad", "nzxt", "corsair",
        "thermaltake", "cooler master", "deepcool", "lian li", "noctua", "zotac", "palit",
        "sapphire", "inno3d", "powercolor", "asrock", "crucial", "kingston ram", "sandisk",
        "wacom", "xp-pen", "ubiquiti", "mikrotik", "tp-link", "synology", "qnap", "ក្តារចុច"
    ]
    if any(k in q for k in keyboard_pc_keywords):
        if "keychron" in q:
            brand = "Keychron"
            model = query.title() if any(x in q for x in ["q1", "q2", "q3", "k2", "k3", "v1", "v2"]) else "Keychron Q1 Pro / Max"
            trims = [
                ("Keychron Q1 Max Full Aluminum QMK/VIA Wireless Hot-swap ថ្មីកេះ", 185),
                ("Keychron V1 QMK Custom Mechanical Keyboard ថ្មីកេះ", 85),
                ("Keychron K2 Pro Wireless Bluetooth/Type-C ថ្មីកេះ", 95),
                ("Keychron K3 Ultra-Slim Wireless Low Profile ថ្មីកេះ", 88)
            ]
            years = ["Wireless 2.4GHz + BT", "Type-C Wired", "Low Profile"]
            core_specs = ["តួ Full CNC Aluminum Body និង Double-Gasket Design", "Hot-Swappable អាចប្តូរ Switch បានងាយស្រួល (Red/Brown/Banana)", "គាំទ្រ macOS & Windows និងកម្មវិធី QMK/VIA"]
            colors = ["Carbon Black", "Silver Gray", "Shell White"]
        elif any(k in q for k in ["akko", "royal kludge", "redragon", "fantech", "dareu", "keyboard", "ក្តារចុច"]):
            brand = "Custom Keyboard"
            model = query.title()
            trims = [
                ("Wireless Multi-Mode Mechanical Keyboard RGB Hot-swap ថ្មីកេះ", 75),
                ("Custom Mechanical Keyboard Gasket Mount ថ្មីកេះ 100%", 55),
                ("Budget Gaming Keyboard Rainbow Backlit ស្អាត 99%", 32)
            ]
            years = ["Tri-Mode Wireless", "Wired RGB", "Compact 75%"]
            core_specs = ["Switch ប្រភេទ Linear / Tactile ចុចស្រួលដៃ គ្មានសម្លេងរំខាន", "ភ្លើង RGB Backlit ច្រើនម៉ូដ និង Keycaps PBT ធន់មិនរលុប", "ធានាគុណភាពពីហាងកុំព្យូទ័រផ្លូវការ"]
            colors = ["Black RGB", "Retro White", "Cyberpunk Pink"]
        else:
            brand = "PC Components & Gaming Gear"
            model = query.title()
            trims = [
                ("High-End PC Component / Upgrade Part ថ្មីកេះ ធានា 3 ឆ្នាំ", 165),
                ("Mid-Tier Gaming Accessory ថ្មីកេះ 100%", 85),
                ("Entry-Level Hardware Part ស្អាត 99%", 45)
            ]
            years = ["Gaming Grade", "Commercial Series", "Pro Series"]
            core_specs = ["ស្តង់ដារគុណភាពម៉ាកយីហោល្បីៗលើពិភពលោក", "ធានាផលិតផលសុទ្ធ 100% ជាមួយការធានាផ្លូវការ", "ផ្គត់ផ្គង់ដោយ Gold One, Mastertech, PTC, Chantra Computer"]
            colors = ["Black", "White ARGB"]

        return {
            "domain": "COMPUTERS", "category": "COMPUTERS", "category_label": "គ្រឿងបន្លាស់កុំព្យូទ័រ & Keyboards / PC Gear",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=800&q=80"],
            "colors": colors, "core_specs": core_specs, "is_vehicle": False
        }

    # 5.3 BEAUTY, SKINCARE & COSMETICS DOMAIN (Cosrx, Beauty of Joseon, Torriden, Round Lab, La Roche-Posay, SK-II, Sulwhasoo)
    beauty_keywords = [
        "cosrx", "beauty of joseon", "round lab", "torriden", "anua", "skin1004", "some by mi",
        "klairs", "pyunkang", "isntree", "la roche-posay", "laroche", "bioderma", "avene",
        "eucerin", "cetaphil", "kiehl", "loccitane", "body shop", "estee lauder", "esteelauder",
        "sulwhasoo", "hera", "3ce", "shiseido", "sk-ii", "sk2", "snail mucin", "serum", "toner",
        "sunscreen", "cleanser", "moisturizer", "essence", "mask", "lipstick", "ឡេ", "ម្សៅ", "ក្រែម"
    ]
    if any(k in q for k in beauty_keywords):
        brand = "Cosrx" if "cosrx" in q else ("Beauty of Joseon" if "joseon" in q else ("La Roche-Posay" if "roche" in q else ("Torriden" if "torriden" in q else ("Round Lab" if "round lab" in q else "Korean & French Skincare"))))
        model = query.title()
        trims = [
            ("ផលិតផលថែរក្សាសម្រស់ Original 100% នាំចូលផ្ទាល់ពីកូរ៉េ/បារាំង", 24),
            ("ឈុត Skincare Set Promotion ពិសេស", 48),
            ("សេរ៉ូម ឬឡេការពារកម្តៅថ្ងៃស៊េរីពេញនិយម", 18)
        ]
        years = ["100ml Full Size", "50ml Standard", "150ml Value Pack"]
        core_specs = [
            "ផលិតផលសុទ្ធ 100% មានបាកូដត្រួតពិនិត្យ និងកាលបរិច្ឆេទផុតកំណត់ច្បាស់លាស់",
            "រូបមន្តគ្មានជាតិកាត់ ស័ក្តិសមសម្រាប់ស្បែកងាយប្រតិកម្ម និងស្បែកកើតមុន",
            "នាំចូលដោយហាងកែសម្ផស្ស និងឱសថស្ថានល្បីៗនៅកម្ពុជា"
        ]
        colors = ["Original Formula", "Sensitive Skin Type"]

        return {
            "domain": "BEAUTY", "category": "BEAUTY", "category_label": "សម្រស់ & គ្រឿងសម្អាង / Skincare & Beauty",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1571781926291-c477ebfd024b?auto=format&fit=crop&w=800&q=80"],
            "colors": colors, "core_specs": core_specs, "is_vehicle": False
        }

    # 5.4 SMART HOME APPLIANCES & CLEANING ROBOTICS (Roborock, Dreame, Ecovacs, Herman Miller, Toto, Daikin)
    smart_home_keywords = [
        "roborock", "dreame", "ecovacs", "deebot", "vacuum", "robot vacuum", "herman miller",
        "steelcase", "merryfair", "toto", "washlet", "inax", "grohe", "kohler", "daikin",
        "gree", "delonghi", "breville", "nespresso", "tefal", "ម៉ាស៊ីនបោសផ្ទះ", "កៅអីការិយាល័យ"
    ]
    if any(k in q for k in smart_home_keywords):
        if "roborock" in q:
            brand = "Roborock"
            model = query.title() if any(x in q for x in ["s8", "q revo", "s7", "q7"]) else "Roborock S8 Pro Ultra"
            trims = [
                ("Roborock S8 Pro Ultra Robot Vacuum & Mop (RockDock Ultra) ថ្មីកេះ", 1150),
                ("Roborock Q Revo MaxV AI Obstacle Avoidance ថ្មីកេះ", 890),
                ("Roborock Q7 Max+ Auto-Empty Dock ថ្មីកេះ 100%", 520)
            ]
            years = ["RockDock Ultra", "Auto-Empty Dock", "Standard"]
            core_specs = ["កម្លាំងបឺតខ្លាំង 6000Pa - 10000Pa និងធុងជូតសម្អាតកម្តៅស្ងួតស្វ័យប្រវត្តិ", "ប្រព័ន្ធ Reactive AI 3D Obstacle Avoidance ឆ្លាតវៃ", "ភ្ជាប់ Wi-Fi បញ្ជាតាមទូរស័ព្ទដៃ និងកំណត់បន្ទប់ឆ្លាតវៃ"]
            colors = ["Pure White", "Matte Black"]
        elif "herman miller" in q:
            brand = "Herman Miller"
            model = "Herman Miller Aeron Chair"
            trims = [
                ("Herman Miller Aeron Remastered Size B Full Option PostureFit SL ថ្មីកេះ ធានា 12 ឆ្នាំ", 1350),
                ("Herman Miller Embody Ergonomic Task Chair ថ្មីកេះ", 1680),
                ("Herman Miller Aeron Classic ស្អាត 99% សំណុំហ្ស៊ីន", 780)
            ]
            years = ["Size B (Medium)", "Size C (Large)", "Size A (Small)"]
            core_specs = ["កៅអី Ergonomic លំដាប់ពិភពលោកការពារការឈឺចង្កេះ និងខ្នង", "សំណាញ់ Pellicle 8Z ខ្យល់ចេញចូលត្រជាក់ស្រួលមិនក្តៅស្អុះ", "ធានារហូតដល់ 12 ឆ្នាំពីតំណាងចែកចាយផ្លូវការ"]
            colors = ["Graphite", "Carbon", "Mineral"]
        else:
            brand = "Home Living & Smart Appliances"
            model = query.title()
            trims = [
                ("Smart Home Appliance ថ្មីកេះ 100% ធានាក្រុមហ៊ុន", 450),
                ("ម៉ូដែលពេញនិយម Promotion ពិសេស ថ្មីកេះ", 280),
                ("ទំនិញស្អាត 99% គុណភាពខ្ពស់ ធានាហាង", 160)
            ]
            years = ["Smart Series", "Inverter", "Premium"]
            core_specs = ["បច្ចេកវិទ្យាសន្សំសំចៃថាមពលអគ្គិសនី និងធន់រឹងមាំ", "ធានាគុណភាពផលិតផលសុទ្ធ 100% ពីហាងផ្លូវការ", "ផ្គត់ផ្គង់ដោយ Kano Furniture, Steelcase KH, Lixil, Toto Cambodia"]
            colors = ["Classic White", "Silver", "Black"]

        return {
            "domain": "FURNITURE", "category": "FURNITURE", "category_label": "គ្រឿងសង្ហារិម & ឧបករណ៍ផ្ទះ / Home & Living",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=800&q=80"],
            "colors": colors, "core_specs": core_specs, "is_vehicle": False
        }

    # 5.5 REAL ESTATE, CONDOS, BOREYS & COMMERCIAL (The Peak, The Bridge, Borey Peng Huoth, Chip Mong, Vattanac Tower)
    re_keywords = [
        "the peak", "the bridge", "borey", "peng huoth", "chip mong", "orkide", "piphup thmey",
        "vattanac", "morgan tower", "gia tower", "flatiron", "le conde", "agile sky",
        "vue aston", "star bay", "bodaiju", "olympia city", "sky villa", "condo", "villa", "បុរី", "ខុនដូ", "វីឡា"
    ]
    if any(k in q for k in re_keywords):
        brand = "Borey Peng Huoth" if "peng huoth" in q else ("Borey Chip Mong" if "chip mong" in q else ("The Peak" if "peak" in q else "Premium Property Cambodia"))
        model = query.title()
        if any(c in q for c in ["condo", "peak", "bridge", "tower", "ខុនដូ", "conde", "agile", "aston"]):
            trims = [
                ("1-Bedroom Luxury Riverview Condo Fully Furnished ប្លង់រឹង", 115000),
                ("Studio Room City View ជួល ឬទិញប្រាក់ចំណេញខ្ពស់", 68000),
                ("2-Bedroom Penthouse High Floor ទេសភាពទន្លេ 360°", 220000)
            ]
            years = ["Freehold (ប្លង់រឹង)", "Hard Title", "Strata Title"]
            core_specs = ["ប្លង់រឹងស្របច្បាប់ 100% អាចកាន់កាប់ដោយជនបរទេស និងខ្មែរ", "អាងហែលទឹកលើអាកាស Sky Pool, Gym, និងសន្តិសុខ 24 ម៉ោង", "អត្រាជួលត្រឡប់មកវិញ (Rental Yield) 6-8% ក្នុងមួយឆ្នាំ"]
            colors = ["Fully Furnished", "Modern Minimalist Interior"]
        else: # Borey Villa / Townhouse
            trims = [
                ("វីឡាកូនកាត់ (Link Villa) ក្នុងបុរី ទីតាំងល្អ ម៉ាស៊ីនត្រជាក់គ្រប់បន្ទប់", 145000),
                ("វីឡាភ្លោះ (Twin Villa) ដីធំទូលាយ ប្លង់រឹងផ្ទេរសិទ្ធិឥតគិតថ្លៃ", 285000),
                ("វីឡាឃ្វីន ឬ ឃីង (Queen / King Villa) ប្រណីតភាពកម្រិតខ្ពស់", 650000)
            ]
            years = ["ប្លង់រឹងផ្ទេរសិទ្ធិ", "កាត់ប្លង់បុរី", "បង់រំលស់សុទ្ធ"]
            core_specs = ["សំណង់រឹងមាំស្តង់ដារបុរីលំដាប់លេខមួយនៅកម្ពុជា", "បរិស្ថានរស់នៅស្ងប់ស្ងាត់ មានសួនច្បារ ក្លឹបហាត់ប្រាណ និងអាងហែលទឹក", "ទីតាំងមានសក្តានុពលសេដ្ឋកិច្ចខ្ពស់ ងាយស្រួលធ្វើដំណើរ"]
            colors = ["Modern Classic", "Luxury European Design"]

        return {
            "domain": "REAL_ESTATE", "category": "REAL_ESTATE", "category_label": "អចលនទ្រព្យ & ខុនដូ / Real Estate",
            "brand": brand, "model": model, "years": years, "trims": trims,
            "images": ["https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80"],
            "colors": colors, "core_specs": core_specs, "is_vehicle": False
        }

'''

content = content.replace(target, new_classifiers + target)

with open('scrapers/ai_search_service.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected new specialized domain classifiers into scrapers/ai_search_service.py successfully!")
