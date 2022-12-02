import numpy as np

loss = [-750, -250]

profit = [100] * 18
cf = loss + profit

cashflow = np.array(cf)

npv = np.npv(0.045, cashflow)
irr = np.irr(cashflow)