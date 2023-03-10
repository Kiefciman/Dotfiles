from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from libqtile import hook
from libqtile import qtile
import os
import subprocess

mod = 'mod4'
terminal = 'kitty'
filemanager = 'pcmanfm'
termfilemanager = 'ranger'
browser = 'chromium'

dgroups_key_binder = simple_key_binder("mod4")
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "Qtile"

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
    Key([mod], "Return", lazy.spawn(terminal + " -o background_opacity=0.6"), desc="Launch terminal"),
    Key([mod], "space", lazy.spawn("rofi -show drun -drun-display-format {name} -show-icons -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc="Launch applications menu"),
    Key([mod], "Tab", lazy.spawn("rofi -show window -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc="Switch between open apps"),

    # Toggle between different layouts as defined below
    Key([mod], "BackSpace", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "Delete", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "End", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show run -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.spawn(filemanager), desc="Launch file manager"),
    #Key([mod, "control"], "f", lazy.spawn(termfilemanager), desc="Launch terminal file manager"),
    Key([mod], "x", lazy.spawn("xkill"), desc="Kill unresponsible application, scroll mouse weel to cancel"),
    Key([mod], "b", lazy.spawn(browser), desc ="Lauch web browser"),
    # Key([mod], "v", lazy.spawn("vscodium"), desc="Launch Vscodium"),
    #Key([mod], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "w", lazy.spawn("nitrogen"), desc="Change wallpaper"),
    Key([mod], "F11", lazy.window.toggle_fullscreen(), desc='Toggle fullscreen'),
    Key([mod], "a", lazy.spawn("flameshot full"), desc='Takescreenshot'),
    # Key([mod], "m", lazy.spawn("kitty -e ranger ~/.config")),
    Key([mod], "n", lazy.spawn("fish -c ~/.config/qtile/control-center.sh"), desc='Notifications'),
    Key([mod, "shift"], "n", lazy.spawn("dunstctl close"), desc='Close notification'),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+"), desc='Volume +5%'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-"), desc='Volume -5%'),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle"), desc='Toggle mute'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("blight set -2%"), desc='Brightness -2%'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("blight set +2%"), desc='Brightness +2%'),
    #Key([mod], "h", lazy.spawn("kitty -o background_opacity=0.95 --class floating -e keybindings.sh"), desc='Get help'),
    Key([mod, "control"], "Escape", lazy.spawn("fish -c ~/.config/qtile/powermenu.sh"), desc='Power menu'),
    Key([mod], "L", lazy.spawn("betterlockscreen -l"), desc='Lock screen'),
    Key([mod], "period", lazy.spawn("rofi -modi emoji -show emoji -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc='Launch emoji picker'),
    Key([mod], "d", lazy.spawn("fish -c ~/.config/qtile/dashboard.sh"), desc='Dashboard widgets'),
]

groups = [#Group("??\_(???)_/??", layout='columns'),
          Group("(^??? ??? ???^)", layout='columns'),
          Group("\_(^_^)_/", layout='columns'),
          #Group("(???^???^)???", layout='columns'),
          #Group("\ (???-???) /", layout='monadtall'),
          Group("(?????????)", layout='columns'),
          #Group("??????(????????)??????", layout='monadtall'),
          Group("(???^_^)???", layout='columns'),
          Group("(=^~^=)", layout='columns')]

layout_theme = {"border_width": 3,
                "margin": 6,
                "border_focus": "7287fd",
                "border_normal": "C9CBFF",
                "border_on_single": True
                }

layouts = [
    layout.Columns( **layout_theme),
    layout.Max( **layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    #layout.Bsp(**layout_theme),
    layout.Matrix( **layout_theme),
    #layout.MonadTall(**layout_theme),
    layout.MonadWide( **layout_theme),
    layout.RatioTile( **layout_theme),
    #layout.Tile(**layout_theme),
    # layout.TreeTab(),
    #layout.VerticalTile(**layout_theme),
    # layout.Zoomy(),
    layout.Floating( **layout_theme)
]

widget_defaults = dict(
    font='Source Code Pro Bold',
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()

colors = ["#F28FAD", #0 red
          "#F8BD96", #1 orange
          "#FAE3B0", #2 yellow
          "#ABE9B3", #3 green
          "#89DCEB", #4 cian
          "#7aa2f7", #5 blue
          "#bb9af7", #6 pink
          "#D9E0EE", #7 white
          "#C3BAC6", #8 cream
          "#575268", #9 indigo
          "#302D41", #10 dark
          "#1A1823", #11 black
]

def init_widgets_list_right():
    widgets_list = [
        #widget.Sep(background = colors[0],
        #    linewidth = 10,
        #    foreground = colors[0]),
        widget.TextBox(background = colors[0],
            foreground = colors[10],
            text = ' ??? ',
            fontsize = 16,
            markup = True,
            font = 'HeavyData Nerd Font Bold'),
        widget.CurrentLayout(background = colors[0],
            foreground = colors[11],
            font = 'Hack Nerd Font Bold'),
        widget.TextBox(background = colors[5],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.GroupBox(background = colors[5],
            active = colors[11],
            inactive = colors[9],
            disable_drag = True,
            highlight_method = 'line',
            highlight_color = colors[0],
            fontsize = 14,
            font = 'Source Code Pro'),
        widget.TextBox(background = colors[0],
            foreground = colors[5],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Spacer(background = colors[0]),
        #widget.TextBox(background = colors[3],
        #    foreground = colors[0],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.Clock(format = '%H:%M',
        #    background = colors[3],
        #    foreground = colors[10]),
        #widget.TextBox(background = colors[3],
        #    foreground = colors[0],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.Spacer(background = colors[0]),
        #widget.TextBox(background = colors[0],
        #    foreground = colors[5],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.TextBox(text='???',
        #    fontsize = 17,
        #    font = 'HeavyData Nerd Font bold',
        #    background = colors[5],
        #    foreground = colors[9]),
        #widget.CPU(background = colors[5],
        #    foreground = colors[10],
        #    format = '{load_percent}%'),
        #widget.TextBox(background = colors[5],
        #    foreground = colors[0],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.TextBox(text='???',
        #    markup = True,
        #    font = 'HeavyData Nerd Font',
        #    fontsize = 17,
        #    background = colors[0],
        #    foreground = colors[9]),
        #widget.NvidiaSensors(background = colors[0],
        #    foreground = colors[10],
        #    format = '{temp}??C'),
        #widget.TextBox(background = colors[0],
        #    foreground = colors[5],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.TextBox(text='???',
        #    fontsize = 17,
        #    font = 'HeavyData Nerd Font',
        #    background = colors[5],
        #    foreground = colors[9]),
        #widget.Memory(background = colors[5],
        #    foreground = colors[10],
        #    format = '{MemUsed:.0f}MB'),
        widget.TextBox(background = colors[0],
            foreground = colors[5],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            fontsize = 17,
            font = 'HeavyData Nerd Font',
            background = colors[5],
            foreground = colors[9]),
        widget.Volume(background = colors[5],
            foreground = colors[11],
            update_interval = 0.1),
        widget.TextBox(background = colors[5],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            fontsize = 17,
            font = 'HeavyData Nerd Font bold',
            background = colors[0],
            foreground = colors[9]),
        widget.Wttr(background = colors[0],
            foreground = colors[11],
            format = '%f ',
            location = {'46.9601847': '25.2392115'},
            units = 'm',
            padding = 4,
            update_interval = 7200),
        widget.TextBox(background = colors[0],
            foreground = colors[3],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Clock(format = '%H:%M',
            background = colors[3],
            foreground = colors[10]),
        #widget.TextBox(background = colors[3],
        #    foreground = colors[0],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        widget.TextBox(background = colors[3],
            foreground = colors[1],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Clock(format='%d.%m %a',
            background = colors[1],
            foreground = colors[10]),
        widget.TextBox(background = colors[1],
            foreground = colors[6],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Systray(background = colors[6],
            icon_size = 20,
            padding = 1),
        #widget.Sep(background = colors[6],
        #    linewidth = 10,
        #    foreground = colors[6],
        #    padding = 5),
        ]
            #27,
            #margin = [0, -12, 0, -12]
    return widgets_list

def init_widgets_list_left():
    widgets_list = [
        #widget.Sep(background = colors[0],
        #    linewidth = 10,
        #    foreground = colors[0]),
        widget.TextBox(background = colors[0],
            foreground = colors[10],
            text = ' ??? ',
            fontsize = 16,
            markup = True,
            font = 'HeavyData Nerd Font Bold'),
        widget.CurrentLayout(background = colors[0],
            foreground = colors[11],
            font = 'Hack Nerd Font Bold'),
        widget.TextBox(background = colors[5],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.GroupBox(background = colors[5],
            active = colors[11],
            inactive = colors[9],
            disable_drag = True,
            highlight_method = 'line',
            highlight_color = colors[0],
            fontsize = 14,
            font = 'Source Code Pro'),
        widget.TextBox(background = colors[0],
            foreground = colors[5],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Spacer(background = colors[0]),
        #widget.TextBox(background = colors[3],
        #    foreground = colors[0],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.Clock(format = '%H:%M',
        #    background = colors[3],
        #    foreground = colors[10]),
        #widget.TextBox(background = colors[3],
        #    foreground = colors[0],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.Spacer(background = colors[0]),
        widget.TextBox(background = colors[0],
            foreground = colors[5],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            fontsize = 17,
            font = 'HeavyData Nerd Font bold',
            background = colors[5],
            foreground = colors[9]),
        widget.CPU(background = colors[5],
            foreground = colors[10],
            format = '{load_percent}%'),
        widget.TextBox(background = colors[5],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            markup = True,
            font = 'HeavyData Nerd Font',
            fontsize = 17,
            background = colors[0],
            foreground = colors[9]),
        widget.NvidiaSensors(background = colors[0],
            foreground = colors[10],
            format = '{temp}??C'),
        widget.TextBox(background = colors[0],
            foreground = colors[5],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            fontsize = 17,
            font = 'HeavyData Nerd Font',
            background = colors[5],
            foreground = colors[9]),
        widget.Memory(background = colors[5],
            foreground = colors[10],
            format = '{MemUsed:.0f}MB'),
        widget.Sep(background = colors[5],
            linewidth = 5,
            foreground = colors[5],
            padding = 5)
        ]
    return widgets_list

def init_widgets_list_single():
    widgets_list = [
        #widget.Sep(background = colors[0],
        #    linewidth = 10,
        #    foreground = colors[0]),
        widget.TextBox(background = colors[0],
            foreground = colors[10],
            text = ' ??? ',
            fontsize = 16,
            markup = True,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show drun -show-icons -hover-select -me-select-entry '' -me-accept-entry MousePrimary"),
                               'Button3': lambda: qtile.cmd_spawn(terminal + " -o background_opacity=0.6")},
            font = 'HeavyData Nerd Font Bold'),
        widget.CurrentLayout(background = colors[0],
            foreground = colors[11],
            font = 'Hack Nerd Font Bold'),
        widget.TextBox(background = colors[5],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.GroupBox(background = colors[5],
            active = colors[11],
            inactive = colors[9],
            disable_drag = True,
            highlight_method = 'line',
            highlight_color = colors[0],
            fontsize = 14,
            font = 'Source Code Pro'),
        widget.TextBox(background = colors[0],
            foreground = colors[5],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Spacer(background = colors[0]),
        widget.TextBox(background = colors[3],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Clock(format = '%H:%M',
            background = colors[3],
            foreground = colors[10],
                     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('fish -c "~/.config/qtile/time.sh"')}),
        widget.TextBox(background = colors[3],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Spacer(background = colors[0]),
        widget.TextBox(background = colors[0],
                foreground = colors[6],
                fontsize = 22,
                markup = True,
                padding = -1,
                text = '???'),
        widget.TextBox(background = colors[6],
                foreground = colors[10],
                text = '??????????????????',
                fontsize = 13,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("xterm -e nyancat")}),
        widget.TextBox(background = colors[6],
            foreground = colors[5],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            fontsize = 17,
            font = 'HeavyData Nerd Font bold',
            background = colors[5],
            foreground = colors[9]),
        widget.CPU(background = colors[5],
            foreground = colors[10],
            format = '{load_percent}%'),
        #widget.TextBox(background = colors[5],
        #    foreground = colors[0],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.TextBox(text='???',
        #    markup = True,
        #    font = 'HeavyData Nerd Font',
        #    fontsize = 17,
        #    background = colors[0],
        #    foreground = colors[9]),
        #widget.NvidiaSensors(background = colors[0],
        #    foreground = colors[10],
        #    format = '{temp}??C'),
        widget.TextBox(background = colors[5],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            fontsize = 17,
            font = 'HeavyData Nerd Font',
            background = colors[0],
            foreground = colors[9]),
        widget.Memory(background = colors[0],
            foreground = colors[10],
            format = '{MemUsed:.0f}MB'),
        widget.TextBox(background = colors[0],
            foreground = colors[5],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            fontsize = 17,
            font = 'HeavyData Nerd Font',
            background = colors[5],
            foreground = colors[9]),
        widget.Volume(background = colors[5],
            foreground = colors[11],
            update_interval = 0.1,
            step = 5),
        widget.TextBox(background = colors[5],
            foreground = colors[0],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.TextBox(text='???',
            markup = True,
            font = 'HeavyData Nerd Font',
            fontsize = 17,
            background = colors[0],
            foreground = colors[9]),
        widget.NvidiaSensors(background = colors[0],
            foreground = colors[10],
            format = '{temp}??C'),
        #widget.TextBox(text='???',
        #    fontsize = 17,
        #    font = 'HeavyData Nerd Font bold',
        #    background = colors[0],
        #    foreground = colors[9]),
        #widget.Wttr(background = colors[0],
        #    foreground = colors[11],
        #    format = '%f ',
        #    location = {'46.9601847': '25.2392115'},
        #    units = 'm',
        #    padding = 4,
        #    update_interval = 7200),
        #widget.TextBox(background = colors[0],
        #    foreground = colors[3],
        #    text = '???',
        #fontsize = 22,
        #    markup = True,
        #    padding = -1),
        #widget.Clock(format = '%H:%M',
        #    background = colors[3],
        #    foreground = colors[10]),
        #widget.TextBox(background = colors[3],
        #    foreground = colors[0],
        #    text = '???',
        #    fontsize = 22,
        #    markup = True,
        #    padding = -1),
        widget.TextBox(background = colors[0],
            foreground = colors[1],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Clock(format='%d.%m %a',
            background = colors[1],
            foreground = colors[10],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("fish -c ~/.config/qtile/dashboard.sh")}),
        widget.TextBox(background = colors[1],
            foreground = colors[6],
            text = '???',
            fontsize = 22,
            markup = True,
            padding = -1),
        widget.Systray(background = colors[6],
            icon_size = 20,
            padding = 1),
        #widget.Sep(background = colors[6],
        #    linewidth = 10,
        #    foreground = colors[6],
        #    padding = 5),
        ]
            #27,
            #margin = [0, -12, 0, -12]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list_right()
    return widgets_screen1
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list_left()
    return widgets_screen2
def init_widgets_screen3():
    widgets_screen3 = init_widgets_list_single()
    return widgets_screen3

#def init_screens():
#    return [Screenw(top = bar.Bar(widgets = init_widgets_screen1(), size = 27)),
#            Screen(top = bar.Bar(widgets = init_widgets_screen2(), size = 27))]

def init_screens():
    return [Screen(top = bar.Bar(widgets = init_widgets_screen3(), size = 27))]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

if __name__ in ["config", "__main__"]:
    screens = init_screens()
#    widgets_list = init_widget_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='floating'),
])

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

#@hook.subscribe.startup_complete
#def startupafter():
#    home = os.path.expanduser('~/.config/qtile/startup-after.sh')
#    subprocess.run([home])

groups.append(ScratchPad("scratchpad", [
    DropDown("keybindings", terminal + " -e keybindings.sh", width=0.5, height=0.9, x=0.25, y=0.02, opacity=0.9),
    DropDown("termfilemanager", terminal + " -e " + termfilemanager, width=0.8, height=0.7, x=0.1, y=0.15, opacity=0.9),
]))

keys.extend([
    Key([mod], "h", lazy.group['scratchpad'].dropdown_toggle('keybindings'),desc='Show keybindings'),
    Key([mod, "control"], "f", lazy.group['scratchpad'].dropdown_toggle('termfilemanager'), desc='Terminal file manager'),
])
