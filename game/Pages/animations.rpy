transform bounce:
    ysize 1.0
    ease 0.1 ysize 1.05 ypos -0.05
    ease 0.1 ysize 1.0 ypos -0.0
    ease 0.1 ysize 1.025 ypos -0.025
    ease 0.1 ysize 1.0 ypos -0.0
    ease 0.1 ysize 1.00625 ypos -0.00625
    ease 0.1 ysize 1.0 ypos -0.0
    ysize None

transform bounceLesser:
    ysize 1.0
    ease 0.1 ysize 1.05 ypos 1.0
    ease 0.1 ysize 1.0 ypos 1.0
    ease 0.1 ysize 1.025 ypos 1.0
    ease 0.1 ysize 1.0 ypos 1.0
    ease 0.1 ysize 1.00625 ypos 1.0
    ease 0.1 ysize 1.0 ypos 1.0
    ysize None

transform continuousBounce(intensity=1.1, speed=0.5):
    ysize 1.00 ypos (intensity - 1.0)
    ease speed ysize intensity ypos 0.0
    ease speed ysize 1.00 ypos (intensity - 1.0)
    repeat

transform continuousBounce2(intensity=1.1, speed=0.5):
    ysize 1.00 ypos (intensity)
    ease speed ysize intensity ypos 1.0
    ease speed ysize 1.00 ypos (intensity)
    repeat


transform asyncDissolve(seconds, end=0.0):
    ease seconds alpha end

transform asyncDissolve2(start, end, seconds):
    alpha start
    ease_back seconds alpha end

transform asyncDissolve3(start, end, seconds):
    on show:
        alpha start
        ease_back seconds alpha end 
    on hide:
        alpha end
        ease_back seconds alpha start

transform asyncDissolve35(start, end, seconds):
    on show:
        linear seconds alpha end 
    on hide:
        linear seconds alpha start


transform jumpy:
    ysize 1.0 ypos 1.0
    ease 0.1 ypos 0.9 ysize 1.0
    ease 0.1 ypos 1.0 ysize 1.0
    ysize None
    ypos None

transform blbm_slide:
    ypos 1.0 xpos -0.2 zoom 0.5
    ease 0.5 ypos 0.14 xpos -0.22 zoom 0.92
    ease 0.2 ypos 0.2 xpos -0.24 zoom 0.9

transform imp_stats_1:
    ypos 0.2 xpos -0.24 zoom 0.9
    ease 0.3 zoom 0.5 ypos 0.18 xpos -0.04

transform imp_stats_2:
    parallel:
        zoom 0.5 xpos -0.04
        ease 0.30 xpos 0.35
    parallel:
        ypos 0.18
        ease 0.15 ypos 0.13
        ease 0.15 ypos 0.18  

transform imp_stats_3:
    zoom 0.5 xpos 0.35 ypos 0.2
    xzoom -1
    
transform imp_stats_4:
    parallel:
        zoom 0.5 xpos 0.35 xzoom 1
        ease 0.30 xpos -0.04
    parallel:
        ypos 0.18
        ease 0.15 ypos 0.13
        ease 0.15 ypos 0.18  

image imp_flipjump:
    parallel:
        parallel:
            zoom 0.5 xpos 0.6 xzoom -1
            ease 0.3 xpos 0.2 xzoom 1
        parallel:
            ypos 0.7
            ease 0.15 ypos 0.6
            ease 0.15 ypos 0.7  
    parallel:
        "imp_stand"
        pause 0.15
        "imp_happyface"
        
transform imp_stats_5:
    parallel:
        zoom 0.5 xpos -0.05
        ease 0.30 xpos -0.5
    parallel:
        ypos 0.2
        ease 0.15 ypos 0.13
        ease 0.4 ypos 0.5  

transform squishAway:
    xpos 0.0 ypos 0.0 ysize 1.0
    parallel:
        ease 0.3 ysize 0.9 ypos 0.1
        ease 0.3 ysize 0.95 ypos 0.05
        repeat 2
    parallel:
        ease 2 xpos -1.5

transform goRight:
    ease 2 xpos 1.5

transform locationNameAnimation:
    zoom 0.5 xpos -0.5 ypos 0.01
    ease 1 xpos 0.01 ypos 0.01 zoom 1.0 
    parallel:
        easein 5 xpos 0.2 ypos 0.02 zoom 1.0
    parallel:
        ease 3 alpha 0.0


transform shopMenuMainImg:
    xpos 0.0
    ease_back 0.9 xpos 0.3 

transform shopMenuMainImgBounce:
    xpos 0.3
    ysize 1.0
    ease 0.15 yzoom 1.05 ypos -0.05
    ease 0.15 yzoom 1.0 ypos -0.0
    ease 0.15 yzoom 1.025 ypos -0.025
    ease 0.15 yzoom 1.0 ypos -0.0
    ease 0.15 yzoom 1.00625 ypos -0.00625
    ease 0.15 yzoom 1.0 ypos -0.0
    ysize None

transform playerMenuMainText:
    xpos -0.15 ypos -0.6
    easein_back 0.7 ypos -0.15

transform playerMenuMainInventory:
    ypos 1.0 xpos -0.15
    easein_back 0.8 ypos 0.3

transform combatMenuMainText:
    xpos -0.2
    easein_back 0.7 xpos 0.05

transform combatMenuMainMenu:
    ypos -0.5
    easein_back 0.8 ypos 0.1

transform combatMenuMainImg:
    xpos 0.7
    easein_back 0.9 xpos 0.3 

transform combatMenuBg:
    alpha 0.0 yzoom 0.0 ypos 0.5
    ease 1 alpha 0.7 yzoom 1.0 ypos 0.10

transform combatMenuInventory:
    ypos 0.5
    easein_back 0.5 ypos 0.1

transform downPopup(x=0.5, y=0.2):
    xpos x ypos y alpha 0.0
    parallel:
        ease 0.3 alpha 0.7
        ease 1.5 alpha 0.0
    parallel:
        linear 2.3 ypos (y + 0.5)

transform upPopup(x=0.5, y=0.2):
    xpos x ypos y alpha 0.0
    parallel:
        ease 0.3 alpha 0.7
        ease 1.5 alpha 0.0
    parallel:
        linear 2.3 ypos (y - 0.5)

transform slideInLeft(start, end, time):
    xpos start
    ease_back time xpos end

transform slideInBottom(start, end, time):
    ypos start
    ease_back time ypos end

transform slideInOther(startX, startY, endX, endY, time):
    xpos startX ypos startY
    ease_back time xpos endX ypos endY

transform objectiveAnim:
    xpos 1.4 ypos 0.1
    ease_back 1 xpos 0.7

transform timeAnim:
    xpos 1.4 ypos 0.11
    ease_back 1 xpos 0.65

transform objectiveCompletedAnim:
    xpos 1.4 ypos 0.0
    ease_back 1 xpos 0.73
    pause 2.0
    ease_back 1 xpos 1.3

transform lookAround:
    xzoom 1.0 xanchor 0.5 xpos 0.6
    ease 0.7 xzoom -1.0
    
transform lookBack:
    xanchor 0.5 xpos 0.6 xzoom -1.0
    ease 0.7 xzoom 1.0

transform lesserslimeguardentercave2:
    ease 1 xpos 0.8 ypos 0.1

transform lesserslimeguardcave2:
    xpos 0.3 ypos 0.1

transform leftMirrored:
    xpos -1.0 xzoom -1.0
    ease_back 1 xpos -0.3

transform walkupslimecutscene:
    xpos -0.3 xzoom -1.0
    ease 0.3 xpos -0.2 zoom 1.2

transform pushawayslimecutscene:
    xpos -0.2 zoom 1.2
    ease 0.3 xpos -0.4

transform walkuplesserslimecutscene:
    ease 0.3 xpos 0.0 zoom 1.2

transform argue_leftw:
    ease 0.3 xpos -0.1

transform argue_rightl:
    ease 0.3 xpos 0.2

transform argue_leftl:
    ease 0.3 xpos -0.4 zoom 1.1

transform argue_rightw:
    ease 0.3 xpos 0.0

transform slime_winfight:
    xzoom -1 xpos -0.4 zoom 1.1
    ease 1 xpos -0.3 zoom 1.0

transform lookaround_slimecutscene:
    xpos 0.4 xanchor 0.5
    ease 0.5 xzoom 1

transform lookback_slimecutscene:
    xpos 0.4 xanchor 0.5
    ease 0.5 xzoom -1

image merchant_flipAss:
    xanchor 0.5 ypos 1.0
    parallel:
        xzoom 1
        ease 0.1 xzoom 0 
        ease 0.1 xzoom 1
    parallel:
        ease 0.3 zoom 2 ypos 1.2
    parallel:
        "merchant_lean_open"
        pause 0.05
        "merchant_ass"

transform merchant_zoomin(start, end, time):
    zoom start
    ease time zoom end ypos end

transform merchant_closekiss:
    zoom 1
    ease 1 zoom 1.7

transform merchant_closekiss_kiss:
    zoom 1.7
    ease 0.7 zoom 4.0
    ease 0.7 zoom 1.7

transform merchant_closekiss_kiss2:
    zoom 1.7
    ease 0.7 zoom 4.0 xpos 0.1 ypos 1.0
    ease 0.7 zoom 1.7 xpos 0.5 ypos 1.0

transform merchant_closekiss_kiss_3:
    zoom 1.0
    ease 0.7 zoom 2.0
    ease 0.7 zoom 1.0

transform statusEffect:
    alpha 0.0 zoom 0.05
    ease 1 alpha 1.0

transform innKeeperSit:
    yanchor 0.5 xanchor 0.5
    xpos 0.5 ypos 0.6
    zoom 1.2

transform casino_zoomin(start, end, time, yfactor=1, yfactorstart=0):
    zoom start xanchor 0.5 yanchor 0.5 ypos 0.5 - yfactorstart xpos 0.5
    ease time zoom end ypos end - yfactor

transform statsPopupAnim:
    xpos -1.0
    ease_back 1 xpos 0.0
    pause 3
    ease_back 1 xpos -1.0








