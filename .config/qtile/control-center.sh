
#!/bin/sh

controlcenter(){
LOCK_FILE="$HOME/.cache/eww-powermenu.lock"
EWW_BIN="/usr/bin/eww"
historysize=$(dunstctl count history)

function repeat(){
  for ((i=0;i<$1;i++)); do
    eval ${*:2}
  done
}

run() {
    ${EWW_BIN} open controlcenter
	dunstctl close-all
	repeat $historysize dunstctl history-pop
}

# Run eww daemon if not running
if [[ ! `pidof eww` ]]; then
    ${EWW_BIN} daemon
    sleep 1
fi

# Open widgets
if [[ ! -f "$LOCK_FILE" ]]; then
    touch "$LOCK_FILE"
    run
else
    ${EWW_BIN} close controlcenter
	dunstctl close-all
    rm "$LOCK_FILE"
fi
}

controlcenter
