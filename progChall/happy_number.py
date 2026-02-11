#!/usr/bin/env python3

import sys

def is_happy(num: str, seen: set[int]) -> bool:
    '''
    >>> is_happy("19", set())
    True

    >>> is_happy("1", set())
    True

    >>> is_happy("2", set())
    False

    >>> is_happy("7", set())
    True
    '''
    n = int(num)
    # base case
    if n  == 1: return True
    if n in seen: return False

    seen.add(n)
   
    total = sum(int(d) ** 2 for d in num)

    # recursive step
    return is_happy(str(total), seen)

# With memoization
'''
def is_happy(num: str, seen: set[int], cache: dict[int, bool]) -> bool:
    n = int(num)

    if n in cache:
        return cache[n]

    if n == 1:
        cache[n] = True
        return True

    if n in seen:
        cache[n] = False
        return False

    seen.add(n)

    total = sum(int(d) ** 2 for d in num)
    result = is_happy(str(total), seen, cache)

    cache[n] = result
    return result

def main() -> None:
    cache = {}
    for word in sys.stdin:
        print('Yes' if is_happy(word.rstrip(), set(), cache) else 'No')
'''

# Main Execution

def main() -> None:
    for word in sys.stdin:
        print('Yes' if is_happy(word.rstrip(), set()) else 'No')

if __name__ == '__main__':
    main()
