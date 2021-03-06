import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

file = os.path.join("Harmonic_Centrality_Output.txt")
harmonic_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        harmonic_list.append(float(s[1]))

fig, ax = plt.subplots()
ax.hist(harmonic_list, bins=35)
plt.xlabel('Harmonic Centrality Value')
plt.ylabel('Frequency')
plt.title('Harmonic Centrality Histogram')
plt.savefig("Harmonic_Centrality_Histogram.png")