'''
any(list of iterables), return True if any o the items is True.
'''
# a = False
a = any([False, False, False])
# b = True
b = any([False, True, False])

'''
all(list of iterables), return True if all of the items are True
'''
# a = False
a = all([False, False, False])
# b = False
b = all([False, True, False])
# c = True
c = all([True, True, True])
