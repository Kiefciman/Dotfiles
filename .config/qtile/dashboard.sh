
#!/bin/sh

dashboard(){
LOCK_FILE="$HOME/.cache/eww-powermenu.lock"
EWW_BIN="/usr/bin/eww"

run() {
    ${EWW_BIN} open profile
	${EWW_BIN} open calendar
	${EWW_BIN} open time
	${EWW_BIN} open image
	${EWW_BIN} open music
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
    ${EWW_BIN} close profile
	${EWW_BIN} close calendar
	${EWW_BIN} close time
	${EWW_BIN} close image
	${EWW_BIN} close music
    rm "$LOCK_FILE"
fi
}

dashboard
