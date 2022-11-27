import os, re, codecs
os.chdir(r'/Users/edwardkim/Documents/doit_python_daily_programming/03')
# f = codecs.open('friends101_t.txt', 'r', encoding = 'utf-8')
# script101 = f.read()
# print(script101[:100])

"""
Line = re.findall(r'Monica:.+', script101)
for item in Line[:3]:
    print(item)

f.close()

monica = ''
for i in Line:
    monica += i + '\n'

f = open('monica.txt', 'w', encoding = 'utf-8')
f.write(monica)
f.close()
"""

""""
char = re.compile(r'[A-Z][a-z]+:')
y = set(re.findall(char, script101))
z = list(y)
character = []
for i in z:
    character += [i[:-1]]
print(character)
f.close()
"""

"""
print(re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)[:6])
f.close()
"""
f = open('friends101_t.txt', 'r')

sentences = f.readlines()
"""
for i in sentences[:20]:
    if re.match(r'[A-z][a-z]+:', i):
        print(i)
"""

"""
lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
print(lines[:10])
"""

would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
print(would[:3])

newf = open('would.txt', 'w')
newf.writelines(would)
newf.close()

f.close()

"""
연습문제
1. m.group()
2.findall , [a-z]
3.'\d.+?년'
4.split, '\.'
5.[A-Za-z] , set
"""
