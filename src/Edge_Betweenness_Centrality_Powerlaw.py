import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import powerlaw
import numpy as np
import os

file = os.path.join("Edge_Betweenness_Centrality_Output.txt")
edge_betweenness_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        edge_betweenness_list.append(float(s[2]))

fit = powerlaw.Fit(edge_betweenness_list)
fig2 = fit.plot_pdf(color='b', linewidth=2)
fit.power_law.plot_pdf(color='b', linestyle='--', ax=fig2)
plt.savefig("Edge_Betweenness_Centrality_Powerlaw.png")
