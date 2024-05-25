
label imp_talk:
    call hideAllImp from _call_hideAllImp_5
    show imp_boobhand with myDissolve
    if (game.objective[1].completed == False 
        and game.objective[1].completionFlags[1] == False 
        and isTalking == False):
            if player.level > 4:
                "[imp]" "Hey hey, you've been fighting well, good job~! Are you ready to head into the cave?"
                "[imp]" "It's at the end of the forest, you should reach it pretty easily as long as you just head north~"
            else:
                "[imp]" "Hey hey~ You should go find some more enemies to defeat~ Let's go inside the cave once you're level 5, okay?"
            
            return

    if isTalking == False:
        "[imp]" "Oh hey~!"
        "[imp]" "What's up, [pronouns.mister]~? Do you need help with anything?"
    else:
        "[imp]" "Have you got any other questions~?"
    $ isTalking = True
    menu:
        "About Lulu":
            call imp_talk_about from _call_imp_talk_about
        "Help":
            call imp_talk_help from _call_imp_talk_help
        "Bye":
            return
    
    jump imp_talk

label imp_talk_about:
    "[imp]" "Oh? You want to know more about me?"
    "[imp]" "Weeell~ I'm a pretty simple imp, just like most other monster girls~"
    "[imp]" "As for why I don't attack you... Well..."
    hide imp_boobhand with myDissolve
    call hideAllImp from _call_hideAllImp_6
    show imp_happyface with myDissolve
    "[imp]" "It's simple really~! I just don't feel the need, you know~?"
    hide imp_happyface with myDissolve
    show imp_sadface with myDissolve
    "[imp]" "It may be hard to imagine, but draining people all day gets pretty tiring, you know?"
    hide imp_sadface with myDissolve
    show imp_stand with myDissolve
    "[imp]" "Heck, some imps charge money if you want to be drained, can you believe that~?"
    "[imp]" "I've been told it's very good though and that you should totally look into it~ ♡"
    hide imp_stand with myDissolve
    show imp_boobhand with myDissolve
    "[imp]" "Fufu, anyway~"
    return

label imp_talk_help:
    "[imp]" "Oh, you need help with something? That's okay~! Ask away~!"
    menu imp_talk_help_menu:
        "About combat":
            "[imp]" "Oh, you've got some more questions about combat?"
            "[imp]" "I suppose there are some aspects I haven't really explained yet~"
            call imp_talk_help_combat from _call_imp_talk_help_combat
        
        "What do I do now?":
            "[imp]" "What do you do now~? Hmm, let's see~"
            if (game.objective[2].completed == True):
                "[imp]" "Well... You asked the slimeprincess for magic power... But it doesn't seem like they have enough nectar to help you get home."
                "[imp]" "I'm sure the alraunes might be able to help you though~"
                "[imp]" "Hmm but..."
                "[imp]" "Maybe it's best if we wait a while before we go there... Another Imp I know needs some more time to prepare..."
            elif (game.objective[2].completed == False 
                and game.objective[2].completionFlags[2] == True):
                    "[imp]" "Oh gosh~ You really got a meeting with the princess of the slimes huh~? How exciting~"
                    "[imp]" "I'll be watching you fight, okay~? She's pretty strong so don't go in unprepared~!"
                    "[imp]" "You'll find her in slime village's royal district~"
            elif (game.objective[2].completionFlags[2] == False 
                and game.objective[2].completionFlags[1] == True):
                    "[imp]" "Weeell~ I think that slime just gave you a chance at meeting the slime princess~"
                    "[imp]" "You should be grateful to that slime for helping you get inside~!"
                    "[imp]" "I told you, not all monster girls are out to get you~!"
                    "[imp]" "...most of them are... But not all of them~!"
                    "[imp]" "Fufu~ Anyway~! Try and enter slime village in the caves, okay~?"
            elif(game.objective[2].completionFlags[1] == False 
                and game.objective[2].completionFlags[0] == True):
                    "[imp]" "Well... It doesn't look like you're allowed inside slime village..."
                    "[imp]" "But... I've heard noises coming from the deepest parts of the cave, I'm sure if you go there you can find a solution~!"
            elif(game.objective[2].completionFlags[0] == False 
            and game.objective[1].completionFlags[1] == True):
                    "[imp]" "Well, here we are in the cave~ Let's try and find slime village so they can help us, okay~?"
            elif(game.objective[1].completionFlags[1] == False 
                and game.objective[1].completionFlags[0] == True):
                    "[imp]" "Before we enter the cave, you should level up to at least level 5~ Those slimes are pretty strong, you know~?"
            else:
                "[imp]" "Hehe~ I think you should just explore the forest for now~"
                "[imp]" "After we're done, we can enter the cave where the slimes live~ They might be able to help us~!"

        "Back":
            return

    jump imp_talk_help_menu

label imp_talk_help_combat:
    menu:
        "Restraining":
            "[imp]" "Ah~ Restraining~"
            "[imp]" "Kufufu~ It's any monster girl's favorite way of draining, trust me~"
            "[imp]" "That's because of how dangerous it is though, you should avoid being restrained at all cost~!"
            "[imp]" "If you ever notice an enemy being suspicious or planning an attack, make sure you defend when it's your turn, okay~?"
            "[imp]" "But if you ever DO end up restrained, try and struggle your way out of it, okay~?"
            "[imp]" "If you manage your SP accordingly, you'll be fine, I promise~"
        "Arousal":
            "[imp]" "Oooh arousal~"
            "[imp]" "It's pretty simple really~ Whenever you get hit, your weakness for that type of attack increases"
            "[imp]" "Additionally, your arousal also increases by however much your weakness for that attack type is!"
            "[imp]" "Arousal can be cleared pretty easily~ Just rest in the inn and you'll be fine. Weaknesses, on the other hand aren't as easy..."
            "[imp]" "You have to use holy magic to get them restored... I don't like holy magic that much so I can't do it for you..."
            "[imp]" "But~! There's a pond powered by the alraune tree in the forest~"
            "[imp]" "I think the path might be covered in vines but if you look well enough you might be able to find it~"
        "Equipment":
            "[imp]" "Oooh equipment~?"
            "[imp]" "It's really simple~! Armor increases your max HP and weapons increase your attack~!"
            "[imp]" "They can be equipped by opening the menu and then selecting the piece you'd like to equip"
            "[imp]" "Oh~! And don't forget to equip your items after buying them!"
        "Nevermind":
            return

    jump imp_talk_help_combat
