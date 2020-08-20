'''
\
[]  a character class
^   the beginning
$   the end
.   any char except newline
?   0 or one
|   or
*   0 or more
+   1 or more
{}  number of occurrences
()  enclose a group o REs
'''
import re

re.compile('[a-e]')

'''
\d  [0-9]
\D  any non-digit character
\s  any whitespace character
\S  any non-whitespace character
\w  [a-zA-Z0-9_]
\W  any non-alphanumeric character
'''

'''
re.split(pattern, string, maxsplit=0, flags=0)
'''
s = ''.join(re.split(' |,|:', s))

'''
re.sub(pattern, repl, string, count=0, flags=0)
re.subn(pattern, repl, string, count=0, flags=0)
'''

'''
re.escape(string)
'''

'''
re.fullmatch(pattern, string)
'''
pattern = '[a-zA-Z0-9]'
b = 'abc'
a = re.fullmatch(pattern, b)

word = 'Flag'
pattern = '[A-Z]*|[A-Z]?[a-z]*'
a = re.fullmatch(pattern, word)