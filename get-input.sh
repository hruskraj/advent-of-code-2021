#!/bin/bash

# Downloads all input files. Expects valid session cookie as argument. 

if [ -z "$1" ]
then
	echo "Insert the value of 'session' cookie"
	exit 2
fi

if [ ! -d "./input" ]
then
	mkdir "input"
fi 

for day in $(seq 1 25)
do
	wget -q --header "Cookie: session=$1" -O "input/$day.txt" "https://adventofcode.com/2021/day/$day/input"
	if [ $? -ne 0 ]
	then
		exit
	fi
done

