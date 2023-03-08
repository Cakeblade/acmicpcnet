#!/bin/bash
SRC_NAME=$1
output=$(g++ $SRC_NAME 2>&1)
if [[ $? != 0 ]]; then
	# error
	echo -e "Error: \n$output"
else
	# success
	./out.sh $SRC_NAME
fi
