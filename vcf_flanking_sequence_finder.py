#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:21:33 2021

@author: alina
"""

# import allel >>> imported in from_vcf_to_df
# import pandas as pd >>> imported in from_vcf_to_df
import fastaparser

import from_vcf_to_df as vcf_df # import module



# .vcf file >>> SNPs location info:   @@@@@@@@@@@@@@@ DELETE LATER
# @@@@@@@@ LATER: ASK FOR USER INPUT TO GET THE filepath TO THE .vcf
filepath = '/media/alina/Pen/Genome/20219-tomato-snps.vcf.gz'

# @@@@@@@@ LATER: ASK FOR USER INPUT TO GET THE filepath TO THE .vcf
# filepath = input()

raw_df = vcf_df.extract_data_from_vcf(filepath)
data = vcf_df.create_working_dataframe(raw_df)

# REMOVE THIS? would removing it release memory?
# del raw_df <<<<<<<<<<<<<<<<<

























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

seq = seq.sequence_as_string() # this line needs to change, it only works with fastaparser
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

### extras:

### check memory availavility:
    ### https://pypi.org/project/psutil/
    ### https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
    
### CLI arguments:
    ### https://www.tutorialspoint.com/python/python_command_line_arguments.htm

### numpy broadcast? vectorization?:
    ### https://stackoverflow.com/questions/5197650/broadcasting-a-python-function-on-to-numpy-arrays
    ### https://www.experfy.com/blog/bigdata-cloud/why-you-should-forget-loops-and-embrace-vectorization-for-data-science/
