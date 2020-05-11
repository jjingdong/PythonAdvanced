'''
Python Dictionary
'''

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

# -------------------------------
for k in dict.keys():
    a = 0

for v in dict.values():
    a = 0

for k, v in dict.items():
    a = 0






