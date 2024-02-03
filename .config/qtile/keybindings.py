from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile.dgroups import simple_key_binder
from variables import *

dgroups_key_binder = simple_key_binder(mod)

keys = [
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(),
        #desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "Escape", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #Key([mod], "space", lazy.spawn("fish -c ~/scripts/dmenu_drun.sh")),
    Key([mod], "space", lazy.spawn("rofi -show drun -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc="Switch between open apps"),
    #Key([mod], "space", lazy.spawn("fish -c '~/scripts/sounds.sh confirm'"), lazy.spawn("fish -c '~/scripts/dmenu_drun.sh; ~/scripts/sounds.sh pokemon'"), desc="dmenu drun"),
    Key([mod], "Tab", lazy.spawn("rofi -show window -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc="Switch between open apps"),

    # Toggle between different layouts as defined below
    Key([mod], "BackSpace", lazy.next_layout(), desc="Toggle between layouts"),
    #Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "control"], "Delete", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "End", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawn("fish -c ~/scripts/dmenu_run.sh")),
    Key([mod], "r", lazy.spawn("dmenu_run"), desc="Switch between open apps"),
    #Key([mod], "r", lazy.spawn("fish -c '~/scripts/sounds.sh pause'"), lazy.spawn("fish -c '~/scripts/dmenu_run.sh'")),
    #Key([mod], "r", lazy.spawn("dmenu_run")),
    Key([mod], "f", lazy.spawn(filemanager), desc="Launch file manager"),
    #Key([mod, "control"], "f", lazy.spawn(termfilemanager), desc="Launch terminal file manager"),
    Key([mod], "x", lazy.spawn("xkill"), desc="Kill unresponsible application, scroll mouse weel to cancel"),
    Key([mod], "b", lazy.spawn(browser), desc ="Lauch web browser"),
    # Key([mod], "v", lazy.spawn("vscodium"), desc="Launch Vscodium"),
    #Key([mod], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "w", lazy.spawn("nitrogen"), desc="Change wallpaper"),
    Key([mod], "F11", lazy.window.toggle_fullscreen(), desc='Toggle fullscreen'),
    Key([mod], "Print", lazy.spawn("fish -c ~/scripts/ss.sh"), desc='Takescreenshot'),
    # Key([mod], "m", lazy.spawn("kitty -e ranger ~/.config")),
    Key([mod], "n", lazy.spawn("fish -c ~/.config/qtile/control-center.sh"), desc='Notifications'),
    Key([mod, "shift"], "n", lazy.spawn("dunstctl close"), desc='Close notification'),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+"), desc='Volume +5%'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-"), desc='Volume -5%'),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle"), desc='Toggle mute'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc='Brightness -2%'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc='Brightness +2%'),
    #Key([mod], "h", lazy.spawn("kitty -o background_opacity=0.95 --class floating -e keybindings.sh"), desc='Get help'),
    Key([mod, "control"], "Escape", lazy.spawn("fish -c ~/.config/qtile/powermenu.sh"), desc='Power menu'),
    Key([mod], "L", lazy.spawn("betterlockscreen -l"), desc='Lock screen'),
    Key([mod], "period", lazy.spawn("rofi -modi emoji -show emoji -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc='Launch emoji picker'),
    Key([mod], "d", lazy.spawn("fish -c ~/.config/qtile/dashboard.sh"), desc='Dashboard widgets'),
    #Key([mod], "k", lazy.spawn("fish -c ~/.config/qtile/keqinging.sh"), desc='Keqinging'),
    Key([mod], "k", lazy.spawn("eww open keqing"), desc='Keqinging'),
    Key([mod], "t", lazy.spawn("fish -c ~/.config/qtile/trayer.sh")),
    Key([mod], "h", lazy.group['scratchpad'].dropdown_toggle('keybindings'),desc='Show keybindings'),
    Key([mod, "control"], "f", lazy.group['scratchpad'].dropdown_toggle('termfilemanager'), desc='Terminal file manager'),
]
