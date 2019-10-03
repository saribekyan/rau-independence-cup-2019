#!/bin/bash

problemId=$1
executable=`ls problems/$problemId*/a.out 2> /dev/null`
if [ -z $executable ]; then
    pysol=`ls problems/$problemId*/sol.py 2> /dev/null`
    if [ -z $pysol ]; then
        echo "No solution found for problem $problem"
        exit 1
    fi
    executable="python $pysol"
fi
echo $executable

FILES=tests/$problemId/[0-9][0-9][0-9]
for f in $FILES
do
    echo "Running $f"
    $executable < $f > $f.a
done

