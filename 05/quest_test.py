import os, usecsv
import numpy as np
os.chdir(r'/Users/edwardkim/Documents/doit_python_daily_programming/05')

quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))

print(quest)

quest[quest > 5] = 5
print(quest)
usecsv.writecsv('resultcsv.csv', list(quest))