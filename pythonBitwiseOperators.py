'''

a & b
#bitwise or
a | b
#bitwise not
~a
~b
#bitwise xor
a ^ b
#bitwise right shift
a >> num
b >> num
#bitwise left shift
a << num
b << num
'''

'''
Brian Kernighan's algorithm which is applied to turn off the rightmost bit of one in a number.
a & (a-1)
'''
# pow(2,32) == 1<<32
a = pow(2,32)
b = 1<<32

'''
a.count('1')
'''
# a = 2
a = bin(5).count('1')

#
a = 3

# c = a
c = a ^ 0

# c = 0
c = a ^ a

