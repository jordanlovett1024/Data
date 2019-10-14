import numpy as np
import pandas as pd
import sys
import os

#get list of every file in mapping files 
path = '/../../home/labs/holscher_lab/alex/AGP_2019/mapping_files/'
os.system("ls /../../home/labs/holscher_lab/alex/AGP_2019/mapping_files/ > files.txt")

with open('files.txt') as f:
    filenames = f.readlines()
filenames = [x.strip() for x in filenames]

def count_gaps(path,tsv,gaps,entries):
    df = pd.read_csv(path+tsv,sep='\t')
    for i in df.columns: df[i] = df[i].astype(str)
    
    for col_index,col_value in enumerate(df.columns):
        entries[col_index] = entries[col_index] + len(df[col_value])
        gaps[col_index] = gaps[col_index] + len([i for i in df[col_value] if i.__contains__('Not provided')
                               or i.__contains__('nan')])  

df1 = df = pd.read_csv(path+filenames[1],sep='\t')
gaps = np.zeros((len(df1.columns),))
entries = np.zeros(gaps.shape)

for i in range(len(filenames[:200])):
    count_gaps(path,filenames[i],gaps,entries)
for i in range(entries.shape[0]):
    if entries[i] == 0: 
        gaps = gaps[:i]
        entries = entries[:i]

print(gaps.shape,entries.shape)
results = pd.DataFrame({'Name':df.columns,'Missing':gaps,'Occurences':entries, '% Missing':gaps/entries *100})
results.to_csv('results.tsv',sep='\t')
