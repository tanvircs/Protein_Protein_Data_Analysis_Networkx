import os
import numpy as np
import scipy.io as sio

# Load the dataset

file = os.path.join('data','KEGG_04022019.txt')

first_dict = {}
labels = []

# Interate into dataset line by line. 
# Make dictionay called first_dict which keys are connected with all the labels data. 
# Besides create a list labels which contains all the labels from the dataset

with open(file) as p:
    for i in p:
        s = i.split()
        labels.append(s[0][5:])
        if s[1] in first_dict:
            a= first_dict[s[1]]
            a.append(s[0])
        else:
            #first_dict[s[1]]=a
            if s[0].startswith('path:'):
                temp_val = (s[0][5:]) 
                first_dict[s[1]]=[temp_val]
       
            
unique_labels = set(labels)
sorted_unique_labels= sorted(unique_labels)

list_from_first_dict = []

# Iterate through the list of lists from first_dict.
# Calculate the unique list
# Sorted the list

for list_1 in first_dict.values():
    unique_list_first_dict = set(list_1)
    sorted_unique_list_first_dict = sorted(unique_list_first_dict)
    list_from_first_dict.append(sorted_unique_list_first_dict)
    
keys_list = []

# Get the keys from first_dict 

for i in first_dict.keys():
    keys_list.append(i)
    
# Sorted the keys list
    
sorted_keys_list = sorted(keys_list)

# Make a new dictionay final_dict from sorted key list and list from the first dictionay 

final_dict = dict(zip(sorted_keys_list,list_from_first_dict))

# Get the length of sorted key list from first_dict and sorted unique labels from the first list 
# Which was created while iterate through the dataset line by line

rows = len(sorted_keys_list)
cols = len(sorted_unique_labels)

zeros_array = [[0]*cols]*rows
np_array = np.array(zeros_array)

# Iterate into the final_dict and get the keys index position
# Compare final_dict values with sorted unique label list and check the index position
# If find any match put 1 in the array value

for k,v in final_dict.items():
    key_index = sorted_keys_list.index(k)
    for value in v:
        if value.startswith('path:'):
            value = value[5:]
            value_key = sorted_unique_labels.index(value)
            np_array[key_index,value_key]=1

# Finally save numpy array into a mat file
        
sio.savemat('Final_Kegg.mat',{'final_kegg':np_array,'proteins':sorted_keys_list,'labels':sorted_unique_labels})