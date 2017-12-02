#!/usr/bin/env python

'''
Advent of Code - Day Two, Part One
'''

CHECKSUM = 0

with open('../input.txt', 'r') as f:
    FILE_CONTENT = f.read().split('\n')
    f.close()

for row in FILE_CONTENT:
    if len(row) > 1:
        row = row.split('\t')
        row = map(int, row)
        row = sorted(row)
        CHECKSUM += row[-1] - row[0]

print(CHECKSUM)
