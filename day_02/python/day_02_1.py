#!/usr/bin/env python

'''
Advent of Code - Day Two, Part One
'''

checksum = 0

with open('../input.txt', 'r') as f:
    file_content = f.read().split('\n')

for row in file_content:
    if len(row) > 1:
        row = row.split('\t')
        row = map(int, row)
        row = sorted(row)
        checksum += row[-1] - row[0]

print("Answer:", checksum)
