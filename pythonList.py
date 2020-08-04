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

# a = [1,2,3,4]
a = [1,2] + [3,4]

'''
list.insert(index, ele)
list.extend(list2)
list.index(ele) ----> exception
list.remove(ele) ---> exception
list.pop(index)
list.pop()
sorted(list)
reversed(list
'''