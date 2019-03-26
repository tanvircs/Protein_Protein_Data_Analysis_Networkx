import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Closeness_Centrality_Output.txt")
closeness_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        closeness_list.append(s[1])

fig, ax = plt.subplots()
ax.hist(closeness_list, bins=35, orientation="horizontal")
plt.xlabel('Closeness Centrality Value')
plt.ylabel('Frequency')
plt.title('Closeness Centrality Histogram')
labels = [item.get_text() for item in ax.get_xticklabels()]
for tick in ax.get_xticklabels():
    tick.set_rotation(80)
plt.savefig("Closeness_Centrality_Histogram.png")