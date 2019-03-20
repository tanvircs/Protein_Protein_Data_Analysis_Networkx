import networkx as next 
import os
G = nx.Graph() #Create an empty graph with no nodes and no edges.
file = os.path.join("write your pathname") #Load the data file
with open(file) as p:	#Try to open the data file
    next(p)				#ignore the firts row of the dataset
    for line in p:		#iterate in the dataset
        s=line.split()	#Break the dataset into different columns
        G.add_edge(s[0],s[1],weight=int(s[2]))	#Add edges and weights from the dataset
        
load_centrality = nx.load_centrality(G)	#Calculate the load centrality of the network which will return a dictionary 
with open("Load_Centrality_Output.txt","w") as f:	#Create a text file name Load_Centrality_Output 
    f.write("\t\t\t\t\t\t\t\t\t************************************\t\t\tLoad Centrality Output\t\t\t************************************"+"\n")
    #Write a header title 
    for k,v in load_centrality.items():	#Iterate into the dictionary
        f.write(str(k)+": "+str(v)+"\n")	#Write Dictionary keys and values in the file