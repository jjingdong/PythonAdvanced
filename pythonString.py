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
s.startswith('')
s.endwith('')
s.find('')
s.replace('old', 'new')
s.split('delim')
s.split()
s.join(lst)
s[start:end]
'''



s = ''.join(re.split(' |,|:', s))