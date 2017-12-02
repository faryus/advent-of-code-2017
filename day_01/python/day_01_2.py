#!/usr/bin/env python

'''
Advent of Code - Day One, Part Two
'''

with open('../input.txt', 'r') as f:
    d1_input = f.read()

captcha = 0
step = int(len(d1_input) / 2)

i = 0
while i in range(len(d1_input)):
    if d1_input[i - step] == d1_input[i]:
        captcha += int(d1_input[i])
    i += 1

print("Answer:", captcha)