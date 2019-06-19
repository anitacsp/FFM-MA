import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans 
from mpl_toolkits.mplot3d import Axes3D

USE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US equities.csv") 
DMX = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\DM ex US.csv")
AZE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\Asian equities.csv")
CNE = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\China equities.csv")
UST = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US treasuries.csv")
USHY = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\US high Yield.csv")
AZC = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\Asian Credit.csv")
oil = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\oil.csv")
gold = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\gold.csv")
cop = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\copper.csv")
#data = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\cleanAssets.csv")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#ax.scatter(USE['growth'], USE['inflation'], USE['return'], c='paleturquoise')
#ax.scatter(DMX['growth'], DMX['inflation'], DMX['return'],c='moccasin')
#ax.scatter(AZE['growth'], AZE['inflation'], AZE['return'],c='lightcoral')
#ax.scatter(CNE['growth'], CNE['inflation'], CNE['return'],c='seagreen')
#ax.scatter(UST['growth'], UST['inflation'], UST['return'],c='mediumpurple')
#ax.scatter(USHY['growth'], USHY['inflation'], USHY['return'],c='dimgray')
#ax.scatter(AZC['growth'], AZC['inflation'], AZC['return'],c='honeydew')
#ax.scatter(oil['growth'], oil['inflation'], oil['return'],c='darkblue')
#ax.scatter(gold['growth'], gold['inflation'], gold['return'],c='red')
#ax.scatter(cop['growth'], cop['inflation'], cop['return'],c='hotpink')

#ax.set_xlabel('growth')
#ax.set_ylabel('inflation')
#ax.set_zlabel('returns')

ax.scatter(USE['growth'], USE['risk app'], USE['return'], c='paleturquoise')
ax.scatter(DMX['growth'], DMX['risk app'], DMX['return'],c='moccasin')
ax.scatter(AZE['growth'], AZE['risk app'], AZE['return'],c='lightcoral')
ax.scatter(CNE['growth'], CNE['risk app'], CNE['return'],c='seagreen')
ax.scatter(UST['growth'], UST['risk app'], UST['return'],c='mediumpurple')
ax.scatter(USHY['growth'], USHY['risk app'], USHY['return'],c='dimgray')
ax.scatter(AZC['growth'], AZC['risk app'], AZC['return'],c='honeydew')
ax.scatter(oil['growth'], oil['risk app'], oil['return'],c='darkblue')
ax.scatter(gold['growth'], gold['risk app'], gold['return'],c='red')
ax.scatter(cop['growth'], cop['risk app'], cop['return'],c='hotpink')

ax.set_xlabel('growth')
ax.set_ylabel('risk app')
ax.set_zlabel('returns')


plt.show()
 