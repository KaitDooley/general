#!/usr/bin/env python3

# create a dynamic array
v = [1, 2, 3]

# append
v.append(4)

# prepend
v.insert(0, 0)

# display number of elements
print(len(v))

# traverse elements
for e in v:
    print(e)

# traverse elements with index
for i, e in enumerate(v):
    printf(f'{i}. {e}')
