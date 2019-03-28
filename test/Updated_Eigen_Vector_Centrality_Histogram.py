import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import os


file = os.path.join("Updated_Eigen_Vector_Centrality_Output.txt")
eigen_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        eigen_list.append(float(s[1]))

fig, ax = plt.subplots()
ax.hist(eigen_list, bins=45)
plt.xlabel('Eigen Value')
plt.ylabel('Frequency')
plt.title('Updated Eigen Vector Histogram')
plt.savefig("Updated_Eigen_Vector_Histogram.png")