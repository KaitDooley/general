#!/usr/bin/env python3

# Exericse 05-A: PBB-matched

import sys

# Functions

OPEN_SYMBOLS  = ('(', '[', '{')
CLOSE_SYMBOLS = (')', ']', '}')

def is_pbbmatched(s: str) -> bool:
    # TODO: Process string s using a stack to determine if the symbols are balanced 
    stack = []    
    # For each symbol
    for c in s:
    # Check if symbol is open
    # Push symbol to Stack
        if (c in OPEN_SYMBOLS):
            stack.append(c)
    # Otherwise, symbol is close
    #     Check if stack is empty, pop, compare
        elif (c in CLOSE_SYMBOLS):
            if (not(stack)):
                 return False
            #left = stack.pop()
            if OPEN_SYMBOLS.index(stack.pop()) != CLOSE_SYMBOLS.index(c):
                return False

    return not stack

# Main execution

def main():
    for line in sys.stdin:
        line   = line.rstrip()
        result = 'Yes' if is_pbbmatched(line) else 'No'
        print(f'{line:>10}: {result}')

if __name__ == '__main__':
    main()
