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
# count = 0
# with open(genome_filepath) as fasta_file:
#   parser = fastaparser.Reader(fasta_file, parse_method='quick') # Reader object contains all sequences
#   for seq in parser:
#     count += 1

# how many sequences do I have in the genome file?
print(count) # 3148 sequences

######################################################################
######################################################################

# This is my parser:

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

# this is wip:

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
            'ALT_1': ['C', 'A', 'G', 'G', 'T'],
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

flanking_seqs = []
   
with open(wip_filepath) as handle:
    for fastaseq in SimpleFastaParser(handle): # fastaseq is a tuple ('header', 'sequence')
        for i in range(len(wip_df)):
            chrom = wip_df.loc[i, 'CHROM'] # get the chromosome id from df
            if chrom in fastaseq[0]:
                # I can find each nucleotide!
                # print(fastaseq[1][wip_df.loc[i, 'POS']])
                seq = fastaseq[1]
                print("Lenght of Sequence: {}".format(len(seq)))
                ref_snp = wip_df.loc[i, 'REF']
                ref_pos = wip_df.loc[i, 'POS']
                alt_snp = wip_df.loc[i, 'ALT_1']
                if ref_snp == fastaseq[1][ref_pos]:
                    if ref_pos - 50 < 0:
                        flanking_5 = seq[:ref_pos]
                    else:
                        flanking_5 = seq[(ref_pos - 50):ref_pos]             
                    flanking_3 = seq[(ref_pos + 1): ref_pos + 51]
                    flanking_5_3_seq = assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3)
                    flanking_seqs.append(flanking_5_3_seq)

wip_df['FLANKING_SEQS'] = flanking_seqs

# 10073070 SNPs * 3148 genome sequences = 31710024360 loops >>> Ups, this is too much!


def assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3):
    """
    (str, str, str, str) -> str
    
    ref_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the reference SNP.
    alt_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the variant SNP.
    flanking_5 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp upstream from ref_snp.
    flanking_3 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp downstream from ref_snp.

    Returns a new str, the reference SNP concatenated with its variant 
    and its flanking sequences, like this:
        
        ref_snp = 'T'
        alt_snp = 'C'
        50 bp = 'XXXXXXXXXXXXXXX'
        
        'XXXXXXXXXXXXXXX[T/C]XXXXXXXXXXXXXXX'

    
    """
    return flanking_5 + '[' + ref_snp + '/' + alt_snp + ']' + flanking_3

 

######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################

# genome_fasta_parser_Bio.py - first BIG run, on BigCompu
# I printed the flanking sequences to screen, run from 13:49 to 18:30 >>> Ctrl+C
# last sequence length >>> 25609 >>> it doesn't exist???

from Bio.SeqIO.FastaIO import SimpleFastaParser
import pandas as pd

def assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3):
    """
    (str, str, str, str) -> str
    
    ref_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the reference SNP.
    alt_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the variant SNP.
    flanking_5 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp upstream from ref_snp.
    flanking_3 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp downstream from ref_snp.

    Returns a new str, the reference SNP concatenated with its variant 
    and its flanking sequences, like this:
        
        ref_snp = 'T'
        alt_snp = 'C'
        50 bp = 'XXXXXXXXXXXXXXX'
        
        'XXXXXXXXXXXXXXX[T/C]XXXXXXXXXXXXXXX'

    
    """
    return flanking_5 + '[' + ref_snp + '/' + alt_snp + ']' + flanking_3


genome_filepath = '/media/hernan/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

data = pd.read_csv('sub_df.csv')

flanking_seqs = []
   
with open(genome_filepath) as handle:
    for fastaseq in SimpleFastaParser(handle): # fastaseq is a tuple ('header', 'sequence')
        for i in range(len(data)):
            chrom = data.loc[i, 'CHROM'] # get the chromosome id from df
            if chrom in fastaseq[0]:
                # I can find each nucleotide!
                # print(fastaseq[1][wip_df.loc[i, 'POS']])
                seq = fastaseq[1]
                print("Lenght of Sequence: {}".format(len(seq)))
                ref_snp = data.loc[i, 'REF']
                ref_pos = data.loc[i, 'POS']
                alt_snp = data.loc[i, 'ALT_1']
                if ref_snp == fastaseq[1][ref_pos]:
                    if ref_pos - 50 < 0:
                        flanking_5 = seq[:ref_pos]
                    else:
                        flanking_5 = seq[(ref_pos - 50):ref_pos]             
                    flanking_3 = seq[(ref_pos + 1): ref_pos + 51]
                    flanking_5_3_seq = assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3)
                    flanking_seqs.append(flanking_5_3_seq)

data['FLANKING_SEQS'] = flanking_seqs

data.head()


######################################################################
######################################################################
######################################################################
######################################################################

# genome_fasta_parser_Bio.py - second BIG run, on BigCompu
# I printed the flanking sequences to screen, run from 12:32 to 18:43 >>> Ctrl+C

from Bio.SeqIO.FastaIO import SimpleFastaParser
import pandas as pd
import datetime

def assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3):
    """
    (str, str, str, str) -> str
    
    ref_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the reference SNP.
    alt_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the variant SNP.
    flanking_5 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp upstream from ref_snp.
    flanking_3 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp downstream from ref_snp.

    Returns a new str, the reference SNP concatenated with its variant 
    and its flanking sequences, like this:
        
        ref_snp = 'T'
        alt_snp = 'C'
        50 bp = 'XXXXXXXXXXXXXXX'
        
        'XXXXXXXXXXXXXXX[T/C]XXXXXXXXXXXXXXX'

    
    """
    return flanking_5 + '[' + ref_snp + '/' + alt_snp + ']' + flanking_3



genome_filepath = '/media/hernan/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

data = pd.read_csv('sub_df.csv')

flanking_seqs = []
   
start = 0
with open(genome_filepath) as handle:
    counter = 0
    for fastaseq in SimpleFastaParser(handle): # fastaseq is a tuple ('header', 'sequence')
        print('\n\n', fastaseq[0])
        print('Current time: ', datetime.datetime.now())
        for i in range(start, len(data)):
            if fastaseq[0][:10] == data.loc[i, 'CHROM']:
                seq = fastaseq[1]
                ref_snp = data.loc[i, 'REF']
                ref_pos = data.loc[i, 'POS']
                alt_snp = data.loc[i, 'ALT_1']
                # only gets flanking_seqs for those that match this condition
                if ref_snp == fastaseq[1][ref_pos]:
                    if ref_pos - 50 < 0:
                        flanking_5 = seq[:ref_pos]
                    else:
                        flanking_5 = seq[(ref_pos - 50):ref_pos]             
                    flanking_3 = seq[(ref_pos + 1): ref_pos + 51]
                    flanking_5_3_seq = assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3)
                    flanking_seqs.append(flanking_5_3_seq)
                    counter += 1
                    print(flanking_seqs)
                    print(counter)
            else:
                start = i
                break

data['FLANKING_SEQS'] = flanking_seqs

data.head()
data.to_csv('/home/hernan/Desktop/at_Big_Compu/SNPs_w_flanking_seqs.csv', index=False)

######################################################################
######################################################################
######################################################################
######################################################################

### I want the genome headers to sort the snps in the headers order

genome_filepath = '/media/hernan/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'
   
headers = []
len_seq = []
counter = 0

with open(genome_filepath) as handle:
    for fastaseq in SimpleFastaParser(handle):
        headers.append(fastaseq[0])   # get the headers
        len_seq.append(len(fastaseq[1]))

df = pd.DataFrame(list(zip(len_seq, headers)),
                  columns=['len_seq', 'headers'])

# save headers in a .csd
df.to_csv('/home/hernan/Desktop/at_Big_Compu/genome_headers.csv', index=False)
##### it took less than a minute to run

headers = pd.read_csv('genome_headers.csv')
headers.head(15)
headers.tail(15)

# # yesterday it run until len == 25609, I try to see what number that seq was but:
# headers[headers['len_seq' == 25609]] # KeyError: False????!!!!
# 25609 in headers.len_seq # False????!!!!

data.shape # (10073070, 5)

data[data['CHROM'] == 'CM001064.3']
# 1st CHROM, [522418 rows x 5 columns], last row index: 522417

data[data['CHROM'] == 'CM001065.3']
# 2nd CHROM, [283941 rows x 5 columns], first row index: 522418, last row index: 806358 

data[data['CHROM'] == 'CM001066.3']
# 3rd CHROM, [448580 rows x 5 columns], first row index: 806359, last row index: 1254938

# OK, it looks like the SNPs are already sorted by position in each CHROM

######################################################################
######################################################################
######################################################################
######################################################################

# genome_fasta_parser_Bio.py - third BIG run, on BigCompu, without printing to screen
# Completed everything in 15 minutes! 
# Got a ValueError when appending to df >>> it really run through everything!

from Bio.SeqIO.FastaIO import SimpleFastaParser
import pandas as pd
import datetime

def assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3):
    """
    (str, str, str, str) -> str
    
    ref_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the reference SNP.
    alt_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the variant SNP.
    flanking_5 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp upstream from ref_snp.
    flanking_3 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp downstream from ref_snp.

    Returns a new str, the reference SNP concatenated with its variant 
    and its flanking sequences, like this:
        
        ref_snp = 'T'
        alt_snp = 'C'
        50 bp = 'XXXXXXXXXXXXXXX'
        
        'XXXXXXXXXXXXXXX[T/C]XXXXXXXXXXXXXXX'

    
    """
    return flanking_5 + '[' + ref_snp + '/' + alt_snp + ']' + flanking_3

genome_filepath = '/media/hernan/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

data = pd.read_csv('sub_df.csv')

flanking_seqs = []
   
start = 0
with open(genome_filepath) as handle:
    #counter = 0
    for fastaseq in SimpleFastaParser(handle): # fastaseq is a tuple ('header', 'sequence')
        print('\n\n', fastaseq[0])
        print('Current time: ', datetime.datetime.now())
        for i in range(start, len(data)):
            if fastaseq[0][:10] == data.loc[i, 'CHROM']:
                seq = fastaseq[1]
                ref_snp = data.loc[i, 'REF']
                ref_pos = data.loc[i, 'POS']
                alt_snp = data.loc[i, 'ALT_1']
                # only gets flanking_seqs for those that match this condition
                if ref_snp == fastaseq[1][ref_pos]:
                    if ref_pos - 50 < 0:
                        flanking_5 = seq[:ref_pos]
                    else:
                        flanking_5 = seq[(ref_pos - 50):ref_pos]             
                    flanking_3 = seq[(ref_pos + 1): ref_pos + 51]
                    flanking_5_3_seq = assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3)
                    flanking_seqs.append(flanking_5_3_seq)
                    #counter += 1
                    #print(flanking_seqs)
                    #print(counter)
            else:
                start = i
                break

data['FLANKING_SEQS'] = flanking_seqs

data.head()
data.to_csv('/home/hernan/Desktop/at_Big_Compu/SNPs_w_flanking_seqs.csv', index=False)

Traceback (most recent call last):
  File "genome_fasta_parser_Bio.py", line 67, in <module>
    data['FLANKING_SEQS'] = flanking_seqs
  File "/home/hernan/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 3163, in __setitem__
    self._set_item(key, value)
  File "/home/hernan/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 3242, in _set_item
    value = self._sanitize_column(key, value)
  File "/home/hernan/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 3899, in _sanitize_column
    value = sanitize_index(value, self.index)
  File "/home/hernan/.local/lib/python3.8/site-packages/pandas/core/internals/construction.py", line 751, in sanitize_index
    raise ValueError(
ValueError: Length of values (1398800) does not match length of index (10073070)
Fri 23 Apr 2021 08:15:33 AM CDT

######################################################################
######################################################################
######################################################################
######################################################################

# It extracted 1398800 from the 10073070 SNPs in data
# >>> only 1398800 meet this condition: if ref_snp == fastaseq[1][ref_pos]:
# So, now I'll modify the code to accomplish 2 things:
#     1- Get those 1398800 'SNPs'
#     2- Get ALL 10073070 'SNPs' and their flanking sequences
    
#     From there I want:
#         * compare run times:  15 min vs. 22 min
#         * compare final_results file size: 188.6 MB vs. 1.3 GB
#         * what are those 8674270 'SNPs' >>> is_snp?

##############################     ###################################

##############################     ###################################

# 1- Get those 1398800 'SNPs'

# genome_fasta_parser_Bio.py - fourth BIG run, on BigCompu (1.5 of 7.7 GiB)
# around 15 minutes to run, creates a 188.6 MB .csv file


from Bio.SeqIO.FastaIO import SimpleFastaParser
import pandas as pd
import datetime

def assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3):
    """
    (str, str, str, str) -> str
    
    ref_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the reference SNP.
    alt_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the variant SNP.
    flanking_5 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp upstream from ref_snp.
    flanking_3 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp downstream from ref_snp.

    Returns a new str, the reference SNP concatenated with its variant 
    and its flanking sequences, like this:
        
        ref_snp = 'T'
        alt_snp = 'C'
        50 bp = 'XXXXXXXXXXXXXXX'
        
        'XXXXXXXXXXXXXXX[T/C]XXXXXXXXXXXXXXX'

    
    """
    return flanking_5 + '[' + ref_snp + '/' + alt_snp + ']' + flanking_3

genome_filepath = '/media/hernan/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

data = pd.read_csv('sub_df.csv')

flanking_seqs = []
chrom_id = []
pos = []
ref = []
alt = []
is_snp = []

start = 0
with open(genome_filepath) as handle:
    for fastaseq in SimpleFastaParser(handle): # fastaseq is a tuple ('header', 'sequence')
        print('\n\n', fastaseq[0])
        print('Current time: ', datetime.datetime.now())
        for i in range(start, len(data)):
            if fastaseq[0][:10] == data.loc[i, 'CHROM']:
                seq = fastaseq[1]
                ref_snp = data.loc[i, 'REF']
                ref_pos = data.loc[i, 'POS']
                alt_snp = data.loc[i, 'ALT_1']
                # only gets flanking_seqs for those that match this condition
                if ref_snp == fastaseq[1][ref_pos]:
                    if ref_pos - 50 < 0:
                        flanking_5 = seq[:ref_pos]
                    else:
                        flanking_5 = seq[(ref_pos - 50):ref_pos]             
                    flanking_3 = seq[(ref_pos + 1): ref_pos + 51]
                    flanking_5_3_seq = assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3)
                    flanking_seqs.append(flanking_5_3_seq)
                    chrom_id.append(data.loc[i, 'CHROM'])
                    pos.append(ref_pos)
                    ref.append(ref_snp)
                    alt.append(alt_snp)
                    is_snp.append(data.loc[i, 'is_snp'])

            else:
                start = i
                break

results = {'CHROM': chrom_id,
            'POS': pos,
            'REF': ref,
            'ALT_1': alt,
            'is_snp': is_snp,
            'FLANKING_SEQS': flanking_seqs}

results_df = pd.DataFrame.from_dict(results)

print(results_df.head())
results_df.to_csv('/home/hernan/Desktop/at_Big_Compu/SNPs_w_flanking_seqs.csv', index=False)

##############################     ###################################

##############################     ###################################

# 2- Get ALL 10073070 'SNPs' and their flanking sequences

# genome_fasta_parser_Bio.py - fifth BIG run, on BigCompu (1.5 of 7.7 GiB)
# around 22 minutes to run, creates a 1.3GB .csv file (1.4 of 7.7 GiB)

from Bio.SeqIO.FastaIO import SimpleFastaParser
import pandas as pd
import datetime

def assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3):
    """
    (str, str, str, str) -> str
    
    ref_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the reference SNP.
    alt_snp : str
        DESCRIPTION: 1 character (A, T, G or C), the variant SNP.
    flanking_5 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp upstream from ref_snp.
    flanking_3 : str
        DESCRIPTION: 50 characters (A, T, G or C), the 50 bp downstream from ref_snp.
    Returns a new str, the reference SNP concatenated with its variant 
    and its flanking sequences, like this:
        
        ref_snp = 'T'
        alt_snp = 'C'
        50 bp = 'XXXXXXXXXXXXXXX'
        
        'XXXXXXXXXXXXXXX[T/C]XXXXXXXXXXXXXXX'
    """
    return flanking_5 + '[' + ref_snp + '/' + alt_snp + ']' + flanking_3

genome_filepath = '/media/hernan/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

data = pd.read_csv('sub_df.csv')

flanking_seqs = []
chrom_id = []
pos = []
ref = []
alt = []
is_snp = []

start = 0
with open(genome_filepath) as handle:
    for fastaseq in SimpleFastaParser(handle): # fastaseq is a tuple ('header', 'sequence')
        print('\n\n', fastaseq[0])
        print('Current time: ', datetime.datetime.now())
        for i in range(start, len(data)):
            if fastaseq[0][:10] == data.loc[i, 'CHROM']:
                seq = fastaseq[1]
                ref_snp = data.loc[i, 'REF']
                ref_pos = data.loc[i, 'POS']
                alt_snp = data.loc[i, 'ALT_1']
                # I comment out this condition, so it should returns ALL 10073070 SNPs
                # if ref_snp == fastaseq[1][ref_pos]:
                if ref_pos - 50 < 0:
                    flanking_5 = seq[:ref_pos]
                else:
                    flanking_5 = seq[(ref_pos - 50):ref_pos]             
                flanking_3 = seq[(ref_pos + 1): ref_pos + 51]
                flanking_5_3_seq = assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3)
                flanking_seqs.append(flanking_5_3_seq)
                chrom_id.append(data.loc[i, 'CHROM'])
                pos.append(ref_pos)
                ref.append(ref_snp)
                alt.append(alt_snp)
                is_snp.append(data.loc[i, 'is_snp'])

            else:
                start = i
                break

results = {'CHROM': chrom_id,
            'POS': pos,
            'REF': ref,
            'ALT_1': alt,
            'is_snp': is_snp,
            'FLANKING_SEQS': flanking_seqs}

results_df = pd.DataFrame.from_dict(results)

print(results_df.head())
results_df.to_csv('/home/hernan/Desktop/at_Big_Compu/SNPs_w_flanking_seqs_10M.csv', index=False)


























######################################################################
######################################################################

### extras:

### check memory availavility:
    ### https://pypi.org/project/psutil/
    ### https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
    
### CLI arguments:
    ### https://www.tutorialspoint.com/python/python_command_line_arguments.htm

### numpy broadcast? vectorization?:
    ### https://stackoverflow.com/questions/5197650/broadcasting-a-python-function-on-to-numpy-arrays
    ### https://www.experfy.com/blog/bigdata-cloud/why-you-should-forget-loops-and-embrace-vectorization-for-data-science/
