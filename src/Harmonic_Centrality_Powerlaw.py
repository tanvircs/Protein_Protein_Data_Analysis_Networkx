import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import powerlaw
import numpy as np
import os

file = os.path.join("Harmonic_Centrality_Output.txt")
harmonic_list=[]

with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        harmonic_list.append(float(s[1]))

fit = powerlaw.Fit(harmonic_list)
fig2 = fit.plot_pdf(color='b', linewidth=2)
fit.power_law.plot_pdf(color='b', linestyle='--', ax=fig2)
plt.savefig("Harmonic_Centrality_Powerlaw.png")