################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    if inCombat:
        style_prefix "sayCombat"
        fixed:
            image "gui/textboxcombat.png"
            id "windows"
            xpos 0.0
            ypos 0.735

            if who is not None:
                fixed:
                    id "namebox"
                    ypos -0.45
                    xpos -0.08
                    text who id "who"

            text what: 
                id "what"
                xpos 800
                xanchor 0.5
                xsize 1250
                ypos 100
                yanchor 0.1
                

    else:
        style_prefix "say"

        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style sayCombat_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textBox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False
    
## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    if len(items) > 4:
        style_prefix "choiceMany"

        grid 4 4:
            for i in items:
                textbutton i.caption action i.action, Function(buttonClicked)
    else:
        if inCombat:
            style_prefix "choiceCombat"

            vbox:
                for i in items:
                    textbutton i.caption action i.action, Function(buttonClicked)
        else:
            style_prefix "choice"

            vbox:
                for i in items:
                    textbutton i.caption action i.action, Function(buttonClicked)


style choice_vbox is vbox
style choice_hbox is hbox
style choice_button is button
style choice_button_text is button_text

style choiceCombat_vbox is vbox
style choiceCombat_hbox is hbox
style choiceCombat_button is button
style choiceCombat_button_text is button_text

style choiceMany_vbox is vbox
style choiceMany_hbox is hbox
style choiceManyutton is button
style choiceMany_text is button_text

style choice_vbox:
    xpos 0.55
    ypos 0
    yanchor 0.0
    xanchor 0.5

    spacing gui.choice_spacing

style choice_hbox:
    xalign 0.5
    ypos 0.1
    yanchor 0.5
    xanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    xanchor 0.9
    xpos 0.8
    ypos 800
    activate_sound "/Sfx/decision1.mp3"

style choice_button_text is default:
    properties gui.text_properties("choice_button")

# Combat menu

style choiceCombat_vbox:
    xalign 0.4
    ypos 0.123
    yanchor 0.5

    spacing gui.choice_spacing

style choiceCombat_hbox:
    xalign 0.5
    ypos 0.1
    yanchor 0.45
    xanchor 0.625

    spacing gui.choice_spacing

style choiceCombat_button is default:
    properties gui.button_properties("choice_button")
    xanchor 0.9
    xpos 0.8
    ypos 800

style choiceCombat_button_text is default:
    properties gui.text_properties("choice_button")

# Many menu

style choiceMany_grid:
    xalign 0.4
    ypos 0.123
    yanchor 0.5
    xsize 10

    spacing gui.choice_spacing

style choiceMany_button is default:
    properties gui.button_properties("choice_button")
    xanchor 1.18
    xpos 0.8
    ypos 820
    xsize 335

    spacing 0.5

style choiceMany_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            # textbutton _("Back") action Rollback()
            # textbutton _("History") action ShowMenu('history')
            # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("Auto") action Preference("auto-forward", "toggle")
            # textbutton _("Save") action ShowMenu('save')
            # textbutton _("Q.Save") action QuickSave()
            # textbutton _("Q.Load") action QuickLoad()
            # textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    if renpy.get_screen("main_menu"):
        hbox:
            style_prefix "hnavigation"

            xalign 0.5
            yalign 1.0
            yoffset -50

            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("Start") action Start() style "start_button"

            else:

                textbutton _("History") action ShowMenu("history")

                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load") style "load_button"

            # textbutton _("Preferences") action ShowMenu("preferences")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Main Menu") action MainMenu()

            # textbutton _("About") action ShowMenu("about")

            # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            #     ## Help isn't necessary or relevant to mobile devices.
            #     textbutton _("Help") action ShowMenu("help")

            # if renpy.variant("pc"):

            #     ## The quit button is banned on iOS and unnecessary on Android and
            #     ## Web.
            #     textbutton _("Quit") action Quit(confirm=not main_menu)
    else:
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("Start") action Start()

            # else:

            #     textbutton _("History") action ShowMenu("history")

            #     textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            # textbutton _("Preferences") action ShowMenu("preferences")

            # if _in_replay:

            #     textbutton _("End Replay") action EndReplay(confirm=True)

            # elif not main_menu:

            #     textbutton _("Main Menu") action MainMenu()

            # textbutton _("About") action ShowMenu("about")

            # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            #     ## Help isn't necessary or relevant to mobile devices.
            #     textbutton _("Help") action ShowMenu("help")

            # if renpy.variant("pc"):

            #     ## The quit button is banned on iOS and unnecessary on Android and
            #     ## Web.
            #     textbutton _("Quit") action Quit(confirm=not main_menu)

style start_button_text:
    size 100
    xpos 0.0
    ypos 0.8
    outlines [ (absolute(10), "#43a047", absolute(3), absolute(3)) ]

style load_button_text:
    size 100
    ypos 0.8
    outlines [ (absolute(10), "#FFB300", absolute(3), absolute(3)) ]
    

style navigation_button is gui_button
style navigation_button_text is gui_button_text
style hnavigation_button is navigation_button
style hnavigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

style hnavigation_button_text:
    xalign 0.1

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        hbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    # background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

define combatMenu = "Main"
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    if inCombat:
        add gui.game_menu_background alpha 0.7
        textbutton "{size=100}< Close":
            action Return()
        fixed:
            fixed:
                xpos 0.05
                ypos 0.1
                at combatMenuMainText
                text "{color=[currentEnemy.profile.color]}[currentEnemy.profile.name]{/color}": 
                    size 100

                add "./gui/textBox.png":
                    xzoom 0.45
                    yzoom 3.0
                    xoffset -23
                    at combatMenuBg

                text "[currentEnemy.profile.description]":
                    ypos 0.15
                    xsize 0.35
                    text_align 0.5


            # add "./gui/textBox.png":
            #     alpha 0.5    
            #     xzoom 0.27
            #     yzoom 3.0
            #     xoffset 800
            #     yoffset 100
            #     at combatMenuBg

            use stats_stats

            fixed:
                xpos 0.43
                at combatMenuInventory
                text "{color=[currentEnemy.profile.color]}Inventory{/color}":
                    ypos 0.5
                    size 75
                text "Weapon: [currentEnemy.inventory.weapon.name]":
                    ypos 0.6
                text "Damage: {color=#ff0}+[currentEnemy.inventory.weapon.attack]":
                    ypos 0.64
                text "Armor: [currentEnemy.inventory.armor.name]":
                    ypos 0.7
                text "Health: {color=#ff0}+[currentEnemy.inventory.armor.health]":
                    ypos 0.74
                


            fixed:
                xpos 0.3
                ypos 10
                text "{color=#f00}Saving disabled during combat{/color}"
                
            fixed:
                xpos 0.3
                at combatMenuMainImg
                add "[currentEnemy.profile.pageId]_display"

    else:
        style_prefix "game_menu"

        if main_menu:
            add gui.main_menu_background

            frame:
                style "game_menu_outer_frame"

                hbox:

                    ## Reserve space for the navigation section.
                    frame:
                        style "game_menu_navigation_frame"

                    frame:
                        style "game_menu_content_frame"

                        if scroll == "viewport":

                            viewport:
                                yinitial yinitial
                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                pagekeys True

                                side_yfill True

                                vbox:
                                    spacing spacing

                                    transclude

                        elif scroll == "vpgrid":

                            vpgrid:
                                cols 1
                                yinitial yinitial

                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                pagekeys True

                                side_yfill True

                                spacing spacing

                                transclude

                        else:

                            transclude

            use navigation

            textbutton _("Return"):
                style "return_button"

                action Return()

            label title

            if main_menu:
                key "game_menu" action ShowMenu("main_menu")

        else:
            add gui.game_menu_background alpha 0.8
            use inGameNav
            

            fixed:
                xpos 0.4
                fixed:
                    xpos 0.05
                    ypos 0.1
                    fixed:
                        at playerMenuMainText
                        text "{color=[player.profile.color]}Stats{/color}": 
                            size 100 
                            ypos 0.15
                        text "Level: {color=[statsColor]}[player.level]":
                            ypos 0.25
                        text "XP: {color=[statsColor]}[player.levelBottom]{/color}/{color=[statsColor]}[player.XP]{/color}/{color=[statsColor]}[player.levelTop]":
                            ypos 0.3
                        text "Health: {color=[statsColor]}[player.health]{/color}/{color=[statsColor]}[player.maxHealth]":
                            ypos 0.35
                        text "Attack: {color=[statsColor]}[player.attack]":
                            ypos 0.4
                        text "Money: {color=[statsColor]}[player.money]":
                            ypos 0.45

                    fixed:
                        at playerMenuMainInventory
                        text "{color=[player.profile.color]}Inventory{/color}": 
                            size 100 
                            ypos 0.15
                        
                        textbutton "Weapon: [player.inventory.weapon.name] \n Attack:{color=#ff0} [player.inventory.weapon.attack]":
                            ypos 0.25
                            action ShowMenu("invWeapons")
                        
                        textbutton "Armor: [player.inventory.armor.name] \n Health:{color=#ff0} [player.inventory.armor.health]":
                            ypos 0.35
                            action ShowMenu("invArmors")

            transclude

screen inGameNav:
    fixed:
        xpos 0.05
        fixed:
            ypos 0.2
            textbutton _("Home"):
                        action ShowMenu("save")
                        style "profile"
        
        fixed:
            ypos 0.3
            textbutton _("Load"):
                        action ShowMenu("load")
                        style "profile"

        fixed:
            ypos 0.4
            textbutton _("Save"):
                        action ShowMenu("save")
                        style "profile"  

        fixed:
            ypos 0.5
            textbutton _("Quit game"):
                        action MainMenu()
                        style "profile"  

        textbutton "{size=100}< Close":
                action Return()
              
screen invWeapons:
    tag menu
    add gui.game_menu_background alpha 0.7
    use inGameNav

    fixed:
        xpos 0.3
        ypos 0.1
        text "Weapons":
            size 100

        viewport:
            ypos 0.15
            mousewheel True
            draggable True
            grid 2 8:
                xspacing 50
                for weapon in player.inventory.unlockedWeapons:
                    if weapon == player.inventory.weapon:
                        text "[weapon.name]":
                            color "#ff7979"
                            size 50
                    else:
                        textbutton "[weapon.name]":
                            style "equipmentBtn"
                            action SetVariable("player.inventory.weapon", weapon), ShowMenu("save")
        
screen invArmors:
    tag menu
    add gui.game_menu_background alpha 0.7
    use inGameNav

    fixed:
        xpos 0.3
        ypos 0.1
        text "Armors":
            size 100

        viewport:
            ypos 0.15
            mousewheel True
            draggable True
            grid 2 8:
                xspacing 50
                for armor in player.inventory.unlockedArmors:
                    if armor == player.inventory.armor:
                        text "[armor.name]":
                            color "#ff7979"
                            size 50
                    else:
                        textbutton "[armor.name]":
                            style "equipmentBtn"
                            action SetVariable("player.inventory.armor", armor), ShowMenu("save")

screen shopGui(place):
    add gui.game_menu_background alpha 0.7 at asyncDissolve2(0, 1, 0.9)
    fixed:         
        fixed:
            at slideInLeft(-0.5, 0.1, 1)
            
            add "./gui/textBox.png":
                rotate 90
                xsize 0.3
                ysize 0.4
                xpos -0.1
                ypos 0.01

            use itemSelection

        fixed:
            xpos 0.3
            ypos 0.08
            add "./gui/textBox.png":
                xzoom 0.2
                yzoom 0.2
            text "Money: {color=#ff0} [player.money]":
                ypos 7
                xpos 10
            at slideInBottom(-0.5, 0.08, 1)

        fixed:
            at slideInBottom(1.5, 0.7, 1)
            xpos 0.25
            add "./gui/textBox.png":
                xzoom 0.5
                alpha 0.7

            use shoptext
            
            text shopKeeperDialogue:
                xanchor 0.5
                xpos 0.2
                xsize 0.3
                ypos 0.05

        fixed:
            at slideInOther(-0.1, 1.0, 0.1, 0.8, 1)
            xpos 0.1
            ypos 0.8
            textbutton "< Exit":
                action Return()
                style "ExitBtnShop"

        fixed:
            at shopMenuMainImg
            add "[place]_shopdisplaycharacter"
            imagebutton:
                xpos 0.4
                ysize 0.8
                xsize 0.2
                ypos 0.2
                idle "alphaBlack" 
                action Function(renpy.call, "setShopTouchyText", place) 

screen shopGuiTouchy(place):
    add gui.game_menu_background alpha 0.7
    fixed:         
        fixed:
            xpos 0.1            
            add "./gui/textBox.png":
                rotate 90
                xsize 0.3
                ysize 0.4
                xpos -0.1
                ypos 0.01

            use itemSelection

        fixed:
            xpos 0.3
            ypos 0.08
            add "./gui/textBox.png":
                xzoom 0.2
                yzoom 0.2
            text "Money: {color=#ff0} [player.money]":
                ypos 7
                xpos 10

        fixed:
            ypos 0.7
            xpos 0.25
            add "./gui/textBox.png":
                xzoom 0.5
                alpha 0.7

            use shoptext
            
            text shopKeeperDialogue:
                xanchor 0.5
                xpos 0.2
                xsize 0.3
                ypos 0.05

        fixed:
            xpos 0.1
            ypos 0.8
            textbutton "< Exit":
                action Return()
                style "ExitBtnShop"

        fixed:
            at shopMenuMainImgBounce
            add "[place]_shopdisplaycharacter"
            imagebutton:
                xpos 0.4
                ysize 0.8
                xsize 0.2
                ypos 0.2
                idle "alphaBlack" 
                action Function(renpy.call, "setShopTouchyText", place) 



screen itemSelection:
    if place == "town":
        fixed:
            ypos 0.1
            text "Weapons":
                size 75

            fixed:
                ypos 0.1
                if not weapons[1].name in [weapon.name for weapon in player.inventory.unlockedWeapons]:
                    textbutton "Wooden sword {color=#ff0}[weapons[1].price]G{/color}":
                        action ShowMenu("confirmWeaponPurchase", weapons[1], place)
                else:
                    text "Wooden sword [weapons[1].price]G":
                        color "#aaa"

            fixed:
                ypos 0.15
                if not weapons[2].name in [weapon.name for weapon in player.inventory.unlockedWeapons]:
                    textbutton "Silver blade {color=#ff0}[weapons[2].price]G{/color}":
                        action ShowMenu("confirmWeaponPurchase", weapons[2], place)
                else:
                    text "Silver blade [weapons[2].price]G":
                        color "#aaa"
    
        fixed:
            ypos 0.35
            text "Armors":
                size 75

            fixed:
                ypos 0.1
                if not armors[1].name in [armor.name for armor in player.inventory.unlockedArmors]:
                    textbutton "Leather armor {color=#ff0}[armors[1].price]G{/color}":
                        action ShowMenu("confirmArmorPurchase", armors[1], place)
                else:
                    text "Leather armor [armors[1].price]G":
                        color "#aaa"

            fixed:
                ypos 0.15
                if not armors[2].name in [armor.name for armor in player.inventory.unlockedArmors]:
                    textbutton "Silver shield {color=#ff0}[armors[2].price]G{/color}":
                        action ShowMenu("confirmArmorPurchase", armors[2], place)
                else:
                    text "Silver shield [armors[2].price]G":
                        color "#aaa"

    elif place == "merchant":
        fixed:
            ypos 0.1
            text "Items":
                size 75

            fixed:
                ypos 0.1
                if True:
                    textbutton "Cure for poison":
                        action Function(renpy.jump, "merchantPoisonBuy")

            fixed:
                ypos 0.2
                if game.pfp.merchantUnlocked == False:
                    textbutton "Poster of her face":
                        action Function(renpy.jump, "merchantPfpBuy")

                else:
                    text "Poster of her face":
                        color "#aaa"
    
        

screen shoptext:
    if place == "town":
        text "[shopKeeper]":
            xanchor 0.5
            xpos 0.2
            ypos -0.05
            size 60
    else:
        text "[merchant]":
            xanchor 0.5
            xpos 0.2
            ypos -0.05
            size 60




screen confirmWeaponPurchase(weapon, place):
    add gui.game_menu_background alpha 0.7
    tag confirmShop

    fixed:
        xpos 0.15
        ypos 0.35
        xsize 0.35
        add "./gui/textBox.png":
            xpos -40
            ypos -40
            xzoom 0.5

        if not player.money >= weapon.price:
            fixed:
                text "{color=#f00}You don't have enough money!"
                xpos 0.6
                xanchor 0.5
                ypos 0.15

        text "Are you sure you want to purchase this \n [weapon.name]":
            xanchor 0.5
            xpos 0.5
            text_align 0.5
        fixed:
            xpos 0.3
            ypos 0.1
            if player.money >= weapon.price:
                textbutton "Yes":
                    action Function(unlockWeaponF, player, weapon, place)
            else:
                text "Yes":
                    color "#aaa"
        textbutton "No":
            ypos 0.1
            xpos 0.5
            action Return()

    fixed:
        xpos 0.3 
        add "[place]_shopdisplaycharacter"

screen confirmArmorPurchase(armor, place):
    add gui.game_menu_background alpha 0.7
    tag confirmShop

    fixed:
        xpos 0.15
        ypos 0.35
        xsize 0.35
        add "./gui/textBox.png":
            xpos -40
            ypos -40
            xzoom 0.5

        if not player.money >= armor.price:
            fixed:
                text "{color=#f00}You don't have enough money!"
                xpos 0.6
                xanchor 0.5
                ypos 0.15

        text "Are you sure you want to purchase this \n [armor.name]":
            xanchor 0.5
            xpos 0.5
            text_align 0.5
        fixed:
            xpos 0.3
            ypos 0.1
            if player.money >= armor.price:
                textbutton "Yes":
                    action Function(unlockArmorF, player, armor, place)
            else:
                text "Yes":
                    color "#aaa"
        textbutton "No":
            ypos 0.1
            xpos 0.5
            action Return()

    fixed:
        xpos 0.3 
        add "[place]_shopdisplaycharacter"


screen objective:
    fixed:
        add "./gui/textBox.png":
            alpha 0.7
            xzoom 0.3
            yzoom 0.7
        text "Objective":
            outlines [ (absolute(5), "#511818", absolute(0), absolute(0)) ]
            size 40
            ypos -30
            xpos 0.1
            xoffset -60
        text "[getCurrentObjective().description]":
            xsize 0.2
            xpos 50
            ypos 30
            color "#fff"
            outlines [ (absolute(5), "#511818", absolute(0), absolute(0)) ]

        at objectiveAnim
        
screen objectiveComplete:
    fixed:
        add "./gui/checkcompletewhitefull.png" zoom 0.05 xpos -75
        text "Objective completed!":
            outlines [ (absolute(5), "#66dc6c", absolute(0), absolute(0)) ]

        at objectiveCompletedAnim

screen statusEffects:
    zorder 10
    if inCombat:
        fixed:
            xpos 0.78
            ypos 0.5
            grid 6 5:
                xpos 10
                spacing 10
                use statusEffectsList

    else:
        fixed:
            if inShopGui:
                xpos 0.3
                ypos 0.15
                fixed:
                    if hasStatusEffect():
                        add "./gui/textBox.png":
                            alpha 0.7
                            xzoom 0.2
                            yzoom 0.6
                            ypos -20
                            at asyncDissolve2(0.0, 1.0, 1)
    
                grid 7 5:
                    xpos 10
                    spacing 10
                    use statusEffectsList
            else:
                xpos 0.7
                ypos 0.3
                fixed:
                    if hasStatusEffect():
                        add "./gui/textBox.png":
                            alpha 0.7
                            xzoom 0.3
                            yzoom 0.6
                            ypos -20
                            at asyncDissolve2(0.0, 1.0, 1)

                grid 7 5:
                    xpos 10
                    spacing 10
                    use statusEffectsList

screen statusEffectsList:
    if player.conditions.poisoned > 0:
        imagebutton:
            idle "/images/Status/poison.png"
            hover "/images/Status/poison.png"
            at statusEffect
            hovered Show("tooltipscreen", None, "Poisoned: take damage at the start of each turn, based on your current health.\n{color=#ff0}"+str(player.conditions.poisoned)+"{/color} turns left")
            unhovered Hide("tooltipscreen")
            action SetVariable(uselessVar, "blep")
    
    if player.conditions.horny:
        imagebutton:
            idle "/images/Status/charmed.png"
            hover "/images/Status/charmed.png"
            at statusEffect
            hovered Show("tooltipscreen", None, "Horny: Take extra damage from sex attacks")
            unhovered Hide("tooltipscreen")
            action SetVariable(uselessVar, "blep")

    if player.conditions.casinoDebt:
        imagebutton:
            idle "/images/Status/casinodebt.png"
            hover "/images/Status/casinodebt.png"
            at statusEffect
            hovered Show("tooltipscreen", None, "Casino girls' curse: increase your arousal intake by 1.5X until your debt is paid off")
            unhovered Hide("tooltipscreen")
            action SetVariable(uselessVar, "blep")

    if player.conditions.princessServant:
        imagebutton:
            idle "/images/Status/princessservant.png"
            hover "/images/Status/princessservant.png"
            at statusEffect
            hovered Show("tooltipscreen", None, "Princess's servant: Share 50% of XP with the slime princess upon winning a battle.")
            unhovered Hide("tooltipscreen")
            action SetVariable(uselessVar, "blep")

    if player.conditions.slimePet:
        imagebutton:
            idle "/images/Status/slimepet.png"
            hover "/images/Status/slimepet.png"
            at statusEffect
            hovered Show("tooltipscreen", None, "Weak to mouths: Take double damage from mouth related attacks.")
            unhovered Hide("tooltipscreen")
            action SetVariable(uselessVar, "blep")
            

screen tooltipscreen(text="tip"):
    if inCombat:
        fixed:
            at asyncDissolve3(0.0, 1.0, 0.2)
            xpos 0.783
            ypos 0.62
            xsize 0.21
            text "[text]"
    else:
        fixed:
            at asyncDissolve3(0.0, 1.0, 0.2)
            xpos 0.71
            ypos 0.45
            xsize 0.21
            add "./gui/textBox.png":
                ypos -15
                xpos -17
                xzoom 0.3
            text "[text]"

    

define yellowKiss = Matrix([
    1.0, 1.0, 1.0, 1.0,
    0.3, 0.9, 1.1, 0.1,
    0.3, 0.9, 1.1, 0.1,
    0.0, 0.0, 0.0, 0.8,
])

label clearAllLipstick:
    hide screen lipstickMark onlayer kiss1
    hide screen lipstickMark onlayer kiss2
    hide screen lipstickMark onlayer kiss3
    hide screen lipstickMark onlayer kiss4
    hide screen lipstickMark onlayer kiss5
    hide screen lipstickMark onlayer kiss6
    hide screen lipstickMark onlayer kiss7
    return


screen lipstickMark(x, y, opacity=1, enterTime=1, p_size=1, rotation=0, dissolveOverTime=True):
    fixed:
        if dissolveOverTime:
            at asyncDissolve2(1.0, 0.0, 10)
        else:
            at asyncDissolve2(1.0, 0.0, 60)
            
        xpos x
        ypos y
        add "kiss_mark":
            matrixcolor yellowKiss
            at asyncDissolve2(0.0, opacity, enterTime)
            zoom p_size
            rotate rotation

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style ExitBtnShop:
    size 500

style ExitBtnShop_text:
    size 75
    hover_color rose

style profile:
    size 500

style profile_text:
    size 75
    hover_color rose

style equipmentBtn:
    size 500

style equipmentBtn_text:
    color "#fff"
    size 50
    hover_color "#ff5d5d"

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "#bf8f8fdd"
    # foreground "gui/fuzzy.png" 
    

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title, overworld=False):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:
            if main_menu:
                ypos 0.05

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            # button:
            #     style "page_label"

            #     key_events True
            #     xalign 0.5
            #     action page_name_value.Toggle()

            #     input:
            #         style "page_label_text"
            #         value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                if main_menu:
                    ypos -0.2
                else:
                    yalign 0.4
                xalign 0.8

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.85
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")
    color rose
    hover_color "#f00"

## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

# style pref_vbox:
#     variant "medium"
#     xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
# screen quick_menu():
#     variant "touch"

#     zorder 100

#     if quick_menu:

#         hbox:
#             style_prefix "quick"

#             xalign 0.5
#             yalign 1.0

#             textbutton _("Back") action Rollback()
#             textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
#             textbutton _("Auto") action Preference("auto-forward", "toggle")
#             textbutton _("Menu") action ShowMenu()


# style window:
#     variant "small"
#     background "gui/phone/textbox.png"

# style radio_button:
#     variant "small"
#     foreground "gui/phone/button/radio_[prefix_]foreground.png"

# style check_button:
#     variant "small"
#     foreground "gui/phone/button/check_[prefix_]foreground.png"

# style nvl_window:
#     variant "small"
#     background "gui/phone/nvl.png"

# style main_menu_frame:
#     variant "small"
#     background "gui/phone/overlay/main_menu.png"

# style game_menu_outer_frame:
#     variant "small"
#     background "gui/phone/overlay/game_menu.png"

# style game_menu_navigation_frame:
#     variant "small"
#     xsize 510

# style game_menu_content_frame:
#     variant "small"
#     top_margin 0

# style pref_vbox:
#     variant "small"
#     xsize 600

# style bar:
#     variant "small"
#     ysize gui.bar_size
#     left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#     right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

# style vbar:
#     variant "small"
#     xsize gui.bar_size
#     top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#     bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

# style scrollbar:
#     variant "small"
#     ysize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

# style vscrollbar:
#     variant "small"
#     xsize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

# style slider:
#     variant "small"
#     ysize gui.slider_size
#     base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

# style vslider:
#     variant "small"
#     xsize gui.slider_size
#     base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

# style slider_vbox:
#     variant "small"
#     xsize None

# style slider_slider:
#     variant "small"
#     xsize 900
