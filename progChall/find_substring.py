#!/usr/bin/env python3
import sys

string = "TTEUM GQNDV EOIOL EDIRE MQTGS DAFDR CDYOX IZGZP PTAAI TUCSI XFBXY SUNFE SQRHI SAFHR TQRVS VQNBE EEAQG IBHDV SNARI DANSL EXESX EDSNJ AWEXA ODDHX   EYPKS YEAES RYOET OXYZP PTAAI TUCRY BETHX UFINR"

while True:
    sub = sys.stdin.readline().strip()
    if not sub:
        break

    s = ''.join(string.split())

    first = s.find(sub)
    second = s.find(sub, first + 1)

    print(f"First:    {first}")
    print(f"Second:   {second}")
    print(f"Distance: {second - first}")
