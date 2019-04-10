import os
import numpy as np
import scipy.io as sio
file = os.path.join("data","KEGG_04022019.txt")
values=[]
my_dic={}

# In the below section, I make a map where the dictionary keys are the values of protein
# and dictionary values is a list of labels where I check one Protein is connected with
# how many unique labels. Also I make a list of labels from the dataset.

with open(file) as p:
    for line in p:
        s=line.split()
        values.append(s[0])
        if s[1] in my_dic:
            a=my_dic[s[1]]
            a.append(s[0])
        else:
            a=[]
            a.append(s[0])
            my_dic[s[1]] = a
            
# Sorted the dictionary keys

keys = sorted(list(my_dic.keys()))

# Sorted the labels list which i generated earlier

values.sort()
rows = len(keys)
cols = len(values)

# Make an 2D arrays of zeros from unique number of proteins and 
# Labels from the dataset. In here rows value are the
# Unique number of protein and columns value are the 
# Unique number of Labels. Rows and Columns are not equal.

arr=[[0]*cols]*rows
np_arr =  np.array(arr)

# Iterate into the dictionay I created earlier. 
# Now check for the index of keys and get the values for that particular 
# Key and then search with the list of the Lables which i sorted earlier. 
# When it find one match put 1 in the 
# Array index number and if no match then there will be zero beacuse 
# I made a m*n zeros 2D array earlier.

for k,v in my_dic.items():
    index_key = keys.index(k)
    for value in v:
        value_key = values.index(value)
        np_arr[index_key,value_key] = 1

# Finally Save the array into a mat file format.

sio.savemat('kegg.mat',{'kegg':np_arr})