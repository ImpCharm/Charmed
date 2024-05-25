define timeBetweenFramesS = 0.12
image slime_succ_anim:
    "slime_succ (1)"
    pause timeBetweenFramesS
    "slime_succ (2)"
    pause timeBetweenFramesS
    "slime_succ (3)"
    pause timeBetweenFramesS
    "slime_succ (4)"
    pause timeBetweenFramesS
    "slime_succ (5)"
    pause timeBetweenFramesS
    "slime_succ (6)"
    pause timeBetweenFramesS
    repeat

define timeBetweenFramesF = 0.12
image slime_fellatio_anim:
    "slime_fellatio (1)"
    pause timeBetweenFramesF
    "slime_fellatio (2)"
    pause timeBetweenFramesF
    "slime_fellatio (3)"
    pause timeBetweenFramesF
    "slime_fellatio (4)"
    pause timeBetweenFramesF
    "slime_fellatio (5)"
    pause timeBetweenFramesF
    "slime_fellatio (6)"
    repeat

default randomDialogueInt = 0

label fight_slime_intro:
    call hideAllImp from _call_hideAllImp_1
    show slime_main
    if game.slimeTutoFight:
        "[slime]" "Huh..? A human..?"
        "[slime]" "Are we gonna fight..?"
    
    elif currentEnemy.playerEncounters == 2:
        "[slime]" "A human..? Again?"
        "[slime]" "..."
        "[slime]" "Huh..? Oh, it's you!"
        "[slime]" "Hmpf~ You're back for a rematch huh~?"
        "[slime]" "Alright then~! Bring it on~"

    elif currentEnemy.winCount == 1:
        "Oh~? It's you again?"
        "..."
        hide slime_main with myDissolve
        show slime_sexy with myDissolve
        play audio "/audio/slime/11w7.mp3"
        "Oh I get it~ You couldn't get enough of me after I beat you that one time huh~?"
        "Kufufu~ Then why not just give in right here~? Or would you rather pretend you don't want this slimy body~?"
        "Come on~ Just lay down and let me make you feel good and we can stop pretending to be strong~"
        

    call fight_intro from _call_fight_intro_1
    jump fight_player_turn
    return

label fight_slime_turn:
    call calculateLevel(slime) from _call_calculateLevel_4

    default randomI = 0
    call random(1,100) from _call_random_1
    $ randomI = _return

    if player.conditions.restrained:
        jump fight_slime_restrained

    elif willRestrain:
        jump fight_slime_willRestrain

    elif (((player.health / player.maxHealth) * 100) > 99 or randomI < 30):
        $ attackType = sexTypes.blowjob
        
        call calculateDamage from _call_calculateDamage_2
        call fight_slime_blowJobBoobs from _call_fight_slime_blowJobBoobs

    elif randomI > 40 and ((player.health / player.maxHealth) * 100) < 70 :
        $ attackType = sexTypes.blowjob
        call calculateDamage from _call_calculateDamage_3
        call fight_slime_blowJobSuck from _call_fight_slime_blowJobSuck

    else:
        $ attackType = sexTypes.blowjob
        call calculateDamage from _call_calculateDamage_4
        call fight_slime_blowJobLess from _call_fight_slime_blowJobLess

    play sound blow1
    call takeDamageText(damage) from _call_takeDamageText_2
    stop sound fadeout 0.5
    if player.health <= 0:
        "You're unable to resist any longer..."
        call fight_slime_victory from _call_fight_slime_victory
        call player_dead from _call_player_dead_1

    call hideAllSlime from _call_hideAllSlime
    show slime_main with myDissolve

    call random(1, 100) from _call_random_2
    if ((player.health < player.maxHealth / 2 and _return < 30) or (player.arousal > 50 and _return > 70)) and game.slimeTutoFight == False:
        play audio song
        "[slime.profile.name] seems to be preparing something..."
        "It might be best to {color=#f00}defend next turn"
        $ willRestrain = True
    
    # = player.attack = 0
    
    jump fight_player_turn
    "slimey4"
    return

# Slime attacks start

    label fight_slime_restrained:
        if currentTurnNumber % 2 == 1:
            "[slime]" "Don't you love this pleasure [pronouns.mister]~? I promise it'll feel even better if you don't resist~"
        else:
            "[slime]" "You know you can feel even better than this right~? All you have to do is let me have my way with you and I'll help you spurt over and over~"
        
        "[currentEnemy.profile.name] is trying to drain more of your levels! Resist for 1SP?"
        menu:
            "Resist" if player.SP > 0:
                $ player.SP -= 1
                play audio success2
                "You managed to not lose your XP. You're still restrained though!"
            "Rest":
                "[slime]" "Hehe good~ I'll drain you of every last drop~"
                "[slime.profile.name] rides your dick faster and faster, you feel it twitch as you're about to cum more."

                if currentTurnNumber % 5 == 1:
                    "[slime]" "Hehe~ That's it, let me take control, okay~?"
                elif currentTurnNumber % 5 == 2:
                    "[slime]" "You don't need to resist anymore~ I'll make you my little pet~"
                elif currentTurnNumber % 5 == 3:
                    "[slime]" "You should be grateful I'm doing this, you know~? If I didn't, you might end up someone else's pet~"
                elif currentTurnNumber % 5 == 4:
                    "[slime]" "You don't really need to return home, do you~? Why don't you just stay here as my little semen tank~?"
                else:
                    "[slime]" "Come on come on~ Let's have lots of sex together, okay [pronouns.mister]~?"

                "[slime]" "Come on~ Let eeeverything out~"
                call pyupyu from _call_pyupyu_1
                call levelDrain(player, slime, slime.levelTop - slime.XP) from _call_levelDrain_5
                call restore(slime) from _call_restore_1
                "[slime]" "Ahnnn~~ Amazing~ But I bet you have even more semen in there, right~?"
        
        jump fight_player_turn
        return
        

    label fight_slime_willRestrain:
        "[slime.profile.name] tried restraining you!"
        $ willRestrain = False
        if player.profile.lastAction == "Defend":
            "You evaded her attack!"
            "[slime]" "Come on~ You don't wanna feel good~?"
            "[slime]" "Don't be so booooring~"
            jump fight_player_turn
            return
            
        call hideAllSlime from _call_hideAllSlime_1
        show slime_sex with myDissolve
        play sound pistonslightlydrymediumspeed5times loop
        play audio "/audio/slime/11w5.mp3"
        play audio failure1
        "{color=#f00}You failed to evade the attack."
        "[slime]" "Hehe~ That's it, let me take control, okay~?"
        "[slime]" "You don't need to resist anymore~ I'll make you feel amazing~"
        call enterRestraint from _call_enterRestraint
        show slime_sex at continuousBounce2() with myDissolve
        "[slime.profile.name] pushes you down and proceeds to take your dick deep inside her, making it impossible to escape."
        play audio "/audio/slime/11w6.mp3"
        "[slime]" "Hehe, don't struggle, okay~? It'll feel much better that way, I promise~"
        "[slime]" "You were pretty violent just now, you know?"
        "[slime]" "Don't you think it's fair if I restore a little power~? Especially after you've tried hurting me like this~"
        "[slime]" "Come on, come on~ Just a few, okaaay~?"

        "[slime.profile.name] rides your dick faster and faster, you feel it twitch as you're about to cum."
        "[slime]" "Don't hold back, okay~?"
        "[slime]" "You're too weak to fight back anyway~ Just give me everything~"
        call hideAllSlime from _call_hideAllSlime_2
        show slime_mount at continuousBounce
        call pyupyu from _call_pyupyu_2
        show slime_mount at continuousBounce(1.1, 0.8)
        play audio "/audio/slime/11w5.mp3"
        "[slime]" "Ahnnn~~ That feels amazing~ Let's stay like this until you're dry, okay~?"
        jump fight_player_turn
        return

    label fight_slime_blowJobBoobs:
        call hideAllSlime from _call_hideAllSlime_3
        show slime_succless with myDissolve
        call damagePlayer(damage) from _call_damagePlayer_2
        play sound sucking004 loop fadein 0.0
        play audio "/audio/slime/11w5.mp3"
        "Suck suck suck"
        $ randomDialogueInt = renpy.random.randint(0,2)
        if (randomDialogueInt == 0):
            "[slime]" "Do you like it when I do this~? I bet you do, right~?"
            "[slime]" "Here, I'll take it aaall the way inside my mouth, okay~?"

        elif (randomDialogueInt == 1):
            "[slime]" "Hey hey~ how does this feel~?"
            "[slime]" "Us slime girls specialize in making dicks like yours feel {i}reaaally{/i} good~ ❤️"

        else:
            "[slime]" "I'll take it aaaall the way inside~ This should teach you a lesson for messing with me~!"
            "[slime]" "Don't expect me to hold back on you~ I'm gonna milk all that cum~!"

        return

    label fight_slime_blowJobSuck:
        call hideAllSlime from _call_hideAllSlime_4
        show slime_bj with myDissolve
        call damagePlayer(damage) from _call_damagePlayer_3
        play sound sucking047 loop fadein 1
        play audio "/audio/slime/11n4.mp3"
        "Kufufu~ Getting weak yet, [pronouns.mister]~?"
        $ randomDialogueInt = renpy.random.randint(0,2)
        if (randomDialogueInt == 0):
            "[slime]" "I can tell from the way you're throbbing~ You're getting weaker aren't you~?"
            "[slime]" "I bet if I keep going like this you'll go pyu pyu in no time~"

        elif (randomDialogueInt == 1):
            "[slime]" "Don't you feel good~? I'll keep going, okay~?"
            "[slime]" "You're getting close~ I want your semen mixed with my slime~!"

        else:
            "[slime]" "Hey hey~ If you stop resisting I'll make you feel extra good, you know~?"
            "[slime]" "I'm only a weak slime remember~? You can miss one turn right~?"

        return

    label fight_slime_blowJobLess:
        call hideAllSlime from _call_hideAllSlime_5
        show slime_fellatio_anim with myDissolve
        call damagePlayer(damage) from _call_damagePlayer_4
        play sound suckinglong loop fadein 1
        play audio "/slime/11n4.mp3"
        "Slop slop~"
        $ randomDialogueInt = renpy.random.randint(0,2)
        if (randomDialogueInt == 0):
            "[slime]" "You're about to cum, I can feel it~! I'll make you feel good if you do, okay~?"

        elif (randomDialogueInt == 1):
            "[slime]" "I can't wait to drain you dry soon~"

        else:
            "[slime]" "Come on, come on~ Let's go pyu pyu, okay~?"

        return    

label fight_slime_reaction:
    if player.profile.lastAction == "Fight":
        if(currentEnemy.health / currentEnemy.maxHealth <= 0):
            call hideAllSlime from _call_hideAllSlime_6
            show slime_main_sad with myDissolve
            "[slime]" "Oh... No..."
            return

        if(currentEnemy.health / currentEnemy.maxHealth <= 0.25):
            call hideAllSlime from _call_hideAllSlime_7
            show slime_main_sad with myDissolve
            "[slime]" "I- I don't know how much longer I can do this for..."
            return

        if(currentEnemy.health / currentEnemy.maxHealth <= 0.5):
            call hideAllSlime from _call_hideAllSlime_8
            show slime_main_sad 
            "[slime]" "Ow! Stop it! At this rate I'm going to turn into sludge"
            return

        if(currentEnemy.health / currentEnemy.maxHealth <= 0.75):
            if (renpy.random.randint(1,2) == 2):
                "[slime]" "Hey~ Do you wanna touch my slime, [pronouns.mister]~?"
                return
            else:
                call hideAllSlime from _call_hideAllSlime_9
                show slime_main_sad
                "[slime]" "Ow~! If you wanted to touch my slime you could have just said so, you know~?"   
                return 
    else: 
        "[slime]" "..."
    
    return

label fight_slime_hitAnimation:
    call hideAllSlime from _call_hideAllSlime_10
    show slime_main_sad at bounce
    return

label fight_slime_dead:
    "[slime]" "Oh... No..."
    show slime_main at asyncDissolve(0.5)
    return

label fight_slime_victory:
    stop music fadeout 2
    $ slime.winCount += 1
    if slime.winCount == 1:
        label fight_slime_victory_1:
        "[slime]" "Suck suck suck~"
        play music rose volume 0.25
        play sound sucking041 loop
        call hideAllSlime from _call_hideAllSlime_11
        show slime_bj with myDissolve
        "[slime.profile.name] keeps sucking your dick. It throbs as her slime slowly engulfs more and more of it."
        play audio "/audio/slime/11w5.mp3"
        "[slime]" "You really can't hold it much longer can you [pronouns.mister]~?"
        "[slime]" "I'm not surprised, after all that fighting you must be so horny~"
        "[slime]" "Espeeecially when you have so many levels~"
        "[slime]" "and nobody to drain them from you~"
        "[slime]" "Hehe~ It's okay, I'm gonna do juuust that~ I'll take care of those needy feelings for you, okay~?"
        "[slime]" "Let me guess, you couldn't get enough of me after that first fight so you came back here to feel my slimy mouth even more~"
        "[slime]" "You just didn't give in that time because your {i}{color=[imp.profile.color]}demon friend{/color}{/i} was watching huh~? Luckily they're gone now"
        "[slime]" "Don't you worry~ I'll only drain a couple levels, okay~? She won't even notice~"
        "[slime]" "Are you ready to cum inside my mouth, [pronouns.mister]~?"
        hide slime_bj
        show slime_mouthcum
        call pyupyu from _call_pyupyu_3
        play audio "/audio/slime/11n4.mp3"
        "[slime]" "Mphhh~"
        stop sound fadeout 3
        stop music fadeout 10
        call levelDrain(player, slime, 200) from _call_levelDrain_6
        "[slime]" "Ahh delicious, right~? I bet it felt reaaally good for you too~"
        play audio "/audio/slime/11w4.mp3"
        "[slime]" "Kufufu thanks for the levels [pronouns.mister]~ See you soon~!"
        hide slime_bj with myDissolve
        scene black with myDissolve
        "[slime.profile.name] creeps away after draining some of your XP"

    if slime.winCount >= 2:
        "[slime]" "Hehe so you really came back huh~?"
        "[slime]" "Did you miss me that much~? It's almost like you're forming an addiction, you know~?"
        play music rose volume 0.25
        call hideAllSlime from _call_hideAllSlime_13
        show slime_sexy with myDissolve
        play audio "/audio/slime/11w4.mp3"
        "[slime]" "Hey hey~ Let's just cut to the chase, okay~?"
        "[slime]" "I know you crave my slimy body~ There's no need to be shy~"
        "[slime]" "Just relax and let me do my thing okay~? It's not like you have the power to resist anyway~"
        hide slime_sexy
        show slime_mount at continuousBounce() with myDissolve
        play sound pistongutuovertonesmediumspeed16times loop
        play audio "/audio/slime/11w5.mp3"
        "The slime girl mounts you and leaves you unable to escape."
        "[slime]" "Ahh~ Here we are, doesn't your dick feel good like this~?"
        "[slime]" "Plap plap plap plap~"
        "[slime]" "Your dick is reaching my core~ It's so deep and covered in my slime~"
        "[slime]" "Hehe~ You're so slimy, you can barely even move~"
        "[slime]" "You don't need to move though, I'll do all the work for now, okay~? You just focus on cumming~"
        "Your dick throbs as you feel an orgasm building up..."
        play audio "/audio/slime/11w6.mp3"
        "[slime]" "What's that [pronouns.mister]~? Are you gonna cum~? Really~?"
        "[slime]" "Hehe you just love feeding me more and more levels don't you~?"
        "[slime]" "Good [pronouns.boy]~ Go ahead and cum your levels inside me~"
        hide slime_mount
        show slime_sex at continuousBounce()
        call pyupyu from _call_pyupyu_8
        call levelDrain(player, slime, 500) from _call_levelDrain_7
        play audio "/audio/slime/11w7.mp3"
        "[slime]" "Ahh~~~"
        "[slime]" "Right into my core as well~ Good job [pronouns.mister]~"
        "[slime]" "Hey hey~ You're really good at this whole feeding levels thing, you know~?"
        "..."
        hide slime_sex with myDissolve
        call hideAllSlime from _call_hideAllSlime_14
        stop sound fadeout 3
        "The slime girl gets off of you"
        "[slime]" "Come here for a second, won't you~?"
        "The slime lets go of you. now's your chance to get away..."
        menu:
            "...":
                "..."
                "[slime]" "...Hehe good [pronouns.boy]~"
                call hideAllSlime from _call_hideAllSlime_15
                show forest with myDissolve
                show slime_succ_anim with myDissolve
                play sound sucking041 loop
                play audio "/audio/slime/11w9.mp3"
                "[slime]" "I'll make sure you never get away again, okay~?"
                "She wraps her hand around your dick and starts stroking it again..."
                "[slime]" "Just relax okay~? This will feel reaaally good~"
                "[slime]" "She gently kisses the tip of your penis..."
                call gainStatusEffect(1) from _call_gainStatusEffect_4
                $ game.pfp.slimeUnlocked = True
                "[slime]""You'll take double damage from blowjobs now hehe~"
                "[slime]""You weren't thinking of fighting back anymore anyway, were you~?"
                "[slime]""Hehe good pet~ Let's spurt out some more levels now, okay~?"
                "You feel her hands stroke faster and more of your dick. It throbs in excitement as you're about to cum."
                call pyupyu from _call_pyupyu_4
                call levelDrain(player, slime, 500) from _call_levelDrain_8
                "[slime]" "Hehehe~ Good job cumming your levels out [pronouns.mister]~"
                hide slime_succ_anim with myDissolve
                show slime_main with myDissolve
                stop sound fadeout 3
                stop music fadeout 10
                "[slime]" "Well then, I've drained you enough~ How about you go grind some more XP for me to drain okay~?"
                call slime_skyecheck from _call_slime_skyecheck
                call hideAllSlime from _call_hideAllSlime_16
                "As [slime.profile.name] lets go of your dick, you collapse to the ground..."
                "..."
                "Skye pfp unlocked!"
                call unlockPfp(1) from _call_unlockPfp_1
                "..."
            
            "Run away":
                "You quickly got up and ran away from the slime..."
                "[slime]" "Hey! Where are you going?"
                "You managed to run away from her..."
    
    scene black with myDissolve
    "You pass out..."
    pause 3
    "When you wake up, you find yourself back in the inn."
    return

label fight_slime_dry:
    call escapeRestraint from _call_escapeRestraint_1
    "[slime]" "Ehh~? You don't have any more XP to give me~?"
    "[slime]" "What a shame~ I guess I'll just have to find someone else then~"
    call hideAllSlime from _call_hideAllSlime_17
    show slime_main with myDissolve
    pause 0.5
    "[slime]" "Hmm~ What should I do with you though~?"
    "[slime]" "Ah~ You really do look exhausted..."
    "[slime]" "..."
    scene black with myDissolve
    "Before you pass out you hear [slime.profile.name] sigh..."
    "With what little consciousness you have left, you feel yourself being dragged towards the inn."
    pause 0.5
    "You wake up in the inn"
    call player_dead from _call_player_dead_2

label slime_skyecheck:
    if slime.profile.name != "Skye":
        "My name is {size=40}{color=[slime.profile.color]}Skye{/color}{/size} by the way~ I live in the forest~ Come visit me sometime, 'kay~?"
        $ slime.profile.name = "Skye"
    return