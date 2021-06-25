#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:21:33 2021

@author: alina
"""

# import allel >>> imported in from_vcf_to_df
# import pandas as pd >>> imported in from_vcf_to_df

import from_vcf_to_df as vcf_df # import module
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


# @@@@@@@@ LATER: ASK FOR USER INPUT TO GET THE filepath TO THE .vcf
# filepath = input()
# @@@@@@@@ LATER: REMOVE THE NEXT LINE
filepath = '/media/alina/Pen/Genome/20219-tomato-snps.vcf.gz'


raw_df = vcf_df.extract_data_from_vcf(filepath)
data = vcf_df.create_working_dataframe(raw_df)   ##### data IS HERE!!!

# REMOVE THIS? would removing it release memory?
# del raw_df <<<<<<<<<<<<<<<<< ???

genome_filepath = '/media/hernan/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'

data = pd.read_csv('sub_df.csv')    ##### data IS ALSO HERE!!!

# @@@@@@@@ LATER:
### give the user the option of starting from the .vcf or from the .csv 'sub_df.csv'


flanking_seqs = []
chrom_id = []
pos = []
ref = []
alt = []
is_snp = []

### THIS VERSION OF THE PROGRAM GETS ALL FLANKING SEQUENCES,
### WITHOUT CHECKING IF THEY ARE VALID SNPs OR NOT >>>>>> CHECK THIS LATER

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