'''
bisect.bisect(list,num,beg,end)
bisect.bisect_left(list,num,beg,end)
bisect.bisect_right(list,num,beg,end)
'''
import bisect

a = [1, 3, 4, 4, 4, 6, 7]
# b = 5, the rightmost index to insert
b = bisect.bisect(a, 4)
# c = 2, the leftmost index to insert
c = bisect.bisect_left(a,4)
# d = 4, the rightmost index to insert, so list remains sorted
d = bisect.bisect_right(a, 4, 0, 4)

'''
insort(list, num, beg, end)
insort_left(list, num, beg, end)
insort_right(list, num, bed, end)
'''