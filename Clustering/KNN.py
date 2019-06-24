import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

all = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\cleanAssets.csv") 
USE  = all[['growth','inflation','liquidity','risk app', 'return']]
 
kmeans = KMeans(n_clusters=10, random_state=10)
kmeans.fit(USE)
all['cluster'] = kmeans.predict(all[['growth','inflation','liquidity','risk app', 'return']])

#print(kmeans.cluster_centers_)

#np.savetxt("centroids.csv",kmeans.cluster_centers_, delimiter=",")

#all.to_csv('output.csv')
#print(all)
combi = all.groupby(['cluster', 'type']).size().to_frame('count').reset_index()
#print(combi)
#combi.to_csv('centroidConcentration.csv')

columns = ('0','1','2','3','4','5','6','7','8','9')
rows = ['Cluster No.%d' % x for x in combi['cluster'].unique()]

values = np.arange(0, 100, 5)
value_increment = 5;

colors = plt.cm.Set3(np.linspace(0,1, len(rows)))
n_rows = 10

index = np.arange(len(columns))
bar_width = 0.4

y_offset = np.zeros(len(columns))
#print(y_offset)

data = []

for x in combi['type'].unique():
    types = combi.loc[combi['type'] == x]
    row_data = []
    for i in combi['cluster'].unique():
        if(types.loc[types['cluster']==i].empty):
            row_data.append(0)
        else:
            store = types.loc[types['cluster']==i]
            row_data.append(store['count'].values[0])   
    #print(row_data)
    data.append(row_data)

legend =[] 
print(data)
cell_text = []
for row in range(n_rows):
    bar = plt.bar(index, np.array(data[row]),bar_width, bottom = y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    print(y_offset)
    cell_text.append(data[row])
    legend.append(bar[0])

#colors = colors[::-1]
#cell_text.reverse()

table = plt.table(cellText = cell_text, 
                  rowLabels = rows,
                  colColours = colors,
                  colLabels=columns,
                  loc='bottom')

plt.ylabel("Count")
plt.xticks([])
plt.title("Distribution of asset classes in clusters")

plt.show()

    
       

