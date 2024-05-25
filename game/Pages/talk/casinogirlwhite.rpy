label casinogirlwhite_talk:
    if isTalking:
        "[casinoGirlWhite]" "Have you got any other questions?"
    else:
        "[casinoGirlWhite]" "Yes~?"
    $ isTalking = True
    menu:
        "How does the casino work?":
            "[casinoGirlWhite]" "How does it work?"
            show casinogirlwhite_sit with myDissolve
            "[casinoGirlWhite]" "It's quite simple, you bet a certain amount of money and depending on whether you win or lose, you'll walk out with more or less money than before."
            "[casinoGirlWhite]" "It's not all luck of course, there's a certain amount of skill and restrain needed to win too."
            "[casinoGirlWhite]" "After all..."
            "[casinoGirlWhite]" "Practice makes perfect, no~?"
        "Refund policy?":
            show casinogirlwhite_sit with myDissolve
            "[casinoGirlWhite]" "Ahaha~ A refund policy?"
            "[casinoGirlWhite]" "Sorry, sweetheart, but we don't do that here."
            "[casinoGirlWhite]" "Feel free to play some more in hopes of returning your investment though~"
        "Bye":
            $ isTalking = False
            return
    jump casinogirlwhite_talk
