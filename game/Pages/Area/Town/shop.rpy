label town_shop:

    if getTimePeriod() == "night":
        "It's closed..."
        return

    if getTimePeriod("evening") and shopKeeperStatus != "walking":
        "The door is closed."
        "There's a sign hanging from the door that reads \"Out gathering materials, will be back soon!\""
        return

    if game.shopUnlocked == False:
        call shop_entry_1 from _call_shop_entry_1

    
        
    if shopKeeperStatus == "sleeping":
        scene shop with myDissolve
        "You enter the shop... The bell rings but there aren't any signs of [shopKeeper.profile.name]"
        "..."
        "It's still early..."
        menu:
            "Call out for her":
                "You yell [shopKeeper.profile.name]'s name."
                "[shopKeeper]" "Wuh... Who's..."
                "[shopKeeper]" "Oh gosh! The shop!"
                "You hear footsteps coming down the stairs."
                show shopkeeper_leanforward_open with myDissolve
                "[shopKeeper]" "I'm so sorry! I must have overslept..."
                "[shopKeeper]" "I'm here now though! What do you need?"
                $ shopKeeperStatus = "shopKeeping"

            "Let her sleep":
                "You silently leave the shop."
                $ shopKeeperStatus = "upstairs"
                return

    elif shopKeeperStatus == "upstairs":
        scene shop with myDissolve
        "You enter the shop... The bell rings before you hear someone running down the stairs..."
        "[shopKeeper]" "I'm coming!"
        pause 1
        show shopkeeper_leanforward with myDissolve
        "[shopKeeper]" "Sorry for the delay! How may I help you?"
        $ shopKeeperStatus = "shopKeeping"
    elif shopKeeperStatus == "welcome-back":
        scene shop with myDissolve
        show shopkeeper_leanforward with myDissolve
        "[shopKeeper]" "So, did anything catch your eye?"

    elif shopKeeperStatus == "walking":
        scene shop with myDissolve
        "You enter the shop and see [shopKeeper.profile.name] putting supplies on shelves"
        show shopkeeper_leanforward_open with myDissolve
        "[shopKeeper]" "Oh hey! Sorry but I'm just about to close."
        show shopkeeper_leanforward with myDissolve
        "[shopKeeper]" "You should come back in the morning though!"
        "[shopKeeper]" "Sleep well, adventurer~"
        hide shopkeeper_leanforward_open
        hide shopkeeper_leanforward with myDissolve
        "You walk out of the shop again..."
        return

    else:
        scene shop with myDissolve
        show shopkeeper_leanforward with myDissolve
        "[shopKeeper]" "Welcome! How may I help you?"
        $ shopKeeperStatus = "shopKeeping"
        

    menu:
        "Buy":
            call shop_buy from _call_shop_buy
        "Sell":
            call hideAllShopKeeper from _call_hideAllShopKeeper
            show shopkeeper_pout with myDissolve
            "[shopKeeper]" "Hey! This isn't some pawnshop, you know? I SELL stuff here"
        "Exit":
            return

    jump town_shop

label shop_buy:

    $ randomI = rand(1,3)
    if randomI == 1:
        $ shopKeeperDialogue = "What'll it be?"
    elif randomI == 2: 
        $ shopKeeperDialogue = "Need some better armor?"
    else:
        $ shopKeeperDialogue = "I've got some of the best items here!"


    call hideAllShopKeeper from _call_hideAllShopKeeper_1
    call screen shopGui("town")
    
    $ shopKeeperStatus = "welcome-back"

    
    return

label shop_entry_1:
    scene shop with myDissolve
    "You walk into the shop, a bell rings as you open the door. There's nobody behind the counter though..."
    "..."
    "...You hear floorboards squeaking upstairs. It sounds like someone is running down."
    "Suddenly, a girl comes rushing down the stairs"
    "{size=*1.5}{color=#7986CB} ??? {/color}{/size}" "Excuse me, excuse me!"
    show shopkeeper_leanforward_open with myDissolve
    "[shopKeeper]" "Oh gosh, I'm so sorry for the delay..."
    show shopkeeper_leanforward_o with myDissolve
    hide shopkeeper_leanforward_open
    "[shopKeeper]" "We- Um, I don't get customers too often."
    show shopkeeper_leanforward_open with myDissolve
    hide shopkeeper_leanforward_o
    "[shopKeeper]" "...Oh um, you must be here to buy something, right?"
    call hideAllShopKeeper from _call_hideAllShopKeeper_2
    show shopkeeper_leanforward
    "[shopKeeper]" "That's just perfect~!"
    $ shopKeeper.profile.name = "Tessa"
    "[shopKeeper]" "My name is Tessa, welcome to my shop!"
    "[shopKeeper]" "How may I assist you? I've got some good items in stock."
    "[shopKeeper]" "You must be an adventurer or something, right?"
    "[shopKeeper]" "Wait up, one second."
    hide shopkeeper_leanforward with myDissolve
    "Tessa quickly rummages through a bunch of drawers to find a leather piece of armor"
    "[shopKeeper]" "I'm sure you could use some armor. I'm not sure if you're aware but there's a forest nearby that's filled to the brim with slimes!"
    "She grabs a leather piece of armor and walks back up to you"
    show shopkeeper_pout with myDissolve
    "[shopKeeper]" "Gosh they're so pesky! They keep attacking innocent adventurers, it's unbelievable"
    hide shopkeeper_pout with myDissolve
    show shopkeeper_leanforward with myDissolve
    "[shopKeeper]" "Anyway, I've got something for you!"
    "[shopKeeper]" "It's not much but..."
    call unlockArmor(player, armors[1]) from _call_unlockArmor
    "[shopKeeper]" "This should at least keep you safe for now!"
    "[shopKeeper]" "And of course, if you ever wanna chat, I'll be right here!"
    $ game.shopUnlocked = True
    $ shopKeeperStatus = "welcome-back"
    "Your armor can be equipped by opening the menu and clicking armor, then selecting the piece of armor you'd like to equip."
    return
