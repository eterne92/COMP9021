#!/bin/sh
for i in $(seq 1990 2015)
do
    for j in $(seq 1990 2015)
    do
        echo -e $i'--' $j'\n 10000'|python quiz_4.py|grep Korea
    done
done
