#!/usr/bin/env python3

import sys

# Type Aliases

Matrix = list[list[int]]

# Functions

def read_matrix() -> Matrix:
    n = int(sys.stdin.readline())
    return [
        list(map(int, sys.stdin.readline().split())) 
        for _ in range(n)
    ]

def find_max_row(matrix: Matrix) -> int:
    max_row = 0
    max_sum = 0

    for cur_row, cur_numbers in enumerate(matrix, 1):
        cur_sum = sum(cur_numbers)
        if cur_sum > max_sum:
            max_row = cur_row
            max_sum = cur_sum

    return max_row½,½,

# Main Executuion

def main():
    while matrix := read_matrix():
        max_row = find_max_row(matrix)
        print(max_row)

if __name__ == '__main__':
    main()
