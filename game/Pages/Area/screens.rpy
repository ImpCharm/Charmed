screen locationMarker:
    text "[currentArea]" at locationNameAnimation:
        size 100
        outlines [ (absolute(5), "#ff7979", absolute(3), absolute(3)) ]

screen timeMarker:
    fixed:
        if False:
            add "clock_dynamic" zoom 0.07 alpha 0.5
            at timeAnim

screen casinoGui:
    fixed:
        xpos 0.1
        ypos 0.65
        add "./gui/textBox.png":
            alpha 0.7
            xzoom 0.5
            yzoom 0.3
        if casinoBetIndex == 1:
            text "Money: {color=#ff0}[player.money]{/color} | Color: {color=#f00}Red{/color} | Bet: {color=#ff0}[casinoBetAmount]":
                ypos 20
                xpos 20
                color "#fff"
                outlines [ (absolute(5), "#511818", absolute(0), absolute(0)) ]
        else:
            text "Money: {color=#ff0}[player.money]{/color} | Color: {color=#fff}White{/color} | Bet: {color=#ff0}[casinoBetAmount]":
                ypos 20
                xpos 20
                color "#fff"
                outlines [ (absolute(5), "#511818", absolute(0), absolute(0)) ]
        
screen menuBtn:
    textbutton "{size=100}{font=[normalFont]}☰":
        action ShowMenu('save')

