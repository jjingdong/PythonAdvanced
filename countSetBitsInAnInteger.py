'''
count number o 1s in binary representation of an integer
'''

def countBits(n):
    count = 0
    while n:
        count += n & 1
        n >> 1
    return count

# Time O(logN)
def countBits(n):
    if n == 0 :
        return 0
    else:
        return n & 1 + countBits(n>>1)

# brian kernighan's algorithm
def countBits(n):
    count = 0
    while n:
        n = n & (n-1)
        count += 1
    return count

def countBits(n):
    if n == 0:
        return 0
    else:
        return 1 + countBits(n & (n-1))

# use lookup table:

# use bin()
a = bin(2).count('1')
