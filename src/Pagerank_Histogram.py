import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Pagerank_Output.txt")
pagerank_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        pagerank_list.append(s[1])

fig, ax = plt.subplots()
ax.hist(pagerank_list, bins=35, orientation="horizontal")
plt.xlabel('Pagerank Value')
plt.ylabel('Frequency')
plt.title('Pagerank Histogram')
labels = [item.get_text() for item in ax.get_xticklabels()]
for tick in ax.get_xticklabels():
    tick.set_rotation(80)
plt.savefig("Pagerank_Histogram.png")