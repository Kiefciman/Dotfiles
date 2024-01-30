#! /bin/bash
source /usr/local/lib/simple_curses.sh

main() {
	window "Keybindings" "blue"
	append_tabbed "Win+Arrows:move focus" 2
	append_tabbed "Win+Shift+arrow:move window" 2
	append_tabbed "Win+Ctrl+arrow:grow window" 2
	append_tabbed "Win+Esc:reset windows sizes" 2
	append_tabbed "Win+Backspace:change layout" 2
	append_tabbed "Win+Q:close window" 2
	append_tabbed "Win+Shift+F:toggle floating" 2
	append_tabbed "Win+F11:toggle fullscreen" 2
	addsep
	append_tabbed "Win+Control+Detele:restart qtile" 2
	append_tabbed "Win+Control+End:exit qtile (logout)" 2
	append_tabbed "Win+L:lock screen" 2
	append_tabbed "Win+H:help" 2
	addsep
	append_tabbed "Win+Space:launch applications" 2
	append_tabbed "Win+R:run prompt" 2
	append_tabbed "Win+Tab:switch windows" 2
	addsep
	append_tabbed "Win+W:change wallpaper" 2
	append_tabbed "Win+A:take screenshot" 2
	append_tabbed "Win+Enter:terminal" 2
	append_tabbed "Win+F:graphical file manager" 2
	append_tabbed "Win+Control+F:terminal file manager" 2
	append_tabbed "Win+N:web browser" 2
	addsep
	append_tabbed "Win+N:notification history" 2
	append_tabbed "Win+Shift+N:close notification" 2
	addsep
	append_tabbed "And Fn+Simbols" 1
	endwin
}

main_loop -t 9999999999999999999999999999 $@
