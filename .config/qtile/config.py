
#  ██████╗ ██╗   ██╗██╗    ██╗██╗   ██╗████████╗██╗██╗     ███████╗
# ██╔═══██╗██║   ██║██║    ██║██║   ██║╚══██╔══╝██║██║     ██╔════╝
# ██║   ██║██║   ██║██║ █╗ ██║██║   ██║   ██║   ██║██║     █████╗  
# ██║▄▄ ██║██║   ██║██║███╗██║██║   ██║   ██║   ██║██║     ██╔══╝  
# ╚██████╔╝╚██████╔╝╚███╔███╔╝╚██████╔╝   ██║   ██║███████╗███████╗
#  ╚══▀▀═╝  ╚═════╝  ╚══╝╚══╝  ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝

from keybindings import keys, dgroups_key_binder
from mouse import mouse
from quick_settings import *
from app_rules import dgroups_app_rules
from groups import groups
from layouts import layouts, floating_layout
from widgets_settings import widget_defaults, extension_defaults
from screens import init_screens, switch_screens
from move_windows import window_to_prev_group, window_to_next_group, window_to_previous_screen, window_to_next_screen

if __name__ in ["config", "__main__"]:
    screens = init_screens()
