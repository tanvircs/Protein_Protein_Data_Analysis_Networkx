import networkx as nx
import os
G = nx.Graph()    #Create an empty graph with no nodes and no edges.
file = os.path.join("write your pathnam")    #Load the data file
with open(file) as p:    #Try to open the data file
    next(p)    #ignore the firts row of the dataset
    for line in p:    #iterate in the dataset
        s=line.split()    #Break the dataset into different columns
        G.add_edge(s[0],s[1],weight=int(s[2]))    #Add edges and weights from the dataset
        
betweenness_centrality_dic = nx.betweenness_centrality(G)    #Calculate the Betweenness centrality of the network which will return a dictionary 
with open("Betweenness_Centrality_Output.txt","w") as f:    #Create a text file name Betweenness_Centrality_Output 
    f.write("\t\t\t\t\t\t\t\t\t************************************\t\t\tBetweenness Centrality Output\t\t\t************************************"+"\n")
     #Write a header title 
    for k,v in betweenness_centrality_dic.items():   #Iterate into the dictionary
        f.write(str(k)+": "+str(v)+"\n")    #Write Dictionary keys and values in the file