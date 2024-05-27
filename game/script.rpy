init python:
    import math
    import random

    def dbg():
        unlockWeaponF(player, weapons[5]) 
        player.inventory.weapon = weapons[5]
        return

    class DiscordStatus():
        def __init__(self):
            self.location = "In the forest"
            self.details = "  "
            self.largeImage = "charmedicon"

    renpy.music.register_channel("ambience", "sound")

    class Pronouns():
        def __init__(self):
            self.boy = "boy"
            self.him = "him"
            self.he = "he"
            self.his = "his"
            self.mister = "mister"

    class WeaponData():
        def __init__(self, name, attack, price):
            self.name = name
            self.attack = attack
            self.price = price

    class ArmorData():
        def __init__(self, name, health, price):
            self.name = name
            self.health = health
            self.price = price

    weapons = [
        WeaponData("nothing",0, 0),
        WeaponData("wooden sword",2, 50),
        WeaponData("silver blade",5, 200),
        WeaponData("torn blade",5, 1000),
        WeaponData("royal slime staff",3, 0),
        WeaponData("debug stick",999999999, 0),
        WeaponData("nature's branch",3, 500),
    ]
    
    armors = [
        ArmorData("nothing",0,0),
        ArmorData("leather armor",2,50),
        ArmorData("silver shield",5,200),
        ArmorData("normal armor?",-2, -10),
        ArmorData("royal crown",7, 0)
    ]
    
    class Inventory():
        def __init__(self, p_weapon=weapons[0], p_armor=armors[0]):
            self.weapon = p_weapon
            self.unlockedWeapons = [p_weapon]

            self.armor = p_armor
            self.unlockedArmors = [p_armor]


    class Objective():
        def __init__(self, description):
            self.completed = False
            self.completionFlags = [False, False, False, False, False]
            self.description = description

    class Pfp():
        def __init__(self):
            self.slimeUnlocked = False
            self.slimePrincessUnlocked = False
            self.merchantUnlocked = False

    class XPBar():
        def __init__(self):
            self.barValue = 50
            self.resetting = False
            self.startResetDelay = 1

    class Game():
        def __init__(self):
            self.objective = [
            Objective("Enter the inn to look for a place to rest"),
            Objective("Explore the forest and enter the cave"),
            Objective("Enter slime village and talk to the slime princess for help"),
            Objective("Wait for the next update and follow @ImpCharm on twitter~!"),
            Objective("Go to the alraune tree to collect magic energy"),
            ]

            self.pfp = Pfp()

            self.hasSave = False

            self.levelDrainSlimeEvent = True
            self.bellsFound = [False, False, False, False, False, False, False]

            self.currentPage = "a_town_central"
            self.currentEvent = ""

            self.slimeTutoFight = True

            self.foundPond = False
            self.shopUnlocked = False
            self.slimeHouseUnlocked = False

            self.casinoUnlocked = False
            self.casinoDebtCutscene = False
            
            self.slimeInnUnlocked = False


            self.casinoRouletteUnlocked = False

            self.shopKeeperFavor = 0
            self.casinoDrained = 0
            self.casinoDebt = 0

            self.dayTime = round(time_morning)
            self.dayOfTheWeek = 0

    class Character:
        def __init__(self, baseMaxHealth, baseMaxSP, baseAttack, money, XP, profile, conditions, inventory=Inventory()):
            self.baseMaxHealth = baseMaxHealth
            self.maxHealth = baseMaxHealth
            self.health = baseMaxHealth
            self.arousal = 0
            self.baseMaxSP = baseMaxSP
            self.maxSP = baseMaxSP
            self.SP = baseMaxSP
            self.baseAttack = baseAttack
            self.attack = baseAttack
            self.money = money
            self.oldLevel = 0
            self.oldLevelTop = 0
            self.oldLevelBottom = 0
            self.level = 1
            self.XP = XP
            self.levelBottom = 0
            self.levelTop = 0
            self.playerEncounters = 0
            self.lostCount = 0
            self.winCount = 0
            self.profile = profile
            self.conditions = conditions
            self.inventory = inventory
            self.weaknesses = Weaknesses()

        def __str__(self):
            return "{size=*1.5}{color=" + self.profile.color + "}" + self.profile.name + "{/color}{/size}"

    class Profile:
        def __init__(self, name, color, pageId, description=""):
            self.name = name
            self.description = description
            self.color = color
            self.pageId = pageId
            self.favor = 0
            self.lastAction = ""
            self.title = ""

            self.introPage = "fight_" + pageId + "_intro"
            self.turnPage = "fight_" + pageId + "_turn"
            self.reactionPage = "fight_" + pageId + "_reaction"
            self.hitAnimationPage = "fight_" + pageId + "_hitAnimation"
            self.deadPage = "fight_" + pageId + "_dead"
            self.dryPage = "fight_" + pageId + "_dry"

            self.XPBar = XPBar()

    class Conditions:
        def __init__(self):
            self.restrained = False
            self.horny = False
            self.poisoned = 0
            self.slimePet = False
            self.princessServant = False
            self.casinoDebt = False

    class Weaknesses():
        def __init__(self):
            self.feet = 0
            self.blowjob = 0
            self.kiss = 0
            self.sex = 0
            self.paizuri = 0
            self.armpits = 0
            self.butt = 0 

    

    class SexTypes():
        def __init__(self):
            self.feet = "feet"
            self.blowjob = "blowjob"
            self.kiss = "kiss"
            self.sex = "sex"
            self.paizuri = "paizuri"
            self.armpits = "armpits"
            self.butt = "butt"
            

    
    debug = False
    
    rose = "#ff7979"
    guideColor = "#ffaa00"
    gold = "#ffff00"

    casinoRouletteNumbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
    casinoBetAmounts = [10, 15, 30, 50, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 5000, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 1000000]

    def setCombatMenu():
        combatMenu = "index"    

label start:
    default slimecastlemonologue = False

    default sexTypes = SexTypes()
    default attackType = sexTypes.sex
    default arousalBarText = ""

    default willRestrain = False
    default isRestrained = False
    default inCombat = False
    default currentTurnNumber = 0

    default temptationEvent = False

    default dangerAreaDepth = 0

    default shopKeeperStatus = ""
    default shopKeeperDialogue = ""

    default innKeeperStatus = ""

    default time_mnreset = 120
    
    default time_midnight = 0
    default time_morning = (time_mnreset / 4) * 1
    default time_afternoon = (time_mnreset / 4) * 2
    default time_evening = (time_mnreset / 4) * 3

    default uselessVar = "im almost useless :3"
    default isTalking = False
    default inShopGui = False

    default merchantSoldPoison = False

    default dailyRandomI = 0

    default combatMenu = "Main"
    default game = Game()

    default discStatus = DiscordStatus()

    default player = Character(
        10, 5, 3, 0, 140,  
        Profile("You", "#ffffff", "player", 
        "It's you."
        ),
        Conditions(),
        Inventory()
    )
    $ player.profile.title = "Hero"

    default imp = Character(
        10, 10, 5, 100, 5000, 
        Profile("Lulu", "#FFEBEE", "imp",
        "Lulu is a succubus. Succubi are demons who feed on sexual energy by arousing their victims. They look like pretty women and often seduce their victims. \n \n Lulu doesn't appear to be anything like this though. She saved you from the forest when you first arrived here and now she's assisting you on your journey!"
        ),
        Conditions()
    )

    default slime = Character(
        10, 5, 2, 10, 130,  
        Profile("The slime", "#92d3fd", "slime",
        "Slimes are fragile creatures. They don't pose a very big threat by themselves, but don't let your guard down. slimes tend to come in pairs, allowing them to overpower humans if they're not careful... \n \n Slimes excel at restraining humans. Their sticky surface makes it difficult for them to escape from restraints. They tend to physically get on top of their prey and force the penis to shoot mana straight into their core, which is located in the center of every slime's body. \n \n This particular slime, however, doesn't seem to be much of a team player..."
        ),
        Conditions(),
        Inventory()
    )

    default slimePrincess = Character(
        20, 5, 1, 1, 2000,  
        Profile("The slime princess", "#ffa8ce", "slimeprincess",
        "One of the direct daughters of the slime queen herself. She's the current ruler of Slime Village and controls the slime army. Her lesser slimes are tasked with attacking humans to collect XP, Feeding it to the princess upon victory. \n \n Despite her arrogant and naive behaviour, she does pose quite a threat, even without her army backing her up. \n \n Her main technique of victory is seduction. When she's in a pinch, she'll offer humans a chance to have sex with her, usually ending in the human's defeat..."
        ),
        Conditions(),
        Inventory(weapons[4], armors[4])
    )


    default shopKeeper = Character(
        6, 5, 2, 1000, 130,  
        Profile("The shopkeeper", "#7986CB", "shopkeeper",
        "A sweet girl who runs, and lives in the local shop. She likes supporting new adventurers who are just starting out on their journey, having adventurers as family, she knows how important proper equipment is."
        ),
        Conditions(),
        Inventory()
    )

    default merchant = Character(
        10, 10, 5, 1000, 401,  
        Profile("The merchant", "#FFEB3B", "merchant",
        "Just a humble businesswoman trying to make a living. She seems to have a specialty when it comes to dealing with poison and other toxins. No other info available..."),
        Conditions(),
        Inventory()
    )

    default casinoGirlWhite = Character(
        3, 10, 7, 3000, 4500,  
        Profile("The girl", "#BDBDBD", "casinogirlwhite",
        "The first of the sisters who run the casino. She has the ability to stay calm, even in the most tense of situations. She's the brain behind the casino. Setting up the games and advertising the place to adventurers, desperate for money."),
        Conditions(),
        Inventory()
    )

    default casinoGirlRed = Character(
        10, 10, 3, 3000, 4500,  
        Profile("The girl", "#E57373", "casinogirlred",
        "The second of the sisters who run the casino. She's the looks of the casino, tempting customers to lose by charming them and telling them to make bad decisions"),
        Conditions(),
        Inventory()
    )

    default innKeeper = Character(
        10, 10, 3, 100, 6096,  
        Profile("Musei", "#d2b8d3", "innkeeper",
        "The alleged owner of Slime Village's inn. Nobody knows for sure when she arrived or if she even owns the inn, but she does, and she takes care of it. If you're ever in Slime Village, give her a visit! She offers her services for free to adventurers because she \"Loves taking care of cute inexperienced adventurers\". \n \n Despite her seemingly sweet nature, she's still a monster girl, so don't let your guard down."),
        Conditions(),
        Inventory()
    )

    default charm = Character(
        1, 1, 1, 60000, 60000,
        Profile("Charm", "#E57373", "charm",
        "Innocent little imp~ Artists source is in the Inn~"),
        Conditions(),
        Inventory()
    )

    

    default currentEnemy = slime

    default myDissolve = Dissolve(0.2)

    default slimePrincessPetTalk = False

    default casinoBetAmount = 0
    default casinoOwed = 0
    default casinoBetIndex = 0
    default casinoSpinPower = 0
    default casinoRouletteIndex = 0
    default casinoRouletteDoubled = 0

    default targetLL = 0
    default targetL = 0
    default targetM = 0
    default targetR = 0
    default targetRR = 0

    default colorLL = "#ffffff"
    default colorL = "#ffffff"
    default colorM = "#ffffff"
    default colorR = "#ffffff"
    default colorRR = "#ffffff"

    default numLeftLeft = ""
    default numLeft = ""
    default numMid = ""
    default numRight = ""
    default numRightRight = ""

    default waitTime = 0
    default colorWon = ""
    default target = 0

    default restrainEscapePower = 0
    default restrainPower = 0

    default randomPopupXpos = 0
    default randomPopupYPos = 0

    default statPopups = []

    default pronouns = Pronouns()

    $ arousalBarText = "Arousal: " + str(player.arousal) + "/100"

    "[anonTalk('#fff', 'Notice')]" "Note: The game currently uses masculine pronouns to refer to the player. You can change this by visiting the inn and pressing settings or changing them here."
    menu:
        "Ignore":
            pass
        "Change pronouns":
            call changePronouns from _call_changePronouns_1

    "[anonTalk('#fff', 'Notice')]" "You can also view image credit in the settings or here"
    menu:
        "Ignore":
            pass
        "View image credits (Potential spoilers)":
            call imageCredit from _call_imageCredit_1

    show screen menuBtn

    "[anonTalk('#fff', 'Notice')]" "If you're on mobile, please press the button in the top left corner of the screen to open the menu.\nThis is how you save, open your inventory and check enemies."
    
    jump succubus_town_1

    return
