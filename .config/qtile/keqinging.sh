
#!/bin/sh

keqinging(){
LOCK_FILE="$HOME/.cache/eww-keqing.lock"
EWW_BIN="/usr/bin/eww"

run() {
    ${EWW_BIN} open keqing
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
    ${EWW_BIN} close keqing
    rm "$LOCK_FILE"
fi
}

keqinging
