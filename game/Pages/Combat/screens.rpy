define xpBarMoveSpeed = 6

define enemyResetting = False
define startEnemyResetting = False
define enemyXPBar = 0
define enemyOverflow = 0

define playerResetting = False
define startPlayerResetting = False
define playerXPBar = 0
define playerOverflow = 0

screen battleGui:
    fixed:
        xpos 0.045
        ypos 0.57
        bar: 
            xmaximum 577
            ymaximum 195
            value AnimatedValue(player.health / player.maxHealth * 100, 100, 3)
            left_bar Frame("/gui/boxfilling.png", 0, 0)
            right_bar Frame("/gui/fullpng.png")
    
    fixed:
        xpos 0.46
        ypos 0.57
        bar: 
            xmaximum 577 
            ymaximum 195
            value AnimatedValue(player.SP / player.maxSP * 100, 100, 0.1)
            left_bar Frame("/gui/spfill.png", 0, 0)
            right_bar Frame("/gui/fullpng.png")

    fixed:
        add "/gui/boxframe.png" alpha 0.9 zoom 0.75
        xpos 0.045
        ypos 0.56
        text ("Health: " + str(player.health) + "/" + str(player.maxHealth)):
            xpos 45
            ypos 130 

    fixed:
        add "./gui/spframe.png" alpha 0.9 zoom 0.75
        xpos 0.46
        ypos 0.56
        text ("SP: " + str(player.SP) + "/" + str(player.maxSP)):
            xpos 45
            ypos 130    

    fixed:
        add "./gui/combatbox.png" alpha 0.75
        xpos 0.0
        ypos 0.47

    # sidebar values
    # enemy values
    fixed:  
        add "./gui/sidebarcombat.png" alpha 0.75

    fixed:
        xpos 0.776
        ypos 0.1
        fixed:
            bar: 
                xmaximum 425
                ymaximum 140
                value AnimatedValue(currentEnemy.health / currentEnemy.maxHealth * 100, 100, 0.2)
                left_bar Frame("/gui/boxfillingenemy1.png", 0, 0)
                right_bar Frame("/gui/fullPng.png")

        fixed:
            ypos -8
            text "Lv: [currentEnemy.level]":
                xpos 350
                ypos 50
                size 30
                xanchor 0.5
            text "{color=[currentEnemy.profile.color]}[currentEnemy.profile.name]{/color}":
                xpos 25
                ypos 50
                size 30
                xanchor 0.0
            add "/gui/boxframecombat.png":
                zoom 0.55
            text ("Health: " + str(currentEnemy.health) + "/" + str(currentEnemy.maxHealth)):
                xpos 25
                ypos 95  
                size 25

    

    fixed:
        xpos 0.776
        ypos 0.16
        fixed:
            if startEnemyResetting:
                if enemyXPBar == 100:
                    timer currentEnemy.profile.XPBar.startResetDelay - 0.01 action SetVariable("enemyResetting", True), SetVariable("enemyXPBar", 0)
                if enemyXPBar == 0:
                    timer currentEnemy.profile.XPBar.startResetDelay - 0.01 action SetVariable("enemyResetting", True), SetVariable("enemyXPBar", 100)

            if enemyResetting:
                bar:
                    xmaximum 425
                    ymaximum 140
                    value AnimatedValue(enemyXPBar, 100, xpBarMoveSpeed)
                    left_bar Frame("/gui/boxfillingenemy1.png", 0, 0)
                    right_bar Frame("/gui/fullpng.png")
                timer 0.01 action SetVariable("enemyResetting", False),  SetVariable("startEnemyResetting", False)
            else:
                bar: 
                    xmaximum 425
                    ymaximum 140
                    value AnimatedValue(enemyXPBar, 100, xpBarMoveSpeed)
                    left_bar Frame("/gui/boxfillingenemy1.png", 0, 0)
                    right_bar Frame("/gui/fullpng.png")
                timer 0.01 action SetVariable("enemyXPBar", (currentEnemy.XP + 1 - currentEnemy.levelBottom + 1) / (currentEnemy.levelTop + 1 - currentEnemy.levelBottom + 1) * 100)
                

                

        fixed:
            ypos -8
            add "./gui/boxframecombat.png":
                zoom 0.55
            text ("XP: " + str(currentEnemy.levelBottom) + "/" + str(currentEnemy.XP) + "/" + str(currentEnemy.levelTop)):
                xpos 25
                ypos 95 
                size 25

    
                # value AnimatedValue((player.XP + 1 - player.levelBottom + 1) / (player.levelTop + 1 - player.levelBottom + 1) * 100, 100, 0.2)
    fixed:
        xpos 0.776
        ypos 0.3
        fixed:
            if startPlayerResetting:
                if playerXPBar == 100:
                    timer player.profile.XPBar.startResetDelay - 0.01 action SetVariable("playerResetting", True), SetVariable("playerXPBar", 0)
                if playerXPBar == 0:
                    timer player.profile.XPBar.startResetDelay - 0.01 action SetVariable("playerResetting", True), SetVariable("playerXPBar", 100)


            if playerResetting:
                bar:
                    xmaximum 425
                    ymaximum 140
                    value AnimatedValue(playerXPBar, 100, xpBarMoveSpeed)
                    left_bar Frame("/gui/boxfillingenemy1.png", 0, 0)
                    right_bar Frame("/gui/fullpng.png")
                timer 0.01 action SetVariable("playerResetting", False),  SetVariable("startPlayerResetting", False)
            else:
                bar: 
                    xmaximum 425
                    ymaximum 140
                    value AnimatedValue(playerXPBar, 100, xpBarMoveSpeed)
                    left_bar Frame("/gui/boxfillingenemy1.png", 0, 0)
                    right_bar Frame("/gui/fullPng.png")
                timer 0.01 action SetVariable("playerXPBar", (player.XP + 1 - player.levelBottom + 1) / (player.levelTop + 1 - player.levelBottom + 1) * 100)
              

        fixed:
            ypos -8
            text "Lv: [player.level]":
                xpos 350
                ypos 50
                size 30
                xanchor 0.5
            text "[player.profile.name]":
                xpos 25
                ypos 25
                size 50
                xanchor 0.0
            text "{color=#ff0}([player.profile.title]){/color}":
                xpos 130
                ypos 52
                size 20
                xanchor 0.0
        
            add "./gui/boxframecombat.png":
                zoom 0.55
            text ("XP: " + str(player.levelBottom) + "/" + str(player.XP) + "/" + str(player.levelTop)):
                xpos 25
                ypos 95  
                size 25

    fixed:
        xpos 0.776
        ypos 0.35
        fixed:
            bar: 
                xmaximum 425
                ymaximum 140
                value AnimatedValue((player.arousal / 100 * 100), 100, 1)
                left_bar Frame("/gui/boxfillingenemy1.png", 0, 0)
                right_bar Frame("/gui/fullPng.png")

        fixed:
            ypos -8
            
            add "./gui/boxframecombat.png":
                zoom 0.55
            text (arousalBarText):
                xpos 25
                ypos 95  
                size 25

screen restrain:
    timer xpBarMoveSpeed action Function(renpy.call, "restrainDrain", from_current = True) repeat True 
# todo: when aroused, make xpbarmovespeed half
screen fuzzy():
    zorder 1000
    image "./gui/fuzzy.png":
        at asyncDissolve35(0, 1, 5)

# menu screens                    

# screen stat_popup():
#     timer 5 action Function(deletePopup) repeat True
#     vbox:
#         for statPopup in statPopups:
#             fixed:
#                 ysize 50
#                 add "./gui/textBox.png":
#                     xsize 0.2
#                     ysize 1.0
#                     alpha 0.7
#                 text "[statPopup]":
#                     xpos 10
#                     ypos 1
#                 at statsPopupAnim

            


define statsColor = "#ff0"
define dwn = "{font=DejaVuSans.ttf}↓{/font}"
define up = "{font=DejaVuSans.ttf}↑{/font}"
screen stats_stats():

    fixed:
        at combatMenuMainMenu
        xpos 0.43
        text "{color=[currentEnemy.profile.color]}Stats{/color}": 
            size 75
            ypos 0.15
        text "Level: {color=[statsColor]}[currentEnemy.level]":
            ypos 0.25
        text "XP: {color=[statsColor]}[currentEnemy.levelBottom]{/color}/{color=[statsColor]}[currentEnemy.XP]{/color}/{color=[statsColor]}[currentEnemy.levelTop]":
            ypos 0.3
        text "Health: {color=[statsColor]}[currentEnemy.health]{/color}/{color=[statsColor]}[currentEnemy.maxHealth]":
            ypos 0.35
        text "Attack: {color=[statsColor]}[currentEnemy.attack]":
            ypos 0.4

screen LostXPPopup(XPLost, x=0.5, y=0.2):
    text "[dwn] [XPLost] XP":
        at downPopup(x, y)
        size 100
        color "#fff"
        outlines [ (absolute(10), "#f55", absolute(3), absolute(3)) ]
        
screen GainedXPPopup(XPGained, x=0.05, y=0.4):
    text "[up] [XPGained] XP":
        at upPopup(x, y)
        size 100
        color "#fff"
        outlines [ (absolute(10), "#5f5", absolute(3), absolute(3)) ]
        
screen GainedLevelPopup(level, x=0.05, y=0.4):
    text "[up] level [level]":
        at upPopup(x, y)
        size 100
        color "#fff"
        outlines [ (absolute(10), "#5f5", absolute(3), absolute(3)) ]
        
screen LostLevelPopup(level, x=0.05, y=0.4):
    text "[dwn] level [level]":
        at downPopup(x, y)
        size 100
        color "#fff"
        outlines [ (absolute(10), "#f55", absolute(3), absolute(3)) ]