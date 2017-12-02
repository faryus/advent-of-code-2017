#!/bin/bash

INPUT='../input.txt'

RESULTS=$(egrep -o '(.)\1+' $INPUT)

TOTAL=0

for RES in $RESULTS
do
	LENGTH=$((${#RES}-1))
  NUMBER=$(tr -s '0-9' <<< $RES)
  ((TOTAL+=((LENGTH*NUMBER))))
done

FIRST=$(cat $INPUT | head -c 1)
LAST=$(cat $INPUT | tail -c 1)

if [ $FIRST -eq $LAST ]
then
  ((TOTAL+=$FIRST))
fi

echo "Answer: $TOTAL"