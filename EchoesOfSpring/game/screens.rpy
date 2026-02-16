# ============================================================================
# screens.rpy — Core UI Screens for Echoes of Spring
# ============================================================================

# ---- Say Screen (dialogue) ------------------------------------------------
screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Solid("#000000cc")

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    ypos gui.name_ypos
    padding (5, 5, 5, 5)

style say_label:
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    xpos gui.dialogue_xpos
    xanchor gui.dialogue_text_xalign
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

# ---- Input Screen ---------------------------------------------------------
screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width

            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xalign gui.dialogue_text_xalign

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

# ---- Choice Screen --------------------------------------------------------
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing 10

style choice_button is default:
    xsize gui.choice_button_width
    background Solid("#444444aa")
    hover_background Solid("#ff99ccaa")
    padding (20, 8, 20, 8)

style choice_button_text is default:
    color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    xalign 0.5
    text_align 0.5
    layout "subtitle"

# ---- Quick Menu (bottom bar during gameplay) ------------------------------
screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back")    action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip")    action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto")    action Preference("auto-forward", "toggle")
            textbutton _("Save")    action ShowMenu('save')
            textbutton _("Q.Save")  action QuickSave()
            textbutton _("Q.Load")  action QuickLoad()
            textbutton _("Prefs")   action ShowMenu('preferences')

default quick_menu = True

style quick_button:
    background None
    padding (10, 2, 10, 2)

style quick_button_text:
    size gui.notify_text_size
    idle_color "#aaa"
    hover_color gui.hover_color

# ---- Navigation (main & game menus) --------------------------------------
screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start")      action Start()
        else:
            textbutton _("History")    action ShowMenu("history")
            textbutton _("Save")       action ShowMenu("save")

        textbutton _("Load")          action ShowMenu("load")
        textbutton _("Preferences")   action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        if not main_menu:
            textbutton _("Main Menu")  action MainMenu()

        textbutton _("About")         action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help")      action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("Quit")       action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

# ---- Main Menu ------------------------------------------------------------
screen main_menu():
    tag menu
    style_prefix "main_menu"

    add Solid("#2a1a3a")

    frame:
        pass

    use navigation

    if gui.show_name:
        vbox:
            xalign 1.0
            yalign 0.0
            xoffset -20
            yoffset 20

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

style main_menu_frame:
    xsize 280
    background Solid("#000000aa")

style main_menu_title:
    size gui.title_text_size
    color gui.accent_color
    xalign 1.0
    text_align 1.0

style main_menu_version:
    size gui.notify_text_size
    color "#ffffff80"
    xalign 1.0
    text_align 1.0

# ---- Game Menu (shared overlay for save/load/prefs etc.) ------------------
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add Solid("#2a1a3a")

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"
                use navigation

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
                        transclude
                else:
                    transclude

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title

style game_menu_outer_frame:
    background Solid("#000000dd")
    xfill True
    yfill True

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    xfill True
    yfill True
    left_margin 40
    right_margin 20
    top_margin 10

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

# ---- About ----------------------------------------------------------------
screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"

        vbox:
            label "[config.name!t]"
            text _("[config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

style about_label_text:
    size gui.label_text_size

# ---- Save / Load ----------------------------------------------------------
screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:
            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing 10

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

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing 5

                textbutton _("<") action FilePagePrevious()
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()

style slot_button:
    xsize gui.slot_button_width
    ysize gui.slot_button_height
    padding gui.slot_button_borders.padding

style slot_time_text:
    size gui.slot_button_text_size

style slot_name_text:
    size gui.slot_button_text_size

# ---- Preferences ----------------------------------------------------------
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
                        textbutton _("Window")     action Preference("display", "window")
                        textbutton _("Fullscreen")  action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable")  action Preference("rollback side", "disable")
                    textbutton _("Left")     action Preference("rollback side", "left")
                    textbutton _("Right")    action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text")       action Preference("skip", "toggle")
                    textbutton _("After Choices")     action Preference("after choices", "toggle")
                    textbutton _("Transitions")       action InvertSelected(
                                                            Preference("transitions", "toggle"))

            null height 20

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

style radio_button:
    padding (18, 4, 4, 4)

style check_button:
    padding (18, 4, 4, 4)

style slider_slider:
    xsize 296

style slider_pref_vbox:
    xsize 225

# ---- History Screen -------------------------------------------------------
screen history():
    tag menu
    use game_menu(_("History"), scroll=("vpgrid"), yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window:
                has hbox:
                    yfill True
                    spacing 20
                text (h.who or "") min_width gui.history_name_width text_align gui.history_name_xalign
                text h.what

style history_window:
    xfill True
    ysize gui.history_height

# ---- Help / Keyboard shortcuts --------------------------------------------
screen help():
    tag menu
    use game_menu(_("Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 15

            hbox:
                label _("Enter")
                text _("Advances dialogue and activates the interface.")
            hbox:
                label _("Space")
                text _("Advances dialogue without selecting choices.")
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
                label _("Page Up / Scroll Up")
                text _("Rolls back to earlier dialogue.")
            hbox:
                label _("Page Down / Scroll Down")
                text _("Rolls forward to later dialogue.")
            hbox:
                label _("H")
                text _("Hides the user interface.")
            hbox:
                label _("S")
                text _("Takes a screenshot.")
            hbox:
                label _("V")
                text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
            hbox:
                label _("F")
                text _("Toggle fullscreen.")

style help_label:
    xsize 250

# ---- Confirm (yes/no) popup -----------------------------------------------
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#000000cc")

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Yes") action yes_action
                textbutton _("No")  action no_action

    key "game_menu" action no_action

style confirm_frame:
    background Solid("#333333ee")
    padding (40, 40, 40, 40)
    xalign 0.5
    yalign 0.5

style confirm_prompt is gui_prompt:
    xalign 0.5
    text_align 0.5

# ---- Skip indicator -------------------------------------------------------
screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 6
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .6)
        repeat

style skip_frame:
    ypos gui.skip_ypos
    background Solid("#000000aa")
    padding (16, 5, 50, 5)

style skip_triangle:
    font "DejaVuSans.ttf"

# ---- Notify ---------------------------------------------------------------
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

style notify_frame:
    ypos 45
    background Solid("#000000aa")
    padding (16, 5, 40, 5)

style notify_text:
    size gui.notify_text_size
