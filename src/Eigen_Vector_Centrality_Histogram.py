import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os


file = os.path.join("Eigen_Vector_Centrality_Output.txt")
eigen_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        eigen_list.append(s[1])

fig, ax = plt.subplots()
ax.hist(eigen_list, bins=35, orientation="horizontal")
plt.xlabel('Eigen Value')
plt.ylabel('Frequency')
plt.title('Eigen Vector Histogram')
labels = [item.get_text() for item in ax.get_xticklabels()]
for tick in ax.get_xticklabels():
    tick.set_rotation(80)
plt.savefig("Eigen_Vector_Histogram.png")