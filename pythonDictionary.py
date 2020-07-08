'''
Python Dictionary
'''
import collections

# Note. key cannot be a list
a_dict = {'a' : 1, 'b' : 2, 'c' : 3}
b_dict = {'a': [1, 3], 9 : 'example'}
c_dict = {}
d_dict = dict({'a' : 1, 'b' : 2, 'c' : 3})
e_dict = dict([('a', 1), ('b', 2)])
c_dict[0] = 'abc'
c_dict[1] = 'def'
c_dict[2] = 'ghi'
# delete a key value
del c_dict[0]
# return and delete
# dict.pop(key)
c_dict.pop(1)
# return and delete
# dict.popitem() the first item
c_dict.popitem()
d_dict.clear()

# ----------------------------------------------
for k in c_dict.keys():
    a = 0

for v in c_dict.values():
    a = 0

for k, v in c_dict.items():
    a = 0

# sort dict by values
c_dict = collections.Counter([1,2,3])
for k, v in c_dict.most_common():
    a = 0

''' 
collections.Counter() 
collections.defaultdict(int) is collections.Counter()

'''
lst = 'abcaabbccaaaaaa'
# count = {'a': 9, 'b': 3, 'c': 3}
count = collections.Counter(lst)
# update
count = collections.Counter()
# count = {'a': 9, 'b': 3, 'c': 3}
count.update('abcaabbccaaaaaa')
# list
lst = ['cat', 'dog', 'cat', 'rabbit']
#count = {'a': 9, 'b': 3, 'c': 3}
# count = {'cat': 2, 'dog': 1, 'rabbit': 1}
count = collections.Counter(lst)

''' 
defaultdict(list) 
'''
d = collections.defaultdict(list)
d = collections.defaultdict(int)

'''
Dictionary Unions: |
If dictionaries share a common key, the key-value pair int he second dictionary will be used
'''
a = {1: 'a', 2: 'b', 3: 'c'}
b = {4: 'd', 5: 'e'}
#  c = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
c = a | b
# a = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
a |= b

a = {1: 'a', 2: 'b', 3: 'c', 6: 'in both'}
b = {4: 'd', 5: 'e', 6: 'but different'}
# c = {1: 'a', 2: 'b', 3: 'c', 6: 'but different', 4: 'd', 5: 'e'}
c = a | b

a = {'a': 'one', 'b': 'two'}
b = ((i, i**2) for i in range(3))
# a = {'a': 'one', 'b': 'two', 0: 0, 1: 1, 2: 4}
a |= b







