import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Edge_Betweenness_Centrality_Output.txt")
edge_betweenness_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        edge_betweenness_list.append(s[2])

fig, ax = plt.subplots()
ax.hist(edge_betweenness_list, bins=35, orientation="horizontal")
plt.xlabel('Edge Betweenness Centrality Value')
plt.ylabel('Frequency')
plt.title('Edge Betweenness Centrality Histogram')
labels = [item.get_text() for item in ax.get_xticklabels()]
for tick in ax.get_xticklabels():
    tick.set_rotation(80)
plt.savefig("Edge_Betweenness_Centrality_Histogram.png")