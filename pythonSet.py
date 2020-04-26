a = set(['a', 'b', 'c'])
a.add('d')
# cannot be modified
b = frozenset('e', 'f', 'g')
c = set(['e', 'f'])

# Merge union is the same as '|'
# d = (['a', 'b', 'c', 'e', 'f'])
d = a.union(c)
d = a | c

# Intersection
d = a.intersection(c)
d = a & c

# Difference
d = a.difference(c)
d = a - c

# Clear
# empty
d = a.clear()
