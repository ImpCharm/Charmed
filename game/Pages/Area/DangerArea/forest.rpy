label forest_1:
    $ dangerAreaDepth = 1
    call areaMarker("forest") from _call_areaMarker_4
    scene forest_dynamic with myDissolve

    if(
    game.objective[0].completed == True
    and game.objective[1].completionFlags[0] == False
    and game.objective[1].completionFlags[1] == False
    and game.objective[1].completed == False):
        $ game.objective[1].completionFlags[0] = True
        "As you walk through the forest, you look around to find Lulu..."
        "[imp]" "Hey [pronouns.mister]~! Over here!"
        pause 1.0
        call cutscene_succubus_forest_1 from _call_cutscene_succubus_forest_1

    menu:
        "Go deeper":
            call randomForestEvent(2) from _call_randomForestEvent_1
        "Wander around":
            call randomForestEvent(1) from _call_randomForestEvent
        "Visit Lulu" if game.objective[0].completed == True:
            call imp_talk from _call_imp_talk_1
        "Enter town":
            jump town_central
    jump forest_1

label forest_2:
    $ dangerAreaDepth = 2
    call areaMarker("forest") from _call_areaMarker_5
    scene forest_dynamic with myDissolve
    menu:
        "Go deeper":
            call randomForestEvent(3) from _call_randomForestEvent_4
        "Wander around":
            call randomForestEvent(2) from _call_randomForestEvent_2
        "Hidden path" if player.level > 5:
            "There's a path leading out of the forest here..."
            "It seems to lead out of the village, it's blocked by leaves though..."
            "There seems to be another path branching out from this one, leading to a small pond"
            menu:
                "Small pond":
                    call forest_pond from _call_forest_pond
                "Back":
                    pass
        "Head towards town":
            call randomForestEvent(1) from _call_randomForestEvent_3
    jump forest_2
    
label forest_3:
    $ dangerAreaDepth = 3
    call areaMarker("forest") from _call_areaMarker_6
    scene forest_dynamic with myDissolve

    if (game.objective[0].completed == True
    and game.objective[1].completionFlags[0] == True
    and game.objective[1].completionFlags[1] == False
    and game.objective[1].completed == False
    and player.level > 4):
        call cutscene_succubus_forest_2 from _call_cutscene_succubus_forest_2
        
    if (game.objective[1].completionFlags[1] == True 
        and game.objective[1].completed == False):
        $ highlight = getHighlightText("Enter cave")
    else:
        $ highlight = "Cave"

    scene forest_dynamic with myDissolve

    menu:
        "[highlight]":
            call cave_1 from _call_cave_1
        "Wander around":
            call randomForestEvent(3) from _call_randomForestEvent_5
        "Wooden shack" if rand(0,5) == 3 and slime.profile.name == 'Skye':
            call forest_woodenShack from _call_forest_woodenShack
        "Head towards town":
            call randomForestEvent(2) from _call_randomForestEvent_6
    jump forest_3

default enoughDonations = False
default amountToDonate = 0
default donatedAmount = 0
label forest_pond:
    if game.foundPond == False:
        "You decide to explore the forest a little deeper and head towards the pond."
        show pond_dynamic with myDissolve
        "...After walking for a while you end up at the pond. There's a sign next to the pond."
        "\"Those who donate to the lady of the pond will have their purity restored\""
        "There's a small box near the pond as well. It looks like you can deposit gold in there..."
    show pond_dynamic with myDissolve
    $ game.foundPond = True
    menu:
        "Donate":
            "How much gold will you donate?"
            menu:
                "10":
                    $ amountToDonate = 10
                "25":
                    $ amountToDonate = 25
                "50":
                    $ amountToDonate = 50
                "Back":
                    jump forest_pond
            
            if player.money >= amountToDonate:
                "You donate [amountToDonate] gold before getting in the water."
                $ donatedAmount += amountToDonate
                pause 3
                "..."
                $ enoughDonations = donatedAmount + rand(1, 90) > 70
                if(enoughDonations):
                    "You feel the water get warmer as your lust decreases."
                    "{color=#0f0}Arousal and weaknesses restored!{/color}"
                    call cleanseSoul from _call_cleanseSoul
                    $ donatedAmount = 0
            else:
                "You don't have enough money..."
        "Back":
            return
    jump forest_pond            

label forest_woodenShack:
    scene shrine with myDissolve
    if not game.slimeHouseUnlocked:
        "You see a wooden shack nearby..."
        "It looks old, yet still in good condition..."
        "Go inside?"
    menu:
        "Go inside":
            scene shrine_inside with myDissolve
            if not game.slimeHouseUnlocked:
                "As you try to go inside you find the floor sticky with slime..."
                "...You hear the drooping of slime nearby. It sounds like there's someone else here..."
                "..."
                "...Suddenly, you hear a familiar voice calling out to you."
                "[slime]" "Hey hey~"
                show slime_main with myDissolve
                "[slime]""It's you again~!"
                "[slime]""Welcome to my little house, [pronouns.mister]~"
                "[slime]""I found this little shack in the forest and decided to make it my own~ Pretty cool, right?"
                "[slime]""The best part is that it's pretty secluded so most slimes don't even know this spot exists~!"
                "[slime]""Anyway, what are you doing here? Do you want to talk about something?"
            else:
                "[slime]" "Hey again, [pronouns.mister]~"

            $ game.slimeHouseUnlocked = True
            call forest_woodenShack_inside from _call_forest_woodenShack_inside
            return

        "Don't":
            "You decide not to."
            return         

label forest_woodenShack_inside:
    menu:
        "Talk to [slime.profile.name]":
            call slime_talk from _call_slime_talk
        "Leave":
            "[slime]" "Aww already~? Alright then~"
            "[slime]" "I'll see you in the forest, [pronouns.mister]~"

    jump forest_woodenShack_inside

define randomNumber = 0
define isWandering = False

label randomForestEvent(targetDepth):
    $ randomNumber = rand(1, 8)
    if (dangerAreaDepth == targetDepth):
            $ randomNumber = rand(1, 3 )
            $ isWandering = True
            pause 0.1
    $ renpy.block_rollback()

    if randomNumber == 1:
        # shopkeeper event if its evening
        if getTimePeriod("evening"):
            if game.shopUnlocked and shopKeeperStatus != "walking" and player.money > 30 and ((player.health / player.maxHealth < 1) or (player.arousal > 0)):
                call event_forest_shopkeeper from _call_event_forest_shopkeeper
            else:
                call forest_wander from _call_forest_wander

        # otherwise do the slime choice event
        elif (player.level > 4 and game.levelDrainSlimeEvent):
                $ renpy.block_rollback()
                call restore(slime) from _call_restore
                call forest_slime_choice from _call_forest_slime_choice
                stop music fadeout 3
        else:
            call forest_wander from _call_forest_wander_1
            
    elif randomNumber == 2:
        if(player.level < 5):
            call enterCombat(
                Character(
                    9, 10, 2, 50, 200,  
                    Profile("The lesser slime", "#1e88e5", "lesserslime",
                    "Lesser slimes are slimes fighting for the slime princess's army. They're fairly weak and don't have a strong work ethic, usually trying to slack off at every opertunity. Despite their low energy, they're very faithful towards their princess, doing almost anything just to drain some more XP to feed her. \n \n Their ways of draining are similar to most slimes. Using their body parts to pleasure humans until they cum inside their core."
                    ),
                    Conditions()
                )
            ) from _call_enterCombat_1
        else:
            call enterCombat(
            Character(
                mathMin(player.level, 10) + rand(5, 8), 10, 2, 50, rand(150, mathMin(800, player.XP)),  
                Profile("The lesser slime", "#1e88e5", "lesserslime",
                "Lesser slimes are slimes fighting for the slime princess's army. They're fairly weak and don't have a strong work ethic, usually trying to slack off at every opertunity. Despite their low energy, they're very faithful towards their princess, doing almost anything just to drain some more XP to feed her. \n \n Their ways of draining are similar to most slimes. Using their body parts to pleasure humans until they cum inside their core."
                ),
                Conditions()
            )
        ) from _call_enterCombat_2  

    elif randomNumber == 3:
            if((player.level > 4 and slime.health > 1 and slime.winCount == 0) or (player.level > 8 and slime.health > 1 and slime.winCount > 0)):
                call enterCombat(slime) from _call_enterCombat_4
            else:
                call forest_wander from _call_forest_wander_2
             
    
    $ renpy.block_rollback()
    
    call move("forest_" + str(targetDepth)) from _call_move_2

label forest_wander:
    if isWandering:
        call randomForestEvent(targetDepth) from _call_randomForestEvent_7
    return

