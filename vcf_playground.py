#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:35:58 2021

@author: alina
"""

# 1 >>> open .vcf, get 4 columns >>> DONE

# 2 >>> get snps position from vcf:
    
    # data['POS'] >>> snps positions are in this column
    
    # find SNP in chromosome in .fna file >>> can I use df.apply for this??????
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html
        # check that SNPx == 'REF'/'ALT'!
    
# 3 >>> find 5-flank-seq and 3-flank-seq and store them in dict/df (50pb each)

# 4 >>> create pd.final_df, 3 columns: CHROM, SNP_POS, 5'-FlankSeq[A/G]3'-FlankSeq as a single str

######################################################################
######################################################################

# trying to read the genome with fastaparser:
import pandas as pd
import fastaparser

data = pd.read_csv('sub_df.csv')

genome_filepath = '/media/alina/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

# the following code is from:  https://pypi.org/project/fastaparser/

with open(genome_filepath) as fasta_file:
  parser = fastaparser.Reader(fasta_file, parse_method='quick') # Reader object contains all sequences
    for seq in parser:
        seq is a FastaSequence object https://fastaparser.readthedocs.io/en/latest/api_fastasequence/
        print('header:', seq.header)
        #print('Description:', seq.description)
        print('Sequence:', seq.sequence)
        print()

# Out[1]: this is just a tiny slice of the complete result:
# header: >AEKE03003133.1 Solanum lycopersicum cultivar Heinz 1706 SL3.00SC0003138, whole genome shotgun sequence
# Sequence: attcttacccttagcagagttctcctacaacaatagctatcactcaagcattgatatggccccatttgaggaactatatgggagaaaatataggtctcccattgggtggtttgatgcatttgaagttagaccttggggcactgaccttctgagggaatcgttagataaagtgaaatctattcaagaaaagcttctagcggcgaaaagtagacagaaggagtacgcagatcggaaggttaaagacatggagtttatggagggtgaacaagtcttgttgaaggtttcgccaatgaaaggggtgatgcggtttgtaagcgaggtaaacttagcccaaggtatattggtccatttgaagtacttaagcgagtagaggaggtggcttatgagttagccttgcctccagcgctgtccggagtgcatccggtatttcatgtgtctatgttgaaaagataccatggggatggaaactacattatccgttgggattcagttttgcttgataaGAATTTGTCCTATGAGAAGGAGCCTGTTTCCATTTTAGGTAGAGAAGTTTGCAagtgaggtcaagagagattgcatccatcaaagttcaatggaggAATCGACCCGTCGAAGAAGctacttgggagaaagaggctgatatgcaagaaagatacccacacctgtttacagattcaggtactccttttcgccattgttttccttcttgttgtcattcggggacgaacgatgggtaaattggtatctattgtaacgacctgttttagccgttttgagcagcaaattttatttttggaaaactgACTGAGACGaaggaccccacgacggaccgtcatggactcgaCGAAACATCGCAgggtcttgtttcaaaacacttagaaaatatgataTTGGGTACTGAAagtcgactctctgaacttcgtgacggaatggcaggacggaccgtcacagagtcttcagtggaaatccagtctctgaaccttgcgatgacctgcaggacggaccatcgcaggcacgacgggccgtcacagattgcgtaatcccagtctgggtcggatttctttatacgttttaagggacgtttttgactattcctgctttaattataaagttagtgggtcaatattaataagtctaattacttggggtttAAAAGAAGTAACCTTAAGATAATTaatgggttattattgccatcttttattcttaattatatactaattagggtaaaagaaagagggtttgaataaagaaaatagaaagaacaaagagggagagaggattgatcgagagaggagaaacaaagaggaaaacacaaagcttttggaatttgcttgcttgatcactaatcttcggtggaggtaggttatggtttctcttacgatattcatagtaaactcttaatagcgaatgatatgtattgataatattgtaaaccctgctatgtgtttaattgtatgcttgcatgaatgtaattatataattgtgattatataagcatgatgaagttattgaatcccaaatcttgcaagaccctaatctcttgttaatgatgaggccttggtataaaaaaagaagtgatggactaaaataatgagattgatgatgccttggtaagaaagaaggcttgatgaattgatagaaggagattaagggatcaggtgtcacgaactgacacgtagatttaggggatcgggtgtcatgaaccgacacgtagatttaggggatcaggtgtcacgaaccgacacgtagatttaggggatcgggtgtcacgaatagacacatagatttaggggatcgggtgtcacgaaccgacacgtagatttaggggatcgggtgtcacgaactgacacgtagatttaggggatcgggtgtcacgaactgacacttagatttaggggatcggagtgtcacgttctgacacatagtagtaggggatcggagtgtcacgtaccgacacaagaggattgatgaatatgtgggagcggagtgtcacgtactgac

# header: >AEKE03003134.1 Solanum lycopersicum cultivar Heinz 1706 SL3.00SC0003139, whole genome shotgun sequence
# Sequence: TAATACTCATTATCTATGaatatagtcaagctaggaattgaattacctgcaggtacggggaacaagtaaggatacttattcttcatttcgtcttccgcttcccaagtcatatcctccctattgttattttgccacaacactttgagggaagccacatccttagtatgtaaccttctaacctgacgatcaagtatagccacgggtttctcctcatatgacaaaTCCTCTGTTACCTGAATATCATCTACAGGGAATGctctagaaggatcaccaatacatttacgtagcatcgatacatggaagactggatgtaccgcctccaaatcagatggtagatccaactcataggcaaccttgcctatcctacgaacaatctgataaggcccaatgtatctcagactgagcttccccttcctgtcgaatctcatcacacccctcatgggtgataccttcaagaatacccagtcaccaatatgaaactccaaatctcgacgccgattatctgcatatgacttctgtcgactctgggctgctaataatctttcttgaataagcttcaccttgtcaacaacttgctgaatcacatccgggcctattaacttagtctcgccaacatcaaaccaaccaataggtgatctgcacttcctcccatatatGGCCTCGTATggtgccatctggatactagaatggtagctattattattaggcaaactcaatgagcggcaagtggtcatcccaactgcctttgaagtcaataatacaggcccgcaacatatcttctagtgtctgaatagtacgctcagcctACCCATCAGTCTAAGGGTGAAATGctgtgctaaggttcacctatgtccccaatcccttctgaaatgatctccaaaagttggctgtaaattgagctcctctgtctgatataatggacgtgggaaccccatgaagtctcactatctccctgacatataacctcgcataatcttcagccgaataagtagtcctgactAGAAGAAAATAGGccgatttcgtcagcctatctacaataacccatatagagtcatacttccgttgagtgcaaggtaagcctgtaatgaagtccatattaatcatctcccattttcaagtcgggatctctatctcctgtaataatccaccaggcttttgatgttcgatcttgacttgttgacaatttgggcactgagaaacaaactctgctatgtcctttttcatgtcatcccaccaatataagcatctgaggtcatgatacatttttgttgaccctgtgtgaatagaataacgggcagagtgtgcctctcccataactTGCCGTCATAGCCCCGCAGTATtgggtacacacaatctgctttcatatcgtaacactccATCAGGTGTAAtcttaaatggggtcttttccttttgaagagctgcatctctatactgtgccagaatagggtctttgtattggtgtctctttacctcatctatgattgaggactcagcaacctctcgaatagaaactccactatcttccgaattagctagacggactccaaggctggatagctgctgaatctcccgaaccatatCCCTCCTTTCTGGTTGTAAATCTATCAAGCTACCCATGAACTTACGGCTAAGAGCATCtactacaacattcgctttccctggatgatataaaatatcaacatcataatcctttagcaactctaaccattgcctctgtcgtaagttcagctctttctatttaaagatatattggagactcttatgatctgtatagatgtccacatggataccatataaataatgtctccatatcttcaaggcatgaaccacgaccgccaactccagatcgtgagtaggatagttcttttcatgcttcctaagttgtcgggagtcataggctataactttgccatgctgcatcaatacacatcctagcccaacacccgaagcatcacaataaataacatagccgtctggtcCCTCCGGAAGAGTTAGGACTGG

# header: >AEKE03003135.1 Solanum lycopersicum cultivar Heinz 1706 SL3.00SC0003140, whole genome shotgun sequence
# Sequence: CGATCCTAAGAAGATCGAGGCAGTTAGAGATTGGGTCAGACCTACTTCAGTTACTGAGATTCGGAGTTTCTTGGGCCTTGCAGGTTATTATCGAcggtttgttgagggtttctcatccattgcatctccattaactagattgacacaaaaggaggtgacttttcagtggtctgacgaatgtgaggttagtttccaaaagctcaagactttattgactactgctCCAATTTTGACCCTACCCTTGGAGGGaaagggttttgttgtatattgtgatgcttctcagattggtcttggttgtgtgttgatgcagaagggaagGGTGATatcttatgcttcgaggcagttaaaggttcatgagaagaactaccctattcatgatttagagttggcgtctgttgtgtttgcattaaagatttgGAGGAATTATCTTTATGGTAtgcattgtgaggtgttcacggatcatcgtagtctccagtatatattcaatcagagggatctcaatttgaggcagaggagatggttggagttgctcaaagactacgatatgactattctttatcacccaggcaaagcaaatgttgtagcaAATGCCTTGAGTCGGaaggcggtaagtatgggtagtctagccaTGTTACAGGTTGGCGAGCGTCCTTTAGCTAGGGATGTCCAATCCTTGgccaatagctttgtgagacttgatatttcagaatctggtaaggtgttggcttatatggaggctaggtcatccttgttggagcagattcgggctcaacagtttgatgatggtgatttatgtaagattagggacaaggttttaaaaggagaagccaaggcttcaattcttgatagtgagggagttttgaggattaagggtcatatatgtgttcctcgtacaggtgatttgactagattgatcatggaggaggctcatagttcgaggtactctattcatccgggggctactaagatgtatcgtgacttgaagcaacattattggtggtgccgtatgaagagggacatagtagattttgtatcccAGTGtctgaattgtcagcaagtgaagtatgaacaccaaaatcCTGGAGGTGTGACACAGAGGATGCCTatacctgagtggaagtgggagcgtattgctatggactttgtggtaggatTGCCATGTActttgggtaagtttgatgctatatgggtcattgtggatcgactgactaagtctgcacactttgtaccagttCAGACAACCTATAattcagagaagttagccaaaatctatattcgagagatagttcgtttgcatggggttcctatatctattatttcagatcgtggcacccaatttacatctcatttctggCGGTCTATGCAGAAGGAGTTGGGTACtcgggtggatcttagtacagctttccaccctcagactgatggtcagtcagagcggactattcaggttcttgaggacatgttgcgagcatgtgtgattgactttggtggtcacTGGGATCAGTTCTTGCCATTAGCGGaattttcttacaataatagttatcattccaGCATCgagatggcaccatttgaggttCTGTACggtaggagatgtcgatctccaattggctggtttgatgcatttgaggttagaccatggggtacagatttgttgagggagtctttggacaaggtcaagttgatccaagatagacttatcatggctcaaagcaggcaaaagagTTACGCAGATAGGAAAGTTCGtgatttggagtttatggttggagagagggttctacttaaggtttcacccatgaagggtgtgatgagatttggaaagaagggaaagttgagtccaaggtacattggtcctttCGAGGTTGTGGAGAGTATTGGTGAGGTGGCATATCAGTTGGCTTTGCCACCTGGGTTGTCAGGTGtccatcctgtatttcatatttcaatgcttaagaagtatcatcagggtggtgatcatgtgattcaatgggattcagtgttacttga

# header: >AEKE03003136.1 Solanum lycopersicum cultivar Heinz 1706 SL3.00SC0003141, whole genome shotgun sequence
# Sequence: aagggaagggtatgtgtaccccgcgtcgatgatttgatcaacattattctgacagaggctcatagttcaaggtattctatacatccgggtgcaaccaagatgtatcgtgacctaaaacaacactttcggtggagtagaatgaagcgtgacattgtggattttattgccaaatgtccaaactgtcaacaagtaaagtatgaacaccaaaggcccggaggaacacttcagagaatgcccattccggaatggaagtgggaaagaattgcaatggactttgtggttggtcttccaaggacaatgggtaagtatgactccatttgggtgattgttgataggttaactaaatctgctcatttcattccgatgaaggtgacttacaatgcagaaaagttagccaaactttacatctcggaagtggtgtgattgcatggggttccactatccatcatatcatatagaggtatgcagtttacttctatgttttggaaaacattgcatgcagaattgggtactaggttggaccttagtactgcgttccatcctcagaccgatggtcagtctgagcgaatgattcaagtgttggaggatatgcttcgtgtgtgtgtgatagagtttggtggtcattgggataacttcctacccttagcggagtttttatacaataatagctatcactcaagcattgacaTGACTCCATtcgaagccttgtatggtaggagatgtaggtctcccattggttggtttgatgcatttgaggttaggccttggggtactgaccttttgagagattcgatagagaaagtgaagtctattcaagaaaagcttctagcggtgcaaagtagacaaaaagaatatgcagatcgaaatgTTAGGGACATAGAGTTCATGAAAGGTGAACATGTCTTGTtaaaggtttcgcccatgaaaggggtgatgcggttcggaAAAAGgtgtaaactaagtccaaggtacattggaccatttgaagtacttaagcgagtatgAGAGGTGGCTTATAAGCTAGCCTTGCCTctagggctgtccggagtacaccggtattccatgtgtcgatgttgaaaagataccatggggatgggaatTACATTATCCgatgggattcagttttgcttgatgggacttgtcttatgaggaggagcctgttgctattttagatagagaagttcgcaagttgaggtcaagagagattgcgtccatcaaggtgcaatggaagaatcgaccggttgaagaagccacttgggagaaggaggcggatatgcaagaaaaatacccacatctgtttacagattcaggtactccttctcgcccttgttttccttcttttgatcattcggggacgaacgatgggtaaattggtatctaatgtaatgacccgtttagtcgtcttgagcaacagacttcaattctggaaaaactggcagaagcgatggaccccacgacggaccgtcaagggcacgacggaccgtcgcagggtctcgtttcaaaacacttagaaaatctgaaattgggtactgaaaattgactctctgaacttcgtgactgaatggcaggacggaccgtcacggagacttcagtgaaaatccattctctgaactttgcgatgacctgcaggacggaccgtcgcagacacgacggcccgtcacaggttgcgcaaatcccaggcagaattggatttccttacacgttttaagggacgtttttggactattctttccttaattatagatttcgtgggtttatattaataactcaaattcttgggggttaaaagaggtaaccctaagttaattagtggggtattattgccatcttttattcttaattatatactaattagggtaaaagaaagagggtttgaataagaaaataagaaagaacaaaaagagacagaaaaaggAATAGAAAGAGTAGAAagagagggaaacgaagaggatagcaagggttctgagaagatagcttgttgatttcaattcttcggtgga

######################################################################
######################################################################

import allel
# import numpy as np
import pandas as pd
#import fastaparser

# .vcf file >>> SNPs location info:
#filepath = '/media/alina/ESD-USB/test_vcf/test_1.vcf.gz'
filepath = '/media/hernan/Pen/Genome/20219-tomato-snps.vcf.gz'

# extract data from .vcf and store it in a pd.dataframe:
raw_df = allel.vcf_to_dataframe(filepath, fields='*')

#raw_df.head() # REMOVE THIS
#raw_df.columns # REMOVE THIS

sub_df = raw_df[['CHROM', 'POS', 'REF', 'ALT_1', 'is_snp']] # I added 'is_snp' to this new df

sub_df_filepath = '/home/hernan/Desktop/sub_df.csv'
sub_df.to_csv(path_or_buf=sub_df_filepath, index=False)

######################################################################
######################################################################

# this is fro the old .vcf, who knows what was in there!!!
data = pd.read_csv('sub_df_old.csv') # len(data) : 1318305


#data.loc[0, 'REF'] # >>> THERE'S A 182 str HERE ?????
#data['REF'] # to access all ref SNPs 
#data['POS'] # to access all positions of interest
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




