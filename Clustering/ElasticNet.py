import pandas as pd
import numpy as np

from sklearn.linear_model import ElasticNetCV 
from sklearn.model_selection import train_test_split

EN = ElasticNetCV(alphas = None, copy_X = True, cv=5, eps = 0.0001, fit_intercept = True, l1_ratio=0.7, max_iter=5000, n_alphas=1000, n_jobs = None,
             normalize=False, positive= False, precompute='auto', random_state = 0, selection = 'random', tol=0.000001, verbose = 2)

USE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US equities.csv") 
x = USE[['growth','inflation','liquidity','risk app']]
y = USE['return'] 

use_train_x, use_test_x, use_train_y, use_test_y = train_test_split(x, y, test_size = 0.2, random_state = 6 )
EN.fit(use_train_x, use_train_y)

print("USE SCORE:")
print(EN.score(use_test_x, use_test_y))