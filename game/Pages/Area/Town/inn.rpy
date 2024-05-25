
default restHighlight = ""
label town_inn:
    if (game.objective[0].completed == False 
        and game.objective[0].completionFlags[1] == False):
        call town_inn_cutscene from _call_town_inn_cutscene

    if game.objective[0].completed == True:
        $ restHighlight = "Rest"
    else:
        $ restHighlight = getHighlightText("Rest")
    
    scene inn_dynamic with myDissolve
    menu:
        "[restHighlight]":
            call inn_rest from _call_inn_rest_1
        "Options":
            call options from _call_options
        "Unlocked pfp's":
            call pfps from _call_pfps_1
        "Town":
            call move("town_central") from _call_move_12
    
    jump town_inn

label town_inn_cutscene:
    scene black with myDissolve
    "You walk into a building with a big sign that reads \"Inn\""
    "There doesn't seem to be anyone inside..."
    "You walk up the stairs and find a small bedroom. You should be able to rest in here for now."
    "{color=#ff0}Important info about saving!{/color}"
    "{color=#ff0}Pressing ESC will open the save menu. You can save there!{/color}"
    "{color=#ff0}Saving is disabled during combat to prevent errors{/color}"
    $ game.objective[0].completionFlags[1] = True
    return

label inn_rest:
    scene black with myDissolve
    if(game.objective[0].completed == False 
        and game.objective[0].completionFlags[2] == False):
        "You get on the bed and start resting. That fight injured you quite a lot."
        "Lulu said something about level drain. You should go to the forest tomorrow to gain some levels..."
        call completeObjective(game.objective[0]) from _call_completeObjective
        $ game.objective[0].completionFlags[2] = True;
        call restoreAll from _call_restoreAll_6
        call dayPass from _call_dayPass_2
        $ game.dayTime = time_afternoon

    else:
        if getTimePeriod("morning") or getTimePeriod("afternoon") or getTimePeriod("evening"):
            menu:
                "Sleep until the next day":
                    call dayPass() from _call_dayPass_4
                    call restoreAll from _call_restoreAll_7
                    "You go to sleep for today."
                    $ game.dayTime = time_morning
                "Sleep until the afternoon" if (getTimePeriod('morning')):
                    "You go to sleep."
                    call restoreAll from _call_restoreAll
                    $ game.dayTime = time_afternoon
                "Sleep until the evening" if (getTimePeriod('morning') or getTimePeriod('afternoon')):
                    "You go to sleep."
                    call restoreAll from _call_restoreAll_1
                    $ game.dayTime = time_evening
                "Sleep until midnight" if (getTimePeriod('morning') or getTimePeriod('afternoon') or getTimePeriod('evening')):
                    "You go to sleep."
                    call restoreAll from _call_restoreAll_2
                    $ game.dayTime = time_midnight
                    call dayPass from _call_dayPass_1

            $ game.dayTime = round(game.dayTime)
            call setAmbience from _call_setAmbience_1
            return
                    
        else:
            call restoreAll from _call_restoreAll_8
            call dayPass() from _call_dayPass_5
            "You go to sleep for today."
            $ game.dayTime = time_morning
            $ game.dayTime = round(game.dayTime)
            pause 3
            call setAmbience from _call_setAmbience_2
    return

label pfps:
    menu:
        "Skye" if game.pfp.slimeUnlocked == True:
            "{size=50}{a=https://i.ibb.co/bmYqnT2/Slimed.jpg}Click here to download the PFP"
        "Slime princess" if game.pfp.slimePrincessUnlocked == True:
            "{size=50}{a=https://i.ibb.co/59Dcrfg/slimep.png}Click here to download the PFP"
        "Merchant" if game.pfp.merchantUnlocked == True:
            "{size=50} {color=#ff0} {a=https://i.ibb.co/PxLQHGF/ad8ba1fed603656573548848b4032a08-2.png}Click here to download the PFP"
        "Back":
            return









