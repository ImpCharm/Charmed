define randomDialogueInt = 0

label fight_lesserslimeguard_intro:
    "The slime princess's guard approaches!"
    show lesserslime_main
    "[currentEnemy]" "Ah... It's the human..."
    "[currentEnemy]" "Please don't hurt the princess... I'll have to take care of you now..."
    call fight_intro from _call_fight_intro_2
    jump fight_player_turn
    return

label fight_lesserslimeguard_turn:
    show lesserslime_main
    call calculateLevel(currentEnemy) from _call_calculateLevel_16

    define randomI = 0
    call random(1,100) from _call_random_3
    $ randomI = _return

    # select attack
    
    if randomI > 20 or ((player.health / player.maxHealth) * 100) > 70:
        $ attackType = sexTypes.blowjob
        call calculateDamage from _call_calculateDamage_5
        call fight_lesserslimeguard_paizuri from _call_fight_lesserslimeguard_paizuri

    else:
        $ attackType = sexTypes.blowjob
        call calculateDamage from _call_calculateDamage_6
        call fight_lesserslimeguard_footjob from _call_fight_lesserslimeguard_footjob

    
    call takeDamageText(damage) from _call_takeDamageText_1
    if player.health <= 0:
        "You're unable to resist any longer..."
        "[currentEnemy]" "Ah..? You're gonna cum..?"
        call hideAllLesserSlime from _call_hideAllLesserSlime_8
        show lesserslime_main with myDissolve
        stop music fadeout 10
        "[currentEnemy]" "..."
        "[currentEnemy]" "My princess... The human..."
        show lesserslime_main at slideInLeft(0.5, 0.2, 2)
        show slimeprincess_smug at slideInLeft(0.8, 0.1, 1)
        "[slimePrincess]" "Ohohoho~! Excellent work!"
        "[slimePrincess]" "I'll take care of [pronouns.him] now, thank you, servant!"
        "[currentEnemy]" "Thank you my princess... I love you..."
        "[slimePrincess]" "I know~ Now scram, I need to drain this pathetic hero~"
        show lesserslime_main at slideInLeft(0.2, -0.7, 2)
        $ currentEnemy = slimePrincess 
        call fight_slimeprincess_victory from _call_fight_slimeprincess_victory
        call player_dead_slimevillage from _call_player_dead_slimevillage
    
    call hideAllLesserSlime from _call_hideAllLesserSlime_9
    show lesserslime_main with myDissolve
    call fight_player_turn from _call_fight_player_turn_1
    return

# Slime attacks start

    label fight_lesserslimeguard_paizuri:
        call hideAllLesserSlime from _call_hideAllLesserSlime_10
        show lesserslime_paizuri at continuousBounce with myDissolve
        call damagePlayer(damage) from _call_damagePlayer_5
        "The slime girl comes closer and gently presses her boobs on your dick."
        $ randomDialogueInt = renpy.random.randint(0,2)
        if (randomDialogueInt == 0):
            "[currentEnemy]" "[pronouns.mister]... You're resisting way too much..."
            "[currentEnemy]" "I'm tired already, can't you just give up..?"

        elif (randomDialogueInt == 1):
            "[currentEnemy]" "Can't you just give up..?"
            "[currentEnemy]" "If you give me your levels the princess might be proud of me..."

        else:
            "[currentEnemy]" "You're so slow..."
            "[currentEnemy]" "Please just surrender already..."

        return

    label fight_lesserslimeguard_footjob:
        call hideAllLesserSlime from _call_hideAllLesserSlime_11
        show lesserslime_footjob with myDissolve
        call damagePlayer(damage) from _call_damagePlayer_6
        "The slime presses her soft, slimy soles against your cock and teases it."
        $ randomDialogueInt = renpy.random.randint(0,2)
        if (randomDialogueInt == 0):
            "[currentEnemy]" "You really are a pervert if you're enjoying this..."
            "[currentEnemy]" "Some sort of foot-freak, bleh... Whatever, cum soon please"

        elif (randomDialogueInt == 1):
            "[currentEnemy]" "I'm not gonna go easy on you... You're full of levels that our princess wants"
            "[currentEnemy]" "The slime princess will be the strongest monster girl around. There's no use in resisting"

        else:
            "[currentEnemy]" "It's really nothing personal, my queen has ordered us to collect XP from heroes whenever we see one."
            "[currentEnemy]" "You're just another prey to me, are you gonna cum soon or do I need to tease you even more?"

        return

label fight_lesserslimeguard_reaction:
    if player.profile.lastAction == "Fight":
        if currentTurnNumber <= 2 and currentEnemy.health <= 0:
            "[currentEnemy]" "...I already lost?"
        
        elif currentEnemy.health <= 0 and (player.health / player.maxHealth <= 0.5):
            "[currentEnemy]" "You fought well..."      
        
        elif currentEnemy.health <= 0:
            "[currentEnemy]" "The princess will be dissapointed..."

        else:
            "[currentEnemy]" "Please stop doing that..."   
    else:
        "[currentEnemy]" "..."

label fight_lesserslimeguard_hitAnimation:
    call hideAllLesserSlime from _call_hideAllLesserSlime_12
    show lesserslime_main at bounce
    return

label fight_lesserslimeguard_dead:
    "[currentEnemy]" "Ah... How unfortunate... I'm sorry princess..."
    stop music fadeout 2
    "[currentEnemy]" "..."
    call hideAllLesserSlime from _call_hideAllLesserSlime_13
    "The slime crawls away to safety as you're left facing the princess in her weakened state..."
    show slimeprincess_smug with myDissolve
    "[slimePrincess]" "Hmpf~ I suppose you're not as pathetic as you look, human~"
    "[slimePrincess]" "Ahh~ Very well then~ Since I'm a generous princess, I'll let you go just this once~"
    "[slimePrincess]" "You said you needed magic energy, right?"
    "[slimePrincess]" "If you leave our cave and head west you'll find the alraune tree. There's enough nectar there to supply all of slime village with magic energy for a lifetime~"
    "[slimePrincess]" "Ohoho~ And as the princess of slime village, I order you to collect some nectar~ You can keep a little for yourself since I'm so merciful, but I expect you to bring some to me as well~"
    "[slimePrincess]" "..."
    hide slimeprincess_smug with myDissolve
    show slimeprincess_laugh with myDissolve
    "[slimePrincess]" "What are you waiting for? A kiss? Get out of here, piggy~"
    scene black with myDissolve
    "Having defeated the slime princess, you leave the castle."
    "She said something about the alraunes. If you explore the forest you might find a path leading to the alraune tree"
    "..."
    call completeObjective(game.objective[2]) from _call_completeObjective_1
    call fight_player_victory from _call_fight_player_victory
    call move("slimevillage_royal") from _call_move_17

    return

label fight_lesserslimeguard_victory:
    if player.level == 1:
        "[currentEnemy]" "Wait a second... you're only level one...?"
        "The slime sighs before getting off of you..."
        call hideAllLesserSlime from _call_hideAllLesserSlime_14
        show lesserslime_main with myDissolve
        pause 0.3
        "[currentEnemy]" "Then..."
        "[currentEnemy]" "You won't be very useful at all..."
        "[currentEnemy]" "The princess is gonna be so disappointed... Oh no..."
        "[currentEnemy]" "Just..."
        "[currentEnemy]" "Just go... I see why it was so easy now..."
        menu:
            "Offer a little XP" if slimePrincess.profile.favor == 0 and player.XP > 10:
                "You tell the lesser slime you want to give her a little XP"
                "[currentEnemy]" "Huh? You'd do that?"
                "[currentEnemy]" "Well, I can't say no to that I suppose~"
                call hideAllLesserSlime from _call_hideAllLesserSlime_15
                show lesserslime_paizuri at continuousBounce with myDissolve
                "The lesser slime presses her boobs against your dick. It leaks precum almost immediately and the slime absorbs it instantly."
                call levelDrain(player, currentEnemy, player.XP - 1) from _call_levelDrain_23
                show lesserslime_paizuri at continuousBounce(1.1, 99.9)
                "[currentEnemy]" "Hehe thank you [pronouns.mister]~ That was nice of you!"
                "[currentEnemy]" "I'll be sure to tell the princess about you!"
                show lesserslime_paizuri at asyncDissolve(1)
                "The slime then leaves with a smile on her face!"
                "..."
                scene black with myDissolve
                call levelDrain(currentEnemy, slimePrincess, currentEnemy.XP - 1) from _call_levelDrain_24
                "..."
                "You pass out..."
                pause 3
                "When you wake up, you find yourself back in the inn."
                return

            "Leave":
                "You leave without having your levels drained."
                return
    
    "[currentEnemy]" "I have to admit, you put up a good fight..!"
    "[currentEnemy]" "But you can't always win~ It's time for me to drain you dry now~"
    call hideAllLesserSlime from _call_hideAllLesserSlime_16
    show lesserslime_sex at continuousBounce with myDissolve
    "The lesser slime straddles you. She lets out a soft moan as she takes your dick inside her."
    "[currentEnemy]" "Ahh~!"
    "After putting it in, she instantly starts bouncing up and down on your waist."
    "[currentEnemy]" "Hehe~ I didn't think I'd actually be able to to capture a human..."
    "[currentEnemy]" "But now that I've captured you, the princess will be so proud~!"
    "[currentEnemy]" "Hehe are you enjoying this~? You are, right~? Hehe, I can see it on your face~"
    "[currentEnemy]" "Do you want to let some semen out~? It's going to a good cause, you know~?"
    show lesserslime_sex at continuousBounce(1.11, 0.3)
    "She starts riding you faster and faster. Your dick can barely keep up..."
    "[currentEnemy]" "Mhm~ They're aaaall going to the slime princess~"
    "[currentEnemy]" "Her pretty pink body is what makes her special~ I'm sure you'll get to meet her soon~"
    "[currentEnemy]" "She's gonna rule over all of monsterkind after we've all given her our levels~"
    "[currentEnemy]" "She'll be sooo proud of me~! Please cum quickly, okay~? That way I can absorb all of it and give it to her~"
    "[currentEnemy]" "Her slimy body bounces on your cock and makes you go crazy with pleasure. You can't resist anymore and give up your orgasm."
    show lesserslime_sex at continuousBounce(1.07, 0.6) 
    call pyupyu from _call_pyupyu_7
    call levelDrain(player, currentEnemy, (player.XP - player.levelBottom) + 10) from _call_levelDrain_25
    "[currentEnemy]" "Hehe I did it~! Thanks [pronouns.mister]~!"
    "[currentEnemy]" "Phew, draining levels is exhausting..."
    hide lesserslime_sex with myDissolve
    show lesserslime_main with myDissolve
    "[currentEnemy]" "I'll go give these to the slime princess... Bye [pronouns.mister]!"
    hide lesserslime_main with myDissolve
    "The lesser slime gets off of you..."
    call levelDrain(currentEnemy, slimePrincess, currentEnemy.XP - 10) from _call_levelDrain_26
    call exitCombat from _call_exitCombat_2
    scene black with myDissolve
    "You pass out..."
    "When you wake up, you find yourself back in the inn." 
    "{cps=1}..."
    return
    
    

label fight_lesserslimeguard_dry:
    "[currentEnemy]" "Ehh~? You don't have any more XP to give me~?"
    "[currentEnemy]" "What a shame~ I guess I'll just have to find someone else then~"
    "[currentEnemy]" "Thanks for the XP [pronouns.mister], but I have no use for you now so byee~"
    "The slime gets off of you and runs off into the forest..."

