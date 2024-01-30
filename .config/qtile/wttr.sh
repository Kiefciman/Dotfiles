#! /bin/bash

curl --silent wttr.in/Stanceni | sed 4!d | cut -d'(' -f2 | cut -d')' -f1
