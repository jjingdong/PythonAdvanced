'''
sorted()
'''

a = [1, 3, 5, 7]
sorted(a)
sorted(a, reverse = True)

b = ['aaa', 'bbb', 'ccc', 'dd', 'f']
sorted(b, key = len)

# sort Tuple
# [(-3, 4), (-5, 10), (-5, 11)]
# [4, 10, 11]
# [(-2, 3), (-4, 7), (-4, 6)]
# [3, 6, 7]
# [(-1, 2), (-3, 5), (-5, 8), (-5, 9)]
# [2, 5, 8, 9]
lst = [val for y, val in sorted(p_dict[k], key=lambda t: (-t[0], t[1]))]


intervals = sorted(intervals, key = lambda x: x[0])
intervals = sorted(intervals, key = lambda x: (x[1], x[0]))


