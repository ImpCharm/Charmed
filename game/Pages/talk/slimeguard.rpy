
label slimeguard_talk:
    $ currentEnemy = Character(9, 10, 2, 50, 200, Profile("The slime guard", "#1e88e5", "lesserslime", "Lesser slimes are slimes fighting for the slime princess's army. They're fairly weak and don't have a strong work ethic, usually trying to slack off at every opertunity. Despite their low energy, they're very faithful towards their princess, doing almost anything just to drain some more XP to feed her. \n \n Their ways of draining are similar to most slimes. Using their body parts to pleasure humans until they cum inside their core."),Conditions())
    show lesserslime_main with myDissolve
    
    if isTalking:
        "[currentEnemy]" "What else do you want to know..?"
    else:
        "[currentEnemy]" "Ah... It's the human..."
        "[currentEnemy]" "How are you enjoying slime village..? {w=0.3} Do you want to talk about anything..?"
    
    $ isTalking = True
    
    menu:
        "About access to slime village":
            "[currentEnemy]" "Ah... I know who do and don't have access..."
            "[currentEnemy]" "Humans aren't allowed in without good reason... The princess has sent the lesser slimes to drain them..."
            "[currentEnemy]" "There's one slime who isn't allowed in... I'm not sure why exactly but... Whatever the princess says goes and I won't question it..."
            "[currentEnemy]" "Um... I think that's about it..."
            "[currentEnemy]" "I'm not even sure why you're allowed in but it's what the princess wants..."
        "About the princess":
            "[currentEnemy]" "The princess? What do you want to know about her?"
            "[currentEnemy]" "I can tell you how amazing she is... She's the greatest slime I've ever seen..."
            "[currentEnemy]" "...um"
            "[currentEnemy]" "Don't tell her I said this, but, I prefer her over the queen... She's been gone for a while anyway..."
        "About levels":
            "[currentEnemy]" "Ah... Her blessing, right..."
            "[currentEnemy]" "She gives all her servants a special blessing that allows us to donate XP right after we gain XP ourselves..."
            "[currentEnemy]" "She uses nectar or something... I don't think the alraunes mind that much..."
        "Bye":
            return
            
    jump slimeguard_talk