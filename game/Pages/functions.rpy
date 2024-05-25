init python:
    import random
    import math
    
    def setDiscord():
        discord.set(state = discStatus.location + " | " + "Level: " + str(player.level),
        details = discStatus.details,
        large_image = discStatus.largeImage
        )

    def f_dayPass():
        game.dayOfTheWeek += 1
        if game.dayOfTheWeek == 7:
            game.dayOfTheWeek = 0

        if game.dayOfTheWeek < 4:
            merchantSoldPoison = False
            game.levelDrainSlimeEvent = True

        dailyRandomI = rand(1, 100)

        renpy.block_rollback()
        shopKeeperStatus = "upstairs"
        innKeeperStatus = "upstairs"
        return

    # def deletePopup():
    #     statPopups.remove(statPopups[0])   
    #     if len(statPopups) == 0:
    #         renpy.hide_screen("stat_popup") 
    #     return

    def buttonClicked():
        game.dayTime += 1
        if(game.dayTime >= time_mnreset):
            game.dayTime = time_midnight
            f_dayPass()
        return

    def hasStatusEffect():
        return (player.conditions.poisoned > 0
        or player.conditions.horny 
        or player.conditions.princessServant 
        or player.conditions.slimePet 
        or player.conditions.casinoDebt)

    def getTimePeriod(p_check="none"): 
        if game.dayTime < time_morning:
            if p_check != "none":
                if p_check == "night":
                    return True
                else:
                    return False
            return "night"
        elif game.dayTime < time_afternoon:
            if p_check != "none":
                if p_check == "morning":
                    return True
                else:
                    return False
            return "morning"
        elif game.dayTime < time_evening:
            if p_check != "none":
                if p_check == "afternoon":
                    return True
                else:
                    return False
            return "afternoon"
        else:
            if p_check != "none":
                if p_check == "evening":
                    return True
                else:
                    return False
            return "evening"

    def getCurrentObjective():
        for eobjective in game.objective:
            if (eobjective.completed == False):
                return eobjective

    def setShopTouchyText(place="town"):

        uselessVar = "wowie KAzowie"

        if place == "town":
            shopKeeperDialogue = "Thank you for your purchase!"
        elif place == "merchant":
            shopKeeperDialogue = "Look at you~ You won't regret this~"

        return

    def unlockArmorF(recipient, armor, place="town"):
        if armor in player.inventory.unlockedArmors:
            return "Duplicate"

        player.inventory.unlockedArmors.append(armor)
        renpy.call("loseMoney", player, armor.price, False, 2, place)
        return "Ok"

    def unlockWeaponF(recipient, weapon, place="town"):
        if weapon in player.inventory.unlockedWeapons:
            return "Duplicate"

        player.inventory.unlockedWeapons.append(weapon)
        renpy.call("loseMoney", player, weapon.price, False, 2, place)
        return "Ok"

    def anonTalk(color="#fff", text="???"):
        return "{size=*1.5}{color=" + color + "}" + text + "{/color}{/size}"



    def closestTo(a, arr):
        closest = arr[0] 

        for i in range(1, len(arr)):
            if abs(a - arr[i]) < abs(a - closest):
                closest = arr[i]

        return closest


    def mathMin(num1, num2):
        return min(num1, num2)

    def mathMax(num1, num2):
        return max(num1, num2)

    def mathFloor(num1):
        return math.floor(num1)

    def mathPow(num1, num2):
        return pow(num1, num2)

    def rand(min, max):
        return random.randint(min, max)

    def getHighlightText(text):
        return "{size=+15}{color="+guideColor+"}"+text+"{/color}{/size}"

label random(min, max):
    return random.randint(min, max)

label min(num1, num2):
    return math.Min(num1, num2)

label options:
    menu:
        "Pronouns":
            call changePronouns from _call_changePronouns
        "Image credit":
            call imageCredit from _call_imageCredit
        "Back":
            return
    jump options

label changePronouns:
    menu:
        "Male":
            $ pronouns.boy = "boy"
            $ pronouns.he = "he"
            $ pronouns.him = "him"
            $ pronouns.his = "his"
            $ pronouns.mister = "mister"
        "Female":
            $ pronouns.boy = "girl"
            $ pronouns.he = "she"
            $ pronouns.him = "her"
            $ pronouns.his = "her"
            $ pronouns.mister = "miss"
        "Custom":
            $ pronouns.boy = renpy.input("Modify 'boy/girl/cutie' pronoun\nYou're such a good {color=#ff0}[pronouns.boy]{/color}!", pronouns.boy)
            $ pronouns.he = renpy.input("Modify 'he/she/they' pronoun\nWhere did {color=#ff0}[pronouns.he]{/color} go?", pronouns.he)
            $ pronouns.him = renpy.input("Modify 'him/her/them' pronoun\nHave you seen {color=#ff0}[pronouns.him]{/color}?", pronouns.him)
            $ pronouns.his = renpy.input("Modify 'his/her/their' pronoun\nThis is {color=#ff0}[pronouns.his]{/color} item", pronouns.his)
            $ pronouns.mister = renpy.input("Modify 'mister/miss' pronoun\nHey {color=#ff0}[pronouns.mister]{/color}~ {color=#ff0}[pronouns.mister]{/color} hero~", pronouns.mister)
        "Back":
            return

    "This game was made with masculine pronouns in mind. The player will still have a dick, regardless of pronouns"
    "Example sentence: [pronouns.mister] hero said [pronouns.he] would help [pronouns.him] with [pronouns.his] quest. What a good [pronouns.boy]!"
    jump changePronouns


label recalculateCapsAll:
    call recalculateCaps(player) from _call_recalculateCaps_4
    call recalculateCaps(currentEnemy) from _call_recalculateCaps_5
    call recalculateCaps(slime) from _call_recalculateCaps_7
    call recalculateCaps(slimePrincess) from _call_recalculateCaps_8
    call recalculateCaps(merchant) from _call_recalculateCaps_9
    return

label recalculateCaps(character=player):
    $ character.health = mathMin(character.maxHealth, character.health)
    $ character.health = mathMax(character.health, 0)
    
    $ character.SP = mathMin(character.maxSP, character.SP)

    $ character.arousal = mathMin(100, character.arousal)
    $ character.arousal = mathMax(0, character.arousal)

    $ character.conditions.poisoned = mathMax(0, character.conditions.poisoned)


    $ character.SP = round(character.SP)
    $ character.health = round(character.health)
    $ character.arousal = round(character.arousal)

    if enemyXPBar != 100 and enemyXPBar != 0:
        $ enemyXPBar = (currentEnemy.XP + 1 - currentEnemy.levelBottom + 1) / (currentEnemy.levelTop + 1 - currentEnemy.levelBottom + 1) * 100

    if playerXPBar != 100 and playerXPBar != 0:
        $ playerXPBar = (player.XP + 1 - player.levelBottom + 1) / (player.levelTop + 1 - player.levelBottom + 1) * 100
    
    $ setDiscord()

    return

label setAmbience():
    
    if (currentArea == "forest" or currentArea == "town") and getTimePeriod("night"):
        play ambience nightambience loop
    else:
        stop ambience fadeout 1
    
    return

label move(destination):
    $ isTalking = False
    if (game.dayTime % 10 == 5):
        $ player.arousal -= 1
        $ player.conditions.poisoned -= 1

    call setAmbience from _call_setAmbience_3

    show screen menuBtn
    show screen objective
    show screen timeMarker
    call updateArousal(player) from _call_updateArousal_4
    call recalculateCaps from _call_recalculateCaps_10
    call expression destination from _call_expression_5
    return

default currentArea = ""
label areaMarker(location=currentArea):
    if location != currentArea:
        play audio movement
        hide screen locationMarker
        show screen locationMarker

    $ currentArea = location
    
    if location == "slime village":
        $ discStatus.location = "In slime village"
    elif location == "town":
        $ discStatus.location = "In town"
    else:
        $ discStatus.location = "In the " + location
    
    $ setDiscord()
    
    return
    
label enterCombatFake(character):
    $ config.rollback_enabled = False
    $ config.has_autosave = False
    $ renpy.block_rollback()

    call calculateLevel(player, False, False, False) from _call_calculateLevel_18 
    call calculateLevel(character, False, False, False) from _call_calculateLevel_19 


    
    $ currentEnemy = character
    $ inCombat = True
    $ currentTurnNumber = 0

    $ discStatus.details = "Fighting " + currentEnemy.profile.name + "."
    $ setDiscord()

    
    hide screen objective
    call showBattleGui from _call_showBattleGui_2 
    
    return

label enterCombat(character):
    $ config.rollback_enabled = False
    $ config.has_autosave = False
    $ renpy.block_rollback()

    call calculateLevel(player, False, False, False) from _call_calculateLevel_7
    call calculateLevel(character, False, False, False) from _call_calculateLevel_8


    
    $ currentEnemy = character
    $ inCombat = True
    $ currentTurnNumber = 0

    $ discStatus.details = "Fighting " + currentEnemy.profile.name + "."
    $ setDiscord()

    
    hide screen objective
    call showBattleGui from _call_showBattleGui_1
    
    play music combat loop volume 0.25
    
    jump expression currentEnemy.profile.introPage
    return
        
label exitCombat():
    stop music fadeout 3.0
    stop sound fadeout 3.0
    
    hide screen LostXPPopup
    hide screen LostLevelPopup
    hide screen GainedLevelPopup
    
    call escapeRestraint from _call_escapeRestraint_2
    call calculateLevel(player) from _call_calculateLevel_9
    $ inCombat = False
    call areaMarker from _call_areaMarker_10

    $ discStatus.details = "  "
    $ setDiscord()

    call hideBattleGui from _call_hideBattleGui
    $ config.has_autosave = True
    $ config.rollback_enabled = True
    $ renpy.block_rollback()
    return



label showBattleGui:
    $ playerHealthBarFilling = player.health / player.maxHealth * 730
    hide battleGui
    show screen battleGui with myDissolve
    $ renpy.restart_interaction() 
    return

label hideBattleGui:
    $ playerHealthBarFilling = player.health / player.maxHealth * 730
    hide screen battleGui with myDissolve
    $ renpy.restart_interaction() 
    return

label hideAllChara:
    call hideAllSlime from _call_hideAllSlime_19
    call hideAllSlimePrincess from _call_hideAllSlimePrincess_10
    call hideAllImp from _call_hideAllImp_4
    call hideAllLesserSlime from _call_hideAllLesserSlime_7
    call hideAllShopKeeper from _call_hideAllShopKeeper_3
    call hideAllMerchant from _call_hideAllMerchant_5
    call hideAllInnkeeper from _call_hideAllInnkeeper
    call hideAllCasino from _call_hideAllCasino_3
    return

label hideAllImp:
    hide imp_boobhand
    hide imp_close
    hide imp_happyface
    hide imp_sadface
    hide imp_stand
    hide imp_wave
    return

label hideAllSlime:
    hide slime_bj
    hide slime_main
    hide slime_main_sad
    hide slime_succless
    hide slime_sexy
    hide slime_sex
    hide slime_paizuri
    hide slime_mouthcum
    hide slime_succ_anim
    hide slime_fellatio_anim
    hide slime_mount
    hide slime_boobpush
    return

label hideAllSlimePrincess:
    hide slimeprincess_boob
    hide slimeprincess_kneel
    hide slimeprincess_laugh
    hide slimeprincess_love
    hide slimeprincess_smug
    hide slimeprincess_stand
    hide slimeprincess_stand2
    hide slimeprincess_sex
    hide slimeprincess_sex2
    hide slimeprincess_presenting
    hide slimeprincess_kiss
    return

label hideAllLesserSlime:
    hide lesserslime_main
    hide lesserslime_footjob
    hide lesserslime_paizuri
    hide lesserslime_sex
    hide lesserslime_assistant
    return

label hideAllShopKeeper:
    hide shopkeeper_leanforward
    hide shopkeeper_leanforward_o
    hide shopkeeper_leanforward_open
    hide shopkeeper_pout
    hide shopkeeper_stand
    hide shopkeeper_close
    hide shopkeeper_forest
    return

label hideAllMerchant:
    hide merchant_handboob
    hide merchant_lean_open
    hide merchant_lean_closed
    hide merchant_paizuri
    hide merchant_tongue
    hide merchant_stand
    hide merchant_leanboobs
    hide merchant_ass
    hide merchant_ass_close
    hide merchant_flipAss
    return

label hideAllInnkeeper:
    hide innkeeper_fullbody
    hide innkeeper_headshot
    hide innkeeper_mouth
    hide innkeeper_sit
    hide innkeeper_headshot_pos
    return

label hideAllCasino:
    hide casinogirlwhite_sit
    hide casinogirlwhite_kneel
    hide casinogirlwhite_pits

    hide casinogirlred_ass
    hide casinogirlred_boobhand
    hide casinogirlred_casual
    hide casinogirlred_closepour
    hide casinogirlred_pour2
    hide casinogirlred_handsapart
    hide casinogirlred_contact
    hide casinogirlred_squat
    hide casinogirlred_pits3
    hide casinogirlred_pits
    hide casinogirlred_kneel
    hide casinogirlred_lean
    return

label setShopTouchyText(place="town"):
        if place == "town":
            $ shopKeeperDialogue = "Hehe~ hey, that tickles~"
            call screen shopGuiTouchy("town")

        elif place == "merchant":
            $ randomI = rand(1,3)
            if randomI == 1:
                $ shopKeeperDialogue = "Kyahaha~! Do you like touching me, [pronouns.mister]? That's totally pathetic, y'know~?"
            elif randomI == 2:
                $ shopKeeperDialogue = "You can't buy me, silly~"
            else:
                $ shopKeeperDialogue = "They're squishy, right~?"

            call screen shopGuiTouchy("merchant")


        return


label setShopKeeperDialogue(place):

        $ uselessVar = "wowie zowie"

        if place == "town":
            $ shopKeeperDialogue = "Thank you for your purchase!"
        elif place == "merchant":
            $ shopKeeperDialogue = "Look at you~ You won't regret this~"
        
        return

label say(whatToSay):
    "[whatToSay]"
    return
    
label takeDamageText(dmg):
    "You took {color=#f77}{size=+20}[dmg]{/size}{/color} damage!"
    return
    



# label popup(p_title):
#     $ statPopups.append(p_title)
#     show screen stat_popup
#     return

label gainXP(character, XP):
    $ character.XP += round(XP)
    "[character.profile.name] gained [round(XP)] XP!"
    call calculateLevel(character) from _call_calculateLevel_10
    return

label loseXP(character, XP):
    $ character.XP -= round(XP)
    "[character.profile.name] lost [round(XP)] XP..."
    call calculateLevel(character) from _call_calculateLevel_11
    return

label gainMoney(character, money):
    play audio coin
    "[character.profile.name] gained {color=#ff0} [round(money)] gold!"
    $ character.money += round(money)
    return

label loseMoney(character, money, message=True, p_audio=1, place=""):
    if character.money - money < 0:
        return "broke"

    if p_audio == 1:
        play audio coin
    elif p_audio == 2:
        play audio shop

    call setShopKeeperDialogue(place) from _call_setShopKeeperDialogue



    if message:
        "[character.profile.name] lost {color=#ff0} [round(money)] gold!"
    $ character.money -= round(money)
    return

label increaseFavor(character, favor):
    $ character.profile.favor += favor
    return

label changeTitle(character, status):
    if character.profile.title == status:
        return

    play audio item1
    "{color=#ff0}[character.profile.name]: [character.profile.title] -> [status]"
    $ character.profile.title = status
    return

label takeDamage(character, damage):
    "[character.profile.name] took [damage] damage."
    $ character.health -= damage


    return

label restoreHealthPartiallyMax(character, percentage):
    $ character.health = round(min((character.health + (percentage / 100) * character.maxHealth), character.maxHealth))
    return

label dayPass:
    $ game.dayOfTheWeek += 1
    if game.dayOfTheWeek == 7:
        $ game.dayOfTheWeek = 0
    
    if game.dayOfTheWeek < 4:
        $ game.levelDrainSlimeEvent = True
    # todo: change this for dailyi

    $ dailyRandomI = rand(1, 100)

    $ renpy.block_rollback()
    $ shopKeeperStatus = "upstairs"
    $ innKeeperStatus = "upstairs"
    call setAmbience from _call_setAmbience_4
    return

label cleanseSoul:
    play audio recovery3
    $ player.weaknesses = Weaknesses()
    $ player.arousal = 0
    call updateArousal from _call_updateArousal_5
    return

label restore(character=player, sound=False):
    if sound:
        play audio recovery3
    $ character.health = character.maxHealth
    $ character.SP = character.maxSP
    $ character.arousal = 0
    $ character.conditions.poisoned = 0
    call clearAllLipstick from _call_clearAllLipstick_1
    call updateArousal(character) from _call_updateArousal_6
    return

label restoreAll:
    call restore(slime) from _call_restore_3
    call restore(slimePrincess) from _call_restore_4
    call restore(player) from _call_restore_5
    call restore(imp) from _call_restore_6
    return

label calculateLevelAll:
    call calculateLevel(player, False, False, False) from _call_calculateLevel_12
    call calculateLevel(imp , False, False, False) from _call_calculateLevel_13
    call calculateLevel(slimePrincess, False, False, False) from _call_calculateLevel_14
    call calculateLevel(slime, False, False, False) from _call_calculateLevel_15
    return

label calculateLevel(character, showPopup=True, showMessage=True, playAudio=True):
    define startMaxHP = 0
    define INCREASEMULTIPLIER = 1.05
    define XPRequirement = 100
    define targetLevel = 0

    $ startMaxHP = character.maxHealth
    $ XPRequirement = 100
    $ targetLevel = 0


    # while 10 >= targetLevel:
    while character.XP >= XPRequirement:
        $ targetLevel += 1
        $ character.oldLevelBottom = character.levelBottom
        $ character.levelBottom = XPRequirement
        $ XPRequirement = mathFloor(XPRequirement * INCREASEMULTIPLIER + 100)

    $ character.oldLevelTop = character.levelTop
    $ character.levelTop = XPRequirement


    $ renpy.restart_interaction()
    $ character.profile.XPBar.startResetDelay = xpBarMoveSpeed

    if (targetLevel == 0): 
        $ character.levelBottom = 0

    if showMessage or showPopup:
        if(character.level < targetLevel):
            $ character.SP += 1
            $ character.level = targetLevel

            $ randomPopupXpos = (rand(0, 10) / 100)
            $ randomPopupYPos = (rand(20, 30) / 100)

            if character.profile.pageId == "player":
                $ startPlayerResetting = True
                $ playerXPBar = 100

            else:
                $ startEnemyResetting = True
                $ enemyXPBar = 100

            # $ distance = character.levelTop - (currentEnemy.XP + 1 - currentEnemy.levelBottom + 1) / (currentEnemy.levelTop + 1 - currentEnemy.levelBottom + 1) * 100
            # $ proportion = distance / (character.XP - ((currentEnemy.XP + 1 - currentEnemy.levelBottom + 1) / (currentEnemy.levelTop + 1 - currentEnemy.levelBottom + 1) * 100))

            if showPopup:
                hide screen GainedLevelPopup
                show screen GainedLevelPopup(targetLevel, randomPopupXpos, randomPopupYPos) 

            if playAudio:
                play audio recovery3

            if showMessage:
                "{color=[character.profile.color]}[character.profile.name] {/color}leveled up to level{color=#0f0} [targetLevel]{/color}!"

        if(character.level > targetLevel):
            $ character.level = targetLevel

            $ randomPopupXpos = (rand(40, 70) / 100)
            $ randomPopupYPos = (rand(35, 45) / 100)

            if character.profile.pageId == "player":
                $ startPlayerResetting = True
                $ playerXPBar = 0

            else:
                $ startEnemyResetting = True
                $ enemyXPBar = 0

            if showPopup:
                hide screen LostLevelPopup
                show screen LostLevelPopup(targetLevel, randomPopupXpos, randomPopupYPos) 

            if playAudio:
                play audio down

            if showMessage:
                "{color=[character.profile.color]}[character.profile.name] {/color}leveled down to level{color=#f00} [targetLevel]{/color}..."
        
    $ character.level = targetLevel

    $ character.maxHealth = round(character.baseMaxHealth * mathPow(1.1, character.level)) + character.inventory.armor.health
    $ character.attack = round(character.baseAttack * mathPow(1.1 , character.level)) + character.inventory.weapon.attack
    $ character.maxSP = character.level + 3

    $ character.health += mathMax(character.maxHealth - startMaxHP, 0)

    call recalculateCaps(character) from _call_recalculateCaps_6
    return

label unlockArmor(recipient, armor, message=True):
    if armor in player.inventory.unlockedArmors:
        
        if message:
            "You already have this piece of armor..."
        
        return "Duplicate"

    $ player.inventory.unlockedArmors.append(armor)
    if message:
        "{color=#0f0}You got [armor.name]!"
    return "Ok"

# 0 merch
# 1 skye
# 2 slimep
label unlockPfp(id):
    if id == 0:
        play audio item1
        $ game.pfp.merchantUnlocked = True
        "{size=50}\[{color=#9575CD}Merchant pfp unlocked!{/color}]"
        "{size=50} {color=#ff0} {a=https://i.ibb.co/PxLQHGF/ad8ba1fed603656573548848b4032a08-2.png}Click here to download the PFP"
        hide merchantPFP with myDissolve

    if id == 1:
        play audio item1
        $ game.pfp.slimeUnlocked = True
        "{size=50}\[{color=#9575CD}Skye pfp unlocked!{/color}]"
        "{size=50}{a=https://i.ibb.co/bmYqnT2/Slimed.jpg}Click here to download the PFP"
        hide slimePFP with myDissolve

    if id == 2:
        play audio item1
        $ game.pfp.slimePrincessUnlocked = True
        "{size=50}\[{color=#9575CD}Slime princess pfp unlocked!{/color}]"
        "{size=50}{a=https://i.ibb.co/59Dcrfg/slimep.png}Click here to download the PFP"
        hide slimePrincessPFP with myDissolve

    return

label completeObjective(p_objective):
    play audio success2
    $ p_objective.completed = True
    hide screen objectiveComplete
    show screen objectiveComplete
    return

# 0 = poison
# 1 = slimecurse
# 2 = slimep
# 3 = charmed
# 4 = debt

label gainStatusEffect(type, intensity=0):
    if type == 0:
        play audio poison
        $ player.conditions.poisoned = intensity
        "{size=50}\[{color=#f00}Status effect gained: Poisoned{/color}]"
        show screen statusEffects

    if type == 1:
        play audio dark1
        $ player.conditions.slimePet = True
        show screen statusEffects
        '{size=50}\[{color=#f00}Status effect gained: Weak to mouths{/color}]'

    if type == 2:
        play audio dark1
        $ player.conditions.princessServant = True
        show screen statusEffects
        '{size=50}\[{color=#f00}Status effect gained: Slime princess\'s servant{/color}]'

    if type == 4:
        play audio dark1
        $ player.conditions.casinoDebt = True
        show screen statusEffects
        "{size=50}\[{color=#f00}Status effect gained: casino girls' curse{/color}]"
    return

label clearStatusEffect(type):
    if type == 0:
        play audio recovery3
        if player.conditions.poisoned == 0:
            $ player.conditions.poisoned = 0
            "{color=#0f0} \[Status effect removed: Poison\]"
            "{color=#0f0} \[Even though you weren't poisoned in the first place...\]"
            show screen statusEffects
        else:
            $ player.conditions.poisoned = 0
            "{color=#0f0} \[Status effect removed: Poison\]"
            show screen statusEffects

    if type == 1:
        play audio recovery3
        $ player.conditions.slimePet = False
        show screen statusEffects
        "{color=#0f0} \[Status effect removed: Weak to mouths\]"

    if type == 2:
        play audio recovery3
        $ player.conditions.princessServant = False
        show screen statusEffects
        "{color=#0f0} \[Status effect removed: Slime princess\'s servant\]"

    if type == 4:
        play audio recovery3
        $ player.conditions.casinoDebt = False
        show screen statusEffects
        "{color=#0f0} \[Status effect removed: Casino girls\' curse\]"
    return