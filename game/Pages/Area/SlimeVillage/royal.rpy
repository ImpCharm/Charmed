label slimevillage_royal:


    if(game.objective[2].completionFlags[0] == True
        and game.objective[2].completionFlags[1] == True
        and game.objective[2].completionFlags[2] == False):
            scene slimevillage_royal with myDissolve
            $ game.objective[2].completionFlags[2] = True
            "While walking into slime village's royal district, a lesser slime approaches you."
            "[anonTalk('#78a6e4')]" "Excuse me."
            show lesserslime_assistant with myDissolve
            "[anonTalk('#78a6e4', 'The slime helper')]" "Hello, human. The princess has sent me to notify you of your meeting."
            "[anonTalk('#78a6e4', 'The slime helper')]" "The princess has scheduled an appointment with you. She is currently waiting for your arrival."
            "[anonTalk('#78a6e4', 'The slime helper')]" "Please take as much time as you need."
            "[anonTalk('#78a6e4', 'The slime helper')]" "..."
            "[anonTalk('#78a6e4', 'The slime helper')]" "I hope you can resolve this peacefully, human."
            "[anonTalk('#78a6e4', 'The slime helper')]" "Goodbye now. Please enter the queen's castle once you're ready to meet the princess."
            show lesserslime_assistant at slideInLeft(0.5, 2.0, 2)
            "The lesser slime walks away silently..."

    scene slimevillage_royal with myDissolve

    if (game.objective[2].completionFlags[2] == True 
        and game.objective[2].completed == False):
        $ highlight = getHighlightText("Slime queen's castle")
    else:
        $ highlight = "Slime queen's castle"

    if(game.objective[2].completed == True and game.objective[3].completionFlags[0] == False):
        $ game.objective[3].completionFlags[0] = True
        if player.conditions.princessServant:
            show imp_boobhand with myDissolve
            "[imp]" "Hey [pronouns.mister]~"
            "[imp]" "Looks like you two had fun huh~?"
            "[imp]" "Kufufu~ Don't worry, I won't tell anyone~"
            "[imp]" "And on the bright side, you found a place to find your magic energy!"
            "[imp]" "She mentioned something about the alraune tree, right?"
            "[imp]" "You should be able to find it in the forest~"
            "[imp]" "How about you explore it and I'll tell you when we're near the entrance!"
            hide imp_boobhand with myDissolve
            show imp_stand with myDissolve
            "[imp]" "Take it easy, okay? You did well back there~ There's no shame in resting a little bit~! There's an inn in the central district!"
            hide imp_stand with myDissolve
        else:
            show imp_happyface with myDissolve
            "[imp]" "Hey! [pronouns.mister]!"
            "[imp]" "Good job back there! I knew you could do it!"
            show imp_sadface with myDissolve
            hide imp_happyface with myDissolve
            "[imp]" "I'm sure she must have been tough on you..."
            "[imp]" "Here, let me help~"
            play audio recovery3
            call whitePyu from _call_whitePyu_5
            call restore(player) from _call_restore_7
            "{color=#0f0} You restored all your health!"
            hide imp_sadface with myDissolve
            show imp_boobhand with myDissolve
            "[imp]" "There~ Much better, right?"
            "[imp]" "The princess said something about the alraune tree, right?"
            "[imp]" "You should be able to find it in the forest~ Let's go there when you're ready, okay?"
            hide imp_boobhand with myDissolve

    menu:
        "[highlight]":
            call move("slimevillage_castle") from _call_move_4
        "Traveling merchant":
            call move("slimevillage_shop") from _call_move_9
        "Central district":
            call move("slimevillage_central") from _call_move_5

    jump slimevillage_royal