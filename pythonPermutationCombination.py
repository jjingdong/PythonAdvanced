'''
permutation()
combination()
'''
import itertools

a = itertools.permutations([1,2,3])
# a = permuations object
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
for i in list(a):
    print(i)

# length = 2
b = itertools.permutations([1,2,3], 2)
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)
for i in b:
    print(i)

'''
combinations
'''
# combinations require 2nd arguments length
c = itertools.combinations([1,2,3],2)
# (1, 2)
# (1, 3)
# (2, 3)
for i in list(c):
    print(i)
