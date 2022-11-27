import os, re
os.chdir(r'/Users/edwardkim/Documents/doit_python_daily_programming/04')
import usecsv
apt = usecsv.switch(usecsv.opencsv('apt_201910.csv'))

"""
print(apt[:3])
print(len(apt))
"""
new_list = []

for i in apt:
    try:
        if i[5] > 120 and i[8] < 30000 and re.match('강원', i[0]):
            new_list.append([i[0], i[4], i[8]])
    except: pass

usecsv.writecsv('over120_lower3000.csv', new_list)