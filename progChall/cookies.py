#!/usr/bin/env python3

# Exercise 11-A: Cookies

import sys

# Functions

def readline() -> list[int]:
    # TODO: Read a line from stdin
    return sorted(map(int, sys.stdin.readline().split()))

def feed_children(children: list[int], cookies: list[int]) -> int:
    # TODO: Return number of children fed with cookies
    total = 0
    i = 0
    j = 0
    while i < len(children) and j < len(cookies):
        if cookies[j] >= children[i]:
            i += 1  # child takes
            total += 1
        j += 1 # check next cookie
        
    return total

# Main execution

def main() -> None:
    while (children := readline()) and (cookies := readline()):
        print(feed_children(children, cookies))

if __name__ == '__main__':
    main()
