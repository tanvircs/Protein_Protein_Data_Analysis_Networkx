import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("put information centrality output file location")
information_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        information_list.append(s[1])

plt.hist(information_list, bins=24)

plt.xlabel('Information Centrality Value')
plt.ylabel('Frequency')
plt.title('Information Centrality Histogram')
plt.savefig("Information_Centrality_Histogram.png")