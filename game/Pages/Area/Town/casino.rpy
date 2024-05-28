label town_casino:
    stop music fadeout 5
    call areaMarker("casino") from _call_areaMarker_9
    scene casino with myDissolve
    if(game.casinoUnlocked == False):
        call town_casino_introcutscene from _call_town_casino_introcutscene
    show casinogirlwhite_sit with myDissolve
    hide screen casinoGui with myDissolve
    
    $ game.casinoDebt += casinoOwed;
    $ casinoOwed = 0
    $ casinoBetAmount = 0
    $ casinoRouletteDoubled = 0

    if game.casinoRouletteUnlocked == True and game.casinoDebt > 0 and game.casinoDebtCutscene == True:
        $ game.casinoDebtCutscene = False
        "[casinoGirlWhite]" "Ah~ You look like you enjoyed yourself~"
        "[casinoGirlWhite]" "You seem to have accumulated some debt though~ Don't worry, you can pay it off here~"
        "[casinoGirlWhite]" "In the meantime you'll be assigned a curse that increases your arousal intake~"
        "[casinoGirlWhite]" "It's nothing personal really~ It's just a way to make sure our clients pay us back~"    
        "[casinoGirlWhite]" "I do hope you understand~"    
        call gainStatusEffect(4) from _call_gainStatusEffect_2

    if game.casinoDebt > 0 and player.conditions.casinoDebt == False:
        call gainStatusEffect(4) from _call_gainStatusEffect_3

    if game.casinoDebt == 0 and player.conditions.casinoDebt:
        call clearStatusEffect(4) from _call_clearStatusEffect_1
        

    menu:
        "Play":
            call town_casino_play from _call_town_casino_play
        "Talk":
            call casinogirlwhite_talk from _call_casinogirlwhite_talk
        "Pay off debt" if game.casinoDebt > 0:
            call town_casino_payoffdebt from _call_town_casino_payoffdebt
        "Exit":
            call move("town_central") from _call_move_11
    
    jump town_casino

label town_casino_payoffdebt:
    default amountToPayOff = "0"
    "[casinoGirlWhite]" "Ahahah~ You're in debt? How unfortunate~"
    "[casinoGirlWhite]" "Don't worry, You can pay it off right here~"
    "[casinoGirlWhite]" "How much would you like to repay?"
    $ amountToPayOff = renpy.input("   Your debt: [game.casinoDebt]\nYour money: [player.money]", allow="0123456789")

    if amountToPayOff == "":
        return

    $ amountToPayOff = int(amountToPayOff)

    if amountToPayOff > player.money:
        "[casinoGirlWhite]" "Ahaha~ sorry but you don't have that much money~"
        return
    if amountToPayOff > game.casinoDebt:
        $ amountToPayOff = game.casinoDebt

    call loseMoney(player, amountToPayOff) from _call_loseMoney_4
    $ game.casinoDebt -= amountToPayOff
    return

label town_casino_introcutscene:
    "You walk into the casino, there are various tables with games around the room."
    "There's a girl with red hair, dressed in a bunnysuit standing near one of the tables, presumably waiting for a new player for her to play with..."
    "Suddenly, you hear someone call out for you"
    "[casinoGirlWhite]" "Ahem~ Over here"
    show casinogirlwhite_sit with myDissolve
    "[casinoGirlWhite]" "Welcome, sweetheart. Is this your first time here? I don't believe I've seen you around before."
    "[casinoGirlWhite]" "My, it is? Alright then, allow me to explain how we operate around here~"
    "[casinoGirlWhite]" "Follow me please~"
    hide casinogirlwhite_sit with myDissolve
    show casinogirlwhite_pits with myDissolve
    "[casinoGirlWhite]" "Behind me, you'll find a selection of games, we're currently short on staff so only one game will be playable as of right now."
    "[casinoGirlWhite]" "You can bet an amount of money at the games. If you win, you'll earn money based on how much you initially bet."
    "[casinoGirlWhite]" "If you lose, however, the opponent will keep your bet."
    "[casinoGirlWhite]" "You can always try to win it back, of course~ But do be careful, trying to earn your money back is a slippery slope to debt."
    hide casinogirlwhite_pits with myDissolve
    show casinogirlwhite_sit with myDissolve
    "[casinoGirlWhite]" "Anyway~ Go talk to my colleague at the table if you'd like to play~"
    "[casinoGirlWhite]" "If you've got any more questions, you can talk to me here at the reception."
    $ game.casinoUnlocked = True
    return

label town_casino_play:
    call hideAllChara from _call_hideAllChara_2
    if player.money < 10:
        show casinogirlwhite_sit with myDissolve
        "[casinoGirlWhite]" "Oh, pardon me~"
        "[casinoGirlWhite]" "Our minimum bet is 10 gold here. I'm afraid you don't have that much~"
        "[casinoGirlWhite]" "Do come back once you've collected enough though~"
        return

    if player.level < 3:
        show casinogirlwhite_sit with myDissolve
        "[casinoGirlWhite]" "Ah, so sorry~"
        "[casinoGirlWhite]" "We actually require you to have a few levels to spare before you're allowed to play~"
        "[casinoGirlWhite]" "Sometimes players will bet levels while gambling, you see~ And to ensure everyone has a fair chance we require you to bring at least 3 levels~"
        "[casinoGirlWhite]" "I do hope you understand~"
        return

    if game.casinoRouletteUnlocked == False:
        jump town_casino_rouletteintrocutscene
    
    hide casinogirlwhite_sit with myDissolve
    show casinogirlred_boobhand with myDissolve
    "[casinoGirlRed]" "Welcome back cutie~ Wanna play some more~?"
    "[casinoGirlRed]" "I'm sure you'll do great this time~"
    jump town_casino_roulette

label town_casino_rouletteintrocutscene:
    "You approach the girl standing near the roulette table."
    $ game.casinoRouletteUnlocked = True
    $ game.casinoDebtCutscene = True
    "She's got red hair and is wearing a black bunnysuit"
    show casinogirlred_boobhand with myDissolve
    play audio "/audio/casinoRed/15w3.mp3"
    "[casinoGirlRed]" "Oh my~ Hey there cutie~"
    "[casinoGirlRed]" "Is this your first time here~? How exciting~"
    "[casinoGirlRed]" "I'll be your guide for today, okay~?"
    hide casinogirlred_boobhand with myDissolve
    show casinogirlred_pour2 at casino_zoomin(1.5, 1.5, 1, 0.8, -0.2) with myDissolve 
    "[casinoGirlRed]" "I know the casino may look scary, but trust me, it's all safe as long as you make the right choices~ Trust me~"
    "[casinoGirlRed]" "I'll be by your side the entire time~ Has my colleague explained how this pretty casino works~?"
    "[casinoGirlRed]" "You deposit cash to make a bet and depending on your result you win or lose money~ Fun right~? ❤️"
    "[casinoGirlRed]" "How about we start out by playing a game of roulette to warm you up~?"
    "[casinoGirlRed]" "Sound like fun~?"
    menu:
        "Play roulette":
            "[casinoGirlRed]" "Kufyuu~ Perfect~ The rules are simple, okay?"
            "[casinoGirlRed]" "First, you choose how much you would like to bet~"
            "[casinoGirlRed]" "Then, you'll choose either white or red~ If the roulette lands on your color, you win~! Simple, right~?"
            "[casinoGirlRed]" "If you lose, or you're feeling confident, you can always do something called 'double or nothing', this increases your bet to the next step size and disregards your previous result~"
            jump town_casino_roulette

        "Maybe later":
            "[casinoGirlRed]" "I'll be waiting here if you'd like to play~"
            return

label town_casino_roulette:
    show screen casinoGui with myDissolve
    menu:
        "Next" if casinoBetAmount > 1:
            call town_casino_roulette_colorselect from _call_town_casino_roulette_colorselect
        "Amount to bet":
            call town_casino_roulette_betselect from _call_town_casino_roulette_betselect
        "Back":
            return

    jump town_casino_roulette

label town_casino_roulette_betselect:
    menu:
        "Back":
            return
        "10" if player.money >= 10:
            $ casinoBetAmount = 10
        "15" if player.money >= 15:
            $ casinoBetAmount = 15
        "30" if player.money >= 30:
            $ casinoBetAmount = 30
        "50" if player.money >= 50:
            $ casinoBetAmount = 50
        "100" if player.money >= 100:
            $ casinoBetAmount = 100
        "250" if player.money >= 250:
            $ casinoBetAmount = 250
        "500" if player.money >= 500:
            $ casinoBetAmount = 500
    
    if casinoBetAmount <= player.money:
        "Amount set to: [casinoBetAmount]"
    else:
        "You don't have enough money."
    
    return

label town_casino_roulette_colorselect:
    menu:
        "Red":
            $ casinoBetIndex = 1
        "White":
            $ casinoBetIndex = 2
        "Back":
            return

    jump town_casino_roulette_confirm

label town_casino_roulette_confirm:
    if casinoBetIndex == 1:
        "Great choice [pronouns.mister]~ So you bet [casinoBetAmount] gold on red, right~?"
    else:
        "Great choice [pronouns.mister]~ So you bet [casinoBetAmount] gold on white, right~?"
    
    menu:
        "That's right":
            hide casinogirlred_pour2 with myDissolve
            call hideAllCasino from _call_hideAllCasino
            show casinogirlred_pits with myDissolve
            
            "[casinoGirlRed]" "Great~ Are you ready to play then cutie~?"
            "[casinoGirlRed]" "I'll spin the wheel and if it lands on your selected color you win~!"
            "[casinoGirlRed]" "Here we go~"
            "She gives the wheel a playful spin and smiles at you"

            $ casinoRouletteIndex = rand(36, 99)
            $ casinoSpinPower = 100
            jump town_casino_roulette_roll

        "Change bet":
            hide casinogirlred_pour2 with myDissolve
            call hideAllCasino from _call_hideAllCasino_1
            show casinogirlred_pits with myDissolve
            "[casinoGirlRed]" "Take all the time you need~ I'll be here when you come back"
            return

label town_casino_roulette_roll:
    $ casinoRouletteIndex += 1
    
    $ targetLL = ((casinoRouletteIndex + 34) % 36)
    $ targetL = ((casinoRouletteIndex + 35) % 36)
    $ targetM = ((casinoRouletteIndex + 36) % 36)
    $ targetR = ((casinoRouletteIndex + 37) % 36)
    $ targetRR = ((casinoRouletteIndex + 38) % 36)


    $ colorLL = "#0f7c48" if targetLL == 0 else ("#f71b23" if targetLL % 2 != 0 else "#ffffff")
    $ colorL = "#0f7c48" if targetL == 0 else ("#f71b23" if targetL % 2 != 0 else "#ffffff")
    $ colorM = "#0f7c48" if targetM == 0 else ("#f71b23" if targetM % 2 != 0 else "#ffffff")
    $ colorR = "#0f7c48" if targetR == 0 else ("#f71b23" if targetR % 2 != 0 else "#ffffff")
    $ colorRR = "#0f7c48" if targetRR == 0 else ("#f71b23" if targetRR % 2 != 0 else "#ffffff")

    $ numLeftLeft = "{color=" + colorLL + "} [" + str(casinoRouletteNumbers[targetLL]) + "]{/color}"
    $ numLeft = "{color=" + colorL + "} [" + str(casinoRouletteNumbers[targetL]) + "]{/color}"
    $ numMid = "{color=" + colorM + "} [" + str(casinoRouletteNumbers[targetM]) + "]{/color}"
    $ numRight = "{color=" + colorR + "} [" + str(casinoRouletteNumbers[targetR]) + "]{/color}"
    $ numRightRight = "{color=" + colorRR + "} [" + str(casinoRouletteNumbers[targetRR]) + "]{/color}"


    $ waitTime = float(((36 / 2)/((casinoSpinPower / 2) + 1)) * 0.1)
    # "{cps=0} num:[casinoSpinPower] waiting:[waitTime] {nw=[waitTime]} a"
    "{cps=0}  [numLeftLeft] [numLeft] {size=40} [numMid] {/size} [numRight] [numRightRight] \n ⇧ \n result {nw=[waitTime]}"
    play audio percmetronomequartzhi

    # pause waitTime

    if casinoSpinPower <= 1:
        if casinoRouletteNumbers[targetM] == 0:
            $ casinoSpinPower += 2
            $ casinoSpinPower -= 1
            jump town_casino_roulette_roll
        play audio item1
        "{cps=0}  [numLeftLeft] [numLeft] {size=50} [numMid] {/size} [numRight] [numRightRight] \n ⇧ \n result"
        jump town_casino_roulette_results
    
    $ casinoSpinPower -= 1
    jump town_casino_roulette_roll

label town_casino_roulette_results:
    $ target = ((targetM + 36) % 36)
    $ colorWon = "green" if target == 0 else ("red" if target % 2 != 0 else "white")

    "You rolled a [casinoRouletteNumbers[targetM]], which is [colorWon]!"

    if casinoRouletteDoubled == 1:
        jump town_casino_roulette_doubled1

    if casinoRouletteDoubled == 2:
        jump town_casino_roulette_doubled2

    if casinoRouletteDoubled == 3:
        jump town_casino_roulette_doubled3

    if casinoRouletteDoubled > 3:
        jump town_casino_roulette_doubledmore

    hide casinogirlred_pits with myDissolve
    hide casinogirlred_contact with myDissolve
    show casinogirlred_pour2 at casino_zoomin(1.5, 1.5, 1, 0.8, -0.2) with myDissolve
    "[casinoGirlRed]" "My my, a [casinoRouletteNumbers[targetM]] huh~?"
    if colorWon == "red":
        if casinoBetIndex == 1:
            jump town_casino_roulette_win
        else:
            jump town_casino_roulette_lose

    else:
        if casinoBetIndex == 2:
            jump town_casino_roulette_win
        else:
            jump town_casino_roulette_lose

label town_casino_roulette_win:
    "[casinoGirlRed]" "And you picked [colorWon] too huh~? Lucky you~"
    "[casinoGirlRed]" "..."
    play music rose volume 0.25
    hide casinogirlred_pour2 with myDissolve
    show casinogirlred_kneel at casino_zoomin(1.5, 1.5, 1, 0.8, -0.2) with myDissolve
    "[casinoGirlRed]" "You know~"
    "[casinoGirlRed]" "I know a secret trick to earn even more money~"
    "[casinoGirlRed]" "Would you like that~? I bet you would, right~?"
    show casinogirlred_kneel at casino_zoomin(1.5, 1.7, 1, 1.0, -0.2)
    "[casinoGirlRed]" "..."
    "[casinoGirlRed]" "Hey hey~ Look here~"
    "[casinoGirlRed]" "You like winning, right~? All you have to do is listen to me~"
    "[casinoGirlRed]" "I mean, I've worked here for years~ Do you really think I don't know what I'm doing~?"
    "[casinoGirlRed]" "Let's go double or nothing, okay~? We can win even more that way~ Sound good?"
    show casinogirlred_kneel at casino_zoomin(1.7, 2.0, 1, 1.4, -0.2)
    "[casinoGirlRed]" "Look look~ I promise I only want what's best for you~"
    
    if colorWon == "red":
        "[casinoGirlRed]" "Just listen to me, okay~? Let's bet on red again~ ♡"
    else:
        "[casinoGirlRed]" "Just listen to me, okay~? Let's bet on red this time~ ♡"
    
    menu:
        "Double or nothing on red":
            $ casinoBetIndex = 1
            jump town_casino_roulette_double

        "Refuse":
            jump town_casino_roulette_refuse

label town_casino_roulette_lose:
    if colorWon == "red":
        "[casinoGirlRed]" "Aww~ but you bet on white~ That's a shame huh?"
    else:
        "[casinoGirlRed]" "Aww~ but you bet on red~ That's a shame huh?"

    "[casinoGirlRed]" "..."
    "[casinoGirlRed]" "...Unless of course~"
    play music rose volume 0.25
    play audio "/audio/casinored/15w3.mp3"
    hide casinogirlred_pour2 with myDissolve
    show casinogirlred_kneel at casino_zoomin(1.5, 1.5, 1, 0.8, -0.2) with myDissolve
    "[casinoGirlRed]" "You'd like to go double or nothing on red~"
    "[casinoGirlRed]" "The rules are simple~ If you win this round, I'll double your initial bet but if you lose..."
    hide casinogirlred_kneel with myDissolve
    show casinogirlred_contact at casino_zoomin(1.6, 1.6, 0, 0.8, -0.2) with myDissolve
    "[casinoGirlRed]" "You'll have to pay me double your bet~"
    "[casinoGirlRed]" "Sound good, [pronouns.mister]~?"
    menu:
        "Double or nothing on red":
            $ casinoBetIndex = 1
            jump town_casino_roulette_double

        "Refuse":
            jump town_casino_roulette_refuse_loss

label town_casino_roulette_doubled1:
    hide casinogirlred_pour2 with myDissolve
    call hideAllCasino from _call_hideAllCasino_2
    show casinogirlred_kneel at casino_zoomin(1.5, 1.5, 1, 0.8, -0.2) with myDissolve
    "[casinoGirlRed]" "Awwww~ Looks like we rolled white, [pronouns.mister]~"
    "[casinoGirlRed]" "There go your precious earnings~ How much did you bet again~? [casinoBetAmount] gold~?"
    "[casinoGirlRed]" "What a shame huh~? You'll owe me that much now~ Guess I'll just have to put aaaall of it in my own pocket~"
    $ casinoOwed = casinoBetAmount
    "[casinoGirlRed]" "..."
    hide casinogirlred_kneel with myDissolve
    show casinogirlred_squat with myDissolve
    "[casinoGirlRed]" "Fufu~ Unless you think you'll win another round of double or nothing~"
    "[casinoGirlRed]" "Hey hey~ I'll forget about your loss, okay~? On the condition that you roll again, okay~?"
    "[casinoGirlRed]" "You'll roll for [closestTo(casinoBetAmount * 2, casinoBetAmounts)] gold, okay [pronouns.mister]~?"
    "[casinoGirlRed]" "It's such a big amount of money isn't it~?"
    "[casinoGirlRed]" "And you can have it all~ That's right~"
    "[casinoGirlRed]" "All you gotta do is just..."
    show casinogirlred_squat at casino_zoomin(1.0, 1.4, 2, 0.8, 0.0) with myDissolve
    "[casinoGirlRed]" "...Listen to me..." 
    "[casinoGirlRed]" "And I promise you'll get your moneys worth~"
    "[casinoGirlRed]" "You trust me... {w} don't you~?"
    menu:
        "Double or nothing":
            "[casinoGirlRed]" "Exactly~ See how smart you are~?"
            label town_casino_roulette_doubled1_double:
            "[casinoGirlRed]" "I'll double your bet for you, okay~?"
            $ casinoBetAmount = closestTo(casinoBetAmount * 2, casinoBetAmounts)
            "Your bet increased to{color=#ff0} [casinoBetAmount]{/color} gold."
            "[casinoGirlRed]" "As long as you follow my voice, everything will be okay~"
            "[casinoGirlRed]" "As long as you just{cps=3}...{/cps} Listen to me...{w=1} Okay~?"
            "[casinoGirlRed]" "We'll try and get that money back, okay~? You can't really quit now, can you~?"
            "[casinoGirlRed]" "In fact, if we're gonna make it back anyway, why don't we just double your bet again~?"
            "[casinoGirlRed]" "You'll only owe me{color=#ff0} [closestTo(casinoBetAmount * 2, casinoBetAmounts)]{/color} gold~ You can pay that right~?"
            "[casinoGirlRed]" "And if you can't, we can always take out a little loan, right~?"
            menu:
                "Double again":
                    hide casinogirlred_boobhand with myDissolve
                    call hideAllChara from _call_hideAllChara_3
                    hide casinogirlred_squat with myDissolve
                    show casinogirlred_closepour with myDissolve
                    "[casinoGirlRed]" "Aww~ Look at you~! You've got courage, you know that~?"
                    "[casinoGirlRed]" "Ladies like me think courage is reaaally attractive, you know~?"
                    "[casinoGirlRed]" "We'll increase your bet to {color=#ff0}[closestTo(casinoBetAmount * 2, casinoBetAmounts)]{/color} gold then~"
                    $ casinoBetAmount = closestTo(casinoBetAmount * 2, casinoBetAmounts)
                    "Your bet increased to {color=#ff0}[casinoBetAmount]{/color} gold."
                    "[casinoGirlRed]" "Hey hey~ Ready to spin again then cutie~?"
                "No":
                    "[casinoGirlRed]" "Kufufu~ Fine~"
                    "[casinoGirlRed]" "You're the one in control after all~ ♡"
                    "[casinoGirlRed]" "Hehe anyway~ Are you ready to spin again, cutie~?"

            "[casinoGirlRed]" "I'm sure you'll do fine this time~"
            "[casinoGirlRed]" "And if you won't, you'll just owe us a little~ That's fine right~?"
            "[casinoGirlRed]" "Ready~?"
            hide casinogirlred_closepour with myDissolve
            hide casinogirlred_squat with myDissolve
            show casinogirlred_contact at casino_zoomin(1.6, 1.6, 0, 0.8, -0.2) with myDissolve
            "[casinoGirlRed]" "The girl smiles smugly as you watch her get ready to spin the roulette again."
            hide casinogirlred_squat with myDissolve
            show casinogirlred_contact at casino_zoomin(1.6, 1.6, 0, 0.8, -0.2) with myDissolve
            play audio "/audio/casinoRed/15w7.mp3"
            "[casinoGirlRed]" "Here we go~ I heard if you keep eye contact it brings good luck~"
            "The girl keeps eye contact while spinning the roulette and..."
            $ casinoSpinPower = ((rand(0, 10) * 2) + 30)
            $ casinoRouletteDoubled += 1
            jump town_casino_roulette_roll
    
        "Back out":
            hide casinogirlred_squat with myDissolve 
            show casinogirlred_boobhand with myDissolve
            "[casinoGirlRed]" "Kufufu~ That's fine too~"
            "[casinoGirlRed]" "I mean... You wouldn't want to make any bad decisions, would you~?"
            "[casinoGirlRed]" "Gosh... Can you imagine the amount of stress you'd build up~?"
            "[casinoGirlRed]" "Seeing that little number... Growing bigger and bigger... As your debt increases..."
            "[casinoGirlRed]" "Good thing we provide some excellent anti-stress services here~"
            "[casinoGirlRed]" "Ah~ But oh well~ You wanted to quit, right~? So go ahead, take your leave~"
            menu:
                "On second thought...":
                    "[casinoGirlRed]" "Kufufu~ That's what I thought, silly~"
                    jump town_casino_roulette_doubled1_double
                "Leave":
                    "[casinoGirlRed]" "Fufu~ Bye then~ I'll see you soon hopefully~"
                    stop music fadeout 10
                    stop sound fadeout 3
                    jump town_casino

label town_casino_roulette_doubled2:
    play audio "/audio/casinoRed/15w6.mp3"
    hide casinogirlred_contact with myDissolve
    show casinogirlred_pits3 with myDissolve
    "[casinoGirlRed]" "Oww~ Poor you~"
    $ casinoOwed = casinoBetAmount
    "[casinoGirlRed]" "Looks like you lost again [pronouns.mister] dummy~ How unfortunate~"
    hide casinogirlred_pits3 with myDissolve
    show casinogirlred_kneel at casino_zoomin(1.7, 1.7, 1, 1.0, -0.2) with myDissolve
    "[casinoGirlRed]" "Hmm~"
    "[casinoGirlRed]" "I've got an idea~"
    "[casinoGirlRed]" "You'll give me a single level and I'll spin again, okay~? Free of charge~"
    "[casinoGirlRed]" "Doesn't that sound wonderful~? You wouldn't want to be in such big debt, right~?"
    "[casinoGirlRed]" "If you land on red, I'll completely forget everything that happened today. deal~?"
    menu:
        "Deal":
            play audio "/audio/casinoRed/15w5.mp3"
            "[casinoGirlRed]" "Kufufu~ Good choice~ I'll only take one, really~"
            hide casinogirlred_kneel with myDissolve
            show casinogirlred_closepour with myDissolve
            "[casinoGirlRed]" "Go on~ Touch yourself for me, okay~?"
            "[casinoGirlRed]" "Kufyuu~ That's right~ Just your sexual energy combined with sexual stimuli is enough to drain your levels~"
            "[casinoGirlRed]" "You begin touching yourself as the lady grins at you..."
            play sound handjobmediumspeed loop
            "[casinoGirlRed]" "It feels really good doesn't it~? Almost magical right~?"
            "[casinoGirlRed]" "Keep touching for me~ You're doing amazing~"
            "[casinoGirlRed]" "You trust me, right~? Don't you like spending time with me like this~?"
            "[casinoGirlRed]" "I really only want what's best for you, I promise~"
            play sound handjobhighspeed fadein 2 loop
            "[casinoGirlRed]" "You stroke faster and faster as you prepare to cum."
            "[casinoGirlRed]" "Kufyuu~ That's it~ Ready~?"
            "[casinoGirlRed]" "Let mommy drain all that sweet XP of yours~ Kufufu~"
            "[casinoGirlRed]" "Spurt out all that semen for me~"
            stop sound fadeout 1
            call pyupyu from _call_pyupyu_6
            call levelDrain(player, casinoGirlRed, 300) from _call_levelDrain_22
            play audio "/audio/casinoRed/15w4.mp3"
            hide casinogirlred_closepour with myDissolve
            show casinogirlred_pour2 at casino_zoomin(1.5, 1.5, 1, 0.8, -0.2) with myDissolve
            "[casinoGirlRed]" "Kufyuu~ Good [pronouns.boy]~! Look at you feeding me like this~ Didn't that feel good~?"
            "[casinoGirlRed]" "Fufu~ I did promise you this, didn't I~?"
            "[casinoGirlRed]" "Hey hey~ come, closer okay~? I'll spin it and you can watch~"
            hide casinogirlred_pour2 with myDissolve
            show casinogirlred_kneel at casino_zoomin(1.7, 1.7, 1, 1.0, -0.2) with myDissolve
            "The girl pulls you close while looking at you smugly before spinning the roulette again..."
            "She gives the roulette a really, {w=0.3}really small push..."
            "An almost... {w=0.3}unfairly small push..."
            $ casinoSpinPower = 4
            $ casinoRouletteDoubled += 1
            jump town_casino_roulette_roll

        "No deal":
            hide casinogirlred_kneel with myDissolve
            show casinogirlred_boobhand with myDissolve
            "[casinoGirlRed]" "Aww okay~ Well then, let's see what you owe me~"
            "[casinoGirlRed]" "..."
            "[casinoGirlRed]" "Aaand that's a total of [casinoOwed] gold you owe~"
            stop music fadeout 10
            "[casinoGirlRed]" "Ufufu~ You'll be able to pay it off at the reception, okay~?"
            "[casinoGirlRed]" "Until next time for now, dummy~"
            "[casinoGirlRed]" "See you sooon~ Kufufu~"
            hide casinogirlred_boobhand with myDissolve
            "The girl walks away with a sly smile on her face..."
            "You now owe [casinoOwed] gold to the casino!"
            "You can pay off your debt at the reception"
            stop music fadeout 10
            stop sound fadeout 3
            jump town_casino

label town_casino_roulette_doubled3:
    play audio "/audio/casinoRed/15w3.mp3"
    "[casinoGirlRed]" "You lost again~ Oh how unfortunate~"
    hide casinogirlred_kneel with myDissolve
    show casinogirlred_lean with myDissolve
    "[casinoGirlRed]" "Hmm~? That's not fair? Why not~?"
    "[casinoGirlRed]" "Since when did you make the rules~? I offered you a chance and I did, didn't I~?"
    hide casinogirlred_lean with myDissolve
    show casinogirlred_squat with myDissolve
    "[casinoGirlRed]" "...Hey hey~"
    "[casinoGirlRed]" "You agree with me, right~?"
    "[casinoGirlRed]" "I didn't really cheat, did I~?"
    "[casinoGirlRed]" "I'd never do something like that, right~?"
    "[casinoGirlRed]" "..."
    hide casinogirlred_squat with myDissolve
    show casinogirlred_handsapart with myDissolve
    "[casinoGirlRed]" "Kyahaha~! Oh you should see your face~ You really are adorable~"
    "[casinoGirlRed]" "Let's call it here for now, okay [pronouns.mister]~?"
    hide casinogirlred_handsapart with myDissolve
    show casinogirlred_pour2 at casino_zoomin(1.5, 1.5, 1, 0.8, -0.2) with myDissolve
    "[casinoGirlRed]" "Let's see... Your total will be... [casinoOwed] gold~"
    "[casinoGirlRed]" "Kufufu~ You can pay it off at the reception~"
    "[casinoGirlRed]" "And if you want to pay me in person, you'll have to schedule an arrangement~ Ahahaha~"
    "[casinoGirlRed]" "Do come back soon, okay~? I can't wait to play with you some more~"
    hide casinogirlred_pour2 with myDissolve
    "The girl starts walking towards her colleague at the reception."
    menu:
        "Finish playing":
            stop music fadeout 10
            stop sound fadeout 3
            jump town_casino

        "\"More please...\"":
            show casinogirlred_pour2 at casino_zoomin(1.5, 1.5, 1, 0.8, -0.2) with myDissolve
            "[casinoGirlRed]" "Hmm~? What's that~?"
            "[casinoGirlRed]" "Kufyuu~ You want more huh~? More of what~?"
            "[casinoGirlRed]" "More of...{w=0.3} me, perhaps~?"
            "[casinoGirlRed]" "How cute~ I'll let you gamble a little more then, okay~? I'll stay right by your side as your debt grows~"
            "[casinoGirlRed]" "Hey hey~ But I'll be the one spinning the wheel the entire time, okay~?"
            "[casinoGirlRed]" "Kufyuu~ So what do you say~? Wanna double again~?"
            menu:
                "Double again":
                    "[casinoGirlRed]" "Kyahaha~! Oh how cute~"
                    "[casinoGirlRed]" "Sure sure~ I'll just..."
                    $ casinoRouletteDoubled += 1
                    $ casinoBetAmount = closestTo(casinoBetAmount * 2, casinoBetAmounts)
                    $ casinoSpinPower = ((rand(0, 10) * 2) + 30)
                    jump town_casino_roulette_roll

                "Nevermind":
                    stop music fadeout 10
                    stop sound fadeout 3
                    jump town_casino

label town_casino_roulette_doubledmore:
    if casinoBetAmount > 100000:
        "[casinoGirlRed]" "Hey dummy~!"
        stop music fadeout 10
        stop sound fadeout 3
        "[casinoGirlRed]" "I think you've had enough of your little addiction~"
        "[casinoGirlRed]" "There's no way you're gonna be able to pay all of this off, you know~?"
        "[casinoGirlRed]" "Kufufu~ I suppose I'll just cut you off here and you can be my little debt-puppy~ How cute~ ♡"
        "[casinoGirlRed]" "Come see me anytime you need to be drained, okay [pronouns.mister]~?"
        "[casinoGirlRed]" "See you later duuuummy~"
        jump town_casino
    
    hide casinogirlred_pour2 with myDissolve
    show casinogirlred_lean with myDissolve
    $ casinoOwed = casinoBetAmount
    "[casinoGirlRed]" "Awwn~ Another loss huh~? Poor dummy~"
    "[casinoGirlRed]" "Don't worry~ I'm sure if you keep going you'll end up fine one of the turns, right~?"
    "[casinoGirlRed]" "Let's keep going, okay~?"
    menu:
        "Double again":
            "[casinoGirlRed]" "Kufyuu~ Good [pronouns.boy]~ ♡"
            "[casinoGirlRed]" "You bet [casinoBetAmount] gold"
            $ casinoRouletteDoubled += 1
            $ casinoBetAmount = closestTo(casinoBetAmount * 2, casinoBetAmounts)
            $ casinoSpinPower = ((rand(0, 10) * 2) + 30)
            jump town_casino_roulette_roll

        "Nevermind":
            "[casinoGirlRed]" "Kufyuu~ Finally calling it quits~?"
            "[casinoGirlRed]" "How cute~ Don't forget to pay of your debt for me, 'kaaay~?"
            "[casinoGirlRed]" "See you later, dummy~"
            stop music fadeout 10
            stop sound fadeout 3
            jump town_casino

label town_casino_roulette_double:
    "[casinoGirlRed]" "That's it~ Smart choice~"
    if colorWon == "white":
        "[casinoGirlRed]" "Let's bet on red this time, okay~?"
        $ casinoBetIndex = 1

    $ player.arousal += 100
    call updateArousal from _call_updateArousal_7
    $ casinoBetAmount = closestTo(casinoBetAmount * 2, casinoBetAmounts)
    "You bet [casinoBetAmount] gold"
            
    if colorWon == "red":
        $ casinoSpinPower = 19
    else:
        $ casinoSpinPower = 20

    $ casinoRouletteDoubled += 1
    jump town_casino_roulette_roll

label town_casino_roulette_refuse:
    hide casinogirlred_kneel with myDissolve
    hide casinogirlred_contact with myDissolve
    call hideAllChara from _call_hideAllChara_4
    show casinogirlred_boobhand with myDissolve
    "[casinoGirlRed]" "Ahaha~ Oh well, that works fine too~"
    "[casinoGirlRed]" "Here's your reward then~"
    jump town_casino_roulette_truewin
    return

label town_casino_roulette_refuse_loss:
    $ casinoOwed = casinoBetAmount  
    hide casinogirlred_kneel with myDissolve
    hide casinogirlred_contact with myDissolve
    call hideAllChara from _call_hideAllChara_5
    show casinogirlred_boobhand with myDissolve
    "[casinoGirlRed]" "Ahaha~ Oh well, that works fine too~"
    "[casinoGirlRed]" "I'll see you later then~ Bye cutie~"
    jump town_casino

label town_casino_roulette_truewin:
    stop music fadeout 10
    stop sound fadeout 3
    "You bet [casinoBetAmount] money and won!"
    call gainMoney(player, casinoBetAmount) from _call_gainMoney_3
    $ casinoBetAmount = 0
    jump town_casino








