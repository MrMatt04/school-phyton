import random

print("==== Welcome to the RPG Game! ====")
print("Laten we beginnen met het maken van je karakter!\n")


def create_character():
    print("=== Karakter Creatie ===")
    name = input("Voer de naam van je karakter in: ").strip()

    while not name:
        print("De naam mag niet leeg zijn.")
        name = input("Voer de naam van je karakter in: ").strip()

    valid_classes = {
        "1": {"naam": "Warrior", "aanvalskracht": 15, "speed": 10, "verdediging": 20, "max_hp": 120, "starter_wapen": "Houten Zwaard", "unieke_aanval": "Schildklap", "schade_uniek": 25},
        "2": {"naam": "Mage", "aanvalskracht": 20, "speed": 15, "verdediging": 10, "max_hp": 80, "starter_wapen": "Oude Staf", "unieke_aanval": "Vuurbal", "schade_uniek": 35},
        "3": {"naam": "Rogue", "aanvalskracht": 25, "speed": 20, "verdediging": 5, "max_hp": 90, "starter_wapen": "Roestige Dolk", "unieke_aanval": "Schaduwsteek", "schade_uniek": 30}
    }

    print("\nKies een klasse:")
    print("[1] Warrior")
    print("[2] Mage")
    print("[3] Rogue")

    while True:
        keuze = input("\nJouw keuze (1, 2 of 3): ").strip()
        if keuze in valid_classes:
            gekozen_klasse = valid_classes[keuze]
            break
        else:
            print("Kies 1, 2 of 3.")

    karakter = {
        "naam": name,
        "klasse": gekozen_klasse["naam"],
        "level": 1,
        "xp": 0,
        "xp_nodig": 100,
        "max_hp": gekozen_klasse["max_hp"],
        "hp": gekozen_klasse["max_hp"],
        "aanvalskracht": gekozen_klasse["aanvalskracht"],
        "speed": gekozen_klasse["speed"],
        "verdediging": gekozen_klasse["verdediging"],
        "equipment": {
            "wapen": gekozen_klasse["starter_wapen"],
            "armor": "Stoffen Kleding",
            "skills": ["Basis Aanval", gekozen_klasse["unieke_aanval"]],
            "potions": {"Health Potion": 2}
        },
        "schade_uniek": gekozen_klasse["schade_uniek"]
    }

    print("\nKarakter succesvol aangemaakt!")
    return karakter


def kies_stat_upgrades(karakter):
    beschikbare_punten = 5
    print(
        f"\n🌟 LEVEL UP! Je bent nu Level {karakter['level']}! Je hebt 5 punten te verdelen.")

    while beschikbare_punten > 0:
        print(f"\nResterende punten: {beschikbare_punten}")
        print("[1] Max HP (+10 & geneest)")
        print("[2] Aanvalskracht (+1)")
        print("[3] Snelheid (+1)")
        print("[4] Verdediging (+1)")

        keuze = input("Kies (1-4): ").strip()

        if keuze == "1":
            karakter["max_hp"] += 10
            karakter["hp"] += 10
            print("-> Max HP verhoogd!")
            beschikbare_punten -= 1
        elif keuze == "2":
            karakter["aanvalskracht"] += 1
            print("-> Aanval verhoogd!")
            beschikbare_punten -= 1
        elif keuze == "3":
            karakter["speed"] += 1
            print("-> Snelheid verhoogd!")
            beschikbare_punten -= 1
        elif keuze == "4":
            karakter["verdediging"] += 1
            print("-> Verdediging verhoogd!")
            beschikbare_punten -= 1
        else:
            print("Kies een getal tussen 1 en 4.")


def geef_xp(karakter, hoeveelheid_xp):
    print(f"\n✨ Je hebt {hoeveelheid_xp} XP gekregen!")
    karakter["xp"] += hoeveelheid_xp

    while karakter["xp"] >= karakter["xp_nodig"]:
        karakter["xp"] -= karakter["xp_nodig"]
        karakter["level"] += 1
        karakter["xp_nodig"] = int(karakter["xp_nodig"] * 1.5)
        kies_stat_upgrades(karakter)


def toon_karakter_stats(karakter):
    print(
        f"\n--- {karakter['naam'].upper()} (Lvl {karakter['level']} {karakter['klasse']}) ---")
    print(f"HP: {karakter['hp']} / {karakter['max_hp']}")
    print(f"XP: {karakter['xp']} / {karakter['xp_nodig']}")
    print(
        f"Aanval: {karakter['aanvalskracht']} | Snelheid: {karakter['speed']} | Verdediging: {karakter['verdediging']}")
    print(f"Wapen: {karakter['equipment']['wapen']}")
    print(f"Skills: {', '.join(karakter['equipment']['skills'])}")
    print(
        f"Health Potions over: {karakter['equipment']['potions']['Health Potion']}")


def start_gevecht(karakter):
    # Basis lijst met monsters
    monster_lijst = [
        {"naam": "Goblin", "hp": 40, "aanval": 10, "xp_reward": 50},
        {"naam": "Orc", "hp": 70, "aanval": 16, "xp_reward": 90},
        {"naam": "Skeleton", "hp": 50, "aanval": 12, "xp_reward": 65},
        {"naam": "Dungeon Boss (Draakje)", "hp": 120,
         "aanval": 22, "xp_reward": 150}
    ]

    # Kies willekeurig een monster en maak een kopie
    vijand = random.choice(monster_lijst).copy()

    # --- MONSTER LEVEL SCHALING ---
    # Het monster krijgt hetzelfde level als de speler (of je kunt er optioneel een willekeurige variatie in gooien)
    vijand["level"] = karakter["level"]

    # Bereken hoeveel levels het monster sterker moet worden dan de basisversie (level 1)
    level_verschil = vijand["level"] - 1

    if level_verschil > 0:
        # Verhoog HP en aanval per level van de speler
        vijand["hp"] += level_verschil * 15
        vijand["aanval"] += level_verschil * 4
        vijand["xp_reward"] += level_verschil * 25

    # Zorg dat de huidige HP van het vijand gelijk is aan zijn nieuwe max HP
    vijand["max_hp"] = vijand["hp"]

    print(
        f"\n⚔️  Je komt een wilde **{vijand['naam']} (Lvl {vijand['level']})** tegen! Gevecht begint!")

    # Gevechtsloop
    while vijand["hp"] > 0 and karakter["hp"] > 0:
        print(
            f"\n--- {karakter['naam']} (HP: {karakter['hp']}) vs {vijand['naam']} [Lvl {vijand['level']}] (HP: {vijand['hp']}/{vijand['max_hp']}) ---")
        print("Wat wil je doen?")
        print("[1] Normale Aanval")
        print(f"[2] Unieke Skill ({karakter['equipment']['skills'][1]})")
        print(
            f"[3] Drink Health Potion (Je hebt er nog: {karakter['equipment']['potions']['Health Potion']})")

        keuze = input("Kies je actie (1-3): ").strip()

        # Speler beurt
        if keuze == "1":
            schade = karakter["aanvalskracht"]
            vijand["hp"] -= schade
            print(
                f"💥 Je valt de {vijand['naam']} aan met je {karakter['equipment']['wapen']} en doet {schade} schade!")

        elif keuze == "2":
            schade = karakter["schade_uniek"]
            vijand["hp"] -= schade
            print(
                f"🔥 Je gebruikt je unieke skill '{karakter['equipment']['skills'][1]}' en doet maar liefst {schade} schade!")

        elif keuze == "3":
            if karakter['equipment']['potions']['Health Potion'] > 0:
                karakter['equipment']['potions']['Health Potion'] -= 1
                karakter['hp'] += 40
                if karakter['hp'] > karakter['max_hp']:
                    karakter['hp'] = karakter['max_hp']
                print(
                    f"🧪 Je drinkt een Health Potion! Je HP is nu {karakter['hp']}.")
                continue
            else:
                print("❌ Je hebt geen Health Potions meer over!")
                continue
        else:
            print("❌ Ongeldige keuze, je verliest je beurt!")

        # Check of het monster verslagen is
        if vijand["hp"] <= 0:
            print(
                f"\n🏆 Gefeliciteerd! Je hebt de {vijand['naam']} (Lvl {vijand['level']}) verslagen!")
            geef_xp(karakter, vijand["xp_reward"])
            break

        # Monster beurt
        monster_schade = max(
            5, vijand["aanval"] - int(karakter["verdediging"] / 4))
        karakter["hp"] -= monster_schade
        print(
            f"⚡ De {vijand['naam']} slaat terug en doet {monster_schade} schade bij jou!")

        if karakter["hp"] <= 0:
            print(
                f"\n💀 Je bent verslagen door de {vijand['naam']}... Game Over.")
            karakter["hp"] = 0
            break


# Start het spel
mijn_speler = create_character()

while True:
    if mijn_speler["hp"] <= 0:
        print("\nJe avontuur is ten einde. Start het script opnieuw om een nieuw karakter te maken.")
        break

    actie = input(
        "\nWat wil je doen? [dungeon / stats / stoppen]: ").strip().lower()

    if actie == "dungeon":
        start_gevecht(mijn_speler)
    elif actie == "stats":
        toon_karakter_stats(mijn_speler)
    elif actie == "stoppen":
        print("Tot ziens!")
        break
    else:
        print("Typ: dungeon, stats of stoppen.")
