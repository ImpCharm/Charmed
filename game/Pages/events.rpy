default deal = False

label forest_slime_choice:
    $ deal = False
    $ game.levelDrainSlimeEvent = False
    call calculateLevelAll from _call_calculateLevelAll
    "You see a lone slime girl in the distance..."
    menu:
        "Approach her":
            show slime_main with myDissolve
            "[slime]" "Ohh~? A human?"
            "[slime]" "Wait a second! It's you!"
            "[slime]" "This is just perfect~! I was just feeling hungry as well~"
            "[slime]" "Can I have a little XP [pronouns.mister]~? I won't take much I promise~"
            menu:              
                "Give her XP":
                    label forest_slime_choice_accept:
                    play music sussy volume 0.25
                    "[slime]" "Hehehe yay~! Here I go~"
                    hide slime_main with myDissolve
                    "The slime girl puts her slimy body on top of yours and presses you down, it feels hard to move."
                    show slime_mount at continuousBounce with myDissolve
                    "[slime]" "Hehehe~ Thanks [pronouns.mister]~"
                    "[slime]" "Don't try to resist okay~? I've been told it feels much better that way~"
                    call whitePyu from _call_whitePyu_2
                    call levelDrain(player, slime, (player.XP - player.levelBottom + 1)) from _call_levelDrain_9
                    "[slime]" "Ufufu~ Doesn't that feel amazing~? I bet you've never felt a slime girls pussy before right~?"
                    "[slime]" "My slimy walls pushing against your pretty dick~ As I cover you in my slime~"
                    "[slime]" "Hey hey~ Let's keep going a little longer okay~? You feel good don't you~?"
                    menu:             
                        "...":
                            "[slime]" "Hehehe~ See~? I knew you were enjoying this~"
                            call whitePyu from _call_whitePyu_3
                            call levelDrain(player, slime, (player.XP - player.levelBottom + 1)) from _call_levelDrain_10
                            "[slime]" "Can you feel your power leaving your body~?"
                            "[slime]" "Hooonestly~ You should be the one thanking me~"
                            if deal:
                                "[slime]" "I think it'd only be fair if I did this for free, don't you think~? I mean, with how good you're feeling and all~"
                            else:
                                "[slime]" "I think it'd only be fair if I took a little more XP right~? As a reward for helping you feel sooo good~"
                            "[slime]" "Right [pronouns.mister]~?"
                            menu:
                                "That makes sense...":
                                    "[slime]" "Hehehe~ That's what I thought~"
                                    "[slime]" "Are you really enjoying my slimy body this much~? I'm flattered~"
                                    call whitePyu from _call_whitePyu_4
                                    call levelDrain(player, slime, (player.XP - player.levelBottom + 1)) from _call_levelDrain_11
                                    "[slime]" "Ahh~ Just what I needed~ Thanks for the levels [pronouns.mister]~"
                                    call slime_skyecheck from _call_slime_skyecheck_3
                                    hide slime_mount with myDissolve
                                    show slime_main with myDissolve
                                    "With that, the slime walks away and leaves you lying on the ground, drained."
                                    show slime_main at asyncDissolve(2)
                                    "..."
                                    if deal:
                                        "She really didn't give you any money either..."
                                    "You get back up and continue your journey with a few levels less..."

                                "That's enough":
                                    "[slime]" "Aww fiiine~"
                                    if deal:
                                        "[slime]" "Well then, a promise is a promise~ Here's your gold~"
                                        call gainMoney(player, 20) from _call_gainMoney_2
                                    call slime_skyecheck from _call_slime_skyecheck_2
                                    "[slime]" "See you later [pronouns.mister]~ I'll be here when you want more~"

                        "Push her off":
                            "[slime]" "Aww already~?"
                            hide slime_mount with myDissolve
                            show slime_main with myDissolve
                            "[slime]" "Fine~ Thanks for the XP anyway [pronouns.mister]~"
                            call slime_skyecheck from _call_slime_skyecheck_1
                            "[slime]" "See you soon hopefully~!"

                "Refuse":
                    "[slime]" "Awww! Why not? Do you really not have any mercy?"
                    "[slime]" "Fine... I'll give you... 20 gold in return~"
                    "[slime]" "Deal?"
                    menu:
                        "Deal":
                            $ deal = True
                            jump forest_slime_choice_accept
                        "No deal":
                            "[slime]" "Hmpf, fine~ be selfish~"
                            "[slime]" "I'll be here when you change your mind though~"

        "Ignore her":
            "You decide not to bother her..."
    return                                    

label event_forest_shopkeeper:
    $ shopKeeperStatus = "walking"
    "[shopKeeper]" "Adventurer! Hey!"
    show shopkeeper_forest with myDissolve
    "[shopKeeper]" "fancy seeing you here!"
    "[shopKeeper]" "Are you here collecting XP for your journey? Remember to be careful, okay?"
    "[shopKeeper]" "Ah speaking of which..."
    hide shopkeeper_forest with myDissolve
    "The girl looks through her bag and grabs a small, green bottle."
    "[shopKeeper]" "I noticed you look pretty hurt so this should help you recover!"
    show shopkeeper_close with myDissolve
    "[shopKeeper]" "...As much as I think you're being brave right now though, I still need to make a living..."
    "[shopKeeper]" "I can sell it for {color=#ff0}30G{/color} for now, okay? It'll completely cure you of all your wounds!"
    menu:
        "Buy" if player.money >= 30:
            call loseMoney(player, 30) from _call_loseMoney
            hide shopkeeper_close with myDissolve
            show shopkeeper_leanforward with myDissolve
            "[shopKeeper]" "Great! Now just stand still...?"
            "[shopKeeper]" "Aaaand..."
            call restore(player, True) from _call_restore_2
            "{color=#0f0}Your health, status effects and arousal have been restored!"
            "[shopKeeper]" "Done!"
            "[shopKeeper]" "I'll be heading to my shop now. It's almost night isn't it?"
            "[shopKeeper]" "Remember to be careful! And get some rest, it's the best medicine, really~"
            "[shopKeeper]" "See you later!"
            hide shopkeeper_leanforward with myDissolve
            
        "Don't buy":
            hide shopkeeper_close with myDissolve
            show shopkeeper_stand with myDissolve
            "[shopKeeper]" "Oh!"
            "[shopKeeper]" "No worries, I understand!"
            hide shopkeeper_stand with myDissolve
            show shopkeeper_leanforward_open with myDissolve
            "[shopKeeper]" "Just remember to take good care of yourself, okay?"
            "[shopKeeper]" "And try to get to a safe place at night. That's when the monsters are most prominent here..."
            hide shopkeeper_leanforward_open with myDissolve
            show shopkeeper_leanforward with myDissolve
            "[shopKeeper]" "Anyway~ I'll be off to my shop now. See you later, adventurer!"
            hide shopkeeper_leanforward with myDissolve

    "The girl walks off towards the town."
    return
        

    

# merchant events
label event_cave_merchant_scam:
    "As you walk through the cave you suddenly see a girl approach you."
    if merchant.profile.favor > 0:
        menu:
            "Let her":
                pass
            "Avoid her":
                return
    else:
        $ merchant.profile.favor += 1

    "[merchant]" "Oi~ [pronouns.mister], over here~"
    show merchant_handboob with myDissolve
    play audio "/audio/merchant/22p2.mp3"
    "[merchant]" "Before you have time to respond, she circles around your body, inspecting it."
    "[merchant]" "Ahh~ I see, I see~"
    "[merchant]" "Mhm mhm~"
    hide merchant_handboob with myDissolve
    "[merchant]" "She keeps inspecting you, her quick movements leaving you unable to react."
    show merchant_handboob with myDissolve
    "[merchant]" "Yup~ I can see it clearly~ You're poisoned, aren'cha [pronouns.mister]~?"
    "[merchant]" "Mhm mhm~ There's no doubt about it, how unlucky~"
    hide merchant_handboob with myDissolve
    show merchant_lean_closed
    "[merchant]" "Well luckily for you, I've got just the thing you need~"
    "[merchant]" "That's..."
    "The girl rummages through her bag, quickly grabbing a small, purple bottle."
    show merchant_lean_open with myDissolve
    hide merchant_lean_closed
    "[merchant]" "Here~ I've got exactly what you're looking for~"
    "[merchant]" "It's a cure for poison~ Juuust for you~"
    "[merchant]" "And it'll only cost you..."
    "[merchant]" "[round(mathFloor(0.01 * (player.money + 111)) / 0.01)] gold~"
    menu:
        "Not enough gold":
            pass
        "Walk away":
            jump event_cave_merchant_scam_leave
    show merchant_lean_open with myDissolve
    hide merchant_lean_closed
    play audio "/audio/merchant/22w1.mp3"
    call clearAllLipstick from _call_clearAllLipstick
    play music sussy volume 0.25
    "[merchant]" "Kyahaha~ Aww you don't have enough~?"
    "[merchant]" "Hmm~ How about this... I'll give ya a slight discount in exchange for a single level~ Pretty simple deal right?"
    "[merchant]" "You've got so many of 'em anyway~ And you really don't wanna lose because of poison, do ya~?"
    show merchant_lean_open with myDissolve
    hide merchant_lean_closed
    "[merchant]" "What do ya say~? Sound fair, [pronouns.mister]~?"
    menu:
        "Deal":
            pass
        "Walk away":
            jump event_cave_merchant_scam_leave
    play audio "/audio/merchant/22w2.mp3" 
    "[merchant]" "Kyahaha~ Great~ Come here then, dummy~"
    play audio blow1
    hide merchant_lean_open
    show merchant_flipAss
    "Womp~"
    "Before you can react, she pushes you to the ground and pushes her ass into your face."
    "[merchant]" "Kyahaha~! Kiss it, dummy, kiss my ass~"
    "[merchant]" "You agreed to my deal right~? This is just how I drain XP~ You can't back out now~"
    play audio kisssound01
    "She pushes her ass deeper into your face, forcing you to kiss it."
    call levelDrain(player, merchant, player.XP - player.levelBottom + 10) from _call_levelDrain_12
    "[merchant]" "There we are~ You want your discount now huh~? Sure~"
    hide merchant_flipAss with myDissolve
    show merchant_lean_closed with myDissolve
    "[merchant]" "Well then~ Your new price will beee..."
    play audio "/audio/merchant/22w3.mp3" 
    "[merchant]" "[round(mathFloor(0.1*(player.money + 11))/0.1)] gold~ Much better right~?"
    menu:
        "Not enough gold":
            pass
        "Walk away":
            jump event_cave_merchant_scam_leave
    hide merchant_lean_closed with myDissolve
    show merchant_handboob with myDissolve
    play audio "/audio/merchant/22w5.mp3" 
    "[merchant]" "Ehh~? You still don't have enough~? You're not broke are you~?"
    "[merchant]" "Hmm~ Fine fine~ Since I'm soooo kind, I'll give ya another discount, 'kay~?"
    "[merchant]" "Ufuu~ You know what I want in return, right~? Just a single level and we'll be good~"
    "[merchant]" "I'll just..."
    play sound pistonslightlydrylowspeed12times loop
    play audio "/audio/merchant/22w6.mp3"
    hide merchant_handboob with myDissolve
    show merchant_paizuri at continuousBounce()
    "[merchant]" "Ufuu~ How does this feel~? Remember, we're just doing business here, right~?"
    "[merchant]" "You could just walk away if you didn't wanna do this, right~? And besides, you really need this cure don't you~? Ya don't wanna end up poisoned, right~?"
    "[merchant]" "I'll drain you a little more~ you need me, don't forget that~"
    "[merchant]" "Come on, leak those levels for me~"
    hide merchant_paizuri
    show merchant_paizuri_cum at continuousBounce()
    call pyupyu from _call_pyupyu_5
    pause 0.5
    stop sound fadeout 1
    show merchant_paizuri_cum at continuousBounce(1.1, 1) with myDissolve
    call levelDrain(player, merchant, player.XP - player.levelBottom + 10) from _call_levelDrain_13
    play audio "/audio/merchant/22w7.mp3"
    "[merchant]" "Kyahaha~ Oh, I love how that feels~ It feels amazing for you too doesn't it~?"
    "[merchant]" "I'll get off ya now~ You've still got a cure to buy, right~?"
    
    hide merchant_paizuri_cum with myDissolve
    show merchant_stand with myDissolve
    "[merchant]" "Well then~ You've given me a buncha levels so I'll cut ya a deal, okay~?"
    "[merchant]" "Considering I'm pretty generous this is one of my final offers~"
    show merchant_stand at merchant_zoomin(1, 1.2, 1)
    "She grabs the cure and dangles it in front of your face..."
    "[merchant]" "Lookie look [pronouns.mister]~ You want it, right~? Don't you want it~?"
    "[merchant]" "You know how dangerous poison is, right~? You wouldn't want to be caught off guard while poisoned~"
    "[merchant]" "I'll sell it to ya, okay~?"
    "[merchant]" "I'll sell it for only..."
    "[merchant]" "..."
    show merchant_stand at merchant_zoomin(1.2, 1.5, 2)
    pause 2.0
    play audio "/audio/merchant/22w8.mp3"
    $ renpy.music.set_pause(True, channel="music")
    "[merchant]" "[player.money + 1] gold~"
    "[merchant]" "Hey hey~ You've got enough cash on ya, right [pronouns.mister]~?"
    "[merchant]" "I'm really not even charging that much, am I~?"
    "[merchant]" "So, do we have a deal~? You can't really walk away after giving me all those levels, can you~?"
    menu:
        "Not enough gold":
            pass
        "Walk away":
            jump event_cave_merchant_scam_leave

    show merchant_stand at merchant_zoomin(1.5, 1.0, 0.5)
    pause 0.4
    $ renpy.music.set_pause(False, channel="music")
    hide merchant_stand with myDissolve
    show merchant_lean_open with myDissolve
    play audio "/audio/merchant/22w9.mp3"
    "[merchant]" "Eehh~? Still not enough~?"
    "[merchant]" "You're a total brokie, y'know that [pronouns.mister]~?"
    "[merchant]" "Fine fine~ This one time only I'll give you one final offer for just one more level~"
    "[merchant]" "You've already come this far, you don't want all those levels to just go to waste, do ya~?"
    "[merchant]" "Do we have a deal~? Just one more level~"
    menu:
        "Deal":
            pass
        "Walk away":
            jump event_cave_merchant_scam_leave
    hide merchant_lean_open with myDissolve
    show merchant_stand with myDissolve
    "[merchant]" "Pleasure doing business wicha, [pronouns.mister]~"
    show merchant_stand at merchant_zoomin(1, 1.8, 0.6)
    pause 0.6
    hide merchant_stand with Dissolve(0.1)
    show merchant_tongue with myDissolve
    "[merchant]" "Now c'mere and let me kiss those levels out of ya~"
    show merchant_tongue at merchant_closekiss with myDissolve
    play sound sucking041 loop
    play audio kisssound09
    play audio "/audio/merchant/22w1.mp3"
    call calculateLevelAll from _call_calculateLevelAll_1
    "[merchant]" "The girl presses her tongue against yours and deeply kisses you."
    show merchant_tongue at merchant_closekiss_kiss
    show screen lipstickMark(0.4, -0.3, 0.8, 1.5, 1.5, 0, False) onlayer kiss1
    pause 0.5
    play audio kisssound01
    "[merchant]" "Mwaahh~"
    call levelDrain(player, merchant, player.XP - player.levelBottom + 10) from _call_levelDrain_14
    play audio "/audio/merchant/22f2.mp3"
    "[merchant]" "Aammffhh~"
    "Despite having already drained some of your levels, she keeps kissing you..."
    menu:
        "This isn't so bad...":
            call event_cave_merchant_scam_kiss from _call_event_cave_merchant_scam_kiss
        
        "Push her off and continue the deal":
            call event_cave_merchant_scam_boring from _call_event_cave_merchant_scam_boring

    menu:
        "Buy":
            pass

        "Walk away":
            jump event_cave_merchant_scam_leave
    
    call hideAllMerchant from _call_hideAllMerchant
    show merchant_lean_open with myDissolve
    "[merchant]" "Kufyuu~ Perfect~! I'm totally starting to like ya, y'know~?"
    "[merchant]" "Here ya go, [pronouns.mister]~"
    $ player.conditions.poisoned = 0
    $ merchant.profile.favor += 1
    play audio item1
    "{size=50} {color=#0f0}\[Your poison ended!\]"
    call loseMoney(player, 10) from _call_loseMoney_1
    
    if pronouns.mister == "mister":
        "[merchant]" "Kyahahaha~! See you around then miiister~"
    elif pronouns.mister == "miss":
        "[merchant]" "Kyahahaha~! See you around then miiissy~"
    else:
        "[merchant]" "Kyahahaha~! See you around then duuummy~"

    "[merchant]" "I've got some urgent matters to get to~ Make sure to say hi if you ever see me again, 'kay~?"
    hide merchant_stand
    show merchant_lean_closed
    "[merchant]" "Hey hey~ One more thing, come here for a moment~"
    menu:
        "Okay":
            pass
            
        "No":
            hide merchant_lean_closed with myDissolve
            call hideAllMerchant from _call_hideAllMerchant_1
            show merchant_stand with myDissolve
            "[merchant]" "Geez~ Don't be such a bore~"
            show merchant_stand at slideInLeft(0.5, 0.5, 1)
            "[merchant]" "Oh well, your loss~ Bye [pronouns.mister]~"
            show merchant_stand at slideInLeft(0.5, -0.2, 2)
            "The girl walks off and leaves and heads off towards slime village."
            "..."
            "...You return to your journey"
            stop music fadeout 3
            return

    show merchant_lean_closed at merchant_zoomin(1, 1.8, 0.6)
    pause 0.6
    call hideAllMerchant from _call_hideAllMerchant_2
    show merchant_tongue with myDissolve
    play audio kisssound16
    show screen lipstickMark(0.3, 0.3, 1, 2, 1.0) onlayer kiss7
    $ player.arousal = 100
    call updateArousal from _call_updateArousal_3
    "[merchant]" "Mwahh~"
    "{color=#f00}Your arousal increased!"
    hide merchant_tongue with myDissolve
    show merchant_handboob with myDissolve
    play audio "/audio/merchant/22w2.mp3"
    "[merchant]" "See ya, dummy~ Don't dream about me too much~ Kyahaha~!"
    show merchant_handboob at asyncDissolve2(1.0, 0, 3)
    "The girl walks off and leaves and heads off towards slime village."
    "..."
    "...You take a moment to breathe and return to your journey..."
    stop music fadeout 3
    return

label event_cave_merchant_scam_kiss:
    play audio "/audio/merchant/22f1.mp3"
    "The girl keeps pushing her tongue deeper into your mouth, leaving your tongue completely overpowered by hers."
    "You hear her moan and grasp for air as you taste her sweet saliva and you feel your power leaving your body..."
    
    call calculateLevelAll from _call_calculateLevelAll_2
    show merchant_tongue at merchant_closekiss_kiss2
    show screen lipstickMark(0.1, -0.3, 0.5, 2, 1.3, 10, False) onlayer kiss2
    play audio kisssound07
    play audio "/audio/merchant/22f3.mp3"
    call levelDrain(player, merchant, player.XP - player.levelBottom + 10) from _call_levelDrain_15

    show merchant_tongue at merchant_closekiss_kiss
    show screen lipstickMark(0.5, 0.4, 0.5, 2, 0.9, 20, True) onlayer kiss3
    play audio kisssound09
    play audio "/audio/merchant/22f4.mp3"

    "[merchant]" "Mwahh~~"

    call levelDrain(player, merchant, player.XP - player.levelBottom + 10) from _call_levelDrain_16

    show merchant_tongue at merchant_closekiss_kiss2
    show screen lipstickMark(0.1, -0.1, 0.5, 2, 1.2) onlayer kiss4
    play audio "/audio/merchant/22f5.mp3"
    play audio kisssound10
    "[merchant]" "Mwaahhh~~"
    call levelDrain(player, merchant, player.XP - player.levelBottom + 10) from _call_levelDrain_17

    show merchant_tongue at merchant_closekiss_kiss2
    show screen lipstickMark(-0.0, 0.3, 1, 2, 1.0, -5, False) onlayer kiss5
    play audio longsmooch
    play audio "/audio/merchant/22f6.mp3"
    "She pushes your face deeper into hers, moaning with each level she absorbs, leaving you completely dazed and out of breath..."
    "[merchant]" "Ahhn~~ Amazing isn't it~?"

    show merchant_tongue at merchant_closekiss_kiss2
    show screen lipstickMark(0.3, 0.3, 1, 2, 0.7) onlayer kiss6
    play audio kisssound16
    play audio "/audio/merchant/22f3.mp3"
    "[merchant]" "Mwah~"
    call levelDrain(player, merchant, player.XP - player.levelBottom + 10) from _call_levelDrain_18
    "[merchant]" "I'll use my kisses to make you mine~ Mmwah~"
    play audio "/audio/merchant/22n1.mp3"
    "[merchant]" "Mmmnn..."
    show merchant_tongue with myDissolve
    stop sound fadeout 3
    stop music fadeout 10
    play audio "/audio/merchant/22f1.mp3"
    "[merchant]" "Ahh~"
    "The girl moans as she pulls away from your face, both of your tongues dripping with saliva..."
    "She swallows and wipes the remaining saliva off of her mouth..."
    "[merchant]" "Ahahah~ Amazing~! You leaked so many levels, [pronouns.mister]~"
    "She takes a deep breath and regains her composure..."
    hide merchant_tongue with myDissolve
    show merchant_lean_open with myDissolve
    "[merchant]" "Kufufu~ How amazing was that huh~?"
    "[merchant]" "Well then, you probably want your cure, right?"
    "[merchant]" "Ufufu~ I'll give it to ya foooooor~"
    "[merchant]" "..."
    "[merchant]" "..."
    "[merchant]" "..."
    show merchant_lean_closed with myDissolve
    hide merchant_lean_open with myDissolve
    $ merchant.profile.favor += 1
    "[merchant]" "10 gold~! Sound good, dummy~?"
    return
    
label event_cave_merchant_scam_boring:
    stop sound fadeout 2
    stop music fadeout 3
    hide merchant_tongue with myDissolve
    call hideAllMerchant from _call_hideAllMerchant_3
    show merchant_lean_closed with myDissolve
    "She takes a deep breath and regains her composure and wipes her lips..."
    "[merchant]" "Booring~ Oh well, a deal's a deal~"
    "[merchant]" "I'll give ya your cure foooor...~"
    "[merchant]" "10 gold~ Sound good, [pronouns.mister]~?"
    return

label event_cave_merchant_scam_leave:
    call hideAllMerchant from _call_hideAllMerchant_4
    "You ignore her and walk away..."
    stop music fadeout 3
    return

label event_cave_poison_trap:
    "As you walk through the cave, you suddenly feel something near your foot..!"
    "You stepped on a booby trap"
    call gainStatusEffect(0, 5) from _call_gainStatusEffect
    return
# merchants end