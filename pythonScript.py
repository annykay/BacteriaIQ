#!/usr/bin/env python


#loading libraries
import pandas as pd
import argparse

#parsing arguments. They are positional 
parser = argparse.ArgumentParser()
parser.add_argument("bacteria", help="bacteria we explore")
parser.add_argument("homedir", help="working directory")
parser.add_argument("numProt", help="number of proteins in bacteria genome", type=int)
args = parser.parse_args()

#reading predefined domains file
domFile = args.homedir+'/domains.txt'
domains = pd.read_table(domFile, names=['Family', 'NFamily', 'Part'])


#make a dummy data frame
all_domains = pd.DataFrame(columns= ['E-value', 'score', 'bias', 'E-value', 'score', 'bias', 'exp',
                             'N', 'Sequence','Family', 'NFamily', 'Part'])

#making a 'big' dataframe, containing all domainound by hmm
for order in range(domains.shape[0]):
 
    Family = domains.iloc[order]['Family']
    NFamily = domains.iloc[order]['NFamily']
    Part = domains.iloc[order]['Part']
    
    #read a file
    fileName = args.homedir+'/results/'+args.bacteria+'/'+Family+'.txt'
    data = pd.read_table(fileName)
    data.columns = ['data']
    
    #finding begining and ending of sequences
    i = 0
    begining = data.iloc[i][0][0]
    j =0 
    #j is the number of the last header line
    while begining == '#':
        j+=1
        i+=1
        begining = data.iloc[i][0][0]
    #i is the number of row from which second block of information begins
    while begining != '>' and i < data.shape[0]-1:
        i+=1
        begining = data.iloc[i][0][0]
    if i < data.shape[0]-4:
    #make nice dataframe
        data1 = pd.DataFrame(data.iloc[j+5:i-1])
        new =  data1["data"].str.split( expand = True)
    
        new = new.iloc[:,:9]
        new.columns = ['E-value', 'score', 'bias', 'E-value', 'score', 'bias', 'exp',
                             'N', 'Sequence']
        new['Family'] = Family
        new['NFamily'] = NFamily
        new['Part'] = Part
        #add the results to the 'big' dataframe
        all_domains = pd.concat([all_domains, new])


#count the number of sequences 
nSigProt = 0
table = pd.crosstab(all_domains[all_domains['NFamily']==0]['Sequence'], all_domains[all_domains['NFamily']==0]['Part'])
nSigProt = table[(table[0]>=1) & (table[1]>=1)].shape[0]
print(nSigProt)
for i in range(1, 6):
    table = pd.crosstab(all_domains[all_domains['NFamily']==i]['Sequence'], all_domains[all_domains['NFamily']==i]['Part'])
    if len(table)>0:
        new_len=table[(table[0]>=1)].shape[0]
        nSigProt+=new_len
        print(new_len)
    else:
        print(0)



print('IQ of ', args.bacteria, ':', nSigProt/args.numProt)


