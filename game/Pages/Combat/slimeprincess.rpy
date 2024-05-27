define timeBetweenFramesSex = 0.12
image slimeprincess_sex:
    "slimeprincess_sex (1)"
    pause timeBetweenFramesS
    "slimeprincess_sex (2)"
    pause timeBetweenFramesS
    "slimeprincess_sex (3)"
    pause timeBetweenFramesS
    "slimeprincess_sex (4)"
    pause timeBetweenFramesS
    "slimeprincess_sex (5)"
    pause timeBetweenFramesS
    "slimeprincess_sex (6)"
    pause timeBetweenFramesS
    "slimeprincess_sex (7)"
    pause timeBetweenFramesS
    repeat

define randomDialogueInt = 0

label fight_slimeprincess_intro:
    call hideAllChara from _call_hideAllChara_7
    show slimeprincess_smug
    call fight_intro from _call_fight_intro_3

    $ temptationEvent = True

    "[slimePrincess]" "Ohohoho~! How exciting~ You really think you stand a chance against me~? Do you know who I am?"
    "[slimePrincess]" "I can't wait to turn you into another one of my servants~"
    "[slimePrincess]" "Be honest~ That's the whole reason you came here, isn't it~? To see the beautiful slime princess with your very own eyes~"
    "[slimePrincess]" "Ohohoho~ Don't worry, I understand~ I'm just that gorgeous~"
    hide slimeprincess_smug with myDissolve
    show slimeprincess_laugh with myDissolve
    "[slimePrincess]" "Well then~ Be a good pet and let me drain all those saved up levels~"
    "[slimePrincess]" "If you do well, I might give you a treat~"
    
    jump fight_player_turn
    return

label fight_slimeprincess_turn:
    call calculateLevel(slimePrincess) from _call_calculateLevel_17 

    define randomI = 0
    call random(1,100) from _call_random_4 
    $ randomI = _return

    if player.conditions.restrained:
        jump fight_slimeprincess_restrained

    elif willRestrain:
        jump fight_slimeprincess_willRestrain

    elif ((player.arousal == 100 
        and randomI > 30) 
        and not (((currentEnemy.health / currentEnemy.maxHealth) * 100) < 51 
        and temptationEvent)):
        $ attackType = sexTypes.paizuri
        
        call calculateDamage from _call_calculateDamage_7 
        call fight_slimeprincess_boobSqueeze from _call_fight_slimeprincess_boobSqueeze

    elif (((currentEnemy.health / currentEnemy.maxHealth) * 100) < 51 
        and temptationEvent):
        jump fight_slimeprincess_temptation

    else:
        $ attackType = sexTypes.sex
        call calculateDamage from _call_calculateDamage_8 
        call fight_slimeprincess_sex from _call_fight_slimeprincess_sex

    play sound blow1
    call takeDamageText(damage) from _call_takeDamageText_3
    stop sound fadeout 0.5
    if player.health <= 0:
        stop music fadeout 2
        "You're unable to resist any longer..."
        "..."
        call fight_slimeprincess_victory from _call_fight_slimeprincess_victory_1 
        call player_dead from _call_player_dead_3 

    call hideAllSlimePrincess from _call_hideAllSlimePrincess 
    show slimeprincess_laugh with myDissolve

    call random(1, 100) from _call_random_5 
    if (player.health < player.maxHealth / 2 and _return < 30) or (player.arousal > 50 and _return > 70):
        play audio song
        "[slimePrincess.profile.name] seems to be preparing something..."
        "It might be best to {color=#f00}defend next turn"
        $ willRestrain = True
    
    # = player.attack = 0
    
    jump fight_player_turn
    "slimeprincessy4"
    return

# Slimeprincess attacks start

    label fight_slimeprincess_restrained:
        call hideAllChara from _call_hideAllChara_8
        show slimeprincess_sex2
        show slimeprincess_sex2 at continuousBounce2() with myDissolve
        play sound sucking041 loop
        play audio kisssound16
        if currentTurnNumber % 4 == 0:
            "[slimePrincess]" "Ohohoho~ How does my tongue feel peasant~? better than anything you've ever experienced I bet~"
        elif currentTurnNumber % 4 == 1:
            "[slimePrincess]" "Few people are actually allowed to enjoy my body this way, I expect a lot of XP in return~"
        elif currentTurnNumber % 4 == 2:
            "[slimePrincess]" "Ugh~ I can't believe I have to do this kind of stuff with a peasant like you... The only place you belong is beneath my feet~!"
        else:
            "[slimePrincess]" "Are you gonna cum soon~? How pathetic~ You truly are a maso-hero~"


        "[currentEnemy.profile.name] is trying to drain your levels! Resist for 1SP?"
        menu:
            "Resist" if player.SP > 0:
                $ player.SP -= 1
                play audio success2
                "You managed to not lose your XP. You're still restrained though!"
            "Rest":
                "[slimePrincess]" "Ohohoho~ Too fazed by my beauty to resist~? "
                "[slimePrincess]" "It can't be helped then~ I'll make sure you tribute all your levels to me~"
                "[slimePrincess.profile.name] rides your dick faster and faster, you feel it twitch as you're about to cum more."

                if currentTurnNumber % 4 == 0:
                    "Don't worry, most heroes end up losing to me~ You're nothing special, just another hero who was defeated by the great slime princess~"
                elif currentTurnNumber % 4 == 1:
                    "I guess you just can't resist how absolutely stunning I look, huh~? I'd want to be drained as well if I were you~"
                elif currentTurnNumber % 4 == 2:
                    "I'm really doing you a favor by draining you if anything~ Wouldn't living as my servant be much easier than being some silly hero~?"
                else:
                    "Come on, keep feeding me as you make me stronger~ Sooner or later your only option will be to serve me~"

                "[slimePrincess]" "Shoot out all that semen for me, peasant~ I deserve it so much more~ Ohohoho~!"
                call pyupyu from _call_pyupyu_9 
                call levelDrain(player, slimePrincess, slimePrincess.levelTop - slimePrincess.XP) from _call_levelDrain_28 
                call restore(slimePrincess) from _call_restore_8 
                "[slimePrincess]" "Ohohoho~ How wonderful~ And you still have more to tribute to me, don't you~?"
        
        jump fight_player_turn
        return
        

    label fight_slimeprincess_willRestrain:
        "[slimePrincess.profile.name] tried restraining you!"
        $ willRestrain = False
        if player.profile.lastAction == "Defend":
            "You evaded her attack!"
            "[slimePrincess]" "Fufufu~ I guess you're not as stupid as you look~"
            "[slimePrincess]" "I'm sure you'll give in soon enough~"
            jump fight_player_turn
            return
            
        call hideAllSlimePrincess from _call_hideAllSlimePrincess_1 
        show slimeprincess_sex2 with myDissolve
        play sound pistongutuovertoneslowspeed5times loop
        play audio "/audio/slimeprincess/10w5.mp3"
        play audio failure1
        "{color=#f00}You failed to evade the attack."
        "[slimePrincess]" "Ohoho~ Not gonna avoid it~? That's what I thought, peasant~"
        "[slimePrincess]" "I can see it in your eyes~ You want to be taken as my little pet don't you~?"
        call enterRestraint from _call_enterRestraint_1 
        show slimeprincess_sex2 at continuousBounce2() with myDissolve
        "[slimePrincess.profile.name] sits on top of you, making it impossible to move."
        play audio "/audio/slimeprincess/10w3.mp3"
        "[slimePrincess]" "Ohoho~ I finally have you tamed now~"
        "[slimePrincess]" "You didn't really think you could challenge me and not wind up just another one of my servants, right~?"
        "[slimePrincess]" "Losing to me is inevitable~ and in the end everyone adores me just the same~ Ask any of my other servants~"
        "[slimePrincess]" "I'll turn you into a servant just like them~ So first, give me your XP~"

        "[slimePrincess.profile.name] elegantly rides your dick with smooth motions"
        "[slimePrincess]" "Are you gonna cum, pet~? Are you finally gonna admit your defeat~?"
        "[slimePrincess]" "Lose your XP to me~ I deserve it a thousand times more than you do~"
        call pyupyu from _call_pyupyu_10 
        call levelDrain(player, slimePrincess, slimePrincess.levelTop - slimePrincess.XP) from _call_levelDrain_29
        show slimeprincess_sex2 at continuousBounce2(1.1, 0.8)
        play audio "/audio/slimeprincess/10w5.mp3"
        "[slimePrincess]" "Ohoho~ You're fulfilling your duties as a servant so well already~"
        "[slimePrincess]" "Your next order is to rest until you're completely dry, and don't you dare disobey me, peasant~!"
        jump fight_player_turn
        return

    label fight_slimeprincess_boobSqueeze:
        hide slimeprincess_laugh with myDissolve
        call hideAllSlimePrincess from _call_hideAllSlimePrincess_2 
        show slimeprincess_boob with myDissolve
        call damagePlayer(damage) from _call_damagePlayer_7
        play sound handjobmediumspeed loop fadein 0.0
        play audio "/audio/slimeprincess/10w4.mp3"
        "You can't control your arousal and press your hands into [slimePrincess.profile.name]'s slimy boobs"
        $ randomDialogueInt = currentTurnNumber % 4

        if (randomDialogueInt == 0):
            "[slimePrincess]" "Touch them as much as you like, perv~"
            "[slimePrincess]" "How long will it take until you give in to your desires~? Maybe a minute~?"

        elif (randomDialogueInt == 1):
            "[slimePrincess]" "Ohoho~ Can't control yourself huh~? How pathetic~"
            "[slimePrincess]" "Good thing that lack of control is exactly what I look for in my servants~"

        elif (randomDialogueInt == 2):
            "[slimePrincess]" "My my~ Getting handsy now are we~?"
            "[slimePrincess]" "You've got some nerve touching me, peasant!"

        elif (randomDialogueInt == 3):
            "[slimePrincess]" "Normally I'd punish you for your disobedience..."
            "[slimePrincess]" "But I can't exactly blame you for wanting to touch someone as gorgeous as I am~ Ohohoho~"

        else:
            "[slimePrincess]" "Disgusting~ Your gross hands have no right touching me."
            "[slimePrincess]" "Then again, I AM beautiful~ So I'll forgive you for having such desires~"

        return

    label fight_slimeprincess_temptation:
        $ temptationEvent = False
        hide slimeprincess_laugh with myDissolve
        call hideAllSlimePrincess from _call_hideAllSlimePrincess_3 
        show slimeprincess_stand2 with myDissolve
        stop sound fadeout 3
        stop music fadeout 3
        "[slimePrincess]""Hmpf~ For a mere peasant you're doing surprisingly well..."
        "[slimePrincess]""You're stronger than you look, you're really persistent about this huh?"
        "[slimePrincess]""After the slime princess belittles you she gets close to you and presents herself to you."
        hide slimeprincess_stand2 with myDissolve
        show slimeprincess_presenting with myDissolve
        play audio "/audio/slimeprincess/10p5.mp3"
        play music rose volume 0.25
        "[slimePrincess]""You must be tired from fighting huh~? I'm a fair princess so I'm offering you a reward here~"
        "[slimePrincess]""That's right~ You get to enjoy my royal body~ Ohohoho~ "
        
        play audio song
        "{color=#f00}This seems like a bad idea..."
        menu:
            "Have sex with her":
                "You listen to your lust and thrust into the slime princess's pussy..."
                hide slimeprincess_presenting with myDissolve
                show slimeprincess_sex with myDissolve
                play sound pistongutuovertonesmediumspeed16times loop
                play audio "/audio/slimeprincess/10w1.mp3"
                "[slimePrincess]" "That's a smart hero~ Listen to your urges~ Listen to your lust~"
                "[slimePrincess]" "You want it, don't you~? You want to feel yourself deep inside my royal pussy~"
                jump fight_slimeprincess_victory_sex

            "Lick her feet":
                "You can't resist the sight and crawl closer to lick one of her feet..."
                play sound sucking041 loop
                "[slimePrincess]" "Ohoho~ How adorable~ I can tell how eager you are to be mine~"
                "[slimePrincess]" "Well then, who am I to deny such a good piggy of their wishes~"
                jump fight_slimeprincess_victory_feet 

            "Ignore her":
                pass

        "You decide not to give in to her temptation..."
        hide slimeprincess_presenting with myDissolve
        show slimeprincess_stand2 with myDissolve
        stop music fadeout 1
        "[slimePrincess]" "Fufu~ It was worth a try~ I suppose you're not as stupid as you look~"
        hide slimeprincess_stand2 with myDissolve
        show slimeprincess_laugh with myDissolve
        play music combat volume 0.25
        jump fight_player_turn
        return 

    label fight_slimeprincess_sex:
        hide slimeprincess_laugh with myDissolve
        call hideAllSlimePrincess from _call_hideAllSlimePrincess_4 
        show slimeprincess_sex2 at continuousBounce(1.1, 0.28) with myDissolve
        call damagePlayer(damage) from _call_damagePlayer_8
        play sound pistonslightlydrylowspeed12times loop
        play audio "/audio/slimeprincess/10w3.mp3"

        $ randomDialogueInt = currentTurnNumber % 4

        if (randomDialogueInt == 0):
            "[slimePrincess]" "Pathetic~ You call that an attack?"
            "[slimePrincess]" "It's honestly laughable~ You think you stand a chance against the slime princess herself~? Ohoho~"

        elif (randomDialogueInt == 1):
            "[slimePrincess]" "Well then~ I'll show you how to REALLY make someone feel good~"
            "[slimePrincess]" "You obviously have no idea what you're doing~ Sit still while I defeat you, \"hero\"~"

        elif (randomDialogueInt == 2):
            "[slimePrincess]" "Ufufu~ This feels amazing doesn't it~? This is what happens daily if you decide to become my servant, you know~?"
            "[slimePrincess]" "Doesn't it sound good~? It's not too late to surrender, you know?"

        elif (randomDialogueInt == 3):
            "[slimePrincess]" "How does it feel~? My royal pussy barely allows you to move~"
            "[slimePrincess]" "It's not like you wanna move anyway, right? Isn't this better than protecting those boring humans?"

        else:
            "[slimePrincess]" "Ohohoho~ You're so lucky to be allowed to feel me like this~"
            "[slimePrincess]" "You're putting up quite a fight~ I could use someone like you as a servant~"

        return

label fight_slimeprincess_reaction:
    if player.profile.lastAction == "Fight":
        "..."
    else: 
        "[slimePrincess]" "..."
    
    return

label fight_slimeprincess_hitAnimation:
    call hideAllSlimePrincess from _call_hideAllSlimePrincess_5 
    show slimeprincess_laugh at bounce
    return

label fight_slimeprincess_dead:
    if temptationEvent:
        $ slimePrincess.health = 1
        jump fight_slimeprincess_turn


    "[slimePrincess]" "No! This is ridiculous!"
    call hideAllSlimePrincess from _call_hideAllSlimePrincess_6
    show slimeprincess_presenting with myDissolve
    "[slimePrincess]" "Ohoho~! Well then human~ I'm allowing you... to..."
    "[slimePrincess]" "Wait I did this already didn't I..."
    "[slimePrincess]" "I... I can't..!"
    "The princess climbs on top of you, despite her exhaustion..."
    hide slimeprincess_presenting with myDissolve
    show slimeprincess_sex2 with myDissolve
    play sound pistonslightlydrylowspeed12times loop
    "[slimePrincess]" "Ohohoho..! You can't defeat me, human..! I'm... Do you know who I am!?"
    "[slimePrincess]" "I'm slime princess Rosé the first! You can't do this to me!"
    "[slimePrincess]" "I.. I'll just drain you! Then I'll restore and... and..."
    "[slimePrincess]" "I'll just... Yes..."
    stop music fadeout 5

    if player.XP > 4:
        call levelDrain(player, slimePrincess, 2, True, True, True) from _call_levelDrain_30
        "[slimePrincess]" "Oho.. ho... ho..."
        "[slimePrincess]" "Only 2 XP..."
    else:
        "[slimePrincess]" "Oho.. ho... ho..."

    stop sound fadeout 5
    "[slimePrincess]" "I need to rest... Human! You will pay for this!"
    "[slimePrincess]" "Guards..! Get [pronouns.him]!"
    hide slimeprincess_sex2 with myDissolve
    call enterCombat(Character(
                    9, 10, 2, 50, 2000,  
                    Profile("The slime guard", "#1e88e5", "lesserslimeguard",
                    "The slime princess's most trusted guard! Despite her exhausted demeanor, she's very commited to her duty. Despite her being a guard, she doesn't have a lot of combat experience. She's mostly used as a guardian for the door of Slime Village, rarely having to result to violence."
                    ),
                    Conditions())) from _call_enterCombat_6

    call hideAllChara from _call_hideAllChara_9
    return

label fight_slimeprincess_victory:
    $ slimePrincess.winCount += 1
    "[slimePrincess]" "Ohoho~ Finally giving in, [pronouns.mister]~?"
    "[slimePrincess]" "It's obvious~ You can't resist any longer~ You just want me to help you feel good, don't you~?"
    call hideAllSlimePrincess from _call_hideAllSlimePrincess_7
    show slimeprincess_smug with myDissolve
    play audio "/audio/slimeprincess/10w5.mp3"
    "[slimePrincess]" "Who would have guessed~ Another \"great hero\" defeated by the mighty slime princess~! Ohohoho~"
    "[slimePrincess]" "Hey hey~ Come closer okay~? I'll have some mercy on you if you kneel for me~"
    "..."
    menu:
        "Kneel...":
            pass

        "Try and escape":
            play audio song
            scene black with myDissolve
            "You run away from the princess while you still can!"
            "[slimePrincess]" "Hey! Come back here right now! What makes you think you can disobey my orders like this?"
            if (rand(1,3) == 2):
                "You dropped some gold while trying to escape!"
                call loseMoney(player, rand(0, mathMin(50, player.money))) from _call_loseMoney_5
                "[slimePrincess]" "Hmpf~ I suppose I can take this as compensation..."
            
            scene black with Dissolve(4)
            "You escape to the the slime village inn..."
            play audio escape
            call dayPass from _call_dayPass_8
            jump player_dead_slimevillage
            # call move("slimevillage_inn_dead")
            return

    "You start kneeling before her"
    hide slimeprincess_smug with myDissolve
    show slimeprincess_kneel with myDissolve
    play music rose volume 0.25
    play audio "/audio/slimeprincess/10w3.mp3"
    "[slimePrincess]" "Ohoho~ What an obedient piggy~"
    "[slimePrincess]" "Do you get it now~? You won't ever defeat me~"
    "[slimePrincess]" "Nobody is as great as I am~ And you will do as I say."
    "[slimePrincess]" "Understood?"
    menu:
        "\"Understood\"":
            play audio "/audio/slimeprincess/10w1.mp3"
            "[slimePrincess]" "Ohoho~ I'm glad we're on the same page, servant~"
            call increaseFavor(slimePrincess, 1) from _call_increaseFavor
            "[slimePrincess]" "You humans are so weak~ Just a minute ago you were promising to defeat me~ Whatever happened to that huh~?"
            "[slimePrincess]" "Of course, when presented with someone as incredible as I am, you really have no choice but to give in~ Though I'm impressed at how long you resisted, peasant~"
            "[slimePrincess]" "I could use some of that stamina in my army though~ And you'd make the perfect servant~"
            hide slimeprincess_kneel with myDissolve
            show slimeprincess_presenting with myDissolve
            play audio "/audio/slimeprincess/10w2.mp3"
            "[slimePrincess]" "Ohoho~ That's why I'm deciding to make you my new servant~"
            "[slimePrincess]" "You're so lucky to be allowed to serve me like this~ Now kiss my feet to seal your fate~"
            menu:
                "Kiss her feet":
                    "You crawl over to [slimePrincess.profile.name] and kiss her feet while touching yourself..."
                    play audio "/audio/slimeprincess/10w3.mp3"
                    "[slimePrincess]" "Ohohoho~! How delightful~"
                    "[slimePrincess]" "The hero who was supposed to stop my reign~ Kissing my feet, how pathetic~"
                    "[slimePrincess]" "But then again, I AM just that powerful aren't I~? Ohohoho~!"
                    "[slimePrincess]" "Well then, \"hero\"~ I hereby deem you my personal servant~"
                    call changeTitle(player, "Slime servant") from _call_changeTitle
                    play audio "/audio/slimeprincess/10w1.mp3"
                    "[slimePrincess]" "Ohohoho~ Welcome to my army, little servant~ I know you've wanted this from the start, it's obvious~"
                    "[slimePrincess]" "Peasants like you shouldn't bother trying to be strong~ You should know how many of you \"heroes\" have tried to defeat me before~ It's pathetic how weak you humans are~"
                    "[slimePrincess]" "Ohoho~ But now, you'll be nothing but my personal XP tank~ And I'll order you to collect as many levels as you can and donate them to me~"
                    "[slimePrincess]" "Come here, I'll give you my curse~"
                    label fight_slimeprincess_victory_main_curse:
                    "[slimePrincess.profile.name] brings her face closer to yours and starts making out with you."
                    hide slimeprincess_presenting with myDissolve
                    hide slimeprincess_boob with myDissolve
                    show slimeprincess_kiss with myDissolve
                    play audio "/audio/slimeprincess/10p6.mp3"
                    play sound licking031 loop
                    "[slimePrincess]" "Mwahh~"
                    call gainStatusEffect(2) from _call_gainStatusEffect_5
                    call changeTitle(player, "Slime servant") from _call_changeTitle_1
                    play audio "/audio/slimeprincess/10w4.mp3"
                    "[slimePrincess]" "From now on half the XP you gain will go to me~ Isn't that wonderful~?"
                    "[slimePrincess]" "This way you can always feed your beloved princess~ Aren't you happy~? You'll be another one of my pretty servants~"
                    "[slimePrincess]" "Ready for your first task as my servant~?"
                    stop sound fadeout 1
                    hide slimeprincess_kiss with myDissolve
                    show slimeprincess_smug with myDissolve
                    "[slimePrincess]" "As your princess, I order you to go fetch me some XP~ Ohohoho~!"
                    "[slimePrincess]" "Go fight some monsters or something~ Any XP you earn will be shared with me~"
                    "[slimePrincess]" "Go on, chop chop~ I have better things to do now~ Good luck, servant~"
                    scene black with myDissolve
                    "[slimePrincess.profile.name] walks away from you, waving her hand dismissively..."
                    "You lie on the ground, exhausted..."
                    "Everything fades to black as you hear the princess say some things to her other servants..."
                    "..."
                    "...You find yourself woken up in the castle..."
                    "..."
                    call completeObjective(game.objective[2]) from _call_completeObjective_2
                    call unlockPfp(2) from _call_unlockPfp_2
                    "..."
                    call player_dead_slimecastle from _call_player_dead_slimecastle

                "Nevermind":
                    hide slimeprincess_presenting with myDissolve
                    show slimeprincess_stand2 with myDissolve
                    "[slimePrincess]" "Oh~? You're changing your mind? How useless..."
                    "[slimePrincess]" "How cute~ You want to pretend you don't want it~ Fine by me~"
                    "[slimePrincess]" "I expect you to change your mind soon~ Bye for now~"
                    scene black with myDissolve
                    "[slimePrincess.profile.name] walks away, leaving you on the ground..."
                    "Everything fades to black..."
                    "When you wake up, you find yourself in the inn."
                    call player_dead_slimevillage from _call_player_dead_slimevillage_1

        "Say nothing":
            "[slimePrincess]" "Ohohoho~ Looks like somebody needs to be punished properly huh~?"
            hide slimeprincess_kneel with myDissolve
            show slimeprincess_sex2 with myDissolve
            show slimeprincess_sex2 at continuousBounce2()
            play sound pistongutuovertoneslowspeed5times loop
            play audio "/audio/slimeprincess/10w2.mp3"
            "[slimePrincess]" "I'll make you regret disobeying me by taking some of your levels~"
            "[slimePrincess]" "Ohoho~ I'll keep draining them until you start giving them up by choice~"
            "[slimePrincess]" "Ready to lose, piggy~?"
            "You feel [slimePrincess.profile.name] bounce with more force... The slime around your dick becomes cold yet comfortable."
            call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, True, True) from _call_levelDrain_31
            "[slimePrincess]" "Ohoho~ What's wrong~? Surprised at how good I am at draining~?"
            "[slimePrincess]" "That's what you get for disobeying me~ This should teach you a lesson~"
            call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, True, True) from _call_levelDrain_32
            "[slimePrincess]" "This pleasure won't last forever so you better enjoy it while it lasts~"
            play audio "/audio/slimeprincess/10w3.mp3"
            "[slimePrincess]" "Ohoho~ Doesn't it feel amazing to tribute to the one and only slime princess~?"
            "[slimePrincess]" "There's people who would do anything to tribute directly to me, you know~? You should be grateful I'm even treating you to such an experience ohohoho~"
            "[slimePrincess]" "Of course, nobody gets this kind of pleasure for free~"
            call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, True, True) from _call_levelDrain_33
            "[slimePrincess]" "But the price is worth it isn't it~? Feeling me like this~"
            "[slimePrincess]" "Besides, you won't need that much XP anyway when serving me~"
            "[slimePrincess]" "Ready to lose one more time~? I'll be sure to take all your XP this time~"
            call pyupyu from _call_pyupyu_11
            call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, True, True) from _call_levelDrain_34
            play audio "/audio/slimeprincess/10w4.mp3"
            "[slimePrincess]" "Ohohoho~ How delicious~ You humans are really only good for being XP farms, aren't you~?"
            stop sound fadeout 2
            "[slimePrincess]" "Ahh~ Well then, I've had enough XP for now~ And since I don't need any more XP you're practically useless~"
            hide slimeprincess_sex2 with myDissolve
            show slimeprincess_laugh with myDissolve
            "[slimePrincess.profile.name] stands up and looks at you, condescendingly."
            "[slimePrincess]" "Look at you~ How pathetic~"
            "[slimePrincess]" "I expect you to bring me even more levels to drain next time~"
            "[slimePrincess]" "See you soon, piggy~"
            hide slimeprincess_laugh with myDissolve
            "[slimePrincess.profile.name] walks away..."
            "..."
            "You pass out..."
            "When you wake up you find yourself back in the inn..."
            call player_dead_slimevillage from _call_player_dead_slimevillage_2


label fight_slimeprincess_victory_sex:
    $ slimePrincess.winCount += 1
    "[slimePrincess]" "Well then~ Thrust inside all you want~ I know how good it feels~"
    "[slimePrincess]" "My slimy pussy, can you feel it engulfing your dick, peasant~?"
    "[slimePrincess]" "You know what will happen now, right~? Unlike all those other slime girls, I don't need your semen in order to drain you~"
    "[slimePrincess]" "Ohohoho~! What's wrong? Surprised~? You didn't think I was really gonna reward you did you~? Are you really that stupid~?"
    "[slimePrincess]" "You feel the princess's slime get colder as your dick gets more sensitive... you feel your strength leaving your body"
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_35
    play audio "/audio/slimeprincess/10w2.mp3"
    "[slimePrincess]" "Ohoho~ You really are dumb huh~? Choosing to let your guard down like this~ Did my body take over your thoughts~?"
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_36
    "[slimePrincess]" "How pathetic~ You humans can't control your urges around me huh~? Weak~"
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_37
    "[slimePrincess]" "Is it worth it~? Giving up your levels like this~? It's like you can't stop thrusting right~? Like my pussy is sucking you back in with each thrust~"
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_38
    "[slimePrincess]" "Keep making me stronger~ So pathetic~ You'll never be able to defeat me if you keep feeding me, you know~?"
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_39
    "[slimePrincess]" "Ohohoho~ Not that you're ever gonna defeat me anyway~ You'll always be trapped by my slimy body~"
    "Despite [slimePrincess.profile.name]'s teasing you feel as if you're about to shoot out a load of semen... Your dick twitches as you moan..."
    play audio "/audio/slimeprincess/10w4.mp3"
    "[slimePrincess]" "Are you gonna cum, peasant~? Good~ I want you to shoot every last one of your levels inside of me~"
    $ timeBetweenFramesSex = 0.3
    call pyupyu from _call_pyupyu_12
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) * 2, True, True, True) from _call_levelDrain_40
    "[slimePrincess]" "Ohohoho~! Look at you, cumming while feeding the enemy you were supposed to defeat~ How low can you get~?"
    play audio "/audio/slimeprincess/10n2.mp3"
    stop sound fadeout 3
    "The princess gets off of you and dusts herself off..."
    hide slimeprincess_sex with myDissolve
    show slimeprincess_smug with myDissolve
    play audio wind4
    "[slimePrincess]" "I needed that~ It feels so much better to drain XP straight from the source instead of having my servants collect it for me~"
    "[slimePrincess]" "...As for you, \"hero\""
    "[slimePrincess]" "I suppose I won't enslave you quite yet~"
    "[slimePrincess]" "I'll let you go this time~ Slime village is near, I'm sure you can find your way there safely~ I expect you to bring me even more XP next time we meet~"
    "[slimePrincess]" "Now take your leave~! I have no more use for you for now~"
    scene black with myDissolve
    "You get up and walk away, defeated... Slime village should be able to heal you"
    "...As you walk away you hear the princess call you a \"piggy\" one last time, teasingly"
    "..."
    jump player_dead_slimevillage

label fight_slimeprincess_victory_feet:
    $ slimePrincess.winCount += 1
    "You eagerly lick the princess's feet... they're slimy but taste surprisingly sweet, almost toxic..."
    play audio "/audio/slimeprincess/10w2.mp3"
    "[slimePrincess]" "Ohoho~ How pathetic~ Who would have thought that a hero like you would be so easy train~"
    "[slimePrincess]" "Lick my feet, you weak hero~ Honestly, you don't even deserve that title~ But I suppose I can't take that from you quite yet~"
    "[slimePrincess]" "In the meantime, I'll steal some levels from you instead~"
    "[slimePrincess]" "Ohoho~ Come here, hero~ I'll let you touch my boobs as I drain you~"
    hide slimeprincess_presenting with myDissolve
    show slimeprincess_boob at continuousBounce(1.01) with myDissolve
    "Unable to control yourself, you press your hands into [slimePrincess.profile.name]'s boobs..."
    "You feel a force pulling you deeper in as you feel your levels leaving your body."
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_41
    "[slimePrincess]" "Ohoho~ My special slime allows me to drain without you having to ejeculate, isn't it amazing~?"
    "[slimePrincess]" "It feels good to touch, doesn't it~? Do you get why everyone wants to be mine now~? "
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_42
    "[slimePrincess]" "Soon you'll experience the same fate, you know~? So many heroes have come by here and most of them end up as my little pet~"
    "[slimePrincess]" "And judging by how eager you are to serve me, I'm sure it won't take long before you turn to one as well~ Ohohoho~"
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_43
    "[slimePrincess]" "You might as well accept it~ I'm only growing stronger with all these levels I'm absorbing~ Soon you'll have no choice but to obey me~"
    "[slimePrincess]" "Ohoho~! Soon everyone will know the power of the great slime princess~! And you lowly humans will have no choice but to watch"
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, False, True) from _call_levelDrain_44
    "[slimePrincess]" "And the best part~? You'll be the one doing it~ You'll be the one feeding me to the top so you pesky humans can't harm our kind anymore~"
    play audio "/audio/slimeprincess/10w1.mp3"
    play sound pistongutuovertonesmediumspeed16times loop
    hide slimeprincess_boob with myDissolve
    show slimeprincess_sex2 at continuousBounce() with myDissolve
    "[slimePrincess.profile.name] gets on top of you as you prepare to cum."
    "[slimePrincess]" "Are you about to spurt, [pronouns.mister]~? Are you ready to give up and spurt your soul inside me~?"    
    call pyupyu from _call_pyupyu_13
    show slimeprincess_sex2 at continuousBounce(1.1, 2) with myDissolve
    call levelDrain(player, slimePrincess, (player.XP - player.levelBottom) + 5, True, True, True) from _call_levelDrain_45
    stop sound fadeout 2
    "[slimePrincess]" "Ohohoho~ How cute~ The maso-hero spurted all it's semen out for my royal slime pussy~"
    "[slimePrincess]" "You truly are a pathetic maso-hero~"
    "[slimePrincess.profile.name] gets off of you and laughs."
    hide slimeprincess_sex2 with myDissolve
    show slimeprincess_laugh with myDissolve
    "[slimePrincess]" "How cute~ The piggy lost it's levels to the royal slime princess herself~"
    "[slimePrincess]" "Honestly, you should be grateful I even let you do this~"
    "You feel tired and begin to pass out."
    "[slimePrincess]" "Oh~? You're passing out?"
    "[slimePrincess]" "Ohoho~ I'll get my guards to pick you up and bring you to the village~ Remember to bring me even more XP next time~ Ohoho~"
    scene black with myDissolve
    "Everything starts fading to black... You feel yourself being lifted by slimy hands and walked to the village..."
    jump player_dead_slimevillage



label fight_slimeprincess_victory_submit:
    call enterCombatFake(slimePrincess) from _call_enterCombatFake
    # $ inCombat = True
    # $ currentEnemy = slimePrincess
    $ slimePrincess.winCount += 1

    play music rose volume 0.25    
    hide slimeprincess_laugh with myDissolve
    show slimeprincess_boob with myDissolve
    "[slimePrincess.profile.name] grabs your arms and pulls them inside her slimy body..."
    play audio "/audio/slimeprincess/10w2.mp3"
    "[slimePrincess]" "It feels amazing right~? Wanna know how many heroes have lost to them~?"
    "[slimePrincess]" "I've honestly lost count already~ They're all so boring anyway~"
    "[slimePrincess]" "You're just like them, really~ Acting all tough until it's time to serve me~"
    "[slimePrincess]" "You aaall just drop to your knees like the dumb little piggies you really are~"
    "Your dick throbs as the princess keeps teasing you."
    "You feel your energy leaving your body."
    call levelDrain(player, slimePrincess, player.XP - player.levelBottom + 1) from _call_levelDrain_46
    play audio "/audio/slimeprincess/10w3.mp3"
    "[slimePrincess]" "Ohoho~ You're doing amazing, my little servant~"
    "[slimePrincess]" "And guess what~? You're gonna become all mine~"
    "[slimePrincess]" "I'll have you assigned a bunch of different tasks as my little slave~"
    play audio "/audio/slimeprincess/10w4.mp3"
    "[slimePrincess]" "Ohoho~ I'm so amazing~"
    "[slimePrincess]" "You'll just have to abandon your journey as a hero~ Not like a pathetic piggy like yourself could ever be a hero in the first place~"
    "[slimePrincess]" "You're much better fit to be my own little pet~ Weak and obedient for the rest of your life~"
    "[slimePrincess]" "Now come here, I'll make you all mine~"
    jump fight_slimeprincess_victory_main_curse


label fight_slimeprincess_dry:
    call escapeRestraint from _call_escapeRestraint_3 
    stop music fadeout 5
    stop sound fadeout 3
    "After cumming again and again, you're finally exhausted of all your levels..."
    "[slimePrincess]" "Ugh~ You're barely spurting any XP anymore~!"
    call hideAllSlimePrincess from _call_hideAllSlimePrincess_8 
    "The slime gets off of you and gives you a cheeky smile..."
    show slimeprincess_smug with myDissolve
    pause 0.5
    "[slimePrincess]" "Kufufu~ But I suppose that just means I've drained you dry, huh~?"
    "[slimePrincess]" "What a pathetic human~ Losing in such a humiliating way~"
    "[slimePrincess]" "Whatever happened to proving your strength hmm~? If you really wanted to prove it, you could have just escaped, right~?"
    "[slimePrincess]" "Ohohoho~ Did you finally realize your place beneath me perhaps~?"
    "[slimePrincess]" "This power I have over you... It feels amazing~"
    "[slimePrincess]" "You're no different from my other servants, really~"
    "[slimePrincess]" "I should just make you my pet, right here, right now~"
    "[slimePrincess]" "..."
    hide slimeprincess_smug with myDissolve
    show slimeprincess_laugh with myDissolve
    "[slimePrincess]" "But I won't~"
    "[slimePrincess]" "You're at my mercy and I'm choosing to let you go, human peasant~"
    "[slimePrincess]" "So go, I'll have my guards escort you to the slime village inn. A weakling like you isn't worth my time~"
    scene black with myDissolve
    "The princess calls some guards to pick you up and escort you to the slime inn..."
    "..."
    pause 0.5
    "You wake up in the inn"
    call player_dead_slimevillage from _call_player_dead_slimevillage_3