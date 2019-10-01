#!/bin/bash

problem=$1
executable=$problem/a.out
if [ ! -f $executable ]; then
    echo "No executable found at $executable"
    exit 1
fi

FILES=$problem/tests/[0-9][0-9][0-9]
for f in $FILES
do
    echo "Running $f"
    $executable < $f > $f.a
done

