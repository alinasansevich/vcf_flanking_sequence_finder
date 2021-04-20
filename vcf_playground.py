#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:35:58 2021

@author: alina
"""

######################################################################
######################################################################

data = pd.read_csv('sub_df.csv')
data.head(10)
len(data) # 10073070 >>> this is SO different!!! what was in the other file he gave me???!!!

##### how many False values are there in 'is_snp'?

# check data types first:
data['is_snp'][0] # True
type(data['is_snp'][0]) # numpy.bool_


data2 = data[data['is_snp'] == True]
len(data2) 10005487
data3 = data[data['is_snp'] == False]
len(data3) # 67583

len(data2) + len(data3) == len(data) # True

# 67583 False snps, let's see what they are:
data3.head(10)

#            CHROM     POS   REF ALT_1  is_snp
# 360   CM001064.3  297213     T     A   False
# 708   CM001064.3  375194     C   CAA   False
# 806   CM001064.3  405268     T     G   False
# 808   CM001064.3  405272     A     C   False
# 839   CM001064.3  411867     T     A   False
# 931   CM001064.3  487360  ATAC  GTAC   False
# 1290  CM001064.3  545645     A    AC   False
# 1422  CM001064.3  558890    AT     A   False
# 1426  CM001064.3  558940     G     C   False
# 1594  CM001064.3  579859     C     A   False

# I continue working with data2, it has the True snps.

# how many sequences do I have in the genome file?
count = 0
with open(genome_filepath) as fasta_file:
  parser = fastaparser.Reader(fasta_file, parse_method='quick') # Reader object contains all sequences
  for seq in parser:
    count += 1

print(count) # 3148 sequences

######################################################################
######################################################################

# I'm here:

from Bio.SeqIO.FastaIO import SimpleFastaParser

# filepath = input("Please enter the absolute filepath to the fasta file: ")
genome_filepath = '/media/alina/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

count = 0
with open(genome_filepath) as handle:
    for values in SimpleFastaParser(handle):
        print(values)
        print(type(values[0]), type(values[1]))
        count += 1

print(count) # 3148, class 'str', class 'str'

######################################################################
######################################################################


# this is a fasta header:
'>AF372922.1 Arabidopsis thaliana AT4g37870/T28I19_150 mRNA, complete cds'
# in the values variable from the parser it is the 1st value in a tuple,
# without the '>'

# # this is the way to access each value in the 'CHROM' column:
# data.loc[1,'CHROM']
# Out[9]: 'CM001064.3'

# I create a fasta file + df to work with:

wip_filepath = '/home/alina/Learning_to_Code/My_Projects/vcf/PCK1.fna'

# I store my wip arabidopsis seqs in this list
wip_seqs = [] 

with open(wip_filepath) as handle:
    for values in SimpleFastaParser(handle):
        wip_seqs.append(values[1])

# AF372922.1 Arabidopsis thaliana AT4g37870/T28I19_150 mRNA, complete cds
# AK226329.1 Arabidopsis thaliana mRNA for phosphoenolpyruvate carboxykinase (ATP) -like protein, complete cds, clone: RAFL05-14-F18
# AL035709.1 Arabidopsis thaliana DNA chromosome 4, BAC clone T28I19 (ESSA project)
# AL161592.2 Arabidopsis thaliana DNA chromosome 4, contig fragment No. 88
# AY078035.1 Arabidopsis thaliana AT4g37870/T28I19_150 mRNA, complete cds

# continue here, use this to find 'CHROM', find 'POS', etc
import pandas as pd

wip_data = {'CHROM': ['AF372922.1', 'AK226329.1', 'AL035709.1', 'AL161592.2', 'AY078035.1'],
            'POS': [123, 888, 9999, 6500, 25],
            'REF': ['T', 'G', 'A', 'A', 'C'],
            'ALT_1': ['C', 'A', 'G', 'A', 'T'],
            'is_snp': [True, True, True, True, True]}

wip_df = pd.DataFrame.from_dict(wip_data)
wip_df # this would be the data from the .vcf file:
# Out[15]: 
#         CHROM   POS REF ALT_1  is_snp
# 0  AF372922.1   123   T     C    True
# 1  AK226329.1   888   G     A    True
# 2  AL035709.1  9999   A     G    True
# 3  AL161592.2  6500   A     A    True
# 4  AY078035.1    25   C     T    True

####### Now, let's find the CHROM in the fasta file:

wip_df.loc[0,'CHROM']
# Out[28]: 'AF372922.1'

 
    
with open(wip_filepath) as handle:
    for fastaseq in SimpleFastaParser(handle):
        for i in range(len(wip_df)):
            chrom = wip_df.loc[i, 'CHROM'] # get the chromosome id from df
            if chrom in fastaseq[0]:
                # I can find each nucleotide!
                print(fastaseq[1][wip_df.loc[i, 'POS']])
                
                
                
            
            






from Bio.SeqIO.FastaIO import SimpleFastaParser



    
count = 0
with open(genome_filepath) as handle:
    for values in SimpleFastaParser(handle):
        print(values)
        print(type(values[0]), type(values[1]))
        count += 1

print(count)

######################################################################
######################################################################

# from:
    # https://www.geeksforgeeks.org/iterating-over-rows-and-columns-in-pandas-dataframe/

dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
  
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)
  
# iterating over rows using iterrows() function 
for i, j in df.iterrows():
    print(i, j)
    print()

# using iteritems() function to retrieve rows
for key, value in df.iteritems():
    print(key, value)
    print()

# using a itertuples() 
for i in df.itertuples():
    print(i)




















