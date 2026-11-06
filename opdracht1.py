# intro van de game
print("====Welcome to the RPG Game!====")
print("In dit spel kun je items verzamelen, vechten tegen monsters en je karakter verbeteren.")
print("Laten we beginnen met het maken van je karakter!")

# main character


def create_character():
    print("=== Karakter Creatie ===")
    name = input("Voer de naam van je karakter in: ").strip()

    while not name:
        print("Ongeldige invoer. De naam mag niet leeg zijn.")
        name = input("Voer de naam van je karakter in: ").strip()

    valid_classes = {
        "1": {"naam": "Warrior", "aanvalskracht": 15, "speed": 10, "verdediging": 20, "starter_wapen": "Houten Zwaard", "unieke_aanval": "Schildklap"},
        "2": {"naam": "Mage", "aanvalskracht": 20, "speed": 15, "verdediging": 10, "starter_wapen": "Oude Staf", "unieke_aanval": "Vuurbal"},
        "3": {"naam": "Rogue", "aanvalskracht": 25, "speed": 20, "verdediging": 5, "starter_wapen": "Roestige Dolk", "unieke_aanval": "Schaduwsteek"}
    }

    print("\nKies een klasse voor je karakter:")
    print("[1] Warrior (Lage aanval, hoge verdediging)")
    print("[2] Mage (Hoge magie, lage verdediging)")
    print("[3] Rogue (Hoge aanval, hoge snelheid)")

    while True:
        keuze = input("\nJouw keuze (1, 2 of 3): ").strip()
        if keuze in valid_classes:
            gekozen_klasse = valid_classes[keuze]
            break
        else:
            print("❌ Ongeldige keuze. Kies 1, 2 of 3.")

    karakter = {
        "naam": name,
        "klasse": gekozen_klasse["naam"],

        # Level & XP tracker
        "level": 1,
        "xp": 0,
        "xp_nodig": 100,  # XP nodig om level 2 te bereiken

        # Stats
        "aanvalskracht": gekozen_klasse["aanvalskracht"],
        "speed": gekozen_klasse["speed"],
        "verdediging": gekozen_klasse["verdediging"],

        # Equipment
        "equipment": {
            "wapen": gekozen_klasse["starter_wapen"],
            "armor": "Stoffen Kleding",
            "skills": ["Basis Aanval", gekozen_klasse["unieke_aanval"]],
            "potions": {"Health Potion": 2}
        }
    }

    print("\n🎉 Karakter succesvol aangemaakt!")
    return karakter


def geef_xp(karakter, hoeveelheid_xp):
    """Voegt XP toe aan het karakter en controleert voor een level-up."""
    print(f"\n✨ Je hebt {hoeveelheid_xp} XP verdiend!")
    karakter["xp"] += hoeveelheid_xp

    # Zolang de speler genoeg XP heeft voor een level-up (kan meerdere keren achter elkaar als je heel veel XP krijgt)
    while karakter["xp"] >= karakter["xp_nodig"]:
        # Trek de gebruikte XP af voor het huidige level
        karakter["xp"] -= karakter["xp_nodig"]
        karakter["level"] += 1

        # Verhoog de benodigde XP voor het volgende level met bijv. 50%
        karakter["xp_nodig"] = int(karakter["xp_nodig"] * 1.5)

        # Verhoog de basis stats bij een level up!
        karakter["aanvalskracht"] += 3
        karakter["verdediging"] += 2
        karakter["speed"] += 1

        print("=" * 40)
        print(f"🌟 LEVEL UP! Je bent nu Level {karakter['level']}!")
        print("Je stats zijn verhoogd: +3 Aanval, +2 Verdediging, +1 Snelheid!")
        print("=" * 40)


def toon_karakter_stats(karakter):
    print("\n" + "=" * 40)
    print(
        f"📊 STATS VAN: {karakter['naam'].upper()} (Lvl {karakter['level']} {karakter['klasse']})")
    print("=" * 40)
    print(f"• XP           : {karakter['xp']} / {karakter['xp_nodig']} XP")
    print(f"• Aanvalskracht: {karakter['aanvalskracht']}")
    print(f"• Snelheid     : {karakter['speed']}")
    print(f"• Verdediging  : {karakter['verdediging']}")
    print("-" * 40)
    print(f"• Skills       : {', '.join(karakter['equipment']['skills'])}")
    print("=" * 40)


# --- TEST HET LEVEL-SYSTEEM EN DE DUNGEON ---
mijn_speler = create_character()

while True:
    actie = input(
        "\nWat wil je doen? [dungeon / stats / stoppen]: ").strip().lower()

    if actie == "dungeon":
        print("\n🗡️  Je gaat de dungeon in en verslaat een goblin!")
        # Geef bijvoorbeeld 60 XP voor het verslaan van de goblin
        geef_xp(mijn_speler, 60)

    elif actie == "stats":
        toon_karakter_stats(mijn_speler)

    elif actie == "stoppen":
        print("Bedankt voor het spelen!")
        break

    else:
        print("Ongeldig commando! Kies uit: dungeon, stats of stoppen.")

# character creator


# inventory = []


# # nieuwe items
# inventory.append("Leren Schild")
# print("Na .append() (Leren Schild toegevoegd):")
# print(inventory)
# print()

# # verwijder item 1
# verwijderd_item = inventory.pop(0)
# print(f"item verwijderd ('{verwijderd_item}'):")
# print(inventory)
# print()

# # Verwijder broodje als ik heb
# if "Broodje" in inventory:
#     inventory.remove("Broodje")
# print("broodje verwijdered")
# print(inventory)
# print()


# # character stats

# # Me
# character = {
#     "naam": "MrMatt04",
#     "level": 1,
#     "max_health": 100,
#     "huidige_gezondheid": 100,
#     "aanvalskracht": 15,
#     "verdediging": 10,
#     "rugzak": []
# }

# item_database = {
#     "Iron chestplate": {"verdediging": +15, "aanvalskracht": -2},
#     "magic staff": {"aanvalskracht": +25, "verdediging": -5},
#     "golden ring": {"max_health": +20, "aanvalskracht": +5}
# }


# def print_character_status(char):
#     print(f"=== Character Status: {char['naam']} (Level {char['level']}) ===")
#     print(f"gezondheid : {char['huidige_gezondheid']}/{char['max_health']}")
#     print(f"Aanval     : {char['aanvalskracht']}")
#     print(f"Verdediging: {char['verdediging']}")
#     print(f"Rugzak     : {char['rugzak']}")
#     print("-" * 45)


# # items oppakken
# def pickup(char, item_naam, database):
#     if item_naam in database:
#         # Voeg item toe aan de rugzak lijst
#         char["rugzak"].append(item_naam)

#         # Pas de stats aan op basis van het item
#         stats_boost = database[item_naam]
#         for stat, waarde in stats_boost.items():
#             if stat in char:
#                 char[stat] += waarde

#         print(f"--> {char['naam']} heeft '{item_naam}' opgepakt!")
#     else:
#         print(f"Item '{item_naam}' bestaat niet in de database.")


# pickup(character, "Iron chestplate", item_database)
# pickup(character, "magic staff", item_database)
# pickup(character, "golden ring", item_database)

# print()
# print_character_status(character)

# # Week 2

# # items op de grond
# grond_loot = [
#     "Gouden Ring",
#     "Roestig Zwaard",
#     "Gouden Beker",
#     "Leren Schoenen",
#     "Gouden Ketting",
#     "Oude Steen"
# ]

# print("Loot op de grond")
# print(grond_loot)
# print()

# # items die gouden rarity zijn

# gouden_schatten = [item for item in grond_loot if "Gouden" in item]

# # goud oppakken
# for schat in gouden_schatten:
#     character["rugzak"].append(schat)

# print("gevonden voorwerpen")
# print(f"Gevonden gouden schatten: {gouden_schatten}")
# print(f"Nieuwe inhoud rugzak van {character['naam']}: {character['rugzak']}")


# # week 3 monsters en xp
# def bereken_monster_xp(monster_level):
#     verdiende_xp = monster_level * 25
#     return verdiende_xp


# # level 5 monster
# monster_lvl = 5
# xp_beloning = bereken_monster_xp(monster_lvl)

# print("monster killed")
# print(f"Je hebt een level {monster_lvl} monster verslagen.")
# print(f"Verdiende XP: {xp_beloning} XP")
# print("-" * 35)

# # errors :(

# # starter goud
# character["goud"] = 50

# # shop catalogus
# winkel_catalogus = {
#     "1": {"naam": "Gezondheidsdrankje", "prijs": 15},
#     "2": {"naam": "Sterk Drankje", "prijs": 30},
#     "3": {"naam": "Gouden Sleutel", "prijs": 100}
# }


# def open_winkel(char, catalogus):
#     print("\n" + "="*40)
#     print("         WELKOM IN DE WINKEL!")
#     print("="*40)
#     print(f"Jouw huidige goud: {char['goud']} munten\n")

#     print("Wat wil je kopen?")
#     for sleutel, item in catalogus.items():
#         print(f"[{sleutel}] {item['naam']} - {item['prijs']} goud")
#     print("[4] Stoppen met winkelen")
#     print("-" * 40)

#     # try block voor fouten
#     try:
#         keuze = int(input("Typ het nummer van je keuze: "))

#         if keuze == 4:
#             print("Je verlaat de winkel. Tot ziens!")
#             return

#         keuze_str = str(keuze)
#         if keuze_str in catalogus:
#             gekozen_item = catalogus[keuze_str]
#             prijs = gekozen_item["prijs"]

#             # Check goud
#             if char["goud"] >= prijs:
#                 char["goud"] -= prijs  # Haal het goud eraf
#                 # Voeg toe aan rugzak
#                 char["rugzak"].append(gekozen_item["naam"])
#                 print(
#                     f" Gelukt! Je hebt een '{gekozen_item['naam']}' gekocht.")
#                 print(f"Restant goud: {char['goud']} munten.")
#             else:
#                 print(
#                     f" Niet genoeg goud! Je hebt {char['goud']} munten, maar dit kost {prijs} goud.")
#         else:
#             print(" Dit item bestaat niet. Kies een nummer uit de lijst.")

#     except ValueError:
#         # Foutmelding voor letter invoer
#         print("\n[FOUTMELDING] Oeps! Dat is geen geldig getal. Typ alstublieft eencijferig getal in (bijv. 1, 2 of 3).")


# # Test de winkel functie
# open_winkel(character, winkel_catalogus)

# # week 4 charater creator


# class Character:
#     def __init__(self, naam, level=1, max_health=100, aanvalskracht=15, verdediging=10):
#         self.naam = naam
#         self.level = level
#         self.max_health = max_health
#         self.huidige_health = max_health
#         self.aanvalskracht = aanvalskracht
#         self.verdediging = verdediging
#         self.skills = []
#         self.rugzak = []

#     # print karakter
#     def toon_status(self):
#         print(f"=== Character Status: {self.naam} (Level {self.level}) ===")
#         print(f"Health     : {self.huidige_health}/{self.max_health}")
#         print(f"Aanval     : {self.aanvalskracht}")
#         print(f"Verdediging: {self.verdediging}")
#         print(
#             f"Skills     : {', '.join(self.skills) if self.skills else 'Geen'}")
#         print(
#             f"Rugzak     : {', '.join(self.rugzak) if self.rugzak else 'Leeg'}")
#         print("-" * 45)

#     def leer_skill(self, nieuwe_skill):
#         self.skills.append(nieuwe_skill)
#         print(f"✨ {self.naam} heeft de skill '{nieuwe_skill}' geleerd!")

#     # leveling up
#     def level_up(self):
#         self.level += 1
#         self.max_health += 20
#         self.huidige_health = self.max_health  # Volledig genezen bij level up!
#         self.aanvalskracht += 5
#         self.verdediging += 3
#         print(f"🎉 LEVEL UP! {self.naam} is nu Level {self.level}!")


# # maak je eigen
# speler1 = Character(naam="MrMatt04", level=1, max_health=120, aanvalskracht=18)

# # team mate
# speler2 = Character(naam="ShadowWarrior", level=3,
#                     max_health=150, aanvalskracht=25)


# print("this is player 1")
# speler1.toon_status()

# speler1.leer_skill("Fireball")
# speler1.leer_skill("Shield Bash")


# speler1.level_up()


# print()
# speler1.toon_status()

# print("--- TESTEN SPELER 2 ---")
# speler2.leer_skill("Stealth Strike")
# speler2.toon_status()
