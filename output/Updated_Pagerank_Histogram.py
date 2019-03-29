import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("Updated_Pagerank_Output.txt")
pagerank_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        pagerank_list.append(float(s[1]))

fig, ax = plt.subplots()
ax.hist(pagerank_list, bins=45)
plt.xlabel('Pagerank Value')
plt.ylabel('Frequency')
plt.title('Updated Pagerank Histogram')
plt.savefig("Updated_Pagerank_Histogram.png")