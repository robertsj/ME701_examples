#!/bin/bash

# This is a comment

echo "Hello World."

x="100."  # Define x to the string '100.'

# Define a function called foo
function foo {
    # Send the value of x to stdout
    echo $x
    return
}

# call the function foo
foo

# Change the value of x
x="new x"
# call foo again
foo
# and again
foo

