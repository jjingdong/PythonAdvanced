'''
map(fun, iter)
'''

a = '1.2.3.4'
# list(b) = [1, 2, 3, 4]
b = map(int, a.split('.'))

a = [1, 2, 3, 4]
# list(b) = [2, 4, 6, 8]
b = map(lambda x: x+x, a)

a = [1, 2, 3]
b = [4, 5, 6]
# list(c) = [5, 7, 9]
c = map(lambda x,y: x+y, a, b)

l = ['123', '456', '789']
# a = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
a = list(map(list, l))