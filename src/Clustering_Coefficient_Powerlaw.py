import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import powerlaw
import numpy as np
import os

file = os.path.join("Clustering_Coefficient_Output.txt")
clustering_coefficient_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        clustering_coefficient_list.append(float(s[1]))

fit = powerlaw.Fit(clustering_coefficient_list)
fig2 = fit.plot_pdf(color='b', linewidth=2)
fit.power_law.plot_pdf(color='b', linestyle='--', ax=fig2)
plt.savefig("Clustering_Coefficient_Powerlaw.png")