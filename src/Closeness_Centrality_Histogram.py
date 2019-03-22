import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("put closenness centrality output file location")
closeness_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        closeness_list.append(s[1])

plt.hist(closeness_list, bins=24)

plt.xlabel('Closeness Centrality Value')
plt.ylabel('Frequency')
plt.title('Closeness Centrality Histogram')
plt.savefig("Closeness_Centrality_Histogram.png")