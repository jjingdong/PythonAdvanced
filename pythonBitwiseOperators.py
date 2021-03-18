'''
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
a.bit_length()
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

'''
#bitwise xor
a ^ b
a or b, but not both
'''
# c = a
c = a ^ 0
# c = 0
c = a ^ a
a ^ 0 = a
a ^ b ^ a = 0 ^ b = b

# Time O(1) Space O(1)
def bitwiseComplement(self, N: int) -> int:

    if N == 0: return 1
    return N ^ ((1 << N.bit_length()) - 1)

'''
Brian Kernighan's algorithm which is applied to turn off the rightmost 
bit of one in a number.
a & (a-1)
'''
# Time O(1) Space O(1), runtime = 32 ms
def isPowerOfTwo(self, n: int) -> bool:
    if not n or n < 1: return False
    if n == 1: return True

    return n & (n - 1) == 0

'''
Get the rightmost 1-bit a & (-a)
'''
# Time O(1) Space O(1), runtime = 24 ms
def isPowerOfTwo(self, n: int) -> bool:
    if not n or n < 1: return False
    if n == 1: return True

    return n == n & (-n)
