#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:21:33 2021

@author: alina
"""

import allel
import numpy as np
import pandas as pd
import fastaparser

# .vcf file >>> SNPs location info:
filepath = '/media/alina/ESD-USB/test_vcf/test_1.vcf.gz'

# extract data from .vcf and store it in a pd.dataframe:
raw_df = allel.vcf_to_dataframe(filepath, fields='*')

raw_df.head() # REMOVE THIS

raw_df.columns # REMOVE THIS
# Out[3]: 
# Index(['CHROM', 'POS', 'ID', 'REF', 'ALT_1', 'ALT_2', 'ALT_3', 'QUAL', 'AC_1',
#        'AC_2', 'AC_3', 'AF_1', 'AF_2', 'AF_3', 'AN', 'DB', 'DP', 'END', 'FS',
#        'MQ', 'MQRankSum', 'QD', 'ReadPosRankSum', 'SOR', 'FILTER_PASS',
#        'FILTER_DRAGENSnpHardQUAL', 'FILTER_DRAGENIndelHardQUAL',
#        'FILTER_LowDepth', 'FILTER_PloidyConflict', 'FILTER_RMxNRepeatRegion',
#        'numalt', 'altlen_1', 'altlen_2', 'altlen_3', 'is_snp'],
#       dtype='object')

# extract target columns: 'CHROM', 'POS', 'REF', 'ALT_1' #### 'ALT_2', 'ALT_3'???
sub_df = raw_df[['CHROM', 'POS', 'REF', 'ALT_1']]

del raw_df # REMOVE THIS? would removing it release memory?

# I create a .csv to continue developing without collapsing my laptop's memory ####### # REMOVE THIS?
sub_df_filepath = '/home/alina/Learning_to_Code/My_Projects/vcf/sub_df.csv'
sub_df.to_csv(path_or_buf=sub_df_filepath, index=False)

data = pd.read_csv('sub_df.csv') # len(data) : 1318305


data.loc[0, 'REF'] # >>> THERE'S A 182 str HERE ?????
data['REF'] # to access all ref SNPs 
data['POS'] # to access all positions of interest

data.head(10)
# Out[6]: 
#         CHROM   POS                                                REF ALT_1
# 0  CM001064.3    58  TTTCGACGATTTTCGTGTGCTATAGCACACCATTTTTTGGGTGATC...     T
# 1  CM001064.3   303                                                  A    AT
# 2  CM001064.3   331                                                  A   AAT
# 3  CM001064.3   923                                                  C    CA
# 4  CM001064.3  2001                                                  A    AT
# 5  CM001064.3  2063                                                  G    GA
# 6  CM001064.3  6838                                                  T   TAA
# 7  CM001064.3  6903                                                  C    CT
# 8  CM001064.3  7632                                                  A    AT
# 9  CM001064.3  9403                                                  C    CA

# access fasta file with genome data
genome_filepath = '/media/alina/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

# the following code is from:  https://pypi.org/project/fastaparser/

with open(genome_filepath) as fasta_file:
    parser = fastaparser.Reader(fasta_file) # Reader object contains all sequences
    for seq in parser:
        # seq is a FastaSequence object https://fastaparser.readthedocs.io/en/latest/api_fastasequence/
        print('ID:', seq.id)
        print('Description:', seq.description)
        print('Sequence:', seq.sequence_as_string())
        print()

# this restarts my kernel...
# [SpyderKernelApp] WARNING | No such comm: 13f65b6e996911eba94ca763352cc9e7
# from Stack Overflow:
    # https://stackoverflow.com/questions/62980313/spyderkernelapp-warning-no-such-comm
# I'm moving this part of the code to the playground to run it from the terminal
# I'M HERE!!!

######################################################################
######################################################################

### for each SNP:
    ### get SNP's position from vcf_df
    ### find SNP in chromosome in .fna file
    ### find 5-flank-seq and 3-flank-seq and store them in dict: (50pb each)
        ### k:v {SNP-POS:{5f: seq}}
        ##### after searching all SNPs in the fasta file, 
        ##### I should have a dict like this: (Do I really need this dict?)
        ##### or maybe a df?
            
            # snp_flanks_dict = {'SNP_ID 1/ POS': {'SNP-5': "5' flanking seq  as str",
            #                                     'SNP-3': "3' flanking seq  as str"},
            #                    'SNP_ID 2/ POS': {'SNP-5': "5' flanking seq  as str",
            #                                     'SNP-3': "3' flanking seq  as str"},
            #                    'SNP_ID 3/ POS': {'SNP-5': "5' flanking seq  as str",
            #                                     'SNP-3': "3' flanking seq  as str"}
            #                    }
            
            # snp_flanks_df:
                # 6 columns:
                # CHROM - POS - 5' flanking seq  as str - REF - ALT - 3' flanking seq  as str
                
            # then I could create pd.final_df
                
### create pd.final_df, 3 columns: CHROM, SNP_POS, 5'-FlankSeq[A/G]3'-FlankSeq as a single str  

######

### REORGANIZE THE DIFFERENT STEPS IN DIFFERENT MODULES:
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

# Here I'm developing the function to find the flanking sequences,
# 50 bp each side, NNNNNNNNNNNNNNN[ref_SNP/alt_SNP]NNNNNNNNNNNNNNN

# at4g37870_fasta
fasta_filepath = '/home/alina/Learning_to_Code/My_Projects/vcf/at4g37870.fna'

with open(fasta_filepath) as fasta_file:    # code from:
    parser = fastaparser.Reader(fasta_file) # https://pypi.org/project/fastaparser/
    for seq in parser:
        # seq is a FastaSequence object
        print('ID:', seq.id)
        print('Description:', seq.description)
        print('Sequence:', seq.sequence_as_string())
        print()

seq = seq.sequence_as_string()
len(seq) # 2583
ref_snp = seq[150] # 'T' >>> I will use this as my ref SNP
ref_pos = 150
alt_snp = 'N'
flanking_5 = seq[(ref_pos - 50):ref_pos]
flanking_3 = seq[(ref_pos + 1): ref_pos + 51]
# this is what the result string should look like:
result_str = 'CGGTTCATTATTAACCATGGTTCTAAAAATCTAACCTTTAAAAAACCACT[T/N]TCGCTTCTCTTCACATTCGCATCATTTTGTATCATCCCTTGAAAACGTTA'


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

x = assemble_result_str(ref_snp, alt_snp, flanking_5, flanking_3)

result_str == x # True

























######################################################################
######################################################################

# this was my first try, REMOVE LATER:

raw_data = allel.read_vcf(filepath)

sorted(raw_data.keys())
# ['calldata/GT',
#  'samples',
#  'variants/ALT',
#  'variants/CHROM',
#  'variants/FILTER_PASS',
#  'variants/ID',
#  'variants/POS',
#  'variants/QUAL',
#  'variants/REF']

raw_data['samples'] # len(raw_data['samples']) # 47
# array(['20218Adv_SL01', '20218Adv_SL02', '20218Adv_SL03', '20218Adv_SL04',
#        '20218Adv_SL05', '20218Adv_SL06', '20218Adv_SL07', '20218Adv_SL08',
#        '20218Adv_SL09', '20218Adv_SL10', '20218Adv_SL11', '20218Adv_SL12',
#        '20218Adv_SL13', '20218Adv_SL14', '20218Adv_SL15', '20218Adv_SL16',
#        '20218Adv_SL17', '20218Adv_SL18', '20218Adv_SL19', '20218Adv_SL20',
#        '20218Adv_SL21', '20218Adv_SL22', '20218Adv_SL23', '20218Adv_SL24',
#        '20218Adv_SL25', '20218Adv_SL26', '20218Adv_SL27', '20218Adv_SL28',
#        '20218Adv_SL29', '20218Adv_SL30', '20218Adv_SL31', '20218Adv_SL32',
#        '20218Adv_SL33', '20218Adv_SL34', '20218Adv_SL35', '20218Adv_SL36',
#        '20218Adv_SL37', '20218Adv_SL38', '20218Adv_SL39', '20218Adv_SL40',
#        '20218Adv_SL41', '20218Adv_SL42', '20218Adv_SL43', '20218Adv_SL44',
#        '20218Adv_SL45', '20218Adv_SL46', '20218Adv_SL47'], dtype=object)

chrom = raw_data['variants/CHROM']
pos = raw_data['variants/POS']
ref = raw_data['variants/REF']
alt = raw_data['variants/ALT']

del raw_data


df = pd.DataFrame({'chrom': chrom, 'pos': pos, 'ref': ref, 'alt': alt})








### extras:

### check memory availavility:
    ### https://pypi.org/project/psutil/
    ### https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
    
### CLI arguments:
    ### https://www.tutorialspoint.com/python/python_command_line_arguments.htm

### to deal with the fastaparser deprecation warning:
    ### https://stackoverflow.com/questions/54379418/how-to-assuredly-suppress-a-deprecationwarning-in-python

### numpy broadcast? vectorization?:
    ### https://stackoverflow.com/questions/5197650/broadcasting-a-python-function-on-to-numpy-arrays
    ### https://www.experfy.com/blog/bigdata-cloud/why-you-should-forget-loops-and-embrace-vectorization-for-data-science/
