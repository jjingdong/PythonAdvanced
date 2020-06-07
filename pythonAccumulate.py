'''
itertools.accumulate(iterable[,func])
'''
import itertools
import operator

a = [1, 3, 5, 7]
itertools.accumulate(a)
itertools.accumulate(a, operator.mul)
itertools.accumulate(a, max)