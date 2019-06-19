import pandas as pd
import numpy as np

from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split

p = BayesianRidge(n_iter = 500, tol = 0.0001, alpha_1 = 0.5, compute_score = True, verbose=2)

USE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US equities.csv") 
x = USE[['growth','inflation','liquidity','risk app']]
y = USE['return'] 

use_train_x, use_test_x, use_train_y, use_test_y = train_test_split(x, y, test_size = 0.3, random_state = 6 )

p.fit(use_train_x, use_train_y)

print("USE SCORE:")
print(p.score(use_test_x, use_test_y))