## Performs Extremely Badly ##
import pandas as pd
import numpy as np

from sklearn.linear_model import LassoLarsCV
from sklearn.model_selection import train_test_split

lm = LassoLarsCV(max_iter = 1000, precompute = 'auto', cv = 10, eps = 0.0001)

USE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US equities.csv") 
x = USE[['growth','inflation','liquidity','risk app']]
y = USE['return'] 

use_train_x, use_test_x, use_train_y, use_test_y = train_test_split(x, y, test_size = 0.2, random_state = 6 )
lm.fit(use_train_x, use_train_y)
print("USE SCORE:")
print(lm.score(use_test_x, use_test_y))