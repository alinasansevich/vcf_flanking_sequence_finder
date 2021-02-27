#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:21:33 2021

@author: alina
"""

import allel
import numpy as np
import pandas as pd

# .vcf file >>> SNPs location info:
filepath = '/media/alina/ESD-USB/test_vcf/test_1.vcf.gz'

# extract data from .vcf and store it in a pd.df:
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

del raw_df # REMOVE THIS?

# I create a .csv to continue developing without collapsing my laptop's memory
####### # REMOVE THIS

sub_df_filepath = '/home/alina/Learning_to_Code/My_Projects/vcf/sub_df.csv'
sub_df.to_csv(path_or_buf=sub_df_filepath, index=False)

data = pd.read_csv('sub_df.csv') # len(data) : 1318305

### NEXT: access fasta file with genome data





### check memory availavility:
    ### https://pypi.org/project/psutil/
    ### https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
    
### CLI arguments:
    ### https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    

### for each SNP:
    ### get SNP's position from vcf_df
    ### find SNP in chromosome in .fna file
    ### find 5-flank-seq and 3-flank-seq and store them in dict: (50pb each)
        ### k:v {SNP-POS:{5f: seq}}
        ##### after searching all SNPs in the fasta file, 
        ##### I should have a dict like this:
            
            # snp_flanks_dict = {'SNP_ID 1/ POS': {'SNP-5': "5' flanking seq  as str",
            #                                     'SNP-3': "3' flanking seq  as str"},
            #                    'SNP_ID 2/ POS': {'SNP-5': "5' flanking seq  as str",
            #                                     'SNP-3': "3' flanking seq  as str"},
            #                    'SNP_ID 3/ POS': {'SNP-5': "5' flanking seq  as str",
            #                                     'SNP-3': "3' flanking seq  as str"}
            #                    }

### create pd.df columns: CHROM, SNP_POS, 5'-FlankSeq[A/G]3'-FlankSeq as a single str  















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










