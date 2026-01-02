# generate_platforms.py
import json

raw_categories = [
    {
        "cat_id": "GENERAL",
        "cat_name_en": "General Classifieds & E-Commerce",
        "cat_name_kh": "ទីផ្សារទូទៅ & E-Commerce",
        "icon": "🛒",
        "items": [
            ("khmer24", "Khmer24", "khmer24.com", "🛒 Classifieds", "Khmer24 (ទីផ្សារធំបំផុត)", "Cambodia's largest general classifieds and secondhand trading hub with direct seller chat", "https://www.khmer24.com/en/search?q={q}", "https://www.khmer24.com", "GENERAL"),
            ("sabaylok", "SabayLok", "sabaylok.com", "🛒 Classifieds", "SabayLok (សប្បាយលក់)", "Peer-to-peer marketplace for user listings, classified ads, and Telegram negotiation", "https://www.sabaylok.com/search?q={q}", "https://www.sabaylok.com", "GENERAL"),
            ("vtenh", "VTENH", "vtenh.com", "🛒 Marketplace", "VTENH (វីទិញ)", "Multi-vendor e-commerce platform with fast local delivery and verified local stores", "https://www.vtenh.com/search?q={q}", "https://www.vtenh.com", "GENERAL"),
            ("loda_kh", "LODA Cambodia", "loda.com.kh", "🛒 Wholesale/Factory", "LODA Cambodia", "Wholesale and retail platform with international supply lines and direct factory prices", "https://www.loda.com.kh/search?q={q}", "https://www.loda.com.kh", "GENERAL"),
            ("tinhtinh", "Tinh Tinh Shop", "tinhtinh.shop", "🛒 Postal E-Mall", "Tinh Tinh Shop (Cambodia Post)", "Postal-backed short-video e-commerce shopping portal backed by Cambodia Post", "https://tinhtinh.shop/search?q={q}", "https://tinhtinh.shop", "GENERAL"),
            ("larue", "LaRue", "larue.com.kh", "🛒 E-Commerce Deals", "LaRue Cambodia", "General retail e-commerce platform for everyday goods and flash consumer sales", "https://larue.com.kh/search?q={q}", "https://larue.com.kh", "GENERAL"),
            ("khdeal", "KHDEAL", "khdeal.com", "🛒 Free Classifieds", "KHDEAL", "Free community classified board for secondhand items and freelance services", "https://khdeal.com/search?q={q}", "https://khdeal.com", "GENERAL"),
            ("smileshop", "Smile Shop", "smileshop.com.kh", "🛒 Installment & Tech", "Smile Shop Cambodia", "E-commerce app featuring buy-now-pay-later (BNPL) options and brand warranties", "https://smileshop.com.kh/search?q={q}", "https://smileshop.com.kh", "GENERAL"),
            ("gladmarket", "Glad Market", "gladmarket.com", "🛒 Local Classifieds", "Glad Market", "Local classifieds and small-business directory for Cambodian goods", "https://gladmarket.com/search?q={q}", "https://gladmarket.com", "GENERAL"),
            ("camboquick", "Cambo Quick", "camboquick.com", "🛒 Overseas Proxy", "Cambo Quick", "Overseas shopping proxy service for global delivery (Amazon, Taobao to Cambodia)", "https://camboquick.com/search?q={q}", "https://camboquick.com", "GENERAL"),
            ("niront", "Niront Marketplace", "niront.com", "🛒 SME Marketplace", "Niront Marketplace", "SME digital platform and general marketplace connecting local entrepreneurs", "https://niront.com/search?q={q}", "https://niront.com", "GENERAL"),
            ("appmall", "AppMall Online", "appmall.online", "🛒 Classifieds & Property", "AppMall Online", "General classifieds and property listing app for urban retail", "https://appmall.online/search?q={q}", "https://appmall.online", "GENERAL"),
            ("maiomall", "MAIO Mall", "maiomall.com", "🛒 Digital Hub", "MAIO Mall", "Local digital shopping hub for retail electronics and lifestyle products", "https://maiomall.com/search?q={q}", "https://maiomall.com", "GENERAL"),
            ("mall855", "Mall855", "mall855.com", "🛒 E-Commerce Portal", "Mall855", "E-commerce directory and online store portal for local Cambodian retail", "https://mall855.com/search?q={q}", "https://mall855.com", "GENERAL"),
            ("roserb", "RoseRb", "roserb.com", "🛒 Consumer Products", "RoseRb", "General fashion and consumer product site with daily deals", "https://roserb.com/search?q={q}", "https://roserb.com", "GENERAL"),
            ("ecamshopping", "ECamShopping", "ecamshopping.com", "🛒 Retail Store", "ECamShopping", "Retail e-commerce store for consumer goods, tech accessories, and fashion", "https://ecamshopping.com/search?q={q}", "https://ecamshopping.com", "GENERAL"),
            ("myphsar", "MyPhsar", "myphsar.com", "🛒 Digital Marketplace", "MyPhsar (ផ្សារខ្ញុំ)", "Digital marketplace application and web store for everyday items", "https://myphsar.com/search?q={q}", "https://myphsar.com", "GENERAL"),
            ("e_gets", "E-GetS Mall", "e-gets.com", "⚡ Super-App Mall", "E-GetS Mall (អ៊ីហ្គេត)", "Super-app delivery platform for retail goods, supermarket items, and food", "https://www.e-gets.com/search?q={q}", "https://www.e-gets.com", "GENERAL"),
            ("wownow", "Wownow Mall", "wownow.com.kh", "🛒 Retail Lifestyle", "Wownow Mall", "Retail lifestyle platform and direct merchandise portal with cross-border supplies", "https://wownow.com.kh/search?q={q}", "https://wownow.com.kh", "GENERAL"),
            ("nham24", "Nham24 Shopping", "nham24.com", "⚡ Express Marketplace", "Nham24 Shopping", "Express delivery marketplace for local products, groceries, and tech items", "https://nham24.com/search?q={q}", "https://nham24.com", "GENERAL")
        ]
    },
    {
        "cat_id": "COMPUTERS",
        "cat_name_en": "Computers, Gaming & IT Equipment",
        "cat_name_kh": "កុំព្យូទ័រ Gaming & សម្ភារៈ IT",
        "icon": "💻",
        "items": [
            ("ptc_computer", "PTC Computer", "ptc-computer.com.kh", "💻 Laptops & PC Builds", "PTC Computer", "Major enterprise IT hardware, laptop, and PC distributor across Cambodia", "https://ptc-computer.com.kh/search?q={q}", "https://ptc-computer.com.kh", "COMPUTERS"),
            ("goldone", "Gold One Computer", "goldonecomputer.com", "💻 PC Parts & Gaming Gear", "Gold One Computer", "Gaming gear, PC components (GPUs, CPUs), and networking setup with free quotes", "https://goldonecomputer.com/search?q={q}", "https://goldonecomputer.com", "COMPUTERS"),
            ("mastertech", "Mastertech Computer", "mastertechkh.com", "🎮 Gaming Rigs & Water Cooling", "Mastertech Computer", "Custom liquid cooling builds and high-end gaming rigs (ASUS ROG, MSI, Razer)", "https://mastertechkh.com/search?q={q}", "https://mastertechkh.com", "COMPUTERS"),
            ("psc_computer", "PSC Computer", "psccomputer.com.kh", "💻 Laptops & Repairs", "PSC Computer", "Desktop packages, laptops, and hardware repairs with motherboard diagnostics", "https://psccomputer.com.kh/search?q={q}", "https://psccomputer.com.kh", "COMPUTERS"),
            ("ice_electronics", "ICE Electronics", "icekh.com", "💻 Commercial IT & Displays", "ICE Electronics", "Imported commercial laptops, workstations, and displays with full warranty", "https://icekh.com/search?q={q}", "https://icekh.com", "COMPUTERS"),
            ("top_tech", "Top Tech Computer", "toptechkh.com", "🎮 Gaming Laptops & Monitors", "Top Tech Computer", "High-refresh-rate gaming monitors and notebooks (MSI Raider, ASUS TUF, ROG)", "https://toptechkh.com/search?q={q}", "https://toptechkh.com", "COMPUTERS"),
            ("computer_arena", "Computer Arena Cambodia", "computerarenakh.com", "💻 Workstations & Students", "Computer Arena Cambodia (CAC)", "Student laptops and office workstations (Asus, Acer, Dell, Lenovo)", "https://computerarenakh.com/search?q={q}", "https://computerarenakh.com", "COMPUTERS"),
            ("chantra_computer", "Chantra Computer", "chantracomputer.com", "💻 Budget PC Builds", "Chantra Computer", "Budget gaming desktops, mechanical keyboards, headsets, and peripherals", "https://chantracomputer.com/search?q={q}", "https://chantracomputer.com", "COMPUTERS"),
            ("anana_computer", "Anana Computer", "ananacomputer.com", "🏢 Enterprise IT & Servers", "Anana Computer", "Enterprise IT servers, enterprise networking hardware, and software licenses", "https://ananacomputer.com/search?q={q}", "https://ananacomputer.com", "COMPUTERS"),
            ("itzone", "IT Zone", "itzone.com.kh", "💻 Office Tech & Network", "IT Zone Computer", "Office printers, UPS power backups, scanners, and networking hardware", "https://itzone.com.kh/search?q={q}", "https://itzone.com.kh", "COMPUTERS"),
            ("central_computer", "Central Computer", "centralcomputer.com.kh", "💻 PC Assembly & Supplies", "Central Computer", "PC assembly parts and office IT supplies with wholesale options", "https://centralcomputer.com.kh/search?q={q}", "https://centralcomputer.com.kh", "COMPUTERS"),
            ("vtech_computer", "V-Tech Computer", "vtechcomputer.com.kh", "💻 Laptops & Repair Services", "V-Tech Computer", "Laptops, repair services, and tech accessories with fast turnaround", "https://vtechcomputer.com.kh/search?q={q}", "https://vtechcomputer.com.kh", "COMPUTERS"),
            ("chhay_hok", "Chhay Hok Computer", "chhayhok.com", "🎮 Gaming PC Hardware", "Chhay Hok Computer", "Gaming PC hardware distributor, high-end GPUs, and motherboard upgrades", "https://chhayhok.com/search?q={q}", "https://chhayhok.com", "COMPUTERS"),
            ("sopheak_computer", "Sopheak Computer", "sopheakcomputer.com", "💻 Used Laptops & Displays", "Sopheak Computer", "Used laptops, desktop monitors, and secondhand enterprise workstations", "https://sopheakcomputer.com/search?q={q}", "https://sopheakcomputer.com", "COMPUTERS"),
            ("memory_computer", "Memory Computer", "memorycomputer.com.kh", "💾 Storage, SSD & RAM", "Memory Computer", "Storage drives, NVMe SSDs, RAM modules, and desktop components", "https://memorycomputer.com.kh/search?q={q}", "https://memorycomputer.com.kh", "COMPUTERS"),
            ("winwin_computer", "WinWin Computer", "winwincomputer.com", "💻 PC Parts Assembly", "WinWin Computer", "PC parts assembly and gaming gear with customized budget options", "https://winwincomputer.com/search?q={q}", "https://winwincomputer.com", "COMPUTERS"),
            ("redfox_gaming", "Redfox Gaming", "redfoxgaming.com.kh", "🎮 Esports Gear & Chairs", "Redfox Gaming", "Esports gear, mechanical keyboards, gaming headsets, and ergonomic chairs", "https://redfoxgaming.com.kh/search?q={q}", "https://redfoxgaming.com.kh", "COMPUTERS"),
            ("ktech_computer", "KTech Computer", "ktech.com.kh", "💻 Office Desktop Packages", "KTech Computer", "Office desktop packages and networking accessories for companies", "https://ktech.com.kh/search?q={q}", "https://ktech.com.kh", "COMPUTERS"),
            ("gamer_zone", "Gamer Zone KH", "gamerzonekh.com", "🎮 Custom PC Gaming", "Gamer Zone KH", "Gaming peripherals and custom PC parts tailored for streamers and gamers", "https://gamerzonekh.com/search?q={q}", "https://gamerzonekh.com", "COMPUTERS"),
            ("bayon_computer", "Bayon Computer", "bayoncomputer.com.kh", "💻 Laptops & Printers", "Bayon Computer", "Laptops, commercial printers, and computer accessories with warranty", "https://bayoncomputer.com.kh/search?q={q}", "https://bayoncomputer.com.kh", "COMPUTERS")
        ]
    },
    {
        "cat_id": "PHONES",
        "cat_name_en": "Smartphones, Tablets & Mobile Accessories",
        "cat_name_kh": "ទូរស័ព្ទ Tablets & គ្រឿងបន្លាស់",
        "icon": "📱",
        "items": [
            ("nika_phone", "NIKA Phone Shop", "web.nika2u.com", "📱 Official Flagship Phones", "NIKA Phone Shop", "Official Apple, Samsung, and Xiaomi flagship retailer with brand warranties", "https://web.nika2u.com/search?q={q}", "https://web.nika2u.com", "PHONES"),
            ("sokly_phone", "Sokly Phone Shop", "soklyphone.com", "📱 Mobile Devices & Trade-In", "Sokly Phone Shop", "Mobile devices, instant trade-ins, Apple ecosystem, and accessories", "https://soklyphone.com/search?key={q}", "https://soklyphone.com", "PHONES"),
            ("apsara_mobile", "Apsara Mobile", "apsaramobile.com.kh", "📱 New & Used Phones", "Apsara Mobile", "New and used smartphone sales, buy/sell/trade used iPhones & Android", "https://apsaramobile.com.kh/search?q={q}", "https://apsaramobile.com.kh", "PHONES"),
            ("oneone_store", "One One Store", "oneonephone.com", "📱 Fast Chargers & Mobile", "One One Store", "Fast chargers, power banks, wireless earbuds, and latest smartphones", "https://oneonephone.com/search?q={q}", "https://oneonephone.com", "PHONES"),
            ("hakse_phone", "Hakse Phone Shop", "haksephone.com", "📱 Phones & Smartwatches", "Hakse Phone Shop", "Mobile phones, smartwatches, cases, and tempered glass accessories", "https://haksephone.com/search?q={q}", "https://haksephone.com", "PHONES"),
            ("angkor_meas", "Angkor Meas", "angkormeas.com.kh", "📱 Audio Gear & Phones", "Angkor Meas Phone Shop", "Consumer audio gear, smartphones, and smart TVs with official warranty", "https://angkormeas.com.kh/search?q={q}", "https://angkormeas.com.kh", "PHONES"),
            ("seyha_mobile", "Seyha Mobile", "seyhamobile.com.kh", "📱 Pre-Owned Flagships", "Seyha Mobile", "Pre-owned flagship smartphones, 99% condition devices, and trade-ins", "https://seyhamobile.com.kh/search?q={q}", "https://seyhamobile.com.kh", "PHONES"),
            ("kstore_mobile", "K-Store Mobile", "kstore.com.kh", "📱 Phone Protection & Cases", "K-Store Mobile", "Mobile phone protection, high-end cases, charging cables, and mounts", "https://kstore.com.kh/search?q={q}", "https://kstore.com.kh", "PHONES"),
            ("vattanac_mobile", "Vattanac Mobile", "vattanacmobile.com", "📱 Authentic Smartphones", "Vattanac Mobile", "Authentic smartphones, tablets, and original mobile accessories", "https://vattanacmobile.com/search?q={q}", "https://vattanacmobile.com", "PHONES"),
            ("hengheng_mobile", "Heng Heng Mobile", "henghengmobile.com", "📱 Used Phones & Repairs", "Heng Heng Mobile", "Used phone sales, screen replacements, and mobile repair hub", "https://henghengmobile.com/search?q={q}", "https://henghengmobile.com", "PHONES"),
            ("rithy_mobile", "Rithy Mobile", "rithymobile.com.kh", "📱 Wireless Audio & Gadgets", "Rithy Mobile", "Wireless earbuds, fast chargers, power banks, and mobile gadgets", "https://rithymobile.com.kh/search?q={q}", "https://rithymobile.com.kh", "PHONES"),
            ("lyhour_mobile", "Ly Hour Mobile", "lyhourmobile.com", "📱 Phone Trading & Installment", "Ly Hour Mobile", "Phone trading, installment sales, and verified secondhand devices", "https://lyhourmobile.com/search?q={q}", "https://lyhourmobile.com", "PHONES"),
            ("bopha_mobile", "Bopha Mobile", "bophamobile.com", "📱 Budget Smartphones", "Bopha Mobile", "Budget smartphones and mobile accessories with local store warranty", "https://bophamobile.com/search?q={q}", "https://bophamobile.com", "PHONES"),
            ("smart_axiata", "Smart Axiata Store", "smart.com.kh", "📱 Telecom Devices & eSIM", "Smart Axiata Shop", "Telecom devices, eSIMs, and bundled smartphone plans directly from Smart", "https://www.smart.com.kh/shop?q={q}", "https://www.smart.com.kh/shop", "PHONES"),
            ("cellcard_shop", "Cellcard Shop", "cellcard.com.kh", "📱 Mobile Routers & SIMs", "Cellcard Shop", "Mobile routers, 5G SIM cards, device offers, and mobile accessories", "https://www.cellcard.com.kh/shop?q={q}", "https://www.cellcard.com.kh/shop", "PHONES"),
            ("metfone_store", "Metfone Online Store", "metfone.com.kh", "📱 Home Broadband & Phones", "Metfone Store", "Smartphones and home broadband hardware with special data packages", "https://metfone.com.kh/search?q={q}", "https://metfone.com.kh", "PHONES"),
            ("realme_kh", "Realme Cambodia", "realme.com/kh", "📱 Official Realme Devices", "Realme Cambodia", "Official site for Realme mobile devices, buds, and smart lifestyle gear", "https://www.realme.com/kh/search?q={q}", "https://www.realme.com/kh", "PHONES"),
            ("oppo_kh", "OPPO Cambodia", "oppo.com/kh", "📱 Official OPPO Phones", "OPPO Cambodia", "Official local portal for OPPO smartphones, Reno series, and Find flagships", "https://www.oppo.com/kh/search?q={q}", "https://www.oppo.com/kh", "PHONES"),
            ("vivo_kh", "vivo Cambodia", "vivo.com/kh", "📱 Official vivo Phones", "vivo Cambodia", "Official local site for vivo camera phones, V-series, and X-flagships", "https://www.vivo.com/kh/search?q={q}", "https://www.vivo.com/kh", "PHONES"),
            ("samsung_kh", "Samsung Cambodia", "samsung.com/kh", "📱 Official Galaxy Showroom", "Samsung Cambodia", "Official local showroom for Galaxy devices, Fold, Flip, and S-series", "https://www.samsung.com/kh/search/?q={q}", "https://www.samsung.com/kh", "PHONES")
        ]
    },
    {
        "cat_id": "CARS",
        "cat_name_en": "Cars, Motorcycles & Auto Parts",
        "cat_name_kh": "រថយន្ត ម៉ូតូ & គ្រឿងបន្លាស់",
        "icon": "🚗",
        "items": [
            ("sabaylokcar", "SabayLokCar", "sabaylokcar.com", "🚗 AI Valuation Tags", "SabayLokCar", "Used and new car portal with market valuation tags (Good Deal) and video previews", "https://www.sabaylokcar.com/search?q={q}", "https://www.sabaylokcar.com", "CARS"),
            ("carmarketkh", "Car Market KH", "carmarketkh.com", "🚗 Auto Yards & Rentals", "Car Market KH", "Mobile-first car marketplace and rental site connecting buyers to auto yards", "https://www.carmarketkh.com/search?q={q}", "https://www.carmarketkh.com", "CARS"),
            ("mykhmercar", "MyKhmerCar", "mykhmercar.com", "🚗 Commercial & Passenger", "MyKhmerCar", "Passenger vehicles, motorcycles, and heavy trucks with detailed filters", "https://www.mykhmercar.com/search?q={q}", "https://www.mykhmercar.com", "CARS"),
            ("libertycarz", "Liberty Carz", "libertycarz.com", "🚗 360° Virtual & Loans", "Liberty Carz", "360° virtual vehicle app and integrated auto financing tracking portal", "https://www.libertycarz.com/search?q={q}", "https://www.libertycarz.com", "CARS"),
            ("wecar_kh", "WE CAR Cambodia", "wecar.com.kh", "🚗 Commission-Free Trading", "WE CAR Cambodia", "Vehicle trading and long-term rental site with zero commission for sellers", "https://www.wecar.com.kh/search?q={q}", "https://www.wecar.com.kh", "CARS"),
            ("autocambodia", "Auto Cambodia", "autocambodia.net", "🚗 Managed Brokerage", "Auto Cambodia", "Car brokerage and private listing management with agent assistance", "https://autocambodia.net/?s={q}", "https://autocambodia.net", "CARS"),
            ("cambodiacarmarket", "Cambodia Car Market", "cambodiacarmarket.com", "🚗 Garage Yards & Ads", "Cambodia Car Market", "Car ads and garage yard listings across Phnom Penh and provinces", "https://cambodiacarmarket.com/search?q={q}", "https://cambodiacarmarket.com", "CARS"),
            ("khmerautotrader", "Khmer Auto Trader", "khmerautotrader.com", "🚗 All-Province Classifieds", "Khmer Auto Trader", "Vehicle classifieds across all provinces with direct seller contact", "https://khmerautotrader.com/search?q={q}", "https://khmerautotrader.com", "CARS"),
            ("honda_cambodia", "Honda Cambodia", "hondacambodia.com", "🏍️ Official Honda NCX", "Honda Cambodia", "Official motorcycles and automobiles distributor with warranty and parts", "https://hondacambodia.com/search?q={q}", "https://hondacambodia.com", "CARS"),
            ("toyota_cambodia", "Toyota Cambodia", "toyota.com.kh", "🚗 Official Toyota & Pre-Owned", "Toyota Cambodia", "Official new models, certified pre-owned, and trade-in inspection services", "https://www.toyota.com.kh/search?q={q}", "https://www.toyota.com.kh", "CARS"),
            ("ford_cambodia", "Ford Cambodia", "ford-cambodia.com", "🚙 Official Ford Pickups", "Ford Cambodia", "Official Ford pickups (Ranger, Raptor) and SUVs (Everest) showroom", "https://www.ford-cambodia.com/search?q={q}", "https://www.ford-cambodia.com", "CARS"),
            ("hyundai_cambodia", "Hyundai Cambodia", "hyundai-cambodia.com", "🚗 Commercial & Passenger", "Hyundai Cambodia", "Official passenger and commercial vehicles, vans, and delivery trucks", "https://www.hyundai-cambodia.com/search?q={q}", "https://www.hyundai-cambodia.com", "CARS"),
            ("mg_cambodia", "MG Cambodia", "mgcambodia.com", "🚗 Official MG SUVs & EVs", "MG Cambodia", "Official MG SUVs, sedans, and electric vehicles with company warranty", "https://mgcambodia.com/search?q={q}", "https://mgcambodia.com", "CARS"),
            ("byd_cambodia", "BYD Cambodia", "bydcambodia.com", "⚡ Electric Vehicles & Network", "BYD Cambodia", "Electric vehicle lineup (Atto 3, Seal, Dolphin) and charging network info", "https://bydcambodia.com/search?q={q}", "https://bydcambodia.com", "CARS"),
            ("mazda_cambodia", "Mazda Cambodia", "mazda.com.kh", "🚗 Mazda Showroom & Service", "Mazda Cambodia", "Official Mazda showroom models (CX-5, BT-50) and maintenance booking", "https://www.mazda.com.kh/search?q={q}", "https://www.mazda.com.kh", "CARS"),
            ("bmw_cambodia", "BMW Cambodia", "bmw.com.kh", "🚘 Luxury Performance", "BMW Cambodia", "Premium luxury vehicles, M Performance, and official certified servicing", "https://www.bmw.com.kh/search?q={q}", "https://www.bmw.com.kh", "CARS"),
            ("autoparts_cambodia", "Auto Parts Cambodia", "autopartscambodia.com", "⚙️ Spare Parts, Tires & Oils", "Auto Parts Cambodia", "Spare parts, tires, motor oils, brake pads, and maintenance components", "https://autopartscambodia.com/search?q={q}", "https://autopartscambodia.com", "CARS"),
            ("khmer_moto", "Khmer Moto", "khmermoto.com", "🏍️ Dirt Bikes & Scooters", "Khmer Moto", "Dirt bikes, scooters, touring bikes, and motorcycle classifieds", "https://khmermoto.com/search?q={q}", "https://khmermoto.com", "CARS"),
            ("sihanoukville_auto", "Sihanoukville Auto", "sihanoukvilleauto.com", "🚗 Regional Coastal Market", "Sihanoukville Auto", "Regional vehicle marketplace and rentals for Sihanoukville and coastal areas", "https://sihanoukvilleauto.com/search?q={q}", "https://sihanoukvilleauto.com", "CARS"),
            ("angkor_auto", "Angkor Auto", "angkorauto.com", "🚗 Vehicle Imports & Auction", "Angkor Auto", "Vehicle imports, auction sourcing, and verified used vehicle brokerage", "https://angkorauto.com/search?q={q}", "https://angkorauto.com", "CARS")
        ]
    },
    {
        "cat_id": "REAL_ESTATE",
        "cat_name_en": "Real Estate, Housing & Property Portals",
        "cat_name_kh": "អចលនទ្រព្យ បុរី & ផ្ទះជួល",
        "icon": "🏠",
        "items": [
            ("realestate_kh", "Realestate.com.kh", "realestate.com.kh", "🏠 47K+ Listings & Loans", "Realestate.com.kh", "Largest property search engine for sale and rent, interactive maps and loan tools", "https://www.realestate.com.kh/buy/?q={q}", "https://www.realestate.com.kh", "REAL_ESTATE"),
            ("compass_kh", "Compass Cambodia", "compass.com.kh", "🏠 Multi-Language Trends", "Compass Cambodia", "Apartments, land plots, boreys, and office spaces with price trend analysis", "https://www.compass.com.kh/search?q={q}", "https://www.compass.com.kh", "REAL_ESTATE"),
            ("harbor_property", "Harbor Property", "harbor-property.com", "🏠 3D Virtual Tours", "Harbor Property", "Verified property listings with 3D virtual tours and direct landlord contact", "https://www.harbor-property.com/?s={q}", "https://www.harbor-property.com", "REAL_ESTATE"),
            ("ips_cambodia", "IPS Cambodia", "ips-cambodia.com", "🏠 Expat Rentals & Leases", "IPS Cambodia", "Expat rentals, residential sales, and commercial leases in PP and provinces", "https://ips-cambodia.com/properties/?keyword={q}", "https://ips-cambodia.com", "REAL_ESTATE"),
            ("fazwaz_kh", "FazWaz Cambodia", "fazwaz.com.kh", "🏠 3D Floor Plans & Analytics", "FazWaz Cambodia", "New housing developments, 3D interactive floor plans, and price analytics", "https://www.fazwaz.com.kh/property-sales/cambodia?q={q}", "https://www.fazwaz.com.kh", "REAL_ESTATE"),
            ("century21_kh", "Century 21 Cambodia", "century21.com.kh", "🏠 25 Provinces Franchise", "Century 21 Cambodia", "Franchised property directory and land verification across 25 provinces", "https://www.century21.com.kh/search?q={q}", "https://www.century21.com.kh", "REAL_ESTATE"),
            ("cbre_kh", "CBRE Cambodia", "cbre.com.kh", "🏢 Corporate & Industrial", "CBRE Cambodia", "Corporate commercial spaces, industrial parks, and institutional valuations", "https://www.cbre.com.kh/properties?search={q}", "https://www.cbre.com.kh", "REAL_ESTATE"),
            ("knightfrank_kh", "Knight Frank Cambodia", "knightfrank.com.kh", "🏠 Luxury Advisory & Research", "Knight Frank Cambodia", "High-end property consulting, prime residential towers, and market research", "https://www.knightfrank.com.kh/properties?keyword={q}", "https://www.knightfrank.com.kh", "REAL_ESTATE"),
            ("towncity_kh", "TownCity Real Estate", "towncity.com", "🏠 Villas & Factories", "TownCity Real Estate", "Villas, land plots, borey rentals, and factory space leasing", "https://towncity.com/property-search/?keyword={q}", "https://towncity.com", "REAL_ESTATE"),
            ("mapletree_realty", "Mapletree Realty", "mapletreer.com", "🏠 Residential & Land", "Mapletree Realty", "Residential and land property portal with transparent advisory", "https://www.mapletreer.com/search?q={q}", "https://www.mapletreer.com", "REAL_ESTATE"),
            ("pointer_property", "Pointer Property", "pointerasia.com", "🏠 Local Agency Directory", "Pointer Property", "Local real estate agency listings, project consulting, and commercial leases", "https://pointerasia.com/search?q={q}", "https://pointerasia.com", "REAL_ESTATE"),
            ("khmerpropertyfree", "Khmer Property Free", "khmerpropertyfree.com", "🏠 Free Property Classifieds", "Khmer Property Free", "Free real estate classified ads for individual landlords and sellers", "https://khmerpropertyfree.com/search?q={q}", "https://khmerpropertyfree.com", "REAL_ESTATE"),
            ("cambodiapropertyshop", "Cambodia Property Shop", "cambodiapropertyshop.com", "🏠 Agency Directory", "Cambodia Property Shop", "Local agency property directory covering apartments, land, and shophouses", "https://cambodiapropertyshop.com/search?q={q}", "https://cambodiapropertyshop.com", "REAL_ESTATE"),
            ("sornseap_property", "Sorn Seap Property", "sornseap.com", "🏠 Land & Residential Advisory", "Sorn Seap Property", "Land and residential advisory portal by prominent Cambodian realtors", "https://sornseap.com/search?q={q}", "https://sornseap.com", "REAL_ESTATE"),
            ("key_realestate", "Key Real Estate", "keyrealestate.com.kh", "🏠 Valuation & Agency", "Key Real Estate", "Property valuation, title deed verification, and agency sales", "https://keyrealestate.com.kh/search?q={q}", "https://keyrealestate.com.kh", "REAL_ESTATE"),
            ("vtrust_property", "VTrust Property", "vtrustproperty.com", "🏢 Commercial Office Leasing", "VTrust Property", "Commercial office tower leasing, appraisal services, and residential homes", "https://vtrustproperty.com/search?q={q}", "https://vtrustproperty.com", "REAL_ESTATE"),
            ("penghuoth", "Borey Peng Huoth", "penghuoth.com", "🏡 Luxury Gated Communities", "Borey Peng Huoth (បុរី ប៉េង ហួត)", "Gated community housing developer site, luxury villas, and shophouses", "https://penghuoth.com/search?q={q}", "https://penghuoth.com", "REAL_ESTATE"),
            ("chipmong_land", "Borey Chip Mong", "chipmongland.com", "🏡 Townhouses & Condos", "Borey Chip Mong Land", "Townhouses, modern condos, luxury villas, and community malls", "https://chipmongland.com/search?q={q}", "https://chipmongland.com", "REAL_ESTATE"),
            ("urbanland", "Urbanland", "urbanland.asia", "🏢 Architectural Condos", "Urbanland Cambodia", "Modern architectural condos, creative offices, and commercial hubs (Embassy Central)", "https://urbanland.asia/search?q={q}", "https://urbanland.asia", "REAL_ESTATE"),
            ("princere", "Prince Real Estate", "princere.com", "🏙️ High-Rise Towers & Malls", "Prince Real Estate (ព្រីនស៍)", "High-rise residential towers, commercial plazas, and mixed developments", "https://princere.com/search?q={q}", "https://princere.com", "REAL_ESTATE")
        ]
    },
    {
        "cat_id": "FASHION",
        "cat_name_en": "Fashion, Apparel, Bags & Shoes",
        "cat_name_kh": "ម៉ូដ សម្លៀកបំពាក់ & ស្បែកជើង",
        "icon": "👗",
        "items": [
            ("zando", "Zando", "zando.com.kh", "👗 Trending Apparel", "Zando Cambodia", "Trendy clothing and footwear store platform with fast nationwide shipping", "https://zando.com.kh/search?q={q}", "https://zando.com.kh", "FASHION"),
            ("l192_fashion", "L192 Fashion", "l192.com", "👗 Low-Cost Daily Drops", "L192 Fashion", "Low-cost fashion, shoes, cosmetics, and lifestyle accessories with flash sales", "https://l192.com/search?q={q}", "https://l192.com", "FASHION"),
            ("ten11", "Ten11", "ten11.com.kh", "👗 Urban Streetwear", "Ten11 Clothing", "Streetwear and casual fashion boutique with seasonal urban collections", "https://ten11.com.kh/search?q={q}", "https://ten11.com.kh", "FASHION"),
            ("pedro_kh", "Pedro Cambodia", "pedroshoes.com/kh", "👠 Footwear & Leather Bags", "Pedro Cambodia", "Official store for footwear, bags, belts, and leather accessories", "https://www.pedroshoes.com/kh/search?q={q}", "https://www.pedroshoes.com/kh", "FASHION"),
            ("charles_keith_kh", "Charles & Keith Cambodia", "charleskeith.com/kh", "👜 Designer Handbags & Heels", "Charles & Keith Cambodia", "Designer handbags, heels, and fashion accessories delivered to your doorstep", "https://www.charleskeith.com/kh/search?q={q}", "https://www.charleskeith.com/kh", "FASHION"),
            ("routine_kh", "Routine Cambodia", "routine.com.kh", "👕 Minimalist Apparel", "Routine Cambodia", "Minimalist everyday apparel, smart-casual trousers, and office shirts", "https://routine.com.kh/search?q={q}", "https://routine.com.kh", "FASHION"),
            ("mango_kh", "Mango Cambodia", "mango.com/kh", "👗 Official Global Apparel", "Mango Cambodia", "Official local site for global apparel, women's dresses, and stylish outerwear", "https://shop.mango.com/kh/search?q={q}", "https://shop.mango.com/kh", "FASHION"),
            ("levis_kh", "Levi's Cambodia", "levis.com.kh", "👖 Official Denim & Jackets", "Levi's Cambodia", "Official denim jeans (501), jackets, and classic graphic tops", "https://www.levis.com.kh/search?q={q}", "https://www.levis.com.kh", "FASHION"),
            ("adidas_kh", "Adidas Cambodia", "adidas.com.kh", "👟 Sportswear & Sneakers", "Adidas Cambodia", "Official sportswear, running shoes, Samba/Stan Smith sneakers, and athletic gear", "https://www.adidas.com.kh/search?q={q}", "https://www.adidas.com.kh", "FASHION"),
            ("nike_kh", "Nike Cambodia", "nike.com/kh", "👟 Running Shoes & Gear", "Nike Cambodia", "Running shoes, Air Jordan/Air Force sneakers, athletic apparel, and workout gear", "https://www.nike.com/kh/w?q={q}", "https://www.nike.com/kh", "FASHION"),
            ("puma_kh", "Puma Cambodia", "puma.com/kh", "👟 Activewear & Slides", "Puma Cambodia", "Activewear, slides, casual sneakers, and training outfits", "https://www.puma.com/kh/search?q={q}", "https://www.puma.com/kh", "FASHION"),
            ("vnc_kh", "VNC Cambodia", "vnc.com.kh", "👠 Women's Footwear & Bags", "VNC Cambodia", "Women's footwear and bag collections with stylish comfort designs", "https://vnc.com.kh/search?q={q}", "https://vnc.com.kh", "FASHION"),
            ("little_fashion", "Little Fashion KH", "littlefashion.com.kh", "👗 Women's Trendy Wear", "Little Fashion KH", "Women's fashion, evening dresses, accessories, and casual tops", "https://littlefashion.com.kh/search?q={q}", "https://littlefashion.com.kh", "FASHION"),
            ("brand_collection", "Brand Collection KH", "brandcollection.com.kh", "👕 Imported Brand Apparel", "Brand Collection KH", "Imported brand-name clothing, polo shirts, and authentic fashion overstocks", "https://brandcollection.com.kh/search?q={q}", "https://brandcollection.com.kh", "FASHION"),
            ("amarak_fashion", "Amarak Fashion", "amarakfashion.com", "👗 Khmer Silk & Traditional", "Amarak Fashion", "Modern Khmer silk, traditional festive wear, and tailored evening garments", "https://amarakfashion.com/search?q={q}", "https://amarakfashion.com", "FASHION"),
            ("clothesline_resale", "Clothesline Resale", "clotheslinekh.com", "👗 Pre-Loved Sustainable", "Clothesline Resale", "Pre-loved secondhand fashion hub promoting sustainable clothing and vintage", "https://clotheslinekh.com/search?q={q}", "https://clotheslinekh.com", "FASHION"),
            ("giordano_kh", "Giordano Cambodia", "giordano.com.kh", "👕 Casual Polos & Tees", "Giordano Cambodia", "Casual polo shirts, cotton tees, chinos, and everyday essentials", "https://giordano.com.kh/search?q={q}", "https://giordano.com.kh", "FASHION"),
            ("bossini_kh", "Bossini Cambodia", "bossini.com.kh", "👕 Family Casual Wear", "Bossini Cambodia", "Family casual wear, children's clothes, and comfortable activewear", "https://bossini.com.kh/search?q={q}", "https://bossini.com.kh", "FASHION"),
            ("aldo_kh", "Aldo Shoes Cambodia", "aldoshoes.com.kh", "👞 Dress Shoes & Leather", "Aldo Shoes Cambodia", "Dress shoes, boots, high heels, and premium leather goods", "https://aldoshoes.com.kh/search?q={q}", "https://aldoshoes.com.kh", "FASHION"),
            ("pandora_kh", "Pandora Cambodia", "pandora.net/kh", "💍 Jewelry & Charms", "Pandora Cambodia", "Jewelry, charm bracelets, rings, necklaces, and luxury gifts", "https://www.pandora.net/kh/search?q={q}", "https://www.pandora.net/kh", "FASHION")
        ]
    },
    {
        "cat_id": "BEAUTY",
        "cat_name_en": "Beauty, Skincare, Cosmetics & Health",
        "cat_name_kh": "សម្រស់ ថែរក្សាស្បែក គ្រឿងសម្អាង & សុខភាព",
        "icon": "💄",
        "items": [
            ("l192_beauty", "L192 Beauty", "l192.com/beauty", "💄 Skincare & Beauty Tools", "L192 Beauty", "Skincare, cosmetics, lipsticks, serums, and beauty tools with flash discounts", "https://l192.com/beauty/search?q={q}", "https://l192.com/beauty", "BEAUTY"),
            ("smileshop_beauty", "Smile Shop Beauty", "smileshop.com.kh/beauty", "💄 Asian Cosmetics & Care", "Smile Shop Beauty", "Asian cosmetics and skincare shop with authentic brand guarantees", "https://smileshop.com.kh/beauty?q={q}", "https://smileshop.com.kh/beauty", "BEAUTY"),
            ("skinfood_kh", "Skin Food Cambodia", "skinfood.com.kh", "🍃 Organic Food Skincare", "Skin Food Cambodia", "Korean organic food-based skincare, cleansers, and hydrating essences", "https://skinfood.com.kh/search?q={q}", "https://skinfood.com.kh", "BEAUTY"),
            ("thefaceshop_kh", "The Face Shop Cambodia", "thefaceshop.com.kh", "🌸 Face Masks & Cleansers", "The Face Shop Cambodia", "Natural face masks, foaming cleansers, and Korean beauty cosmetics", "https://thefaceshop.com.kh/search?q={q}", "https://thefaceshop.com.kh", "BEAUTY"),
            ("innisfree_kh", "Innisfree Cambodia", "innisfree.com/kh", "🌿 Eco-Friendly Skincare", "Innisfree Cambodia", "Eco-friendly skincare products formulated with natural Jeju Island green tea", "https://www.innisfree.com/kh/en/main/index.do?q={q}", "https://www.innisfree.com/kh", "BEAUTY"),
            ("laneige_kh", "Laneige Cambodia", "laneige.com/kh", "💧 Hydrating Serums & Masks", "Laneige Cambodia", "Hydrating water bank serums, sleeping masks, and lip treatment care", "https://www.laneige.com/kh/search?q={q}", "https://www.laneige.com/kh", "BEAUTY"),
            ("watsons_kh", "Watsons Cambodia", "watsons.com.kh", "💊 Health & Beauty Pharmacy", "Watsons Cambodia", "Health, cosmetics, personal care, and licensed pharmacy items", "https://www.watsons.com.kh/search?text={q}", "https://www.watsons.com.kh", "BEAUTY"),
            ("guardian_kh", "Guardian Cambodia", "guardian.com.kh", "🛁 Bath, Body & Skincare", "Guardian Cambodia", "Pharmacy goods, bath items, sunscreens, and international skincare brands", "https://guardian.com.kh/search?q={q}", "https://guardian.com.kh", "BEAUTY"),
            ("yves_rocher_kh", "Yves Rocher Cambodia", "yvesrocher.com.kh", "🌿 Botanical Care & Perfume", "Yves Rocher Cambodia", "Botanical hair care, body lotions, shower gels, and French fragrances", "https://yvesrocher.com.kh/search?q={q}", "https://yvesrocher.com.kh", "BEAUTY"),
            ("paulas_choice_kh", "Paula's Choice Cambodia", "paulaschoice.com.kh", "🧪 Clinical Exfoliants (BHA)", "Paula's Choice Cambodia", "Clinical skincare exfoliants, 2% BHA liquid, niacinamide, and retinol serums", "https://paulaschoice.com.kh/search?q={q}", "https://paulaschoice.com.kh", "BEAUTY"),
            ("cerave_kh", "CeraVe Cambodia", "cerave.com.kh", "🧴 Dermatologist Moisturizers", "CeraVe Cambodia", "Dermatologist-tested ceramide moisturizers, gentle foaming cleansers, and creams", "https://cerave.com.kh/search?q={q}", "https://cerave.com.kh", "BEAUTY"),
            ("pharmacie_de_la_gare", "Pharmacie De La Gare", "pharmaciedelagare.com.kh", "💊 Licensed French Pharmacy", "Pharmacie De La Gare", "Licensed online pharmacy store stocking authentic medicines and health vitamins", "https://pharmaciedelagare.com.kh/search?q={q}", "https://pharmaciedelagare.com.kh", "BEAUTY"),
            ("ucare_pharmacy", "U-Care Pharmacy", "ucarepharmacy.com.kh", "💊 Health Supplements & Care", "U-Care Pharmacy", "Health supplements, prescription goods, dermo-cosmetics, and baby care", "https://ucarepharmacy.com.kh/search?q={q}", "https://ucarepharmacy.com.kh", "BEAUTY"),
            ("extra_pharmacy", "Extra Pharmacy", "extrapharmacy.com.kh", "💊 Medical Supplies & Health", "Extra Pharmacy", "Local medical supplies, health monitors, supplements, and family care products", "https://extrapharmacy.com.kh/search?q={q}", "https://extrapharmacy.com.kh", "BEAUTY"),
            ("pharmacare_kh", "Pharmacie Pharmacare", "pharmacare.com.kh", "🧼 Hygiene & Family Health", "Pharmacie Pharmacare", "Personal hygiene, healthcare products, first-aid equipment, and wellness goods", "https://pharmacare.com.kh/search?q={q}", "https://pharmacare.com.kh", "BEAUTY"),
            ("dermalogica_kh", "Dermalogica Cambodia", "dermalogica.com.kh", "🧴 Professional Skin Therapy", "Dermalogica Cambodia", "Professional skincare treatments, microfoliants, and anti-aging remedies", "https://dermalogica.com.kh/search?q={q}", "https://dermalogica.com.kh", "BEAUTY"),
            ("bath_body_works_kh", "Bath & Body Works KH", "bathandbodyworks.com.kh", "🕯️ Fragrance, Lotions & Soaps", "Bath & Body Works KH", "Scented body lotions, fine fragrance mists, 3-wick candles, and foaming soaps", "https://bathandbodyworks.com.kh/search?q={q}", "https://bathandbodyworks.com.kh", "BEAUTY"),
            ("senteurs_dangkor", "Senteurs d'Angkor", "senteursdangkor.com", "🌺 Handmade Natural Soaps", "Senteurs d'Angkor", "Handmade natural soaps, aromatherapy spa goods, and Khmer herbal balms", "https://senteursdangkor.com/search?q={q}", "https://senteursdangkor.com", "BEAUTY"),
            ("bodia_nature", "Bodia Nature", "bodia.com", "🌿 Organic Spa & Essential Oils", "Bodia Nature (ស្ប៉ាធម្មជាតិ)", "Organic spa items, natural essential oils, body scrubs, and herbal teas", "https://bodia.com/search?q={q}", "https://bodia.com", "BEAUTY"),
            ("k_beauty_kh", "K-Beauty KH", "kbeautykh.com", "✨ Korean Sunscreen & Care", "K-Beauty KH", "Korean sunscreen, centella soothing gels, serums, and trending K-beauty items", "https://kbeautykh.com/search?q={q}", "https://kbeautykh.com", "BEAUTY")
        ]
    },
    {
        "cat_id": "FURNITURE",
        "cat_name_en": "Furniture, Home Decor & Household Appliances",
        "cat_name_kh": "គ្រឿងសង្ហារិម ការតុបតែងផ្ទះ & គ្រឿងផ្ទះបាយ",
        "icon": "🛋️",
        "items": [
            ("sunsimexco_home", "Sunsimexco", "sunsimexco.com", "⚡ Major Home Electronics", "Sunsimexco Appliances", "Major distributor for Sony, Panasonic, and LG home appliances, TVs, and aircon", "https://sunsimexco.com/search?q={q}", "https://sunsimexco.com", "FURNITURE"),
            ("kfour_home", "K-Four Home", "kfour.com.kh", "❄️ Refrigerators & Washers", "K-Four Home Appliances", "Refrigerators, washing machines, air conditioners, and kitchen appliances", "https://kfour.com.kh/search?q={q}", "https://kfour.com.kh", "FURNITURE"),
            ("sb_furniture", "SB Furniture Cambodia", "sbfurniture.com.kh", "🛋️ Bedroom Sets & Desks", "SB Furniture Cambodia", "Modern bedroom sets, ergonomic office desks, wardrobes, and living room sofas", "https://sbfurniture.com.kh/search?q={q}", "https://sbfurniture.com.kh", "FURNITURE"),
            ("index_living_mall", "Index Living Mall KH", "indexlivingmall.com.kh", "🏡 Home Furniture & Kitchen", "Index Living Mall KH", "Home furniture, kitchenware, storage organizers, and modern home decor", "https://indexlivingmall.com.kh/search?q={q}", "https://indexlivingmall.com.kh", "FURNITURE"),
            ("reya_home", "Reya Home", "reya-home.com", "🪑 Minimalist Beds & Tables", "Reya Home", "Minimalist beds, wooden dining tables, TV cabinets, and home furnishings", "https://reya-home.com/search?q={q}", "https://reya-home.com", "FURNITURE"),
            ("leela_home", "Leela Home", "leelahome.com", "🔥 Mattresses & Gas Stoves", "Leela Home", "Comfortable mattresses, gas stoves, range hoods, and water heaters", "https://leelahome.com/search?q={q}", "https://leelahome.com", "FURNITURE"),
            ("home_top", "Home Top Cambodia", "hometop.com.kh", "🔨 Home Improvement & Lighting", "Home Top Cambodia", "Home improvement materials, hardware tools, chandeliers, and LED lighting", "https://hometop.com.kh/search?q={q}", "https://hometop.com.kh", "FURNITURE"),
            ("ashley_furniture", "Ashley Furniture KH", "ashleyfurniture.com.kh", "🛋️ American Sofas & Recliners", "Ashley Furniture KH", "American luxury living room sofas, power recliners, and solid wood sets", "https://ashleyfurniture.com.kh/search?q={q}", "https://ashleyfurniture.com.kh", "FURNITURE"),
            ("nocnoc_kh", "NocNoc Cambodia", "nocnoc.com.kh", "🏡 Interior & Building Goods", "NocNoc Cambodia", "Interior furniture, flooring, tiles, sanitary ware, and building materials", "https://nocnoc.com.kh/search?q={q}", "https://nocnoc.com.kh", "FURNITURE"),
            ("jysk_cambodia", "JYSK Cambodia", "jysk.com.kh", "🛏️ Nordic Furniture & Bedding", "JYSK Cambodia", "Scandinavian Nordic furniture, comfortable bedding, duvets, and home goods", "https://jysk.com.kh/search?q={q}", "https://jysk.com.kh", "FURNITURE"),
            ("dyson_cambodia", "Dyson Cambodia", "dyson.com.kh", "💨 Vacuums & Air Purifiers", "Dyson Cambodia", "Cordless stick vacuums, HEPA air purifiers, and Supersonic hair styling tools", "https://dyson.com.kh/search?q={q}", "https://dyson.com.kh", "FURNITURE"),
            ("electrolux_kh", "Electrolux Cambodia", "electrolux.com.kh", "🧺 Kitchen Care & Washers", "Electrolux Cambodia", "Kitchen appliances, front-load washing machines, dryers, and microwave ovens", "https://www.electrolux.com.kh/search?q={q}", "https://www.electrolux.com.kh", "FURNITURE"),
            ("beko_cambodia", "Beko Cambodia", "beko.com/kh", "❄️ European Refrigerators", "Beko Cambodia", "European-engineered refrigerators, dishwashers, and kitchen cooking gear", "https://www.beko.com/kh-en/search?q={q}", "https://www.beko.com/kh", "FURNITURE"),
            ("haier_cambodia", "Haier Cambodia", "haier.com/kh", "📺 Smart Displays & Freezers", "Haier Cambodia", "Smart 4K displays, chest freezers, inverter air conditioners, and coolers", "https://www.haier.com/kh/search/?q={q}", "https://www.haier.com/kh", "FURNITURE"),
            ("midea_cambodia", "Midea Cambodia", "midea.com/kh", "🍳 Small Kitchen Appliances", "Midea Cambodia", "Small kitchen appliances, rice cookers, electric kettles, blenders, and fans", "https://www.midea.com/kh/search?q={q}", "https://www.midea.com/kh", "FURNITURE"),
            ("locknlock_kh", "LocknLock Cambodia", "locknlock.com.kh", "🍲 Air Fryers & Cookware", "LocknLock Cambodia", "Air fryers, airtight glass containers, thermal tumblers, and non-stick pans", "https://locknlock.com.kh/search?q={q}", "https://locknlock.com.kh", "FURNITURE"),
            ("homecook_kh", "Home Cook KH", "homecookkh.com", "🍳 Cookware Sets & Utensils", "Home Cook KH", "Cookware sets, stainless steel pots, knife blocks, and baking utensils", "https://homecookkh.com/search?q={q}", "https://homecookkh.com", "FURNITURE"),
            ("modernhouse_kh", "Modern House KH", "modernhouse.com.kh", "🛋️ Rugs, Curtains & Decor", "Modern House KH", "Plush floor rugs, blackout curtains, throw pillows, and living accessories", "https://modernhouse.com.kh/search?q={q}", "https://modernhouse.com.kh", "FURNITURE"),
            ("comfort_mattress", "Comfort Mattress KH", "comfortmattress.com.kh", "🛏️ Memory Foam Mattresses", "Comfort Mattress KH", "Beds, orthopedic memory foam mattresses, and latex ergonomic pillows", "https://comfortmattress.com.kh/search?q={q}", "https://comfortmattress.com.kh", "FURNITURE"),
            ("bambou_indochine", "Bambou Indochine", "bambouindochine.com", "🎋 Bamboo & Rattan Decor", "Bambou Indochine", "Handcrafted bamboo home decor, woven baskets, rattan chairs, and lighting", "https://bambouindochine.com/search?q={q}", "https://bambouindochine.com", "FURNITURE")
        ]
    },
    {
        "cat_id": "GROCERIES",
        "cat_name_en": "Supermarkets, Groceries & Daily Essentials",
        "cat_name_kh": "ផ្សារទំនើប គ្រឿងទេស & ទំនិញប្រចាំថ្ងៃ",
        "icon": "🛒",
        "items": [
            ("aeon_online", "AEON Online Shopping", "aeononlineshopping.com", "🏬 Japanese Imports & Groceries", "AEON Online Shopping", "AEON mall groceries, Japanese imports, TopValu items, and fresh produce", "https://aeononlineshopping.com/search?q={q}", "https://aeononlineshopping.com", "GROCERIES"),
            ("chipmong_supermarket", "Chip Mong Supermarket", "chipmong.com/supermarket", "🥩 Fresh Produce & Pantry", "Chip Mong Supermarket", "Fresh produce, imported meats, dairy, bakery goods, and pantry essentials", "https://www.chipmong.com/supermarket?q={q}", "https://www.chipmong.com/supermarket", "GROCERIES"),
            ("makro_cambodia", "Makro Cambodia", "makrocambodia.com", "📦 Wholesale Cash & Carry", "Makro Cambodia (ម៉ាក្រូ)", "Wholesale cash-and-carry grocery site for bulk food, snacks, and catering supplies", "https://www.makrocambodia.com/search?q={q}", "https://www.makrocambodia.com", "GROCERIES"),
            ("grocerdel", "Grocerdel", "grocerdel.com", "🥬 Organic Farm Produce", "Grocerdel Farm Produce", "Fresh local farm produce, organic vegetables, artisan bakery, and eco goods", "https://grocerdel.com/search?q={q}", "https://grocerdel.com", "GROCERIES"),
            ("nham24_groceries", "Nham24 Groceries", "nham24.com/mart", "⚡ Fast On-Demand Mart", "Nham24 Groceries", "Fast on-demand supermarket delivery from local stores in 30-45 minutes", "https://nham24.com/mart?q={q}", "https://nham24.com/mart", "GROCERIES"),
            ("grabmart_kh", "GrabMart Cambodia", "mart.grab.com/kh", "⚡ Convenience & Mart Orders", "GrabMart Cambodia", "Convenience store and market orders delivered directly to your doorstep", "https://mart.grab.com/kh/search?q={q}", "https://mart.grab.com/kh", "GROCERIES"),
            ("foodpanda_shop", "Foodpanda Shop KH", "foodpanda.com.kh/shops", "🐼 Supermarkets & Pharmacy", "Foodpanda Shops KH", "Supermarket goods, pharmacy products, and snacks delivered on-demand", "https://www.foodpanda.com.kh/shops?q={q}", "https://www.foodpanda.com.kh/shops", "GROCERIES"),
            ("lucky_supermarket", "Lucky Supermarket", "luckysupermarket.com.kh", "🛒 Imported Food & Essentials", "Lucky Supermarket (ផ្សារឡាក់គី)", "Cambodia's trusted supermarket for imported food, fresh dairy, and meats", "https://luckysupermarket.com.kh/search?q={q}", "https://luckysupermarket.com.kh", "GROCERIES"),
            ("fairplus_market", "FairPlus Market", "fairplus.com.kh", "🛒 Community Grocery Store", "FairPlus Market", "Local community grocery store offering competitive pricing on staples", "https://fairplus.com.kh/search?q={q}", "https://fairplus.com.kh", "GROCERIES"),
            ("bayon_market", "Bayon Market", "bayonmarket.com.kh", "🧀 European Cheeses & Wine", "Bayon Market", "Imported European snacks, gourmet cheeses, cold cuts, and fine wines", "https://bayonmarket.com.kh/search?q={q}", "https://bayonmarket.com.kh", "GROCERIES"),
            ("super_duper", "Super Duper", "superduper.com.kh", "🕒 24/7 Western Supermarket", "Super Duper 24/7", "24/7 Western grocery site with international snacks, spirits, and frozen goods", "https://superduper.com.kh/search?q={q}", "https://superduper.com.kh", "GROCERIES"),
            ("kiwi_mart", "KiWi Mart", "kiwimart.com.kh", "🏪 Convenience Goods & Drinks", "KiWi Mart Cambodia", "Convenience chain for quick drinks, snacks, instant noodles, and hygiene goods", "https://kiwimart.com.kh/search?q={q}", "https://kiwimart.com.kh", "GROCERIES"),
            ("natural_garden", "Natural Garden", "naturalgarden.com.kh", "🌱 Certified Organic Veggies", "Natural Garden", "Certified organic vegetables, free-range poultry, and healthy wellness groceries", "https://naturalgarden.com.kh/search?q={q}", "https://naturalgarden.com.kh", "GROCERIES"),
            ("khmer_organic", "Khmer Organic Cooperative", "khmer-organic.com", "🥗 Farm-To-Table Produce", "Khmer Organic Cooperative", "Farm-to-table organic produce supporting local Cambodian farmer cooperatives", "https://khmer-organic.com/search?q={q}", "https://khmer-organic.com", "GROCERIES"),
            ("veggys_cambodia", "Veggy's Cambodia", "veggys.com.kh", "🥩 Premium Butchery & Wines", "Veggy's Cambodia", "Premium butchery, Australian beef, French gourmet cheeses, and imported wines", "https://veggys.com.kh/search?q={q}", "https://veggys.com.kh", "GROCERIES"),
            ("danmeats_cambodia", "DanMeats Cambodia", "danmeats.com", "🥓 Specialty Sausages & Cuts", "DanMeats Cambodia", "Specialty sausages, smoked bacon, ham, and European cold cuts", "https://danmeats.com/search?q={q}", "https://danmeats.com", "GROCERIES"),
            ("farmland_kh", "Farmland KH", "farmlandkh.com", "🥛 Dairy, Eggs & Farm Goods", "Farmland Cambodia", "Local pasteurized dairy milk, fresh farm eggs, yogurts, and butter", "https://farmlandkh.com/search?q={q}", "https://farmlandkh.com", "GROCERIES"),
            ("delishop_asia", "Delishop Cambodia", "delishop.asia", "🛒 10,000+ Online Supermarket", "Delishop Cambodia", "Online supermarket with over 10,000 items, imported groceries, and organic food", "https://delishop.asia/search?q={q}", "https://delishop.asia", "GROCERIES"),
            ("asia_supermarket", "Asia Supermarket", "asiasupermarket.com.kh", "🍜 Asian Spices & Noodles", "Asia Supermarket", "Asian culinary spices, Thai/Vietnamese sauces, instant ramen, and seasonings", "https://asiasupermarket.com.kh/search?q={q}", "https://asiasupermarket.com.kh", "GROCERIES"),
            ("wine_company_kh", "Wine Company Cambodia", "winecompany.com.kh", "🍷 Wines, Spirits & Beers", "The Wine Company KH", "Curated international wines, premium whiskeys, spirits, and craft beers", "https://winecompany.com.kh/search?q={q}", "https://winecompany.com.kh", "GROCERIES")
        ]
    },
    {
        "cat_id": "SERVICES",
        "cat_name_en": "Books, Services, Travel & Logistics",
        "cat_name_kh": "សៀវភៅ សំបុត្រធ្វើដំណើរ & ដឹកជញ្ជូន",
        "icon": "📦",
        "items": [
            ("bookmebus", "BookMeBus", "bookmebus.com", "🚌 Bus, Ferry & Taxi Booking", "BookMeBus (កក់សំបុត្រ)", "Bus, ferry, and private taxi booking engine across all Cambodian destinations", "https://bookmebus.com/search?q={q}", "https://bookmebus.com", "SERVICES"),
            ("camboticket", "CamboTicket", "camboticket.com", "🎟️ Intercity Transport Booking", "CamboTicket", "Intercity transport ticket reservation portal for buses, speedboats, and tours", "https://camboticket.com/search?q={q}", "https://camboticket.com", "SERVICES"),
            ("vireak_buntham", "Vireak Buntham Express", "vireakbuntham.com", "🚌 Bus & Logistics Express", "Vireak Buntham (វីរៈប៊ុនថាំ)", "Inter-province sleeping bus tickets and nationwide parcel delivery logistics", "https://vireakbuntham.com/search?q={q}", "https://vireakbuntham.com", "SERVICES"),
            ("vet_airbus", "Vet Air Bus Express", "vetairbus.com", "🚌 Luxury Bus Travel", "VET Air Bus Express", "Luxury bus tickets, VIP minivan travel schedules, and express parcel services", "https://vetairbus.com/search?q={q}", "https://vetairbus.com", "SERVICES"),
            ("larryta_express", "Larryta Express", "larryta.com", "🚐 VIP Minivan Booking", "Larryta Express", "VIP 15-seater minivan booking between Phnom Penh, Siem Reap, and Sihanoukville", "https://larryta.com/search?q={q}", "https://larryta.com", "SERVICES"),
            ("monument_books", "Monument Books", "monument-books.com", "📚 International Books & Mags", "Monument Books", "International books, Southeast Asian history, children's literature, and magazines", "https://monument-books.com/search?q={q}", "https://monument-books.com", "SERVICES"),
            ("scholar_library", "Scholar Library", "scholarlibrary.com.kh", "📖 Textbooks & Literature", "Scholar Library Cambodia", "Academic textbooks, university reference guides, and local Khmer literature", "https://scholarlibrary.com.kh/search?q={q}", "https://scholarlibrary.com.kh", "SERVICES"),
            ("ds_books", "D's Books Cambodia", "dsbookscambodia.com", "📚 Secondhand English Books", "D's Books Cambodia", "Secondhand English paperbacks, fiction, travel guides, and rare books", "https://dsbookscambodia.com/search?q={q}", "https://dsbookscambodia.com", "SERVICES"),
            ("ibc_cambodia", "IBC Cambodia", "ibccambodia.com", "✏️ Stationery & School Supplies", "IBC Cambodia (អាយប៊ីស៊ី)", "Office stationery, school supplies, art tools, textbooks, and toys", "https://ibccambodia.com/search?q={q}", "https://ibccambodia.com", "SERVICES"),
            ("pbc_cambodia", "PBC Cambodia", "pbccambodia.com", "🎨 Paper & Art Supplies", "PBC Book Center", "Paper products, fine art supplies, drafting tools, and office materials", "https://pbccambodia.com/search?q={q}", "https://pbccambodia.com", "SERVICES"),
            ("legend_cinema", "Legend Cinema", "legend.com.kh", "🎬 Movie Tickets & Popcorn", "Legend Cinema", "Online movie ticketing, cinema seat reservations, and combo concessions", "https://legend.com.kh/search?q={q}", "https://legend.com.kh", "SERVICES"),
            ("major_cineplex_kh", "Major Cineplex KH", "majorcineplex.com.kh", "🍿 Showtimes & Seat Booking", "Major Cineplex Cambodia", "Movie showtimes, IMAX/4DX seat booking, and online cinema vouchers", "https://www.majorcineplex.com.kh/search?q={q}", "https://www.majorcineplex.com.kh", "SERVICES"),
            ("wonderpass", "Wonderpass", "wonderpass.asia", "🎫 Events & Sports Passes", "Wonderpass Cambodia", "Digital ticketing and smart passes for festivals, sports matches, and events", "https://wonderpass.asia/search?q={q}", "https://wonderpass.asia", "SERVICES"),
            ("live_bookings", "Live.Bookings KH", "livebookings.asia", "🎸 Concerts & Festival Tickets", "Live.Bookings KH", "Concert tickets, live performance booking, and music festival access", "https://livebookings.asia/search?q={q}", "https://livebookings.asia", "SERVICES"),
            ("jt_express_kh", "J&T Express Cambodia", "jtexpress.com.kh", "📦 Parcel Tracking & Shipping", "J&T Express Cambodia", "Parcel tracking, nationwide courier shipping, and COD e-commerce delivery", "https://jtexpress.com.kh/search?q={q}", "https://jtexpress.com.kh", "SERVICES"),
            ("zto_express_kh", "ZTO Express Cambodia", "zto.com.kh", "🚚 Cross-Border Courier", "ZTO Express Cambodia", "Cross-border China-Cambodia shipping and nationwide express parcel network", "https://zto.com.kh/search?q={q}", "https://zto.com.kh", "SERVICES"),
            ("kerry_express_kh", "Kerry Express KH", "kerryexpress.com.kh", "📦 Next-Day Doorstep Courier", "Kerry Express Cambodia", "Next-day doorstep package delivery and regional corporate dispatch", "https://kerryexpress.com.kh/search?q={q}", "https://kerryexpress.com.kh", "SERVICES"),
            ("cambodia_post", "Cambodia Post", "cambodiapost.post", "📮 State Postal & EMS Express", "Cambodia Post (ប្រៃសណីយ៍កម្ពុជា)", "Official state postal service, EMS express mail, and overseas package parcel post", "https://cambodiapost.post/search?q={q}", "https://cambodiapost.post", "SERVICES"),
            ("ce_logistics", "CE Logistics", "celogistics.com.kh", "🚢 Freight & Cargo Forwarding", "CE Logistics Cambodia", "Air and sea freight forwarding, customs clearance, and commercial cargo", "https://celogistics.com.kh/search?q={q}", "https://celogistics.com.kh", "SERVICES"),
            ("speedwind", "Speedwind Distributions", "speedwind.com.kh", "🚛 Retail & Last-Mile Logistics", "Speedwind Distributions", "Nationwide FMCG retail distribution, warehousing, and last-mile logistics", "https://speedwind.com.kh/search?q={q}", "https://speedwind.com.kh", "SERVICES")
        ]
    }
]

total_count = sum(len(c["items"]) for c in raw_categories)
print(f"Total categories: {len(raw_categories)}, Total platforms: {total_count}")

# Generate Python code
py_platforms = []
for c in raw_categories:
    py_platforms.append(f"    # ── {c['cat_id']} ({len(c['items'])}) ──")
    for item in c["items"]:
        p_dict = {
            "id": item[0],
            "name": item[1],
            "domain": item[2],
            "category": c["cat_id"],
            "badge": item[3],
            "nameKh": item[4],
            "descKh": item[5],
            "searchUrl": item[6],
            "homeUrl": item[7]
        }
        py_platforms.append(f"    {json.dumps(p_dict, ensure_ascii=False)},")

with open("scratch/platforms_py.txt", "w", encoding="utf-8") as f:
    f.write("CAMBODIA_MARKET_PLATFORMS = [\n" + "\n".join(py_platforms) + "\n]\n")

# Generate JS code
js_platforms = []
for c in raw_categories:
    for item in c["items"]:
        js_obj = {
            "id": item[0],
            "name": item[1],
            "domain": item[2],
            "category": c["cat_id"],
            "badge": item[3],
            "nameKh": item[4],
            "descKh": item[5],
            "searchUrl": item[6],
            "homeUrl": item[7],
            "defaultCategory": item[8]
        }
        js_platforms.append(f"        {json.dumps(js_obj, ensure_ascii=False)},")

with open("scratch/platforms_js.txt", "w", encoding="utf-8") as f:
    f.write("    const CAMBODIA_PLATFORMS_DATA = [\n" + "\n".join(js_platforms) + "\n    ];\n")

print("Generated successfully!")
