#!/bin/bash
for DAY in `seq 1 25`;
do
    if [ -d "$DAY" ]; then
        echo "========== DAY: $DAY =========="
        cd $DAY
        python solve.py $1
        cd ..
    fi
done