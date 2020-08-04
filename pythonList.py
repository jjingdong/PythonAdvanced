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
sorted(list, reverse = True)
sorted(list, key = len)
sorted(list, key = str.lower())
sorted(list, key = myFun)
def myFun(s):
    return s[-1]

reversed(list)

'''

a = [1, 2, 3, 4]
# b = [1, 4, 9, 16]
b = [n * n for n in a]
# c = [1, 4]
c = [n * n for n in a if n <=2]

