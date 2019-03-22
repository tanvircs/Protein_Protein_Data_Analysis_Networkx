import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("put betweenness centrality output file location")
betweenness_centrality_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        betweenness_centrality_list.append(s[1])

plt.hist(betweenness_centrality_list, bins=24)

plt.xlabel('Betweenness Centrality Value')
plt.ylabel('Frequency')
plt.title('Betweenness Centrality Output Histogram')
plt.savefig("Betweenness_Centrality_Histogram.png")