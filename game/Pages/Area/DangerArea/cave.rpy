label cave_1:
    $ dangerAreaDepth = 1

    if(game.objective[1].completionFlags[1] == False 
        or game.objective[0].completed == False):
        scene cave with myDissolve
        "This area seems very dangerous. It'd be smart to go back for now..."
        "Let's gain some levels and then come back here."
        menu:
            "Back to forest":
                call forest_3 from _call_forest_3

    call areaMarker("cave") from _call_areaMarker

    if (game.objective[1].completed == False
        and game.objective[2].completionFlags[0] == False 
        and game.objective[2].completed == False):
            call cutscene_succubus_cave_1 from _call_cutscene_succubus_cave_1

    scene cave with myDissolve

    menu:
        "Go deeper":
            call randomCaveEvent(2) from _call_randomCaveEvent_1
        "Wander around" if not (game.objective[2].completionFlags[0] == False or dangerAreaDepth == 2):
            call randomCaveEvent(1) from _call_randomCaveEvent
        "Visit Lulu":
            call imp_talk from _call_imp_talk
        "Leave the cave":
            call forest_3 from _call_forest_3_1
    jump cave_1

label cave_2:
    $ dangerAreaDepth = 2

    call areaMarker("cave") from _call_areaMarker_1

    if (game.objective[2].completionFlags[0] == False):
        call cutscene_slimeguard_cave_0 from _call_cutscene_slimeguard_cave_0

    scene cave
    show lesserslime_main at lesserslimeguardcave2 with myDissolve


    if (game.objective[2].completed == False):
        $ highlight = getHighlightText("Slime village")
    else:
        $ highlight = "Slime village"


    menu:
        "Go deeper":
            call randomCaveEvent(3) from _call_randomCaveEvent_3
        "[highlight]":
            if (game.objective[2].completionFlags[2] == False) and game.objective[2].completionFlags[1] == False:
                "{size=*1.5}{color=#1e88e5}The slime guard{/color}{/size}" "Ah... Sorry but you can't pass through without a good reason... Princess's orders..."
                jump cave_2

            if cave4welcome:
                "{size=*1.5}{color=#1e88e5}The slime guard{/color}{/size}" "Hmm... a human... no sorry..."
                "{size=*1.5}{color=#1e88e5}The slime guard{/color}{/size}" "..."
                "{size=*1.5}{color=#1e88e5}The slime guard{/color}{/size}" "...Wait, you must be..."
                "{size=*1.5}{color=#1e88e5}The slime guard{/color}{/size}" "Ah... I understand... The princess wanted to speak to you..."
                "{size=*1.5}{color=#1e88e5}The slime guard{/color}{/size}" "Please enjoy yourself at slime village..."
                $ cave4welcome = False
            else:
                "{size=*1.5}{color=#1e88e5}The slime guard{/color}{/size}" "Ah... It's you..."
                "{size=*1.5}{color=#1e88e5}The slime guard{/color}{/size}" "Please enjoy yourself at slime village..."
            call slimevillage_central from _call_slimevillage_central
        "Head back":
            call randomCaveEvent(1) from _call_randomCaveEvent_2
    jump cave_2

label cave_3:
    $ dangerAreaDepth = 3

    call areaMarker("cave") from _call_areaMarker_2

    scene cave with myDissolve

    menu:
        "Go deeper":
            call randomCaveEvent(4) from _call_randomCaveEvent_6
        "Wander around":
            call randomCaveEvent(3) from _call_randomCaveEvent_4
        "Head back":
            call randomCaveEvent(2) from _call_randomCaveEvent_5
    jump cave_3

label cave_4:
    $ dangerAreaDepth = 4

    call areaMarker("cave") from _call_areaMarker_3

    scene cave with myDissolve

    if(game.objective[2].completionFlags[1] == False
        and game.objective[2].completionFlags[0] == True):
            call cutscene_slimefight_cave_0 from _call_cutscene_slimefight_cave_0

    menu:
        "Wander around":
            call randomCaveEvent(4) from _call_randomCaveEvent_7
        "Head back":
            call randomCaveEvent(3) from _call_randomCaveEvent_8
    jump cave_3

label randomCaveEvent(targetDepth):
    $ randomNumber = rand(1, 15)

    if(game.objective[2].completionFlags[0] == False or dangerAreaDepth == 2):
            call move("cave_" + str(targetDepth)) from _call_move
            return

    if (dangerAreaDepth == targetDepth):
            $ randomNumber = rand(1, 10)
            $ isWandering = True

    $ renpy.block_rollback()

    if randomNumber == 1 or randomNumber == 2:
        if(game.objective[2].completionFlags[1] == False 
            and game.objective[2].completionFlags[0] == True):
                "You hear noises coming from the back of the cave..."
        else:
            call cave_wander from _call_cave_wander
            
    elif randomNumber == 3 or randomNumber == 4:
        call enterCombat(
            Character(
                    (mathMin(player.level, 10) + rand(5, 12)), 10, 2, 50, (rand(500, mathMax(503, mathMin(1000, player.XP)))),  
                    Profile("The slime soldier", "#1e88e5", "lesserslime",
                    "Lesser slimes are slimes fighting for the slime princess's army. Most are fairly weak but these specific types of lesser slimes are specifically trained to defend the princess. They would do anything to show their devotion to their princess. \n \n Their ways of draining are similar to most slimes. Using their body parts to pleasure humans until they cum inside their core."
                    ),
                    Conditions()
                )) from _call_enterCombat

    elif randomNumber == 5 or randomNumber == 6 or randomNumber == 7:
        if(merchant.profile.favor > 0):
            call cave_wander from _call_cave_wander_1
        elif(player.conditions.poisoned > 0 and player.money > 12 and player.XP > 1100 and getTimePeriod('night') == False):
            call event_cave_merchant_scam from _call_event_cave_merchant_scam
        else:
            call cave_wander from _call_cave_wander_2
        
    elif randomNumber == 8:
        if(merchant.profile.favor != 0):
            call cave_wander from _call_cave_wander_3

    elif randomNumber == 9:
        if(player.money > 12 and player.XP > 1100):
                if(player.conditions.poisoned > 0):
                    if getTimePeriod('night') == False:
                        call event_cave_merchant_scam from _call_event_cave_merchant_scam_1
                    else:
                        call cave_wander from _call_cave_wander_4
                else:
                    call event_cave_poison_trap from _call_event_cave_poison_trap

        else:
            call cave_wander from _call_cave_wander_5
            
    $ renpy.block_rollback()
    
    call move("cave_" + str(targetDepth)) from _call_move_1

label cave_wander:
    if isWandering:
        call randomCaveEvent(targetDepth) from _call_randomCaveEvent_9
    return

