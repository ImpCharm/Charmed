label slimevillage_central:
    scene slimevillage with myDissolve
    call areaMarker("slime village") from _call_areaMarker_7


    if (game.objective[2].completed == False):
        $ highlight = getHighlightText("Royal district")
    else:
        $ highlight = "Royal district"

    menu:
        "[highlight]":
            call move("slimevillage_royal") from _call_move_10
        "Inn":
            call slimevillage_inn from _call_slimevillage_inn
        "Talk to the slime guard":
            call slimeguard_talk from _call_slimeguard_talk
        "Leave slime village":
            call move("cave_2") from _call_move_6

    jump slimevillage_central

    # player.arousal = 100