label profile:
    "Profile"
    call calculateLevelAll from _call_calculateLevelAll_3
    "Weapon: [player.inventory.weapon.name] | Armor: [player.inventory.armor.name] 
    \n [player.levelTop - player.XP] XP to next level 
    \n Title: [player.profile.title]"
    menu:
        "Back":
            return
        "Stats":
            call stats from _call_stats
        "Inventory":
            call inventory from _call_inventory
        "Unlocked pfp's":
            call pfps from _call_pfps

label stats:
    "stats"
    menu:
        "Back":
            return

label inventory:
    "Weapon: [player.inventory.weapon.name] | Armor: [player.inventory.armor.name]"
    menu:
        "Back":
            return
        "Weapons":
            call inventory_weapons from _call_inventory_weapons
        "armors":
            call inventory_armors from _call_inventory_armors
    jump inventory

define options = ["a", "b", "c", "d", "e", "f"]
label inventory_weapons:
    menu:
        "Back":
            return

label inventory_armors:
    menu:
        "Back":
            return