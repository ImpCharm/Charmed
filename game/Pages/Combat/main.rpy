label fight_intro:
    "You encounter [currentEnemy.profile.name]!"
    return

label sexAttack(attacker, defender, type):
    define damage = 0
    define multiplier = 1
    define arousalMultiplier = 1
    $ multiplier = 1
    
    if(player.conditions.horny):
        $ multiplier *= 2

    if(player.conditions.casinoDebt):
        $ arousalMultiplier *= 1.5

    if(type == sexTypes.feet):
        call damageCalculation(attacker.attack * multiplier) from _call_damageCalculation
        $ damage = _return
        $ defender.arousal += (defender.weaknesses.feet) * arousalMultiplier
        $ defender.weaknesses.feet += 1

    elif(type == sexTypes.blowjob):
        call damageCalculation(attacker.attack * multiplier) from _call_damageCalculation_1
        $ damage = _return 
        $ defender.arousal += (defender.weaknesses.blowjob) * arousalMultiplier
        $ defender.weaknesses.blowjob += 1

    elif(type == sexTypes.kiss):
        call damageCalculation(attacker.attack * multiplier) from _call_damageCalculation_2
        $ damage = _return 
        $ defender.arousal += (defender.weaknesses.kiss) * arousalMultiplier
        $ defender.weaknesses.kiss += 1

    elif(type == sexTypes.sex):
        call damageCalculation(attacker.attack * multiplier) from _call_damageCalculation_3
        $ damage = _return 
        $ defender.arousal += (defender.weaknesses.sex) * arousalMultiplier
        $ defender.weaknesses.sex += 1

    elif(type == sexTypes.paizuri):
        call damageCalculation(attacker.attack * multiplier) from _call_damageCalculation_4
        $ damage = _return 
        $ defender.arousal += (defender.weaknesses.paizuri) * arousalMultiplier
        $ defender.weaknesses.paizuri += 1

    elif(type == sexTypes.armpits):
        call damageCalculation(attacker.attack * multiplier) from _call_damageCalculation_5
        $ damage = _return 
        $ defender.arousal += (defender.weaknesses.armpits) * arousalMultiplier
        $ defender.weaknesses.armpits += 1

    elif(type == sexTypes.butt):
        call damageCalculation(attacker.attack * multiplier) from _call_damageCalculation_6
        $ damage = _return 
        $ defender.arousal += (defender.weaknesses.butt) * arousalMultiplier
        $ defender.weaknesses.butt += 1

    call updateArousal(defender) from _call_updateArousal

    if defender.profile.lastAction == "Defend":
        $ damage = math.floor(damage / 2)

    return damage

label updateArousal(character=player):
    call recalculateCaps from _call_recalculateCaps_3
    if character.arousal >= 100:
        if character.conditions.horny == False:
            play audio pollen
            show screen statusEffects()
            show screen fuzzy

        $ character.conditions.horny = True
        $ character.arousal = 100
        $ arousalBarText = "Arousal: {color=#f00}Charmed{/color}"
        show screen fuzzy
        $ xpBarMoveSpeed = 3

    else:
        $ character.conditions.horny = False
        $ arousalBarText = "Arousal: " + str(player.arousal) + "/100"
        hide screen fuzzy
        $ xpBarMoveSpeed = 6
    
    return

label normalAttack(attacker, defender):
    # call popup(defender.profile.name + "'s HP - " + str(attacker.attack + attacker.inventory.weapon.attack))
    call damageCalculation(attacker.attack + attacker.inventory.weapon.attack) from _call_damageCalculation_7 
    return _return

label damageCalculation(attack):
    return attack

label calculateDamage:
    call sexAttack(currentEnemy, player, attackType) from _call_sexAttack
    define damage = _return
    return
    # $ player.health -= damage

label divideDamage(damage, divideBy):
    return round(damage / divideBy)

label partialDamagePlayer(damage, divideBy):
    call divideDamage(damage, divideBy) from _call_divideDamage
    $ player.health -= _return
    call recalculateCaps(player) from _call_recalculateCaps
    return

label damagePlayer(damage):
    # call popup("Your HP - " + str(damage))
    $ player.health -= damage
    call recalculateCaps(player) from _call_recalculateCaps_1
    return

label increaseArousal(gainer, amount):
    $ gainer.arousal += amount
    return

label levelDrain(loser, gainer, XPToDrain, showPopup=True, showMessage=True, playAudio=True):

    $ XPToDrain = round(XPToDrain)

    if loser.XP == 1:
        call expression gainer.profile.dryPage from _call_expression
        
    if showPopup:
        $ randomPopupXpos = (rand(40, 70) / 100)
        $ randomPopupYPos = (rand(20, 30) / 100)
        hide screen LostXPPopup
        show screen LostXPPopup(XPToDrain, randomPopupXpos, randomPopupYPos)

    if playAudio:
        play audio cold5

    if showMessage:
        "{color=[loser.profile.color]}[loser.profile.name]{/color} lost {color=#f00}[XPToDrain] XP {/color} to {color=[gainer.profile.color]}[gainer.profile.name] {/color}."

    if(loser.XP - XPToDrain <= 0):
        $ XPToDrain = loser.XP - 1

    $ loser.XP -= XPToDrain
    $ gainer.XP += XPToDrain
    
    call calculateLevel(gainer, showPopup, showMessage, playAudio) from _call_calculateLevel_1
    call calculateLevel(loser, showPopup, showMessage, playAudio) from _call_calculateLevel_2
    return

label pyupyu:
    play audio ejaculationsoundgooutshort10
    call whitePyu from _call_whitePyu
    pause 0.2
    call whitePyu from _call_whitePyu_1
    "{size=50}{i}Pyu pyuu~{/i}{/size}"
    return

label whitePyu:
    hide fullPng with Fade(.1, .3, .2, color="#fff")
    return

label restrainDrain:
    $ player.arousal += player.weaknesses.sex
    $ player.weaknesses.sex += 1
    call updateArousal(player) from _call_updateArousal_1
    call levelDrain(player, currentEnemy, ((player.levelTop - player.levelBottom) * 0.10), True, False) from _call_levelDrain_4
    return

label restrainDrainNgh:
    $ player.arousal += player.weaknesses.sex
    $ player.weaknesses.sex += 1
    return

label enterRestraint:
    $ player.conditions.restrained = True
    show screen restrain
    $ preferences.text_cps = 0
    return

label escapeRestraint:
    $ player.conditions.restrained = False
    hide screen restrain with myDissolve
    $ preferences.text_cps = 35
    return

label showRestrainBall1:
    $ restrainBallX = (rand(10, 70) / 100)
    $ restrainBallY = (rand(20, 30) / 100)
    show screen restrainBtn1(restrainBallX, restrainBallY) with myDissolve

label showRestrainBall2:
    $ restrainBallX = (rand(10, 70) / 100)
    $ restrainBallY = (rand(20, 30) / 100)
    show screen restrainBtn2(restrainBallX, restrainBallY) with myDissolve

label showRestrainBall3:
    $ restrainBallX = (rand(10, 70) / 100)
    $ restrainBallY = (rand(20, 30) / 100)
    show screen restrainBtn3(restrainBallX, restrainBallY) with myDissolve
