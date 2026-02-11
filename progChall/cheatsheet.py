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



# create map
table = {
    'a': 0,
    'b': 1,
    'c': 2,
}

# add a pair
table['d'] = 3

# access value
print(table['b'])
print(table.get('e', -1))

# display number of pairs
print(len(table))

# traverse pairs (keys)
for key in table:
    print(key)

# traverse pairs (items)
for key, value in table.items():
    print(key, value)

# searching
print('b' in table)
print('e' in table)
print(2 in table.values())
