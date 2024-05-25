label fight_player_turn:
    $ currentTurnNumber += 1
    call updateArousal(player) from _call_updateArousal_2
    call calculateLevel(player) from _call_calculateLevel_3

    if player.conditions.poisoned > 0 and currentTurnNumber > 1:
        $ attackDamage = round(player.health * 0.10)
        $ player.health -= attackDamage

        "You are poisoned!\n
        You took {color=#f77}{size=+20}[attackDamage]{/size}{/color} damage!\n
        Lasts [player.conditions.poisoned] more turns"

        $ player.conditions.poisoned -= 1

    if player.conditions.restrained:
        menu fight_player_turn_menu_restrained:
            "Struggle":
                call fight_player_struggle from _call_fight_player_struggle
            "Meditate":
                call fight_player_meditate from _call_fight_player_meditate
        
        call recalculateCapsAll from _call_recalculateCapsAll
        jump expression currentEnemy.profile.turnPage
        return
            
    else:
        menu fight_player_turn_menu:
            "Fight":
                call fight_player_fight from _call_fight_player_fight
            "Skill":
                call fight_player_skill from _call_fight_player_skill
            "Defend" if game.slimeTutoFight == False:
                call fight_player_defend from _call_fight_player_defend
            "Run" if (game.slimeTutoFight == False and currentEnemy.profile.pageId != "slimeprincess"):
                call fight_player_run from _call_fight_player_run
                return
        
        if not inCombat:
            return
            
        call recalculateCapsAll from _call_recalculateCapsAll_1
    
        if(currentEnemy.health <= 0):
            call expression currentEnemy.profile.deadPage from _call_expression_1 
            if(currentEnemy.health <= 0):
                jump fight_player_victory
                return
            else:
                return
        
        call expression currentEnemy.profile.reactionPage from _call_expression_2
        jump expression currentEnemy.profile.turnPage
        return

    return

label fight_player_struggle:
    play audio blow1
    "You struggle for freedom..."

    $ restrainPower = 70
    $ restrainEscapePower += rand(0, restrainPower)
    
    if restrainEscapePower >= 100:
        $ renpy.block_rollback()
        call escapeRestraint from _call_escapeRestraint
        call hideAllChara from _call_hideAllChara
        call expression currentEnemy.profile.hitAnimationPage from _call_expression_3
        play audio success2
        stop sound fadeout 1
        $ restrainEscapePower = 0
        "You managed to break free from the restraint!"
        return
    else:
        $ renpy.block_rollback()
        play audio failure1
        "You're [restrainEscapePower]\% free! Try again for 1 SP?"
        menu:
            "Try again" if player.SP > 0:
                $ player.SP -= 1
                jump fight_player_struggle
            "Give up":
                return
    return

label fight_player_meditate:
    "Despite the unideal conditions you rest your body..."
    $ player.SP += 3
    "You restored 3 SP"
    return

define attackDmg = 0
label fight_player_fight:
    $ player.profile.lastAction = "Fight"
    call normalAttack(player, currentEnemy) from _call_normalAttack
    play sound blow1
    $ attackDmg = _return
    $ currentEnemy.health -= attackDmg
    $ player.SP += 1
    
    call recalculateCapsAll from _call_recalculateCapsAll_2
    call expression currentEnemy.profile.hitAnimationPage from _call_expression_4
    "You slashed your sword at {size=+10}{color=[currentEnemy.profile.color]}[currentEnemy.profile.name]{/color}{/size}.\nYou dealt {color=#f77}{size=+20}[attackDmg]{/size}{/color} damage!"
    return

# player skill
    label fight_player_skill:
        $ player.profile.lastAction = "Skill"
        menu fight_player_turn_skills:
            "Check":
                "Press {color=#ff0} ESC {/color}to open the enemy profile screen"
                jump fight_player_turn_menu
            "Flail(3SP)" if player.level >= 2:
                if(player.SP >= 3):
                    $ player.SP -= 3
                    call fight_player_flail from _call_fight_player_flail
                else:
                    "You don't have enough SP..."
                    jump fight_player_skill

            "Heal(3SP)" if player.level >= 4:
                if(player.SP >= 3):
                    $ player.SP -= 3
                    call fight_player_heal from _call_fight_player_heal
                else:
                    "You don't have enough SP..."
                    jump fight_player_skill

            "Masturbate" if game.slimeTutoFight == False or debug:
                jump fight_player_masturbate

            "Cancel":
                jump fight_player_turn_menu
            
        return
    
    label fight_player_flail:
        "You flail your sword around randomly"

        call normalAttack(player, currentEnemy) from _call_normalAttack_1
        $ attackDmg = _return
        $ currentEnemy.health -= attackDmg
        play audio blow1
        call recalculateCapsAll from _call_recalculateCapsAll_3
        call expression currentEnemy.profile.hitAnimationPage from _call_expression_6

        "You dealt {color=#f77}{size=+20}[attackDmg]{/size}{/color} damage!"
        
        call normalAttack(player, currentEnemy) from _call_normalAttack_2
        $ attackDmg = _return
        $ currentEnemy.health -= attackDmg
        play audio blow1
        call recalculateCapsAll from _call_recalculateCapsAll_4
        call expression currentEnemy.profile.hitAnimationPage from _call_expression_7 
        "You dealt {color=#f77}{size=+20}[attackDmg]{/size}{/color} damage!"

        return

    label fight_player_heal:
        play audio recovery3
        call restoreHealthPartiallyMax(player, 50) from _call_restoreHealthPartiallyMax
        "You concentrated and restored some of your health!"
        return

    label fight_player_masturbate:
        menu:
            "Drain 100\% health":
                $ player.health = 0
            "Ask to be restrained" if (currentEnemy.profile.pageId == "slime" or currentEnemy.profile.pageId == "slimeprincess"):
                $ willRestrain = True
            "Stare...":
                "You stare at the enemy..."
            "Cancel":
                jump fight_player_turn_skills

        return
 
label fight_player_defend:
    "You brace yourself for the next attack"
    $ player.profile.lastAction = "Defend"
    $ player.SP += 2
    return

label fight_player_run:
    $ player.profile.lastAction = "Run"
    jump exitCombat
    return

label fight_player_victory:
    play sound item1
    stop music fadeout 3.0
    "You won!"
    $ xpGained = (currentEnemy.XP / 5)
    $ currentEnemy.lostCount += 1;
    call gainXP(player, (xpGained)) from _call_gainXP
    if player.conditions.princessServant:
        "You feel some of your XP leaving your body..."
        call levelDrain(player, slimePrincess, round(xpGained / 2)) from _call_levelDrain_27
    call gainMoney(player, (currentEnemy.money / 5)) from _call_gainMoney
    jump exitCombat
    return

label fight_player_dry:
    "How did we get here?"
    return
    
label player_dead:
    call exitCombat from _call_exitCombat_1
    call dayPass from _call_dayPass_3
    call restoreAll from _call_restoreAll_9
    call move("town_inn") from _call_move_18
    return

label player_dead_slimevillage:
    call exitCombat from _call_exitCombat_3
    call dayPass from _call_dayPass_6
    call restoreAll from _call_restoreAll_10
    call move("slimevillage_inn_dead") from _call_move_19
    return

label player_dead_slimecastle:
    call exitCombat from _call_exitCombat_4
    call dayPass from _call_dayPass_7
    call restoreAll from _call_restoreAll_11
    call move("slimevillage_castle") from _call_move_20
    return