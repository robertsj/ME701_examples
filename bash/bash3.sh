#!/bin/bash

# Define a function that checks some things about a provided integer
function checkInt {
    # set the local x to the first argument given to the function checkInt
    x=$1

    # output a blank line
    echo
    # output the square of the given integer.
    # the (( )) compound argument says we are doing some integer manipulation
    # the $ before (( )) is used to get the value of the argument
    echo "$x^2 is $(($x * $x))"

    # Check is x == 0
    if [ $x -eq 0 ]; then
        echo "x = zero"
    else
        # Check if x is negative
        if [ $x -lt 0 ]; then
            echo "x is negative"
        else
            echo "x is positive"
        fi
    fi
    return
}

# $@ is a container that holds all of the arguments given to the script
# We use the for loop to go through them one at a time and send the 
# current variable to our function checkInt

for var in "$@"
do
    checkInt $var
done
