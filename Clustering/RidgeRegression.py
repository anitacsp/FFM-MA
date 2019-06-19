## Ridge Regression         ##
## Performs Extremely Badly ##
import pandas as pd
import numpy as np

from sklearn.linear_model import Ridge 
from sklearn.model_selection import train_test_split

rm = Ridge(alpha = 1.0)

USE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US equities.csv") 
x = USE[['growth','inflation','liquidity','risk app']]
y = USE['return'] 

use_train_x, use_test_x, use_train_y, use_test_y = train_test_split(x, y, test_size = 0.2, random_state = 1 )
rm.fit(use_train_x, use_train_y)
print("USE SCORE:")
print(rm.score(use_test_x, use_test_y))

DMX = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\DM ex US.csv")

x = DMX[['growth','inflation','liquidity','risk app']]
y = DMX['return'] 

use_train_x, use_test_x, use_train_y, use_test_y = train_test_split(x, y, test_size = 0.2, random_state = 6 )
rm.fit(use_train_x, use_train_y)
print("DMX SCORE:")
print(rm.score(use_test_x, use_test_y))

#AZE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\Asian equities.csv")
#CNE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\China equities.csv")
#UST = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US treasuries.csv")
#USHY = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US high Yield.csv")
#AZC = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\Asian Credit.csv")
#oil = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\oil.csv")
#gold = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\gold.csv")
#cop = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\copper.csv")
