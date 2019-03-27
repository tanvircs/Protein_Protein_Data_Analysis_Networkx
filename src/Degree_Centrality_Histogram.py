import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Degree_Centrality_Output.txt")
degree_centrality_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        degree_centrality_list.append(float(s[1]))

fig, ax = plt.subplots()
ax.hist(degree_centrality_list, bins=35)
plt.xlabel('Degree Centrality Value')
plt.ylabel('Frequency')
plt.title('Degree Centrality Histogram')
plt.savefig("Degree_Centrality_Histogram.png")
