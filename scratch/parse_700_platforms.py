# scratch/parse_700_platforms.py
import re
import json

raw_user_text = """
**Electronics, Gadgets & Audio**

201. **Gadget Store KH** (`gadgetstorekh.com`) - Smart home accessories and portable audio.
202. **Bora Mobile** (`boramobile.com`) - Smartphone sales and repair services.
203. **Neth Mobile** (`nethmobile.com.kh`) - Budget Android devices and accessories.
204. **Rithy Tech** (`rithytech.com`) - Audio equipment and wireless headphones.
205. **Smart Life Cambodia** (`smartlifecambodia.com`) - Smart watches and fitness trackers.
206. **Socheat Mobile** (`socheatmobile.com`) - Pre-owned iPhones and iPads.
207. **Vannak Mobile** (`vannakmobile.com.kh`) - Screen replacements and phone parts.
208. **Cambodia Gadgets** (`cambodiagadgets.com`) - Drones and action camera accessories.
209. **Phearun Mobile** (`phearunmobile.com`) - Mobile power banks and charging docks.
210. **Phnom Penh Audio** (`phnompenhaudio.com`) - Hi-Fi speakers and amplifiers.
211. **Sony Cambodia** (`sony.com.kh`) - Official cameras, TVs, and audio products.
212. **Bose Cambodia** (`bose.com.kh`) - Premium noise-canceling headphones and soundbars.
213. **JBL Cambodia** (`jbl.com.kh`) - Portable Bluetooth speakers and party systems.
214. **Xiaomi Cambodia** (`[mi.com/kh](https://mi.com/kh)`) - Official smart home products and phones.
215. **Baseus Cambodia** (`baseus.com.kh`) - Fast chargers, phone holders, and cables.
216. **Anker Cambodia** (`anker.com.kh`) - High-capacity power banks and wireless chargers.
217. **Remax Cambodia** (`remax.com.kh`) - Affordable audio gear and phone accessories.
218. **Joyroom Cambodia** (`joyroom.com.kh`) - Phone cases, cables, and Bluetooth earbuds.
219. **Hoco Cambodia** (`hoco.com.kh`) - Car phone mounts, cables, and power adapters.
220. **LDNIO Cambodia** (`ldnio.com.kh`) - Power strips and multi-port USB chargers.
221. **Sennheiser Cambodia** (`sennheiser.com.kh`) - Professional microphones and headphones.
222. **Marshall Cambodia** (`marshallheadphones.com.kh`) - Bluetooth speakers and retro audio gear.
223. **Garmin Cambodia** (`garmin.com.kh`) - GPS smartwatches and sports tracking.
224. **Fitbit Cambodia** (`fitbit.com.kh`) - Health bands and fitness trackers.
225. **DJI Cambodia** (`dji.com.kh`) - Consumer drones, gimbals, and action cameras.
226. **GoPro Cambodia** (`gopro.com.kh`) - Action cameras and chest mounts.
227. **Insta360 Cambodia** (`insta360.com.kh`) - 360-degree cameras and vlogging kits.
228. **Rode Cambodia** (`rode.com.kh`) - Microphones for content creation and podcasting.
229. **Boyas Mic Cambodia** (`boya-mic.com.kh`) - Wireless lapel microphones.
230. **Godox Cambodia** (`godox.com.kh`) - Studio lighting and camera flashes.
231. **Canon Cambodia** (`canon.com.kh`) - DSLR cameras, lenses, and photo printers.
232. **Nikon Cambodia** (`nikon.com.kh`) - Mirrorless cameras and photography optics.
233. **Fujifilm Cambodia** (`fujifilm.com.kh`) - Instant cameras and mirrorless camera systems.
234. **Manfrotto Cambodia** (`manfrotto.com.kh`) - Professional tripods and camera bags.
235. **SanDisk Cambodia** (`sandisk.com.kh`) - MicroSD cards and high-speed flash drives.
236. **Transcend Cambodia** (`transcend.com.kh`) - External hard drives and memory modules.
237. **Kingston Cambodia** (`kingston.com.kh`) - RAM sticks, SSDs, and USB storage.
238. **Lexar Cambodia** (`lexar.com.kh`) - Professional camera memory cards.
239. **UGreen Cambodia** (`ugreen.com.kh`) - USB-C hubs, HDMI splitters, and cables.
240. **Aukey Cambodia** (`aukey.com.kh`) - Fast-charging wall plugs and power banks.
241. **Tronsmart Cambodia** (`tronsmart.com.kh`) - Waterproof outdoor Bluetooth speakers.
242. **Edifier Cambodia** (`edifier.com.kh`) - Bookshelf speakers and gaming headsets.
243. **Logitech Audio KH** (`logitech.com.kh/audio`) - PC headsets and conference speakers.
244. **Razer Audio KH** (`razer.com.kh`) - Gaming headsets and streaming microphones.
245. **HyperX Cambodia** (`hyperx.com.kh`) - Gaming headsets and USB microphones.
246. **SteelSeries KH** (`steelseries.com.kh`) - Premium esports audio gear.
247. **Astro Gaming KH** (`astrogaming.com.kh`) - Console gaming headsets.
248. **Audio-Technica KH** (`audio-technica.com.kh`) - Studio monitor headphones and turntables.
249. **Shure Cambodia** (`shure.com.kh`) - Professional vocal microphones and monitors.
250. **Harman Kardon KH** (`harmankardon.com.kh`) - Home audio sound systems.

**Computer Systems, Gaming & IT Equipment**

251. **ASUS Cambodia** (`[asus.com/kh](https://asus.com/kh)`) - ROG gaming laptops, ZenBooks, and motherboards.
252. **MSI Cambodia** (`[msi.com/kh](https://msi.com/kh)`) - Gaming laptops, motherboards, and graphics cards.
253. **Lenovo Cambodia** (`[lenovo.com/kh](https://lenovo.com/kh)`) - ThinkPad laptops, Legion gaming PCs, and tablets.
254. **Dell Cambodia** (`dell.com.kh`) - XPS laptops, Latitude business PCs, and Alienware.
255. **HP Cambodia** (`hp.com.kh`) - Spectre laptops, Pavilion desktops, and LaserJet printers.
256. **Acer Cambodia** (`[acer.com/kh](https://acer.com/kh)`) - Predator gaming PCs, Swift ultrabooks, and monitors.
257. **Gigabyte Cambodia** (`gigabyte.com.kh`) - AORUS graphics cards, motherboards, and monitors.
258. **Corsair Cambodia** (`corsair.com.kh`) - PC power supplies, RAM, cooling, and keyboards.
259. **NZXT Cambodia** (`nzxt.com.kh`) - PC cases, liquid coolers, and pre-built gaming rigs.
260. **Thermaltake KH** (`thermaltake.com.kh`) - Computer cases and RGB cooling fans.
261. **Cooler Master KH** (`coolermaster.com.kh`) - CPU air coolers and PC chassis.
262. **DeepCool Cambodia** (`deepcool.com.kh`) - Budget CPU liquid coolers and PC cases.
263. **Lian Li Cambodia** (`lian-li.com.kh`) - Premium aluminum PC cases and RGB fans.
264. **Noctua Cambodia** (`noctua.at/kh`) - High-performance silent CPU fans.
265. **Western Digital KH** (`wd.com.kh`) - Internal SSDs, NVMe drives, and hard drives.
266. **Seagate Cambodia** (`seagate.com.kh`) - Barracuda hard drives and NAS storage.
267. **Crucial Cambodia** (`crucial.com.kh`) - Laptop RAM upgrades and SATA SSDs.
268. **Samsung Storage KH** (`[samsung.com/kh/memory-storage](https://samsung.com/kh/memory-storage)`) - 980 Pro NVMe SSDs and portable SSDs.
269. **AORUS Cambodia** (`aorus.com.kh`) - High-end gaming gear and PC components.
270. **ZOTAC Cambodia** (`zotac.com.kh`) - NVIDIA GeForce RTX graphics cards and mini PCs.
271. **Inno3D Cambodia** (`inno3d.com.kh`) - RTX graphics cards and PC GPUs.
272. **Palit Cambodia** (`palit.com.kh`) - Custom graphics cards for gaming.
273. **Sapphire Tech KH** (`sapphiretech.com.kh`) - AMD Radeon graphics cards.
274. **PowerColor KH** (`powercolor.com.kh`) - AMD GPU cards for custom builds.
275. **ASRock Cambodia** (`asrock.com.kh`) - Budget and gaming motherboards.
276. **BenQ Cambodia** (`benq.com.kh`) - Esports gaming monitors and eye-care displays.
277. **ViewSonic Cambodia** (`viewsonic.com.kh`) - Monitors, projectors, and interactive displays.
278. **AOC Monitors KH** (`aoc.com.kh`) - Curved gaming displays and office monitors.
279. **Philips Displays KH** (`philips.com.kh/monitors`) - Ultra-wide office monitors.
280. **Epson Cambodia** (`epson.com.kh`) - EcoTank ink tank printers and projectors.
281. **Brother Cambodia** (`brother.com.kh`) - Printers, label makers, and sewing machines.
282. **TP-Link Cambodia** (`[tp-link.com/kh](https://tp-link.com/kh)`) - Wi-Fi routers, mesh networks, and range extenders.
283. **Mercusys Cambodia** (`mercusys.com.kh`) - Budget Wi-Fi routers and network adapters.
284. **D-Link Cambodia** (`dlink.com.kh`) - Network switches and routers.
285. **Tenda Cambodia** (`tendacn.com.kh`) - Home Wi-Fi mesh systems and routers.
286. **MikroTik Cambodia** (`mikrotik.com.kh`) - Enterprise routers and network switches.
287. **Ubiquiti Cambodia** (`ui.com.kh`) - UniFi access points and security systems.
288. **Cisco Cambodia** (`cisco.com.kh`) - Enterprise networking gear and switches.
289. **Synology Cambodia** (`synology.com.kh`) - NAS backup servers for homes and businesses.
290. **QNAP Cambodia** (`qnap.com.kh`) - Network attached storage units.
291. **APC Cambodia** (`apc.com.kh`) - UPS battery backups and surge protectors.
292. **Keychron Cambodia** (`keychron.com.kh`) - Mechanical keyboards for Mac and Windows.
293. **Akko Cambodia** (`akkogear.com.kh`) - Custom mechanical keyboards and keycaps.
294. **Royal Kludge KH** (`rkgaming.com.kh`) - Budget wireless mechanical keyboards.
295. **Redragon Cambodia** (`redragon.com.kh`) - Gaming mice, keyboards, and mousepads.
296. **Fantech Cambodia** (`fantechworld.com.kh`) - Gaming headsets and mechanical keyboards.
297. **Dareu Cambodia** (`dareu.com.kh`) - Budget gaming mice and office keyboards.
298. **Glorious Cambodia** (`gloriousgaming.com.kh`) - Lightweight gaming mice and custom keyboards.
299. **Wacom Cambodia** (`wacom.com.kh`) - Drawing tablets for digital artists.
300. **XP-Pen Cambodia** (`xp-pen.com.kh`) - Pen display tablets and graphic monitors.

**Automotive, Bikes, Spare Parts & Rental**

301. **Nissan Cambodia** (`nissan.com.kh`) - Navara pickups, Terra SUVs, and sedans.
302. **Mitsubishi Cambodia** (`mitsubishi-motors.com.kh`) - Xpander, Triton, and Pajero Sport.
303. **Isuzu Cambodia** (`isuzu-cambodia.com`) - D-Max pickup trucks and commercial trucks.
304. **Suzuki Cambodia** (`suzuki.com.kh`) - Jimny, Swift, and Ertiga vehicles.
305. **Kia Cambodia** (`kia.com.kh`) - Carnival, Seltos, and Sportage SUVs.
306. **Land Rover KH** (`landrover.com.kh`) - Defender, Range Rover, and Discovery.
307. **Jaguar Cambodia** (`jaguar.com.kh`) - Luxury sports cars and SUVs.
308. **Porsche Cambodia** (`[porsche.com/cambodia](https://porsche.com/cambodia)`) - Cayenne, Macan, 911, and Taycan.
309. **Mercedes-Benz KH** (`mercedes-benz.com.kh`) - Luxury sedans, G-Wagon, and SUVs.
310. **Audi Cambodia** (`audi.com.kh`) - Luxury Q-series SUVs and e-tron EVs.
311. **Volvo Cambodia** (`[volvocars.com/kh](https://volvocars.com/kh)`) - XC90, XC60, and electric SUVs.
312. **Peugeot Cambodia** (`peugeot.com.kh`) - French SUVs and crossover vehicles.
313. **Subaru Cambodia** (`subaru.asia/kh`) - Forester and Outback AWD vehicles.
314. **GWM Cambodia** (`gwm.com.kh`) - Haval SUVs and Tank 300 off-roaders.
315. **Changan Cambodia** (`changan.com.kh`) - SUV models and sedans.
316. **DFSK Cambodia** (`dfsk.com.kh`) - Commercial vans and family crossovers.
317. **Geely Cambodia** (`geely.com.kh`) - Coolray and Tugella SUVs.
318. **GAC Motor KH** (`gac-motor.com.kh`) - GS8 SUVs and EMPOW sports sedans.
319. **Hongqi Cambodia** (`hongqi.com.kh`) - Luxury Chinese executive sedans and SUVs.
320. **Jetour Cambodia** (`jetour.com.kh`) - Dashing and X70 family SUVs.
321. **Chery Cambodia** (`chery.com.kh`) - Tiggo SUV series and EVs.
322. **Maxus Cambodia** (`maxus.com.kh`) - MPVs, commercial vans, and pickups.
323. **Foton Cambodia** (`foton.com.kh`) - Commercial trucks and cargo vans.
324. **Hino Cambodia** (`hino.com.kh`) - Heavy-duty commercial haulers.
325. **UD Trucks Cambodia** (`[udtrucks.com/cambodia](https://udtrucks.com/cambodia)`) - Cargo logistics trucks.
326. **Yamaha Cambodia** (`yamaha-motor.com.kh`) - Aerox, NMAX, and Exciter motorbikes.
327. **Suzuki Moto KH** (`suzuki.com.kh/motorcycle`) - Raider, Smash, and Burgman scooters.
328. **Vespa Cambodia** (`[vespa.com/kh](https://vespa.com/kh)`) - Italian luxury scooters.
329. **Piaggio Cambodia** (`[piaggio.com/kh](https://piaggio.com/kh)`) - European urban scooters.
330. **Aprilia Cambodia** (`[aprilia.com/kh](https://aprilia.com/kh)`) - Sports motorcycles and performance bikes.
331. **Moto Guzzi KH** (`[motoguzzi.com/kh](https://motoguzzi.com/kh)`) - Classic Italian motorbikes.
332. **Ducati Cambodia** (`[ducati.com/kh](https://ducati.com/kh)`) - Superbikes and Monster roadsters.
333. **BMW Motorrad KH** (`bmw-motorrad.com.kh`) - GS adventure motorcycles.
334. **KTM Cambodia** (`[ktm.com/kh](https://ktm.com/kh)`) - Off-road dirt bikes and Duke streetfighters.
335. **Husqvarna KH** (`[husqvarna-motorcycles.com/kh](https://husqvarna-motorcycles.com/kh)`) - Enduro and street motorcycles.
336. **Royal Enfield KH** (`[royalenfield.com/kh](https://royalenfield.com/kh)`) - Classic 350 and Interceptor 650.
337. **Triumph Cambodia** (`triumphmotorcycles.com.kh`) - Modern classic and adventure bikes.
338. **Harley-Davidson KH** (`[harley-davidson.com/kh](https://harley-davidson.com/kh)`) - Cruiser and touring motorcycles.
339. **Benelli Cambodia** (`benelli.com.kh`) - Budget sports and adventure bikes.
340. **CFMOTO Cambodia** (`cfmoto.com.kh`) - ATVs, UTVs, and street motorbikes.
341. **Bridgestone KH** (`bridgestone.com.kh`) - Passenger car and truck tires.
342. **Michelin Cambodia** (`michelin.com.kh`) - High-performance auto and motorcycle tires.
343. **Dunlop Cambodia** (`dunlop.com.kh`) - All-terrain and highway car tires.
344. **Yokohama Cambodia** (`yokohama.com.kh`) - Japanese tires for sedans and SUVs.
345. **Maxxis Cambodia** (`maxxis.com.kh`) - Off-road tires and scooter tires.
346. **Bosch Auto KH** (`bosch-pt.com.kh`) - Car batteries, spark plugs, and wipers.
347. **Motul Cambodia** (`[motul.com/kh](https://motul.com/kh)`) - Synthetic engine oils and lubricants.
348. **TotalEnergies KH** (`totalenergies.com.kh`) - Quartz engine lubricants and fuels.
349. **Liqui Moly KH** (`liqui-moly.com.kh`) - German motor oils and engine additives.
350. **Shell Cambodia** (`shell.com.kh`) - Helix motor oils and fuel stations.

**Real Estate, Condos, Boreys & Commercial**

351. **Borey Peng Huoth** (`penghuoth.com`) - Grand Star Platinum villas and gated estates.
352. **Borey Chip Mong** (`chipmongland.com`) - Modern townhouses and luxury villas.
353. **Borey Prince Town** (`princetown.com.kh`) - Suburban gated communities.
354. **Borey Orkide** (`orkidevilla.com.kh`) - Botanical villas and luxury residences.
355. **Borey Piphup Thmey** (`piphupthmey.com.kh`) - Affordable suburban housing developments.
356. **Borey Williams** (`boreywilliams.com`) - American-style suburban homes.
357. **Borey VIP** (`boreyvip.com.kh`) - Low-cost family townhouses.
358. **Borey Lorn City** (`lorncity.com.kh`) - Mixed residential developments in Sihanoukville.
359. **Borey Hi-Tech** (`boreyhitech.com.kh`) - Modern family residential homes.
360. **Borey New World** (`newworldborey.com.kh`) - Large-scale residential developments.
361. **Urbanland Asia** (`urbanland.asia`) - Chankiri Palm Creek and Embassy Residences.
362. **Creed Group KH** (`creed-group.com.kh`) - Bodaiju Residences near the airport.
363. **Lixin Group KH** (`lixingroup.com.kh`) - CEO Center and Sihanoukville developments.
364. **Shukaku Inc** (`shukaku-inc.com`) - Phnom Penh City Center (PPCC) mega-project.
365. **Overseas Cambodian Investment Corp** (`ocic.com.kh`) - Koh Pich (Diamond Island) & Chroy Changvar City.
366. **Canadia Group RE** (`canadiagroup.com.kh`) - Commercial towers and industrial parks.
367. **WorldBridge Land** (`worldbridgeland.com.kh`) - The Peak and The Bridge twin towers.
368. **Oxley WorldBridge** (`oxleyworldbridge.com.kh`) - Mixed-use commercial and residential developments.
369. **Hong Lai Huat** (`honglaihuat.com.sg/cambodia`) - D'Seaview Sihanoukville and Royal Platinum.
370. **Royal Group RE** (`royalgroup.com.kh`) - Northbridge Communities and commercial towers.
371. **Vattanac Properties** (`vattanaccapital.com`) - Vattanac Capital Tower Grade-A office spaces.
372. **GIA Tower** (`giatower.com.kh`) - Diamond Island Grade-A office space.
373. **Flatiron by Meridian** (`flatironmeridian.com`) - Apart-hotel and office spaces.
374. **Morgan Tower** (`morgantower.com.kh`) - Koh Pich eco-friendly office skyscraper.
375. **Sino-Plaza** (`sinoplaza.com.kh`) - Commercial complex and apartments.
376. **Prince Central Plaza** (`princecentralplaza.com`) - High-rise residential apartments.
377. **Prince Modern Plaza** (`princemodernplaza.com`) - Studio condos and office suites.
378. **Prince IT Tower** (`princeittower.com`) - Commercial office spaces.
379. **Agile Sky Residence** (`agileskyresidence.com.kh`) - Monivong Boulevard high-rise condos.
380. **Le Condé BKK1** (`leconde.com.kh`) - Smart home serviced apartments in BKK1.
381. **J-Tower Cambodia** (`jtower-cambodia.com`) - Japanese-developed high-rise condos.
382. **Time Square KH** (`timesquarekh.com`) - Affordable condo developments in BKK2/Toul Kork.
383. **La Vista One** (`lavistaone.com.kh`) - Chroy Changvar waterfront condos.
384. **Wealth Mansion** (`wealthmansion.com.kh`) - Riverside luxury serviced apartments.
385. **Peninsula Private Residences** (`thepeninsulacambodia.com`) - Chroy Changvar boutique condos.
386. **Bodaiju Residences** (`bodaiju.com.kh`) - Japanese-inspired airport condo community.
387. **Star Bay Sihanoukville** (`starbay-shv.com`) - Coastal resort apartments.
388. **Vue Aston** (`vueaston.com.kh`) - Norea Island waterfront condos.
389. **Kingland Condo** (`kinglandcondo.com.kh`) - Toul Kork residential apartments.
390. **De Castle Condo** (`decastle.com.kh`) - Pioneer condo brand in Phnom Penh.
391. **Rose Condo** (`rosecondo.com.kh`) - Tonle Bassac residential community.
392. **Bali Scenery** (`baliscenery.com.kh`) - Serviced apartments in Tonle Bassac.
393. **Embassy Central** (`embassycentral.com.kh`) - BKK1 luxury residential tower.
394. **Skylar by Meridian** (`skylarmeridian.com`) - Serviced condos managed by Ascot.
395. **City View Condo** (`cityviewcondo.com.kh`) - Toul Kork mid-range apartments.
396. **Gold Tower 42** (`goldtower42.com.kh`) - Monivong & Sihanouk Blvd landmark.
397. **Diamond Twin Tower** (`diamondtwintower.com.kh`) - Koh Pich office and residential space.
398. **Olympia City** (`olympiacity.com.kh`) - Mixed-use towers around Olympic Stadium.
399. **Sky Villa** (`skyvilla.com.kh`) - Ultra-luxury oversized apartments.
400. **The Gateway** (`thegateway.com.kh`) - Russian Boulevard office and residential towers.

**Fashion, Footwear & Jewelry**

401. **Charles & Keith KH** (`[charleskeith.com/kh](https://charleskeith.com/kh)`) - Fashion footwear and bags.
402. **Pedro KH** (`[pedroshoes.com/kh](https://pedroshoes.com/kh)`) - Men's and women's footwear and accessories.
403. **Mango KH** (`[mango.com/kh](https://mango.com/kh)`) - Spanish casual fashion line.
404. **Zando KH** (`zando.com.kh`) - Streetwear, sportswear, and fashion.
405. **Ten11 KH** (`ten11.com.kh`) - Urban clothing and casual wear.
406. **Routine Fashion** (`routine.com.kh`) - Minimalist everyday apparel.
407. **Levi's Cambodia** (`levis.com.kh`) - Original denim jeans and jackets.
408. **Giordano KH** (`giordano.com.kh`) - Casual polo shirts and chinos.
409. **Bossini KH** (`bossini.com.kh`) - Everyday family apparel.
410. **G2000 Cambodia** (`g2000.com.kh`) - Formal suits and business attire.
411. **Superdry KH** (`superdry.com.kh`) - Graphic tees and winter jackets.
412. **Calvin Klein KH** (`calvinklein.com.kh`) - Denim, underwear, and accessories.
413. **Tommy Hilfiger KH** (`tommy.com.kh`) - Classic American preppy wear.
414. **Lacoste Cambodia** (`lacoste.com.kh`) - Polo shirts and sports-chic wear.
415. **Polo Ralph Lauren KH** (`ralphlauren.asia/kh`) - Designer polo shirts and luxury apparel.
416. **Fred Perry KH** (`fredperry.com.kh`) - British heritage casual wear.
417. **Timberland KH** (`timberland.com.kh`) - Waterproof boots and outdoor wear.
418. **Clarks Cambodia** (`clarks.com.kh`) - Casual leather shoes and Wallabees.
419. **Havaianas KH** (`havaianas.com.kh`) - Brazilian flip-flops and sandals.
420. **Crocs Cambodia** (`crocs.com.kh`) - Comfortable clogs and slides.
421. **Skechers KH** (`skechers.com.kh`) - Walking shoes and athletic sneakers.
422. **Vans Cambodia** (`vans.com.kh`) - Skateboarding shoes and Canvas Old Skools.
423. **Converse KH** (`converse.com.kh`) - Chuck Taylor All Star sneakers.
424. **Puma KH** (`[puma.com/kh](https://puma.com/kh)`) - Running shoes and lifestyle sportswear.
425. **Under Armour KH** (`underarmour.com.kh`) - Gym compression gear and athletic shoes.
426. **New Balance KH** (`newbalance.com.kh`) - Lifestyle running sneakers.
427. **Asics Cambodia** (`asics.com.kh`) - Professional marathon running shoes.
428. **Descente KH** (`descente.com.kh`) - Premium Korean golf and sports apparel.
429. **Fila Cambodia** (`fila.com.kh`) - Chunky sneakers and retro sportswear.
430. **Champion KH** (`champion.com.kh`) - Reverse weave hoodies and sweatpants.
431. **Pandora Jewelry KH** (`pandora.net/kh`) - Sterling silver charms and bracelets.
432. **Swarovski KH** (`swarovski.com.kh`) - Crystal jewelry and accessories.
433. **Ly Hour Jewelry** (`lyhourjewelry.com`) - Local gold, platinum, and diamond jewelry.
434. **Heng Chhay Jewelry** (`hengchhayjewelry.com`) - Custom gold jewelry and gems.
435. **Kimseng Jewelry** (`kimsengjewelry.com`) - Traditional Cambodian gold items.
436. **Chivorn Jewelry** (`chivornjewelry.com`) - Diamond rings and wedding sets.
437. **Cambodia Gemological Institute** (`cgijewelry.com`) - Certified local gemstones.
438. **Samreth Silver** (`samrethsilver.com`) - Handcrafted Cambodian silverware.
439. **Amboh Handmade** (`ambohhandmade.com`) - Handwoven Krama shoes and espadrilles.
440. **Dorsu Cambodia** (`dorsu.org`) - Sustainable, ethically-made cotton basics.
441. **Krama HK** (`kramahk.com`) - Traditional Cambodian scarves and textiles.
442. **Lotus Silk KH** (`lotussilk.com.kh`) - Eco-friendly silk clothing and scarves.
443. **Nomi Network KH** (`nominetwork.org/kh`) - Handcrafted bags and lifestyle goods.
444. **Smateria KH** (`smateria.com`) - Bags made from recycled fishing nets and mesh.
445. **Susette Bags** (`susettebags.com`) - Leather bags and travel accessories.
446. **Samatoa Silk** (`samatoa.com`) - Lotus flower fabric and organic silk.
447. **Watthan Artisans** (`watthan.org`) - Handmade woodcrafts and silk apparel.
448. **Rajana Crafts** (`rajanacrafts.org`) - Traditional crafts, jewelry, and cards.
449. **Colors of Cambodia** (`colorsofcambodia.org`) - Local artisan gifts and art.
450. **Kaya Silk** (`kayasilk.com`) - Artisanal silk scarves and apparel.

**Beauty, Cosmetics & Personal Care**

451. **The Body Shop KH** (`thebodyshop.com.kh`) - Cruelty-free skincare and body butter.
452. **L'Occitane KH** (`loccitane.com.kh`) - French shea butter hand creams and body lotions.
453. **Kiehl's Cambodia** (`kiehls.com.kh`) - Calendula toner and facial creams.
454. **Clinique KH** (`clinique.com.kh`) - Dermatologist-tested moisturizers and foundation.
455. **Estée Lauder KH** (`esteelauder.com.kh`) - Advanced Night Repair serums.
456. **MAC Cosmetics KH** (`maccosmetics.com.kh`) - Professional lipsticks and makeup.
457. **Shiseido KH** (`shiseido.com.kh`) - Japanese skincare and sunscreens.
458. **SK-II Cambodia** (`sk-ii.com.kh`) - Facial Treatment Essence and pitera products.
459. **Sulwhasoo KH** (`sulwhasoo.com.kh`) - Korean ginseng skincare serums.
460. **HERA Cosmetics KH** (`hera.com.kh`) - Korean luxury makeup cushions.
461. **3CE Cambodia** (`[stylenanda.com/3ce](https://stylenanda.com/3ce)`) - Trendy lip tints and eye palettes.
462. **Etude House KH** (`etude.com.kh`) - Budget Korean makeup and lip stains.
463. **Cosrx Cambodia** (`cosrx.com.kh`) - Snail mucin essence and acne patches.
464. **Some By Mi KH** (`somebymi.com.kh`) - AHA BHA PHA 30-day miracle toners.
465. **Beauty of Joseon KH** (`beautyofjoseon.com.kh`) - Relief Sun rice sunscreens.
466. **Anua Skincare KH** (`anua.com.kh`) - Heartleaf 77% soothing toners.
467. **Round Lab KH** (`roundlab.com.kh`) - Dokdo cleansing foams and sunscreens.
468. **Torriden KH** (`torriden.com.kh`) - Dive-In low molecular hyaluronic acid serums.
469. **Skin1004 KH** (`skin1004.com.kh`) - Madagascar Centella ampoules.
470. **Klairs Cambodia** (`dearklairs.com.kh`) - Supple preparation facial toners.
471. **By Wishtrend KH** (`bywishtrend.com.kh`) - Vitamin C serums and exfoliants.
472. **Isntree KH** (`isntree.com.kh`) - Hyaluronic acid watery sun gels.
473. **Pyunkang Yul KH** (`pyunkangyul.com.kh`) - Essence toners for sensitive skin.
474. **La Roche-Posay KH** (`laroche-posay.com.kh`) - Effaclar acne treatments and sunscreens.
475. **Avene Cambodia** (`avene.com.kh`) - Thermal spring water sprays and soothing creams.
476. **Bioderma KH** (`bioderma.com.kh`) - Sensibio H2O micellar water.
477. **Eucerin Cambodia** (`eucerin.com.kh`) - Spotless Brightening serums and sun lotions.
478. **Cetaphil KH** (`cetaphil.com.kh`) - Gentle skin cleansers and moisturizers.
479. **Neutrogena KH** (`neutrogena.com.kh`) - Hydro Boost water gels and sunscreens.
480. **Nivea Cambodia** (`nivea.com.kh`) - Body lotions and lip balms.
481. **Vaseline KH** (`vaseline.com.kh`) - Healthy Bright body lotions.
482. **Dove Cambodia** (`dove.com.kh`) - Hair care shampoos and body washes.
483. **Pantene KH** (`pantene.com.kh`) - Hair repair shampoos and conditioners.
484. **Head & Shoulders KH** (`headandshoulders.com.kh`) - Anti-dandruff hair shampoos.
485. **L'Oreal Paris KH** (`lorealparis.com.kh`) - Elseve hair serums and foundations.
486. **Tresemme KH** (`tresemme.com.kh`) - Keratin smooth salon shampoos.
487. **Sunsilk KH** (`sunsilk.com.kh`) - Smooth and manageable hair care.
488. **Rejoice KH** (`rejoice.com.kh`) - 3-in-1 smooth shampoos.
489. **Darlie Toothpaste KH** (`darlie.com.kh`) - All Shiny White toothpastes.
490. **Colgate Cambodia** (`colgate.com.kh`) - Total protection toothpastes and brushes.
491. **Sensodyne KH** (`sensodyne.com.kh`) - Toothpaste for sensitive teeth.
492. **Listerine KH** (`listerine.com.kh`) - Antiseptic mouthwash.
493. **Rexona Cambodia** (`rexona.com.kh`) - Deodorant sprays and roll-ons.
494. **Nivea Men KH** (`niveamen.com.kh`) - Men's face washes and deodorants.
495. **Gillette Cambodia** (`gillette.com.kh`) - Mach3 razors and shaving gels.
496. **Schick Cambodia** (`schick.com.kh`) - Hydro razors and shaving accessories.
497. **Dettol Cambodia** (`dettol.com.kh`) - Antiseptic liquids and antibacterial soaps.
498. **Lifebuoy KH** (`lifebuoy.com.kh`) - Total 10 hygiene hand washes.
499. **Kleenex Cambodia** (`kleenex.com.kh`) - Facial tissues and wet wipes.
500. **Laurier Cambodia** (`laurier.com.kh`) - Sanitary napkins and feminine care.

**Home & Kitchen Appliances, Furniture & Lighting**

501. **LG Cambodia** (`[lg.com/kh](https://lg.com/kh)`) - OLED TVs, AI InstaView fridges, and washers.
502. **Panasonic KH** (`[panasonic.com/kh](https://panasonic.com/kh)`) - Inverter air conditioners and microwave ovens.
503. **Hitachi KH** (`hitachi.com.kh`) - Multi-door refrigerators and vacuum cleaners.
504. **Toshiba Cambodia** (`[toshiba-lifestyle.com/kh](https://toshiba-lifestyle.com/kh)`) - Induction rice cookers and washers.
505. **Sharp Cambodia** (`sharp.com.kh`) - Plasmacluster air purifiers and fridges.
506. **Mitsubishi Electric KH** (`mitsubishielectric.com.kh`) - Heavy duty air conditioners.
507. **Daikin Cambodia** (`daikin.com.kh`) - Inverter split air conditioners.
508. **Gree Cambodia** (`gree.com.kh`) - Commercial and residential air conditioners.
509. **Media Aircon KH** (`[midea.com/kh/air-conditioners](https://midea.com/kh/air-conditioners)`) - Budget split unit air conditioners.
510. **TCL Cambodia** (`[tcl.com/kh](https://tcl.com/kh)`) - Google Smart TVs and home electronics.
511. **Hisense Cambodia** (`hisense.com.kh`) - ULED TVs and chest freezers.
512. **Philips Appliances KH** (`philips.com.kh/c-m-ho`) - Air fryers and garment steamers.
513. **Tefal Cambodia** (`tefal.com.kh`) - Non-stick pans and steam irons.
514. **KitchenAid KH** (`kitchenaid.com.kh`) - Stand mixers and blender accessories.
515. **DeLonghi KH** (`delonghi.com.kh`) - Espresso coffee machines and electric kettles.
516. **Breville Cambodia** (`breville.com.kh`) - Barista Touch espresso machines.
517. **Nescafe Dolce Gusto KH** (`dolce-gusto.com.kh`) - Capsule coffee makers.
518. **Nespresso Cambodia** (`nespresso.com.kh`) - Original and Vertuo coffee capsules.
519. **Electrolux Kitchen KH** (`electrolux.com.kh/kitchen`) - Built-in ovens and induction hobs.
520. **Bosch Home KH** (`bosch-home.com.kh`) - Dishwashers and front-load washers.
521. **Kärcher Cambodia** (`[kaercher.com/kh](https://kaercher.com/kh)`) - High-pressure washers and steam cleaners.
522. **Roborock Cambodia** (`roborock.com.kh`) - Robot vacuum cleaners and mops.
523. **Ecovacs Cambodia** (`ecovacs.com.kh`) - Deebot robotic vacuum cleaners.
524. **Dreame Cambodia** (`dreame.com.kh`) - Wet and dry cordless stick vacuums.
525. **IKEA Shipping KH** (`ikeashipping.com.kh`) - Swedish flat-pack furniture delivery.
526. **Kano Furniture** (`kanofurniture.com.kh`) - Modern ergonomic office desks and chairs.
527. **Merryfair Cambodia** (`merryfair.com.kh`) - Ergonomic mesh office chairs.
528. **Steelcase Cambodia** (`steelcase.com.kh`) - High-end workstation furniture.
529. **Herman Miller KH** (`hermanmiller.com.kh`) - Aeron ergonomic task chairs.
530. **King Koil Mattress KH** (`kingkoil.com.kh`) - Hotel-grade pocket spring mattresses.
531. **Dunlopillo KH** (`dunlopillo.com.kh`) - Natural latex mattresses and pillows.
532. **Slumberland KH** (`slumberland.com.kh`) - Pocket spring mattresses.
533. **Serta Mattress KH** (`serta.com.kh`) - Orthopedic beds and plush mattresses.
534. **Sealy Cambodia** (`sealy.com.kh`) - Posturepedic hotel mattresses.
535. **Lotus Bedding KH** (`lotusbedding.com.kh`) - Bed sheets, duvets, and pillows.
536. **Akemi Cambodia** (`akemi.com.kh`) - Cotton bed sheets and bath towels.
537. **Cannon Bedding KH** (`cannon.com.kh`) - Luxury bed linen sets.
538. **Muji Cambodia** (`[muji.com/kh](https://muji.com/kh)`) - Minimalist Japanese furniture and organizers.
539. **Miniso Cambodia** (`miniso.com.kh`) - Household storage boxes and decor.
540. **Daiso Japan KH** (`daiso.com.kh`) - Japanese household utility items.
541. **Kompiba KH** (`kompiba.com.kh`) - Kitchen cabinets and custom wardrobes.
542. **Lixil Cambodia** (`lixil.com.kh`) - Sanitaryware, tiles, and aluminum doors.
543. **Inax Cambodia** (`inax.com.kh`) - Japanese bathroom toilets and faucets.
544. **Toto Cambodia** (`toto.com.kh`) - Washlet smart toilets and shower systems.
545. **American Standard KH** (`americanstandard.com.kh`) - Bathroom sinks and faucets.
546. **Kohler Cambodia** (`kohler.com.kh`) - Designer luxury bathroom fixtures.
547. **Grohe Cambodia** (`grohe.com.kh`) - German thermostatic shower systems.
548. **Cotto Cambodia** (`cotto.com.kh`) - Thai ceramic tiles and bathroom fittings.
549. **SCG Building Materials KH** (`scg.com.kh`) - Roofing tiles, cement, and boards.
550. **Schneider Electric KH** (`[se.com/kh](https://se.com/kh)`) - Circuit breakers and light switches.

**Supermarkets, Organic Stores & Gourmet Food**

551. **AEON MaxValu** (`aeoncambodia.com`) - Neighborhood mini-supermarkets.
552. **Circle K Cambodia** (`circlek.com.kh`) - 24-hour convenience store chain.
553. **7-Eleven Cambodia** (`7eleven.com.kh`) - Snacks, beverages, and quick meals.
554. **Relay Cambodia** (`relay.com.kh`) - Airport convenience and travel snacks.
555. **Panda Mart KH** (`foodpanda.com.kh/darkstore`) - 20-minute grocery delivery.
556. **Phsar Small** (`phsarsmall.com`) - Daily fresh market items delivered.
557. **Cambodia Supermarket** (`cambodiasupermarket.com`) - Packaged Western food items.
558. **Thai Huot Market** (`thaihuot.com`) - Imported European cheeses, wines, and meats.
559. **Interfood Cambodia** (`interfood.com.kh`) - Bulk food ingredients for restaurants.
560. **Les Vergers du Mékong** (`levergersdumekong.com`) - Le Fruit juices and Foliet jams.
561. **La Plantations Kampot** (`kampotpepper.com`) - Certified organic Kampot pepper and spices.
562. **Sothy's Pepper Farm** (`sothyspepperfarm.com`) - Red, black, and white Kampot pepper.
563. **Confinat Kampot** (`confinat.com`) - Gourmet artisan condiments and peppers.
564. **IBIS Rice** (`ibisrice.com`) - Organic wildlife-friendly jasmine rice.
565. **Angkor Harvest** (`angkorharvest.com`) - Dried mangoes and local fruit snacks.
566. **Kirirom Food Production** (`kirirom.com.kh`) - Dried tropical fruit products.
567. **Mondulkiri Coffee** (`mondulkiricoffee.com.kh`) - Local roasted robusta and arabica beans.
568. **Ratanakiri Coffee** (`ratanakiricoffee.com`) - Highland shade-grown coffee beans.
569. **Three Corner Coffee** (`threecornercoffee.com`) - Specialty espresso roasters.
570. **Feel Good Coffee** (`feelgoodcoffee.com.kh`) - Social enterprise coffee roasters.
571. **Tube Coffee** (`tubecoffee.com.kh`) - Local drive-thru coffee shop chain.
572. **Brown Coffee** (`browncoffee.com.kh`) - Local specialty coffee and bakery.
573. **Nom Tmey Bakery** (`nomtmey.com.kh`) - Artisan sourdough breads and pastries.
574. **Eric Kayser KH** (`erickayser.com.kh`) - French artisan croissants and baguettes.
575. **Tous Les Jours KH** (`touslesjours.com.kh`) - French-Asian bakery and birthday cakes.
576. **BreadTalk Cambodia** (`breadtalk.com.kh`) - Floss buns and bakery goods.
577. **Amo Bakery** (`amobakery.com.kh`) - Local fresh cakes and celebration pastries.
578. **Yi Sang Restaurant** (`yisang.com.kh`) - Cantonese dim sum and roast meats.
579. **Malu Cambodia** (`malu.com.kh`) - Japanese matcha and dessert shop.
580. **Kbach Ice Cream** (`kbach.com.kh`) - Local coconut and tropical fruit gelatos.
581. **Sons of Wine** (`sonsofwine.com.kh`) - Natural organic wine importer.
582. **Celliers d'Asie KH** (`celliersdasie.com`) - Fine French wine distributor.
583. **Warehouse Wine KH** (`thewarehouse.com.kh`) - Imported spirits and craft beers.
584. **Seekers Spirits** (`seekersspirits.com`) - Mekong dry gin distillery.
585. **Mao Spirits** (`maospirits.com`) - Craft rum distilled from Cambodian sugarcane.
586. **Rivoem Craft Beer** (`rivoem.com`) - Local microbrewery craft beer.
587. **Kingdom Breweries** (`kingdombreweries.com`) - Craft pilsners and IPAs.
588. **Ganzberg Beer** (`ganzberg.com.kh`) - German-style lager beer.
589. **Hanuman Beer** (`hanumanbeer.com.kh`) - Premium Cambodian lager.
590. **Cambodia Beer** (`khmerbrewery.com`) - Flagship lager from Khmer Beverages.
591. **Angkor Beer** (`angkorbeer.com.kh`) - Classic national lager.
592. **Vattanac Brewery** (`vattanacbrewery.com`) - Vattanac and Krud beer lines.
593. **Kulara Water** (`eaukulen.com`) - Eau Kulen natural mineral water.
594. **Vital Premium Water** (`vital.com.kh`) - Purified bottled drinking water.
595. **Joy Water** (`joywater.com.kh`) - Gallon office water delivery.
596. **Pura Water** (`purawater.com.kh`) - Home and office bottled water.
597. **Coca-Cola Cambodia** (`cbcl.com.kh`) - Bottled soft drinks and Monster Energy.
598. **Pepsi Cambodia** (`pepsicambodia.com`) - Soft drinks and Sting energy drinks.
599. **Carabao Cambodia** (`carabao.com.kh`) - Energy drinks and sports beverages.
600. **Red Bull Cambodia** (`redbull.com.kh`) - Krating Daeng energy drinks.

**Logistics, Delivery & Express Freight**

601. **DHL Express KH** (`[dhl.com/kh-en](https://dhl.com/kh-en)`) - Air express document and parcel shipping.
602. **FedEx Cambodia** (`[fedex.com/kh](https://fedex.com/kh)`) - International express courier freight.
603. **UPS Cambodia** (`[ups.com/kh](https://ups.com/kh)`) - Global package shipping and tracking.
604. **SF Express Cambodia** (`[sf-express.com/kh](https://sf-express.com/kh)`) - Cross-border China-Cambodia express.
605. **Kerry Worldbridge** (`kerryworldbridge.com`) - Customs clearance and warehousing.
606. **LINEEX Cambodia** (`lineex.com.kh`) - Cross-border e-commerce logistics.
607. **Speedmark Logistics** (`speedmark.com.kh`) - Air and sea freight forwarding.
608. **DB Schenker KH** (`[dbschenker.com/kh](https://dbschenker.com/kh)`) - Global supply chain solutions.
609. **Kuehne+Nagel KH** (`[kuehne-nagel.com/kh](https://kuehne-nagel.com/kh)`) - Container shipping logistics.
610. **Bolloré Logistics KH** (`[bollore-logistics.com/kh](https://bollore-logistics.com/kh)`) - Industrial project cargo shipping.
611. **Rhenus Logistics KH** (`[rhenus.com/kh](https://rhenus.com/kh)`) - Freight forwarding and warehousing.
612. **Agility Logistics KH** (`[agility.com/kh](https://agility.com/kh)`) - Third-party logistics (3PL).
613. **Yunda Express KH** (`yundaexpress.com.kh`) - China-to-Cambodia courier.
614. **申通 Express KH** (`sto.com.kh`) - Express parcel tracking service.
615. **Best Express KH** (`best-inc.com.kh`) - Nationwide door-to-door express.
616. **CAPITAL Express** (`capitalexpress.com.kh`) - Bus parcel delivery across provinces.
617. **Sorya Express** (`soryaexpress.com.kh`) - Inter-province bus freight.
618. **Mey Hong Transport** (`meyhong.com.kh`) - Express van cargo shipping.
619. **Vet Express Cargo** (`[vireakbuntham.com/cargo](https://vireakbuntham.com/cargo)`) - Same-day provincial parcel shipping.
620. **Cambodia Post Logistics** (`cambodiapost.post`) - EMS international postal shipping.
621. **Grab Express KH** (`[grab.com/kh/express](https://grab.com/kh/express)`) - Instant motorbike courier in cities.
622. **Foodpanda Delivery KH** (`foodpanda.com.kh`) - On-demand rider courier service.
623. **NHAM24 Express** (`[nham24.com/express](https://nham24.com/express)`) - Citywide document and parcel pick-up.
624. **WOWNOW Express** (`wownow.com.kh/express`) - Local e-commerce delivery riders.
625. **L192 Express** (`[l192.com/delivery](https://l192.com/delivery)`) - Internal fashion logistics fleet.
626. **MoveByTukTuk** (`movebytuktuk.com`) - Hauling and small move transport.
627. **Lalamove KH** (`[lalamove.com/kh](https://lalamove.com/kh)`) - On-demand van and truck freight.
628. **TADA Deliver KH** (`tada.global/kh`) - Zero-commission delivery services.
629. **PassApp Delivery** (`passapp.com.kh`) - Rickshaw small parcel dispatch.
630. **Phnom Penh Moving** (`phnompenhmoving.com`) - House and office moving services.
631. **Siem Reap Movers** (`siemreapmovers.com`) - Residential relocation services.
632. **Angkor Relocation** (`angkorrelocation.com`) - International expat moving services.
633. **AVS Relocation** (`avs-relocation.com`) - Pet transport and house moves.
634. **Crown Relocations KH** (`[crownrelo.com/kh](https://crownrelo.com/kh)`) - Corporate expat relocation.
635. **Santa Fe Relocation KH** (`[santaferelo.com/kh](https://santaferelo.com/kh)`) - Global mobility and visa moves.
636. **Royal Cargo KH** (`royalcargo.com.kh`) - Heavy machinery transport.
637. **WorldBridge Freight** (`worldbridge.com.kh`) - Port container terminal logistics.
638. **Sihanoukville Port** (`pas.gov.kh`) - Autonomous deep-sea port services.
639. **Phnom Penh Port** (`ppap.com.kh`) - River container port terminal.
640. **Bavet Dry Port** (`bavetdryport.com`) - Border customs clearance hub.
641. **Poipet Dry Port** (`poipetdryport.com`) - Thai border transit terminal.
642. **Phnom Penh SEZ** (`ppsez.com`) - Special Economic Zone logistics.
643. **Manhattan SEZ** (`msezkohkong.com`) - Industrial park manufacturing hub.
644. **Sihanoukville SEZ** (`ssez.com`) - Coastal industrial trade zone.
645. **Dragon Express KH** (`dragonexpress.com.kh`) - Local door-to-door courier.
646. **Fast Express KH** (`fastexpress.com.kh`) - Provincial logistics network.
647. **LogiKH** (`logikh.com`) - E-commerce fulfillment software.
648. **Ship2Khmer** (`ship2khmer.com`) - US freight forwarding to Cambodia.
649. **BuyUS2Khmer** (`buyus2khmer.com`) - US address forwarding service.
650. **Taobao Cambodia Logistics** (`taobaocambodia.com`) - Freight consolidation from China.

**Books, Travel, Ticketing & Business Services**

651. **Agoda Cambodia** (`[agoda.com/country/cambodia.html](https://agoda.com/country/cambodia.html)`) - Hotel reservations in Siem Reap and Phnom Penh.
652. **Booking.com KH** (`[booking.com/country/kh.html](https://booking.com/country/kh.html)`) - Guesthouse and resort bookings.
653. **Trip.com Cambodia** (`[trip.com/kh](https://trip.com/kh)`) - Flight tickets and hotel deals.
654. **AirAsia Cambodia** (`[airasia.com/kh](https://airasia.com/kh)`) - Domestic and regional budget flights.
655. **Cambodia Angkor Air** (`cambodiaangkorair.com`) - National flag carrier airline.
656. **Lanmei Airlines** (`lanmeiairlines.com`) - Regional budget flights.
657. **Sky Angkor Airlines** (`skyangkorair.com`) - Direct charter and scheduled flights.
658. **Air Cambodia** (`aircambodia.com.kh`) - Flight booking aggregator.
659. **Phnom Penh Airport** (`pnh.cambodia-airports.aero`) - Flight arrival and departure schedules.
660. **Siem Reap Airport** (`sai.cambodia-airports.aero`) - Angkor International airport portal.
661. **Sihanoukville Airport** (`kos.cambodia-airports.aero`) - Coastal flight schedules.
662. **Sokha Hotels** (`sokhahotels.com.kh`) - Luxury beach resorts and hotels.
663. **Sofitel Phnom Penh** (`sofitel-phnompenh-phokeethra.com`) - 5-star French luxury hotel.
664. **Rosewood Phnom Penh** (`[rosewoodhotels.com/phnom-penh](https://rosewoodhotels.com/phnom-penh)`) - Luxury high-rise hotel.
665. **Hyatt Regency PP** (`[hyatt.com/hyatt-regency-phnom-penh](https://hyatt.com/hyatt-regency-phnom-penh)`) - BKK area luxury hotel.
666. **Raffles Le Royal** (`[raffles.com/phnom-penh](https://raffles.com/phnom-penh)`) - Historic luxury hotel in Phnom Penh.
667. **Raffles Grand d'Angkor** (`[raffles.com/siem-reap](https://raffles.com/siem-reap)`) - Historic luxury hotel in Siem Reap.
668. **Courtyard by Marriott** (`[marriott.com/pnhcy](https://marriott.com/pnhcy)`) - Business travel hotel in Phnom Penh.
669. **Fairfield by Marriott** (`[marriott.com/pnhfb](https://marriott.com/pnhfb)`) - Hotel near Phnom Penh center.
670. **Sun & Moon Hotel** (`sunandmoonhotel.com`) - Urban lifestyle hotels.
671. **Baitong Hotel** (`baitonghotel.asia`) - Eco-design resort hotel in BKK1.
672. **FCC Angkor** (`[avatani.com/fcc-angkor](https://avatani.com/fcc-angkor)`) - Riverside hotel in Siem Reap.
673. **Shinta Mani Hotels** (`shintamani.com`) - Luxury boutique stays in Siem Reap.
674. **Song Saa Private Island** (`songsaa-privateisland.com`) - Ultra-luxury island resort.
675. **Six Senses Krabey Island** (`[sixsenses.com/krabey-island](https://sixsenses.com/krabey-island)`) - Eco-luxury coastal island resort.
676. **Koh Russey Resort** (`kohrusseyresort.com`) - Beach villas on Bamboo Island.
677. **Royal Sands Koh Rong** (`theroyalsands-kohrong.com`) - 5-star resort on Koh Rong.
678. **Lazy Beach Koh Rong Samloem** (`lazybeachcambodia.com`) - Bungalow island stay.
679. **Sol Beach Resort** (`solbeachresort.com`) - Koh Rong Samloem beachfront stays.
680. **Saracen Bay Resort** (`saracenbayresort.com`) - Island beach bungalow bookings.
681. **Angkor Ticket Portal** (`angkorenterprise.gov.kh`) - Official Angkor Wat pass booking.
682. **National Museum KH** (`cambodiamuseum.info`) - Historical museum entrance and exhibits.
683. **Phnom Penh Post** (`phnompenhpost.com`) - Daily English-language news publication.
684. **Khmer Times** (`khmertimeskh.com`) - Local daily business and national news.
685. **Fresh News Asia** (`freshnewsasia.com`) - Khmer-language breaking news portal.
686. **ThmeyThmey** (`thmeythmey.com`) - Digital news and current affairs portal.
687. **Sabay News** (`news.sabay.com.kh`) - Youth entertainment and lifestyle news.
688. **B2B Cambodia** (`b2b-cambodia.com`) - Business directory and investment guides.
689. **EuroCham Cambodia** (`eurocham-cambodia.org`) - European business chamber directory.
690. **AmCham Cambodia** (`amchamcambodia.old-site.com`) - American Chamber of Commerce.
691. **BritCham Cambodia** (`britchamcambodia.org`) - British business network directory.
692. **IBC Cambodia Network** (`ibccambodia.com`) - International Business Chamber.
693. **Yellow Pages Cambodia** (`yp.com.kh`) - Official business phone directory.
694. **Ministry of Commerce KH** (`moc.gov.kh`) - Business registration portal (Business Registration Automated System).
695. **General Dept of Taxation** (`gdt.gov.kh`) - Tax filing and e-services portal.
696. **National Bank of Cambodia** (`nbc.gov.kh`) - Exchange rates and financial regulations.
697. **Phnom Penh SEZ Directory** (`[ppsez.com/directory](https://ppsez.com/directory)`) - Factory and industrial listings.
698. **CDC Investment Portal** (`cambodiainvestment.gov.kh`) - Council for Development of Cambodia.
699. **MPWT Portal** (`mpwt.gov.kh`) - Driving license and vehicle registration online.
700. **e-Visa Cambodia** (`evisa.gov.kh`) - Official tourist e-visa application portal.
"""

# Helper to clean domain/url
def clean_domain_and_url(raw_dom):
    # e.g. `[mi.com/kh](https://mi.com/kh)` -> domain: mi.com/kh, url: https://mi.com/kh
    # e.g. `gadgetstorekh.com` -> domain: gadgetstorekh.com, url: https://gadgetstorekh.com
    m = re.search(r'\[(.*?)\]\((.*?)\)', raw_dom)
    if m:
        disp_dom = m.group(1).strip('`')
        url = m.group(2).strip()
        return disp_dom, url
    clean = raw_dom.strip('`').strip()
    return clean, ("https://" + clean)

# Category mapping
cat_headers = {
    "Electronics, Gadgets & Audio": ("PHONES", "🎧 Audio & Gadgets"),
    "Computer Systems, Gaming & IT Equipment": ("COMPUTERS", "💻 Gaming & PC Systems"),
    "Automotive, Bikes, Spare Parts & Rental": ("CARS", "🚗 Auto, Moto & Parts"),
    "Real Estate, Condos, Boreys & Commercial": ("REAL_ESTATE", "🏢 Boreys & Condos"),
    "Fashion, Footwear & Jewelry": ("FASHION", "💎 Fashion & Jewelry"),
    "Beauty, Cosmetics & Personal Care": ("BEAUTY", "🌸 Beauty & Personal Care"),
    "Home & Kitchen Appliances, Furniture & Lighting": ("FURNITURE", "🛋️ Home & Kitchen Appliances"),
    "Supermarkets, Organic Stores & Gourmet Food": ("GROCERIES", "🥩 Supermarkets & Gourmet"),
    "Logistics, Delivery & Express Freight": ("SERVICES", "🚚 Logistics & Freight"),
    "Books, Travel, Ticketing & Business Services": ("SERVICES", "✈️ Travel & Business Portals")
}

parsed_500 = []
current_header = None
current_cat = "GENERAL"
current_badge_prefix = "🛒"

lines = raw_user_text.splitlines()
for line in lines:
    line = line.strip()
    if not line:
        continue
    # Check header
    if line.startswith("**") and line.endswith("**"):
        h_text = line.strip("*").strip()
        for k, v in cat_headers.items():
            if k.lower() in h_text.lower():
                current_header = k
                current_cat = v[0]
                current_badge_prefix = v[1]
                break
        continue

    # Match: 201. **Name** (`domain`) - Description
    m = re.match(r'^(\d+)\.\s+\*\*(.*?)\*\*\s+\((.*?)\)\s+-\s+(.*)$', line)
    if m:
        num = int(m.group(1))
        name = m.group(2).strip()
        raw_dom = m.group(3).strip()
        desc = m.group(4).strip()
        disp_dom, home_url = clean_domain_and_url(raw_dom)
        
        # ID generation
        clean_id = re.sub(r'[^a-zA-Z0-9]', '_', name.lower()).strip('_')
        # Ensure unique id
        item_id = f"{clean_id}_{num}"

        badge = f"{current_badge_prefix.split()[0]} {name.split()[0]}"
        name_kh = f"{name}"
        desc_kh = f"{desc}"
        search_url = f"{home_url}/search?q={{q}}" if not home_url.endswith('/') else f"{home_url}search?q={{q}}"

        parsed_500.append({
            "num": num,
            "id": item_id,
            "name": name,
            "domain": disp_dom,
            "category": current_cat,
            "badge": badge,
            "nameKh": name_kh,
            "descKh": desc_kh,
            "searchUrl": search_url,
            "homeUrl": home_url,
            "defaultCategory": current_cat
        })

print(f"Total parsed items from 201 to 700: {len(parsed_500)}")
if parsed_500:
    print(f"First item: {parsed_500[0]}")
    print(f"Last item: {parsed_500[-1]}")

with open("scratch/parsed_500.json", "w", encoding="utf-8") as f:
    json.dump(parsed_500, f, ensure_ascii=False, indent=2)

print("Saved to scratch/parsed_500.json")
