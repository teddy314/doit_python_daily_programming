import csv, os
os.chdir(r'/Users/edwardkim/Documents/doit_python_daily_programming/04')
f = open('a.csv', 'r')

new = csv.reader(f)
for i in new:
    print(i)

f.seek(0)
a_list = []
for i in new:
    print(i)
    a_list.append(i)

print(a_list)

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

print(opencsv('example2.csv'))

f.close()

a = [['구', '전체', '내국인', '외국인'],
['관악구', '519864', '502089', '17775'],
['강남구', '547602', '542498', '5104'],
['송파구', '686181', '679247', '6934'],
['강동구', '428547', '424235', '4312']]

f = open('abc.csv', 'w', newline = '')
csvobject = csv.writer(f, delimiter = ',')
csvobject.writerows(a)
f.close()