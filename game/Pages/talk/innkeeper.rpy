
label innkeeper_talk:
    call hideAllInnkeeper from _call_hideAllInnkeeper_1
    show innkeeper_sit at innKeeperSit with myDissolve
    if isTalking == False:
        "[innKeeper]" "Ah~? You'd like to talk to me?"
        
        if pronouns.mister == "mister":
            "[innKeeper]" "Fufu~ Aren't you a gentleman~"
        elif pronouns.mister == "miss":
            "[innKeeper]" "Fufu~ Aren't you a kind lady~"
        else:
            "[innKeeper]" "Fufu~ Aren't you a sweetheart~"
        
        "[innKeeper]" "Fufu~ Aren't you a gentleman"
        "[innKeeper]" "Ask away~ I'd love to help you out with whatever you need~ 💜"
    else:
        "[innKeeper]" "Have you got any other questions~?"
    $ isTalking = True
    menu:
        "About the inn":
            call innkeeper_talk_inn from _call_innkeeper_talk_inn
        "About Musei":
            call innkeeper_talk_innkeeper from _call_innkeeper_talk_innkeeper
        "Bye":
            "[innKeeper]" "Take care~ You know where to find me~"
            return
    
    jump innkeeper_talk

label innkeeper_talk_inn:
    "[innKeeper]" "Oh~ My lovely little inn~"
    "[innKeeper]" "What would you like to know about it~?"
    menu:
        "How did you get it?":
            "[innKeeper]" "Fufu~ What a great question~"
            "[innKeeper]" "It's simple really~ A lot of inexperienced adventurers come along here..."
            "[innKeeper]" "Most of them need to rest up every now and then and..."
            hide innkeeper_sit with myDissolve
            call hideAllInnkeeper from _call_hideAllInnkeeper_2
            show innkeeper_mouth with myDissolve
            "[innKeeper]" "Gosh, it just breaks my heart to see them struggling against all those slimes~"
            "[innKeeper]" "That's why I set up this place~" 
            hide innkeeper_sit with myDissolve
            "[innKeeper]" "I know it's not quite a five star hotel yet, but what's important is that those poor adventurers are safe here~"
            "[innKeeper]" "Ahaha~ Anyway~"
            hide innkeeper_mouth with myDissolve
            return
        
        "About the price":
            "[innKeeper]" "Aha~ The price?"
            "[innKeeper]" "Nono~ I don't need your money, really~ Just seeing you adventurers smile is more than enough compensation~"
            "[innKeeper]" "That, and a promise to stay safe, okay~?"
            return
        
        "Back":
            return

label innkeeper_talk_innkeeper:
    "[innKeeper]" "Ah~? You're wondering more about me? How sweet~"
    "[innKeeper]" "What can I say~ I'm really just a sweet old lady who loves helping adventurers~"
    "[innKeeper]" "And I get it~ I'm a succubus and they're scary, but I really only want what's best for you adventurers, I promise~"
    "[innKeeper]" "Ahaha~ I must bore you already~ Let's talk about something else, shall we~?"
    return

            
    