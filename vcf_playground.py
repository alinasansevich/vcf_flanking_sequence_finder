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

# this is a fasta header:
'>AF372922.1 Arabidopsis thaliana AT4g37870/T28I19_150 mRNA, complete cds'
# in the values variable from the parser it is the 1st value in a tuple,
# without the '>'

# # this is the way to access each value in the 'CHROM' column:
# data.loc[1,'CHROM']
# Out[9]: 'CM001064.3'

# for now, I'll use this:

wip_filepath = '/home/alina/Learning_to_Code/My_Projects/vcf/PCK1.fna'

with open(wip_filepath) as handle:
    for values in SimpleFastaParser(handle):
        print(values[0])

# AF372922.1 Arabidopsis thaliana AT4g37870/T28I19_150 mRNA, complete cds
# AK226329.1 Arabidopsis thaliana mRNA for phosphoenolpyruvate carboxykinase (ATP) -like protein, complete cds, clone: RAFL05-14-F18
# AL035709.1 Arabidopsis thaliana DNA chromosome 4, BAC clone T28I19 (ESSA project)
# AL161592.2 Arabidopsis thaliana DNA chromosome 4, contig fragment No. 88
# AY078035.1 Arabidopsis thaliana AT4g37870/T28I19_150 mRNA, complete cds

# continue here, use this to find 'CHROM', find 'POS', etc







