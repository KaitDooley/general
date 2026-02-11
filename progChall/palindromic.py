#!/usr/bin/env python3

# Exercise 08-A: Palindromic Permutations

import collections
import sys

# Functions

def is_palindromic(s: str) -> bool:
    # TODO
    table = {}

    for c in s:
        table[c] = table.get(c, 0) + 1
    '''
    table = collections.defaultdict(int)

    for c in s:
        table[c] += 1
    '''

    odd = 0

    for key, value in table.items():
        if value % 2 == 1:
            odd += 1
    
    return odd <= 1

'''
def is_palindromic(s:str) -> bool:
    seen = set()
    
    for c in s:
        if c in seen:
            seen.remove(c)
        else:
            seen.add(c)

    return len(seen) <= 1
'''


# Main Execution

def main() -> None:
    for word in sys.stdin:
        print('Yes' if is_palindromic(word.rstrip()) else 'No')

if __name__ == '__main__':
    main()
