import os, re
import pandas as pd
os.chdir(r'/Users/edwardkim/Documents/doit_python_daily_programming/05')

"""
data = {'name' : ['Mark', 'Jane', 'Chris', 'Ryan'], 'age' : [33, 32, 44, 42], 'score' : [91.3, 83.4, 77.5, 87.7]}
df = pd.DataFrame(data)
print(df['age'])
"""

df2 = pd.read_csv('survey.csv')
#print(df2.head())
#print(df2.mean())
#print(df2.income.mean())
#print(df2.income.sum())
#print(df2.income.median())
#print(df2.describe())
#print(df2.income.describe())
#print(df2.sex.value_counts())
#print(df2.groupby(df2.sex).mean())

from scipy import stats

male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']

#print(stats.ttest_ind(male, female))
ttest_result = stats.ttest_ind(male, female)
if ttest_result[1] > .05:
    print('p-value는 %f로 95%% 수준에서 유의하지 않음' % ttest_result[1])
else:
    print('p-value는 %f로 95%% 수준에서 유의함' % ttest_result[1])

corr = df2.corr()
#print(corr)
#print(df2.income.corr(df2.stress))

corr.to_csv('corr.csv')