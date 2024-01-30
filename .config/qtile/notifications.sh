#! /bin/bash

historysize=$(dunstctl count history)
displayed=$(dunstctl count displayed)

function repeat(){
  for ((i=0;i<$1;i++)); do
    eval ${*:2}
  done
}

if [ "$displayed" = 0 ] 
then
	repeat $historysize dunstctl history-pop
else
	dunstctl close-all
fi
