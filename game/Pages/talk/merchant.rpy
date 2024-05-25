label merchant_talk:
    if isTalking == False:
        "[merchant]" "Ah~? You wanna talk~?"
        hide merchant_handboob with myDissolve
        show merchant_lean_open with myDissolve
        "[merchant]" "Sorry I don't like to get all close and personal with strangers, y'know~?"
        "[merchant]" "I'd prefer to keep our relationship strictly professional~"
        hide merchant_lean_open with myDissolve
        show merchant_handboob with myDissolve
        "[merchant]" "Fufu~ Anyway, buy something~!"
        return
    $ isTalking = True
    