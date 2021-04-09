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
        # seq is a FastaSequence object https://fastaparser.readthedocs.io/en/latest/api_fastasequence/
        print('header:', seq.header)
        #print('Description:', seq.description)
        print('Sequence:', seq.sequence)
        print()
