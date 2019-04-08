import os
import numpy as np
file = os.path.join('data','KEGG_04022019.txt')
protein=[]
values=[]
with open(file) as l:
    next(l)
    for i in l:
        s = i.split()
        values.append(s[0])
my_dic={}
with open(file) as p:
    next(p)
    for line in p:
        s=line.split()
        if s[1] in my_dic:
            a=my_dic[s[1]]
            a.append(s[0])
        else:
            a=[]
            a.append(s[0])
            my_dic[s[1]] = a
keys = sorted(list(my_dic.keys()))
values.sort()
rows = len(keys)
cols = len(values)
arr=[[0]*cols]*rows
np_arr =  np.array(arr)
for k,v in my_dic.items():
    index_key = keys.index(k)
    for value in v:
        print(value)
        value_key = values.index(value)
        np_arr[index_key,value_key] = 1
np_mat= np.matrix(np.array(np_arr))
with open('kgg_output.mat','w') as p:
    for line in np_mat:
        np.savetxt(p, line, fmt='%i')