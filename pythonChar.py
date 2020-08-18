'''
ord(char)
'''


# Time O(N), n = length of the s, Space O(N), runtime = 28 ms
def titleToNumber(self, s: str) -> int:
    value = ord('A') - 1
    number = 0
    for char in s:
        number = number * 26 + (ord(char) - value)

    return number