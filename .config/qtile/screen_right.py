from libqtile import widget
from colors import *

def init_widgets_list_right():
    widgets_list = [
        widget.TextBox(background = blue,
            foreground = black,
            text = ' ',
            fontsize = 22,
            padding = -3,
            markup = True),
        widget.GroupBox(background = blue,
            active = black,
            inactive = indigo,
            disable_drag = True,
            highlight_method = 'line',
            highlight_color = orange,
            fontsize = 14,
            font = 'Source Code Pro Bold'),        
        widget.TextBox(background = blue,
            foreground = black,
            text = ' ',
            fontsize = 22,
            markup = True,
            padding = -4),
        widget.WindowName(background = red,
        foreground = dark,
        padding = 10),
        widget.Systray(background = green,
            icon_size = 18,
            padding = 5),
        widget.TextBox(background = green,
            foreground = black,
            text = ' ',
            fontsize = 22,
            padding = -1,
            markup = True),

    ]
    return widgets_list

