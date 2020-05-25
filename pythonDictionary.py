'''
Python Dictionary
'''
import collections

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
for k, v in c_dict.most_common():
    a = 0

''' collections.Counter() '''
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

''' defaultdict(list) '''
d = collections.defaultdict(list)
d = collections.defaultdict(int)





