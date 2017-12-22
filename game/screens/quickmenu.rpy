##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.

screen quick_menu():
    # Add an in-game quick menu.
    hbox:
        style_group "quick"
        xalign 1.0
        yalign 1.0

        textbutton _("Inventory")   action ShowMenu('inventory_view')
        textbutton _("Quests")      action ShowMenu('questscreen')
        textbutton _("Stats")       action ShowMenu('statsscreen')
        textbutton _("kms")         action ShowMenu('kms')
        textbutton _("Roadmap")     action ShowMenu('roadmap')
        textbutton _("Back")        action Rollback()
        textbutton _("Save")        action ShowMenu('save')
        textbutton _("Q.Save")      action QuickSave()
        textbutton _("Q.Load")      action QuickLoad()
        textbutton _("Skip")        action Skip()
        textbutton _("F.Skip")      action Skip(fast=True, confirm=True)
        textbutton _("Auto")        action Preference("auto-forward", "toggle")
        textbutton _("Prefs")       action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 20
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"