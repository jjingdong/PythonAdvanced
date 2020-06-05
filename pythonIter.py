'''
iter()
'''

lst = [1, 2, 3, 4]
lst2 = iter(lst)
a = next(lst2)
b = next(lst2)

for i in range(5):
    c = next(lst2)