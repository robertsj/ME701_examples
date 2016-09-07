#!/bin/bash

# The following two lines were used to read in values from the terminal and save to x
#echo -n "Enter a number -> "
#read x

# This line reads the first argument from the terminal call and sets it to x
# Remember $0 returns the name of the function and $1, $2, ${10} etc are the arguments
x=$1

# Print the square of the entered value
echo "$x^2 is $(($x*$x))"

# Check if the variable is equal to zero
if [ $x -eq 0 ]; then
    echo "x = zero"
else
    # Check if the variable is negative
    if [ $x -lt 0 ]; then
        echo "x is negative"
    else
        echo "x is positive"
    fi
fi
    
