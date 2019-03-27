import networkx as nx
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import powerlaw
import numpy as np
import os

file = os.path.join("Load_Centrality_Output.txt")
load_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        load_list.append(float(s[1]))

fit = powerlaw.Fit(load_list)
fig2 = fit.plot_pdf(color='b', linewidth=2)
fit.power_law.plot_pdf(color='b', linestyle='--', ax=fig2)
plt.savefig("Load_Centrality_Powerlaw.png")