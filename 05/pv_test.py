import numpy as np

discount = 0.05
cashflow = 100

def presentvalue(n):
    return(cashflow / ((1 + discount)) ** n)

print(presentvalue(1))