#bitwise and
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
Brian Kernighan's algorithm which is applied to turn off the rightmost bit of one in a number.
'''
a & (a-1)
