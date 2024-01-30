if status is-interactive
    # Commands to run in interactive sessions can go here
end

###########
# Startup #
###########
set fish_greeting
starship init fish | source
#~/projects/nekofetch/nekofetch.sh
#~/Bunnyfetch/bunnyfetch
#figlet Kiefciman 
#~/scripts/asciicat.sh
~/scripts/wow.sh
#colorscript -e 45
#echo "" && pfetch
#clear && ~/pokemon-icat/pokemon-icat.sh
#pokemon-colorscripts -r --no-title
set fish_cursor_default block
set fish_cursor_insert block

export PATH="$PATH:/home/kiefciman/.dotnet/tools"
export YTUI_MUSIC_DIR=/home/kiefciman/Music/

###########
# Aliases #
###########
#alias fortune='fortune | cowthink'
alias mal='cd ~/AniFetch/ && ./AniFetch.py kiefciman && cd'
alias funfact='cd ~/fun-fact-cli/ && ./funfacts.sh | cowthink && cd'
alias copypasta='cd ~/CopypastaBanner && python3 ./banner.py && cd'
#alias clear='clear && ~/scripts/asciicat.sh'
#alias clear='clear && colorscript -e 45'
#alias clear='clear && ~/pokemon-icat/pokemon-icat.sh'
#alias clear='clear && pokemon-colorscripts -r --no-title'
#alias clear='clear && ~/projects/nekofetch/nekofetch.sh'
alias clear='clear && ~/scripts/wow.sh'
alias fishrc='nvim ~/.config/fish/config.fish'
alias qtilerc='nvim ~/.config/qtile/config.py'
alias kittyrc='nvim ~/.config/kitty/kitty.conf'
alias picomrc='nvim ~/.config/picom/picom.conf'
alias ewwrc='nvim ~/.config/eww/eww.yuck'
alias ewwstyle='nvim ~/.config/eww/eww.scss'
alias starshiprc='nvim ~/.config/starship.toml'
alias c='clear'
alias night='redshift -O 3500'
alias day='redshift -x'
alias dunstrc='nvim ~/.config/dunst/dunstrc'
alias vimrc='nvim .config/nvim'
alias rofirc='nvim .config/rofi/config.rasi'
alias note='nvim Documents/vimwiki/quicknotes.md'
alias wiki='nvim Documents/vimwiki/index.md'
alias help='~/.config/fish/help.sh'
alias h='help'
#alias cat='catcat.sh'
alias myanimestats='~/scripts/myanimestats/./myanimestats.sh'
alias lavat='lavat -c blue -R 1 -k red'
alias ls='ptls -a'
alias la='ptls -la'
alias pwd='ptpwd'
alias dotfiles='/usr/bin/git --git-dir=$HOME/Github/Dotfiles/ --work-tree=$HOME'
#alias animu='cd ~/scripts/animu/; ./animu.sh $1; cd'
#alias mpv='flatpak run io.mpv.Mpv'
alias wisdom="python3 ~/wisdom-tree/wisdom_tree/main.py "

############################
# Catppuccin color palette #
############################
# --> special
set -l foreground cdd6f4
set -l selection 313244

# --> palette
set -l teal 94e2d5
set -l flamingo f2cdcd
set -l mauve cba6f7
set -l pink f5c2e7
set -l red f38ba8
set -l peach fab387
set -l green a6e3a1
set -l yellow f9e2af
set -l blue 89b4fa
set -l gray 6c7086

# Syntax Highlighting
set -g fish_color_normal $foreground
set -g fish_color_command $blue
set -g fish_color_param $flamingo
set -g fish_color_keyword $red
set -g fish_color_quote $green
set -g fish_color_redirection $pink
set -g fish_color_end $peach
set -g fish_color_error $red
set -g fish_color_gray $gray
set -g fish_color_selection --background=$selection
set -g fish_color_search_match --background=$selection
set -g fish_color_operator $pink
set -g fish_color_escape $flamingo
set -g fish_color_autosuggestion $gray
set -g fish_color_cancel $red

# Prompt
set -g fish_color_cwd $yellow
set -g fish_color_user $teal
set -g fish_color_host $blue

# Completion Pager
set -g fish_pager_color_progress $gray
set -g fish_pager_color_prefix $pink
set -g fish_pager_color_completion $foreground
set -g fish_pager_color_description $gray

fish_add_path /home/kiefciman/.spicetify

#eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
