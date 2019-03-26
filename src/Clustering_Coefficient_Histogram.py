import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Clustering_Coefficient_Output.txt")
clustering_coefficient_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        clustering_coefficient_list.append(s[1])

fig, ax = plt.subplots()
ax.hist(clustering_coefficient_list, bins=35, orientation="horizontal")
plt.xlabel('Clestering Coefficient Value')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Histogram')
labels = [item.get_text() for item in ax.get_xticklabels()]
for tick in ax.get_xticklabels():
    tick.set_rotation(80)
plt.savefig("Clustering_Coefficient_Histogram.png")