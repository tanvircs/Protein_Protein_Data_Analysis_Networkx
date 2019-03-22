import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

file = os.path.join("put harmonic centrality output file location")
harmonic_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        harmonic_list.append(s[1])

plt.hist(harmonic_list, bins=24)

plt.xlabel('Harmonic Centrality Value')
plt.ylabel('Frequency')
plt.title('Harmonic Centrality Histogram')
plt.savefig("Harmonic_Centrality_Histogram.png")