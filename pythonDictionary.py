'''
Python Dictionary

dict[key1] = value1, key1 can be string, numbers, tuples
popitem(last=False)
popitem()   same as popitem(last = True)
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

'''
dict.get(key) ---> exception
dict.get(key, not_found) ---> specify what value to return
'''

'''
dict.keys()
dict.values()
dict.items()
'''
for k in c_dict.keys():
    a = 0

for v in c_dict.values():
    a = 0

for k, v in c_dict.items():
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
If dictionaries share a common key, the key-value pair in the second dictionary will be used
'''
a = {1: 'a', 2: 'b', 3: 'c'}
b = {4: 'd', 5: 'e'}
#  c = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
c = dict(a.items() | b.items())
# a = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
a |= b

a = {1: 'a', 2: 'b', 3: 'c', 6: 'in both'}
b = {4: 'd', 5: 'e', 6: 'but different'}
# c = {1: 'a', 2: 'b', 3: 'c', 6: 'but different', 4: 'd', 5: 'e'}
c = dict(a.items() | b.items())

a = {'a': 'one', 'b': 'two'}
b = ((i, i**2) for i in range(3))
# a = {'a': 'one', 'b': 'two', 0: 0, 1: 1, 2: 4}
a |= b

'''
Dictionary Intesect
'''
dict1 = {'a': 1, 'b':2, 'c':3}
dict2 = {'c':4, 'd':5}
# new_dict = {'c':3}
new_dict = {x:dict1[x] for x in dict1 if x in dict2}

# new_dict2 = set()
new_dict2 = dict(dict1.items() & dict2.items())

# Note. this is a set operation, both value and key have to match
d1 = {'key1':'value1', 'key2':'value2', 'key3':3}
d2 = {'key1':'value2', 'key5':'value5'}
# c = {('key1', 'value1')}
c = d1.items() & d2.items()

str1 = 'abbccc'
str2 = 'ccccddddd'
# new_dict = Counter({'c': 3})
dict3 = collections.Counter(str1) & collections.Counter(str2)
# d = {'c': 3}
d = dict(dict3)

# Note. It won't work if not using collections.Counter
d1 = {'c': 3, 'b': 2, 'a': 1}
d2 = {'d': 5, 'c': 4}
# d3 = d1 & d2
d4 = d1.items() & d2.items()
print(d4)


str1 = 'abbccc'
str2 = 'ccccddddd'
# dict3 = Counter({'c': 3})
dict3 = collections.Counter(str1) & collections.Counter(str2)
# dict4 = Counter({'d': 5, 'c': 4, 'b': 2, 'a': 1})
dict4 = collections.Counter(str1) | collections.Counter(str2)
# dict5 = Counter({'b': 2, 'a': 1})
dict5 = collections.Counter(str1) - collections.Counter(str2)
# dict6 = Counter({'c': 7, 'd': 5, 'b': 2, 'a': 1})
dict6 = collections.Counter(str1) + collections.Counter(str2)


dict1 = {'c': 3, 'b': 2, 'a': 1}
dict2 = {'d': 5, 'c': 4}
# dict3 = set()
dict3 = dict1.items() & dict2.items()
# dict4 = {('c', 3), ('d', 5), ('a', 1), ('c', 4), ('b', 2)}
dict4 = dict1.items() | dict2.items()
# dict5 = {('b', 2), ('a', 1), ('c', 3)}
dict5 = dict1.items() - dict2.items()
# dict6 = {('c', 3), ('d', 5), ('a', 1), ('c', 4), ('b', 2)}
dict6 = dict1.items() ^ dict2.items()

'''
Dictionary difference
'''
difference = dict(dict1.items() ^ dict2.items())


'''
Sort Dictionary
'''
# sort dict by values
c_dict = collections.Counter([1,2,3])
for k, v in c_dict.most_common():
    a = 0

# sort dict by keys
a_dict = {1:'a', 2:'b'}
for k in sorted(a_dict.keys()):
    a = 0

# sort keys and values by key
a_dict = sorted(a_dict)

'''
OrderedDict preserves the order in which the keys are inserted
move_to_end(key) same as move_toend(key, last=True)
move_to_end(key, last=False)
'''



