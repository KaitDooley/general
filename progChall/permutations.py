#!/usr/bin/env python3

from typing import Iterator

# Functions

def permutations(p: str, c: set[str]) -> Iterator[str]:
    '''
    p: Current permutation we are building
    c: Candidates we can choose
    '''
    # Base Case: Run out of candidates
    if not c:
        yield p
    else: # Recursive step
        for candidate in c:
            yield from permutations(
                p + candidate,      # Adding candidate to permutation
                c - {candidate}     # Remove candidate from set
            )

'''
def permutations(p: list[str], c: set[str]) -> None:
    '''
    #p: Current permutation we are building
    #c: Candidates we can choose
    '''
    # Base Case: Run out of candidates
    if not c:
        print(''.join(p))
    else: # Recursive step
        for candidate in sorted(c):
            p.append(candidate)
            c.remove(candidate)
            permutations(p, c)
            c.add(candidate)
            p.pop()
'''
            

# Easy way
'''
import itertools

s = 'ABC'
for p in itertools.permutations(s):
    print(''.join(p))
'''


# Main Execution

def main():
    for permutation in permutations('', set('ABC')):
        print(permutation)


if __name__ == '__main__':
    main()
