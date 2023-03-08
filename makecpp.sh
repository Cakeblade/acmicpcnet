#!/bin/bash
if [ -z "$1" ]
then
	echo "No filename supplied"
else
	SRC_NAME=$1
	echo -e "#include <iostream>\n\nusing namespace std;\n\nint main(void)\n{\n\n}" >> $SRC_NAME.cpp
	vim $SRC_NAME.cpp
fi
