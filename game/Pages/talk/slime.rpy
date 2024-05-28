default slime_slimeprincess_dialogue = False
label slime_talk:
    call hideAllChara from _call_hideAllChara_1
    show slime_main with myDissolve

    if player.conditions.slimePet and not isTalking:
        "[slime]" "Hey hey~ if it isn't my little dummy~!"
        "[slime]" "Hehe~ Wanna feel my sticky mouth again soon~?"
        if player.conditions.princessServant and not slime_slimeprincess_dialogue:
            "[slime]" "...Wait a second..."
            show slime_main_sad with myDissolve
            hide slime_main
            "[slime]" "{color=#F48FB1}She{/color} captured you? Don't tell me she made you into another servant..."
            "[slime]" "Sigh... She really is strong huh..."
            "[slime]" "I guess our plan failed then..." 
            show slime_main with myDissolve
            hide slime_main_sad
            "[slime]" "Well, I'm sure you still tried, right?"
            "[slime]" "Hey~"
            "[slime]" "It shouldn't be too late, I think I might know a way to heal you of her curse~"
            "[slime]" "If we do that, you might be able to try again~!"
            $ slime_slimeprincess_dialogue = True

    elif isTalking == False:
        if player.conditions.princessServant:
            "[slime]" "What's up?"
        else:
            "[slime]" "Oooh~ You wanna talk about something?"
            "[slime]" "What is it, [pronouns.mister]~?"
    else:
        "[slime]" "Aaany other questions~?"
    $ isTalking = True
    menu slime_talk_mainMenu:
        "About Skye":
            "[slime]" "Me~? Hehe what do you wanna know?"
            call slime_talk_slime from _call_slime_talk_slime
        "About the slime princess":
            call slime_talk_slimeprincess from _call_slime_talk_slimeprincess
        "Bye":
            "[slime]" "Hehe~ See you in the forest, [pronouns.mister]~"
            call move("forest_3") from _call_move_8
    
    jump slime_talk

label slime_talk_slime:
    call hideAllChara
    show slime_main with myDissolve
    menu slime_talk_slime_menu:
        "About family":
            "[slime]" "Hmm... I suppose I've known you for a while now..."
            "[slime]" "I don't really like my family too much, hehe~"
            "[slime]" "..."
            show slime_main_sad with myDissolve
            hide slime_main with myDissolve
            "[slime]" "...Well, I REALLY don't like them."
            "[slime]" "Most slimes are born to serve the slime queen. There are special breeding grounds where we use nectar to reproduce"
            "[slime]" "I wasn't born like that though... hehe..."
            "[slime]" "Um..."
            "[slime]" "Sorry, can we talk about something else..."
        
        "Why do you keep your XP?":
            show slime_main with myDissolve
            hide slime_main_sad
            "[slime]""Why do I keep my XP?"
            "[slime]""Oh~? You mean compared to those lesser slimes?"
            "[slime]""They all serve the slime princess and give their XP to her."
            "[slime]""Hehe~ Why would you give up your XP if you're the one who earned it~? It's a bit silly isn't it?"
            "[slime]""Anyway, it's a long story, hehe~ Don't worry about it too much~"
            hide slime_main with myDissolve
            call hideAllSlime from _call_hideAllSlime_20
            show slime_sexy with myDissolve
            "[slime]" "Besides, isn't it much more fun to see me grow big~? I'm already level [slime.level], you know~?"
        "I love you" if player.conditions.slimePet:
            "[slime]" "Aww~ Hehe~ That's sweet"
            if (slime.inventory.armor.health > player.inventory.armor.health):
                "[slime]" "And don't worry, I know~"
                "[slime]" "Remember when you gave me your armor~? I'm still wearing it, y'know~?"
                "[slime]" "Maybe if you bring me something even better I'll use that instead~"
            else:
                "[slime]" "I just make you feel that good huh~? Like you can't seem to stay away~"
                "[slime]" "Hey hey~ If you really love me, you'll do something for me, right~?"
                if (player.inventory.armor.name == "nothing"):
                    "[slime]" "Go buy some armor and give it to me, okay~?"
                    "[slime]" "It'd be sooo sweet of you~ You'll do it for me, right [pronouns.mister]~?"
                    "[slime]" "Hehe~ I'll be here waiting when you've got some"
                else:
                    "[slime]" "Hey hey~"
                    "[slime]" "Give me your armor~"
                    "[slime]" "You're a human~ You can buy armor as you like, I'm just a weak little slime~"
                    "[slime]" "So~ Good deal isn't it [pronouns.mister]~? You get my love and I get your armor~"
                    "[slime]" "Deal~?"
                    menu:
                        "Deal":
                            "[slime]" "Hehehe~ Perfect~ Come on, give it to me then~"
                            "You took off your armor and handed it to [slime.profile.name]"
                            "[slime]" "Wonderful~ Good job little human~"
                            "{color=#f00} You lost [player.inventory.armor.name]"
                            "{color=#0f0} [slime.profile.name] equipped [player.inventory.armor.name]."
                            
                            $ slime.inventory.armor = player.inventory.armor
                            $ player.inventory.unlockedArmors.remove(player.inventory.armor)
                            $ player.inventory.armor = armors[0]
                            
                            hide slime_main with myDissolve
                            call hideAllSlime from _call_hideAllSlime_12
                            show slime_sexy with myDissolve
                            "[slime]" "Hey hey~ Without armor those levels aren't very useful either, right~?"
                            "[slime]" "Come here~ I'll only take one~"
                            hide slime_sexy with myDissolve
                            show slime_mount with myDissolve
                            "Before you have time to respond, [slime.profile.name] climbs on top of you and begins draining you"
                            call levelDrain(player, slime, player.XP - player.levelBottom + 1) from _call_levelDrain_19
                            "[slime]" "Ahh~ I just love how that feels~ I'll keep it all to myself~"
                            hide slime_mount with myDissolve
                            show slime_sexy with myDissolve
                            "[slime]" "You sure are dedicated to me huh~? So cute~"
                            "[slime.profile.name] gets off of you."
                            hide slime_sexy with myDissolve
                            show slime_main with myDissolve
                            "[slime]" "Hehe~ Anywaay~ Anything else you'd like to know about me, [pronouns.mister]~?"
                            "[slime]" "Hope you don't mind me borrowing a little XP~ We're friends after all, aren't we~?"
                        
                        "No":
                            "[slime]" "Oh come oooon~ I thought you loved me!"
                            "[slime]" "Sigh~ Fiiine~"
                            "[slime]" "Dumb human..."

        
        "Back":
            call slime_talk_mainMenu from _call_slime_talk_mainMenu
    
    jump slime_talk_slime

label slime_talk_slimeprincess:
    if player.conditions.princessServant:
        hide slime_main with myDissolve
        call hideAllSlime from _call_hideAllSlime_21
        show slime_main_sad
        "[slime]" "..."
        menu:
            "...":
                "[slime]" "..."
                "[slime]" "Let's move on."
            "I want to remove her curse" if player.level > 2:
                show slime_main with myDissolve
                hide slime_main_sad with myDissolve
                "[slime]" "You do? Good job!"
                "[slime]" "I told you she's no good~ I'm glad you listened to me, [pronouns.mister]~"
                "[slime]" "Hey hey, stick your hand right between my boobs and I'll take care of it, okay [pronouns.mister]~?"
                hide slime_main with myDissolve
                show slime_boobpush with myDissolve
                play sound handjoblowspeed loop
                play audio "/audio/slime/11w4.mp3"
                "[slime]" "Hehe~ Just like that~ Let me do all the heavy work while you just relax, okay~?"
                "[slime]" "I'll be your caretaker, all you need to do is breathe and squeeze my core, then everything will be back to normal~"
                "[slime]" "Hey hey~ It does feel good doesn't it~? I'm almost done~"
                play audio item1
                call clearStatusEffect(2) from _call_clearStatusEffect_2
                play audio "/audio/slime/11w7.mp3"
                "[slime]" "Here you are~ I'm afraid I can't help you with your title but I'm sure you'll find a way to change it soon anyway, hehe~"
                "[slime]" "..."
                play music sussy2 volume 0.25
                "[slime]" "You know~"
                "[slime]" "You should really be more thankful that I'm even helping you out with this~"
                "[slime]" "I mean~"
                "[slime]" "I'm offering my help to you, letting you touch me like this~"
                "[slime]" "Don't you think it's fair if I..."
                "[slime]" "Just..."
                play audio "/audio/slime/11w9.mp3"
                call levelDrain(player, slime, 50) from _call_levelDrain_20
                "[slime]" "Kufufu~ What? Don't pretend you don't like this~"
                "[slime]" "Besides, I'm only taking a little~ What's the harm in that, right~?"
                "[slime]" "This is just payback for making me remove your curse~ It's only fair~"
                "[slime]" "..."
                play audio "/audio/slime/11w5.mp3"
                call levelDrain(player, slime, 100) from _call_levelDrain_21
                "[slime]" "Kufufu~ Okay okay, I'm done~"
                "[slime]" "It's your fault for being so weak though~"
                stop sound fadeout 3
                stop music fadeout 20
                hide slime_boobpush with myDissolve
                show slime_main with myDissolve
                "[slime]" "..."
                "..."
                "Skye looks happy."
                return
    else:
        "[slime]" "The slime princess?"
        "[slime]" "...What about her?"
        "[slime]" "..."
        show slime_main_sad with myDissolve
        hide slime_main with myDissolve
        "[slime]" "..."
        "[slime]" "Look, I don't like her very much... Okay?"
        "[slime]" "She lives in slime village, she steals from others and she's selfish..."
        "[slime]" "And of course~"
        hide slime_main_sad with myDissolve
        show slime_sexy with myDissolve
        "[slime]" "She's nowhere near as cute as I am~"
        "[slime]" "Right [pronouns.mister]~? 💙"
        hide slime_sexy with myDissolve
        show slime_main with myDissolve
        return
    jump slime_talk

