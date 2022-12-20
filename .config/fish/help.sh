#! /bin/bash
source /usr/local/lib/simple_curses.sh

main() {
	window "Commands" "blue" 
	append_tabbed "fortune:random fortune cookie" 2
	append_tabbed "mal:MyAnimeList stats" 2
	append_tabbed "copypasta:random r/copypasta post" 2
	append_tabbed "funfact:random fun fact" 2
	append_tabbed "day / night:turn blue light filter off/on" 2
	append_tabbed "apropos:show command for usecase specified in argument" 2
	append_tabbed "ps:show running processes" 2
	append_tabbed "note:take a quick vimwiki note" 2
	append_tabbed "wiki:show vimwiki start page" 2
	append_tabbed "lavat:lava lamp" 2
	endwin

	window "Settings" "blue"
	append_tabbed "fishrc:fish shell config" 2
	append_tabbed "qtilerc:qtile window manager config" 2
	append_tabbed "kittyrc:kitty terminal config" 2
	append_tabbed "picomrc:picom compositor config" 2
	append_tabbed "ewwrc:eww widgets config" 2
	append_tabbed "ewwstyle:eww widgets style" 2
	append_tabbed "starshiprc:starship prompt config" 2
	append_tabbed "dunstrc: dunst notifications config" 2
	append_tabbed "vimrc:neovim text editor config" 2
	append_tabbed "rofirc:rofi app launcher/switcher config" 2
	endwin

}

update() {
	return 255
	return 0
}

main_loop $@

