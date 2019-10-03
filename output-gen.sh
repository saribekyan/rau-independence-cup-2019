#!/bin/bash

problemId=$1
echo $executable
if [ ! -f $executable ]; then
    pysol=$problemId*/sol.py
    if [ ! -f $pysol ]; then
        echo "No solution found for problem $problem"
        exit 1
    fi
    executable="python $pysol"
fi

FILES=ejudge/tests/$problemId/[0-9][0-9][0-9]
for f in $FILES
do
    echo "Running $f"
    $executable < $f > $f.a
done

