import networkx as nx
import os
G = nx.Graph()    #Create an empty graph with no nodes and no edges.
file = os.path.join("data.txt")    #Load the data file
with open(file) as p:    #Try to open the data file
    next(p)    #ignore the firts row of the dataset
    for line in p:    #iterate in the dataset
        s=line.split()    #Break the dataset into different columns
        G.add_edge(s[0],s[1],weight=int(s[2]))    
        
pagerank_dic = nx.pagerank(G, max_iter=100000)    #Calculate the Pagerank of the network which will return a dictionary 
with open("Updated_Pagerank_Output.txt","w") as f:    #Create a text file name Pagerank_Output 
    f.write("\t\t\t\t\t\t\t\t\t************************************\t\t\tPagerank Output\t\t\t************************************"+"\n")
     #Write a header title 
    for k,v in pagerank_dic.items():   #Iterate into the dictionary
        f.write(str(k)+": "+str(v)+"\n") 