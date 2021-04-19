#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:13:52 2021

@author: alina
"""

# the following code is from: https://biopython.org/docs/1.75/api/Bio.SeqIO.FastaIO.html

# these generator functions return tuples of strings:
    # from Bio.SeqIO.FastaIO import SimpleFastaParser
    # Iterate over Fasta records as string tuples.
    # For each record a tuple of two strings is returned, 
    # the FASTA title line (without the leading ‘>’ character), 
    # and the sequence (with any whitespace removed). The title line 
    # is not divided up into an identifier (the first word) and comment 
    # or description.
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

# Memory didn't even flinch
# Swap steady at 0
# almost 6 minutes for my MiniCompu




