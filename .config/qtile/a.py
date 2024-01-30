from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder
from libqtile import hook, qtile
import os
import subprocess

mod = 'mod4'
terminal = 'kitty'
filemanager = 'pcmanfm'
termfilemanager = 'ranger'
browser = 'firefox'

dgroups_key_binder= simple_key_binder("mod4")
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "Qtile"

@hook.subscribe.startup_once
def autostart():
    autostart = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([autostart])

keys = [
    Key([mod], "Left", lazy.layout.left(), desc = "Move focus left"),
    Key([mod], "Right", lazy.layout.right(), desc = "Move focus righ"),
    Key([mod], "Down", lazy.layout.down(), desc = "Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc = "Move focus up"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc = "Move window to left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc = "Move window to right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc = "Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc = "Move window up"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc = "Grow window to left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc = "Grow window to right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc = "Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc = "Grow window up"),
    Key([mod], "Escape", lazy.layout.normalize(), desc = "Reset all window sizes"),
    Key([mod], "Return", lazy.spawn(terminal + " -o background_opacity=0.6"), desc = "Launch terminal"),
    Key([mod], "space", lazy.spawn("rofi -show drun -drun-display-format {name} -show-icons -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc = "Launch applications menu"),
    Key([mod], "Tab", lazy.spawn("rofi -show window -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc = "Switch between open apps"),
    Key([mod], "BackSpace", lazy.next_layout(), desc = "Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc = "Kill focused application"),
    Key([mod, "control"], "Delete", lazy.reload_config(), desc = "Reload qtile config"),
    Key([mod, "control"], "End", lazy.shutdown(), desc = "Exit qtile (logout)"),
    Key([mod], "r", lazy.spawn("rofi -show run -hover-select -me-select-entry '' -me-accept-entry MousePrimary"), desc = "Launch commands (run menu)"),
    Key([mod], "f", lazy.spawn(filemanager), desc = "Launch file manager"),
    Key([mod], "x", lazy.spawn("xkill"), desc = "Kill unresponding app or force kill"),
    Key([mod], "b", lazy.spawn(browser), desc = "Launch web browser"),
    Key([mod, "shift"], "f", lazy.toggle_floating(), desc = "Toggle focused window floating mode"),
    Key([mod], "w",lazy.spawn("nitrogen"), desc = "Change wallpaper"),
    Key([mod], "F11", lazy.window.toggle_fullscreen(), desc = "Toggle fullscreen"),
    Key([mod], "a", lazy.spawn("flameshot full"), desc = "Take screenshot"),
    Key([mod], "n", lazy.spawn("dunstctl history-pop"), desc = "Notifications history"),
    Key([mod, "shift"], "n", lazy.spawn("dunstctl close"), desc = "Close notification"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+"), desc = "Volume +5%"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-"), desc = "Volume -5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle"), desc= "Toggle mute"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("blight set -10%"), desc = "Brightness -10%"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("blight set +10%"), desc = "Brightness +10%"),
    Key([mod, "control"], "Escape", lazy.spawn("fish -c ~/.config/qtile/powermenu.sh"), desc = "Power menu"),
    Key([mod], "L", lazy.spawn("betterlockscreen -l"), desc = "Lock screen"),
]

groups = [Group("(^◕ ⋏ ◕^)", layout = 'columns'),
          Group("\_(^_^)_/", layout = 'columns'),
          Group("(＾∇＾)", layout = 'columns'),
          Group("(ノ^_^)ノ", layout = 'columns'),
          Group("(=^~^=)", layout = 'columns')]

layout_theme = {"border_width": 3,
                "margin": 6,
                "border_focus": "7287fd",
                "border_normal": "c9cbff",
                "border_on_single": True}

layouts = [layout.Columns( **layout_theme),
           layout.Max( **layout_theme),
           layout.Matrix( **layout_theme),
           layout.MonadWide( **layout_theme),
           layout.RatioTile( **layout_theme),
           layout.Floating( **layout_theme)]

widget_defaults = dict(
        font = 'Source Code Pro Bold',
        fontsize = 14,
        padding = 1)
extension_defaults = widget_defaults.copy

colors = ["#f28fad", #0 red
          "#f8bd96", #1 orange
          "#fae3b8", #2 yellow
          "#abe9b3", #3 green
          "#89dceb", #4 cian
          "#7aa2f7", #5 blue
          "#bb9af7", #6 pink
          "#d9e0ee", #7 white
          "#c3bac6", #8 cream
          "#575268", #9 indigo
          "#302d41", #10 dark
          "#1a1823", #11 black
]

def init_widgets_list_1():
    widgets_list = [
            widget.TextBox(background = colors[0],
                           foreground = colors[10],
                           text = ' ',
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
                           text = '',
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
                           text='',
                           fontsize = 22,
                           markup = True,
                           padding = -1),
            widget.Spacer(background = colors[0]),
            widget.TextBox(background = colors[3],
                           foreground = colors[0],
                           text = '',
                           fontsize = 22,
                           markup = True, 
                           padding = -1),
            widget.Clock(format = '%H:%M',
                        background = colors[3],
                        foreground = colors[10]),
            widget.TextBox(background = colors[3],
                           foreground = colors[0],
                           text = '',
                           fontsize = 22,
                           markup = True,
                           padding = -1),
            widget.Spacer(background = colors[0]),
            widget.TextBox(background = colors[0],
                           foreground = colors[6],
                           fontsize = 22,
                           markup = True,
                           padding = -1,
                           text = ''),
            widget.TextBox(background = colors[6],
                           foreground = colors[10],
                           fontsize = 13,
                           text = '共食いメロン',
                           mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("xterm -e nyancat")}),
            widget.TextBox(background = colors[6],
                           foreground = colors[5],
                           fontsize = 22,
                           markup = True,
                           padding = -1,
                           text = ''),
            widget.TextBox(fontsize = 17,
                           font = 'HeavyData Nerd Font Bold',
                           background = colors[5],
                           foreground = colors[9],
                           text = '礪'),
            widget.CPU(background = colors[5],
                       foreground = colors[10],
                       format = '{load_percent}%'),
            widget.TextBox(background = colors [5],
                           foreground = colors[0],
                           fontsize = 22,
                           markup = True, padding = -1,
                           text = ''),
            widget.TextBox(fontsize = 17,
                           font = 'HeavyData Nerd Font',
                           background = colors[0],
                           foreground = colors[9],
                           text = '﬙'),
            widget.Memory(background = colors[0],
                          foreground = colors[10],
                          format = '{MemUsed:.0f}MB'),
            widget.TextBox(background = colors[0],
                           foreground = colors [5],
                           fontsize = 22,
                           markup = True,
                           padding = -1,
                           text= ''),
            widget.TextBox(fontsize = 17,
                           font = 'HeavyData Nerd Font',
                           background = colors[5],
                           foreground = colors[9],
                           text = '墳'),
            widget.Volume(background = colors[5],
                          foreground = colors[11],
                          update_interval = 0.1,
                          step = 5),
            widget.TextBox(background = colors[5],
                           foreground = colors[0],
                           fontsize = 22,
                           markup = True,
                           padding = -1,
                           text = ''),
            widget.TextBox(markup = True,
                           fontsize = 17,
                           font = 'HeavyData Nerd Font',
                           background = colors[0],
                           foreground = colors[9],
                           text = '﨏'),
            widget.NvidiaSensors(background = colors[0],
                                 foreground = colors[10],
                                 format = '{temp}°C'),
            widget.TextBox(background = colors[0],
                           foreground = colors[1],
                           fontsize = 22,
                           markup = True,
                           padding = -1,
                           text = ''),
            widget.Clock(format = '%d.%m %a',
                         background = colors[1],
                         foreground = colors[10],
                         mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("fish -c ~/.config/qtile/calendar.sh")}),
            widget.TextBox(background = colors[1],
                           foreground = colors[6],
                           fontsize = 22,
                           markup = True,
                           padding = -1,
                           text = ''),
            widget.Systray(background = colors[6],
                           icon_size = 20,
                           padding = 1),
            ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list_1()
    return widgets_screen1

def init_screens():
    return [Screen(top = bar.Bar(widgets = init_widgets_screen1(), size = 27))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_screen1 = init_widgets_screen1()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

floating_layout = layout.Floating(float_rules = [
    *layout.Floating.default_float_rules,
    Match(wm_class = 'confirmreset'),
    Match(wm_class = 'makebranch'),
    Match(wm_class = 'maketag'),
    Match(wm_class = 'ssh-askpass'),
    Match(title = 'branchdialog'),
    Match(title = 'pinentry'),
    Match(wm_class = 'floating'),
])

mouse = [Drag([mod], "Button1", lazy.window.set_position_floating(),
              start = lazy.window.get_position()),
         Drag([mod], "Button3", lazy.window.set_size_floating(),
              start = lazy.window.get_size()),
         Click([mod], "Button2", lazy.window.bring_to_front())]

groups.append(ScratchPad("scratchpad", [
    DropDown("keybindings", terminal + " -e keybindings.sh", width = 0.5, height = 0.9, x = 0.25, y = 0.02, opacity = 0.9),
    DropDown("termfilemanager", terminal + " -e " + termfilemanager, width = 0.8, height = 0.7, x = 0.1, y = 0.15, opacity = 0.9),]))

keys.extend([
    Key([mod], "h", lazy.group['scratchpad'].dropdown_toggle('keybindings'), desc = "Show keybindings"),
    Key([mod, "control"], "f", lazy.group['scratchpad'].dropdown_toggle('termfilemanager'), desc = "Terminal file manager")])
