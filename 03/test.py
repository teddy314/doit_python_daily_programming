import os, re
"""
def refinder(pattern, script):
    if re.match(pattern, script):
        print("Match!")
    else:
        print("Not a match!")

pattern = r'Life'
script = 'Life is so cool'
refinder(pattern, script) 
"""
number = 'My number is 511223-1******'
print(re.findall('\d{6}',number))