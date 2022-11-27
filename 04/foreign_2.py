import os, re, usecsv
os.chdir(r'/Users/edwardkim/Documents/doit_python_daily_programming/04')
total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total)
# print(newPop[:4])

new = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign])
    except:
        pass

usecsv.writecsv('newPop.csv', new)

