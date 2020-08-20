'''
String
'''

a = "Hello world"
# b = "llo world"
b = a.removeprefix("He")

a = "Hello world"
# b = "Hello wor"
b = a.removesuffix("ld")

'''
s.lower()
s.upper()
s.strip()
s.isalpha()
s.isdigit()
s.isalnum()
s.isspace()
s.istitle()
s.startswith('')
s.endwith('')
s.find('')
s.replace('old', 'new')
s.split('delim')
s.split()
s.join(lst)
s[start:end]

'''
s = 'abcdefg'
# num = 0
num = s.index('a')

# num = 66, return unicode value of 'B'
num = ord('B')

a = "2-5g-3-J"
a = a.replace('-', '').upper

s = ''.join(re.split(' |,|:', s))


word = 'Flag'
#a = True
a = word.isupper() or word.islower() or word.istitle()

'''
Reverse
'''
a = [1, 2, 3, 4]
b = a[::-1]