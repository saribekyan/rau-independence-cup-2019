#!/bin/bash

problem=$1
executable=$problem/a.out
if [ ! -f $executable ]; then
    pysol=$problem/sol.py
    if [ ! -f $pysol ]; then
        echo "No solution found for problem $problem"
        exit 1
    fi
    executable="python $pysol"
fi

FILES=$problem/tests/[0-9][0-9][0-9]
for f in $FILES
do
    echo "Running $f"
    $executable < $f > $f.a
done

