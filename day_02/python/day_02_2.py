#!/usr/bin/env python

'''
Advent of Code - Day Two, Part Two
'''

checksum = 0

with open('../input.txt', 'r') as f:
    file_content = f.read().split('\n')

for row in file_content:
    if len(row) > 1:
        row = row.split('\t')
        row = map(int, row)
        row = sorted(row, reverse=True)

        for value in row:
            result = list(filter((lambda x: value % x == 0), row))
            if len(result) > 1:
                checksum += int(result[0] / result[1])

print("Answer:", checksum)
