#!/bin/bash

INPUT=$(cat $(dirname $0)/../input.txt)
LEN=${#INPUT}
STEP=1

TOTAL=0

I=1
while [ $I -lt $LEN ]
do
  if [ ${INPUT:$((I-1)):1} -eq ${INPUT:$I:1} ]
  then
    ((TOTAL+=${INPUT:$I:1}))
  fi
  ((I++))
done

echo $TOTAL