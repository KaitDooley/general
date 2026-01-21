#!/usr/bin/env python3

import collections
import sys

def is_anagram_sort(s: str, t:str) -> bool:
    # Time:     O(nlogn)
    # Space:    O(n)
    return sorted(s.lower()) == sorted(t.lower())


def is_anagram(s: str, t: str) -> bool:
    # Time: O(n)
    # Space: O(1)
    s_count = [0]*26
    t_count = [0]*26

    for c in s.lower(): s_count[ord(c) - ord('a')] += 1


