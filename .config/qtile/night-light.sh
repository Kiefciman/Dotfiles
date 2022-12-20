#! /bin/bash

file="nightlightstate.txt"
nightlightstate=$(sed 1!d $file)

if [ "$nightlightstate" = "day" ]
then
	redshift -O 3500
	echo night > $file
elif [ "$nightlightstate" = "night" ]
then
	redshift -x
	echo day > $file
else
	echo day > $file
fi
