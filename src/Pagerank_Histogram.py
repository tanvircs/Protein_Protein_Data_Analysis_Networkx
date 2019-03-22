import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os

file = os.path.join("put pagerank output file location")
pagerank_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        pagerank_list.append(s[1])

plt.hist(pagerank_list, bins=24)

plt.xlabel('Pagerank Output Value')
plt.ylabel('Frequency')
plt.title('Pagerank Output Histogram')
plt.savefig("Pagerank_Output_Histogram.png")