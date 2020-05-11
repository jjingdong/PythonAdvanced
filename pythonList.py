'''
Python's list objects are really variable-length arrays, not Lisp-style linked lists
'''

lst = []
lst.append(1)
lst1 = [2]
lst.extend(lst1)
lst2 = [3]
lst.append(lst2)
lst = []
lst.append(lst2)
print(lst)