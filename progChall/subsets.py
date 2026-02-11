#!/usr/bin/env python3

import sys
# Used for reading
'''
def main():
    n = 10
    total = 0

    for b in range(1<<n):
        subset_sum = 0
        for i in range(n):
            if (b&(1<<i)):
                subset_sum += i
        if subset_sum % 3 == 0: total += 1
    print(total)


if __name__ == '__main__':
    main()
'''

# First version in class
'''
import itertools

NUMBERS = range(10)
COUNT   = 0

for length in range(0, len(NUMBERS) + 1):
    for subset in itertools.combinations(NUMBERS, length):
        if sum(subset) % 3 == 0:
            COUNT += 1
print(COUNT)
'''

NUMBERS = list(range(0,10))

# Functions

def subsets(s: list[Any], c: list[Any], k: int=0) -> Iterator[list[Any]]:
    """
    s: current subset we are building
    c: possible canidates
    k: index of current canidate
    """

    # Base case
    if k == len(c):
        yield s

    else:
        # recursive step: skip
        yield from subsets(s, c, k + 1)

        # recursive step: take
        s.append(c[k])
        yield from subsets(s, c, k + 1)
        s.pop()
        # yield from subsets(s + c[k], c, k + 1)

# Main execution

def main() -> None:
    for subset in subsets([], NUMBERS, 0):
        print(subset)
