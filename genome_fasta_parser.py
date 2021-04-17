#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:13:52 2021

@author: alina
"""

import pandas as pd
import fastaparser

data = pd.read_csv('sub_df.csv') # do I need this line here?

genome_filepath = '/media/alina/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'
wip_filepath = '/home/alina/Learning_to_Code/My_Projects/vcf/PCK1.fna'
# the following code is from:  https://pypi.org/project/fastaparser/
# Reader object contains all sequences
# seq is a namedtuple('Fasta', ['header', 'sequence'])

count = 0
with open(wip_filepath) as fasta_file:
    parser = fastaparser.Reader(fasta_file, parse_method='quick')
    for seq in parser:
        count += 1
        # print('Header:', seq.header)
        # print('Sequence:', seq.sequence)
        # print('Header type:', type(seq.header))
        # print('Sequence type:', type(seq.sequence))
        print(seq)
        print()

print('There are {} sequences in this file'.format(count))

type(seq) # fastaparser.reader.Fasta
type(seq[0]) # str
type(seq[1]) # str
################################################




################################################


# def parse_fasta_file():
#     with open(wip_filepath) as fasta_file:
#         parser = fastaparser.Reader(fasta_file, parse_method='quick')
    
#     return parser

# parser = parse_fasta_file() # when I try to use it: TypeError: fasta_file must be opened for reading



# Out[1]: this is just a tiny slice of the complete result:
# header: >AEKE03003133.1 Solanum lycopersicum cultivar Heinz 1706 SL3.00SC0003138, whole genome shotgun sequence
# Sequence: attcttacccttagcagagttctcctacaacaatagctatcactcaagcattgatatggccccatttgaggaactatatgggagaaaatataggtctcccattgggtggtttgatgcatttgaagttagaccttggggcactgaccttctgagggaatcgttagataaagtgaaatctattcaagaaaagcttctagcggcgaaaagtagacagaaggagtacgcagatcggaaggttaaagacatggagtttatggagggtgaacaagtcttgttgaaggtttcgccaatgaaaggggtgatgcggtttgtaagcgaggtaaacttagcccaaggtatattggtccatttgaagtacttaagcgagtagaggaggtggcttatgagttagccttgcctccagcgctgtccggagtgcatccggtatttcatgtgtctatgttgaaaagataccatggggatggaaactacattatccgttgggattcagttttgcttgataaGAATTTGTCCTATGAGAAGGAGCCTGTTTCCATTTTAGGTAGAGAAGTTTGCAagtgaggtcaagagagattgcatccatcaaagttcaatggaggAATCGACCCGTCGAAGAAGctacttgggagaaagaggctgatatgcaagaaagatacccacacctgtttacagattcaggtactccttttcgccattgttttccttcttgttgtcattcggggacgaacgatgggtaaattggtatctattgtaacgacctgttttagccgttttgagcagcaaattttatttttggaaaactgACTGAGACGaaggaccccacgacggaccgtcatggactcgaCGAAACATCGCAgggtcttgtttcaaaacacttagaaaatatgataTTGGGTACTGAAagtcgactctctgaacttcgtgacggaatggcaggacggaccgtcacagagtcttcagtggaaatccagtctctgaaccttgcgatgacctgcaggacggaccatcgcaggcacgacgggccgtcacagattgcgtaatcccagtctgggtcggatttctttatacgttttaagggacgtttttgactattcctgctttaattataaagttagtgggtcaatattaataagtctaattacttggggtttAAAAGAAGTAACCTTAAGATAATTaatgggttattattgccatcttttattcttaattatatactaattagggtaaaagaaagagggtttgaataaagaaaatagaaagaacaaagagggagagaggattgatcgagagaggagaaacaaagaggaaaacacaaagcttttggaatttgcttgcttgatcactaatcttcggtggaggtaggttatggtttctcttacgatattcatagtaaactcttaatagcgaatgatatgtattgataatattgtaaaccctgctatgtgtttaattgtatgcttgcatgaatgtaattatataattgtgattatataagcatgatgaagttattgaatcccaaatcttgcaagaccctaatctcttgttaatgatgaggccttggtataaaaaaagaagtgatggactaaaataatgagattgatgatgccttggtaagaaagaaggcttgatgaattgatagaaggagattaagggatcaggtgtcacgaactgacacgtagatttaggggatcgggtgtcatgaaccgacacgtagatttaggggatcaggtgtcacgaaccgacacgtagatttaggggatcgggtgtcacgaatagacacatagatttaggggatcgggtgtcacgaaccgacacgtagatttaggggatcgggtgtcacgaactgacacgtagatttaggggatcgggtgtcacgaactgacacttagatttaggggatcggagtgtcacgttctgacacatagtagtaggggatcggagtgtcacgtaccgacacaagaggattgatgaatatgtgggagcggagtgtcacgtactgac

# header: >AEKE03003134.1 Solanum lycopersicum cultivar Heinz 1706 SL3.00SC0003139, whole genome shotgun sequence
# Sequence: TAATACTCATTATCTATGaatatagtcaagctaggaattgaattacctgcaggtacggggaacaagtaaggatacttattcttcatttcgtcttccgcttcccaagtcatatcctccctattgttattttgccacaacactttgagggaagccacatccttagtatgtaaccttctaacctgacgatcaagtatagccacgggtttctcctcatatgacaaaTCCTCTGTTACCTGAATATCATCTACAGGGAATGctctagaaggatcaccaatacatttacgtagcatcgatacatggaagactggatgtaccgcctccaaatcagatggtagatccaactcataggcaaccttgcctatcctacgaacaatctgataaggcccaatgtatctcagactgagcttccccttcctgtcgaatctcatcacacccctcatgggtgataccttcaagaatacccagtcaccaatatgaaactccaaatctcgacgccgattatctgcatatgacttctgtcgactctgggctgctaataatctttcttgaataagcttcaccttgtcaacaacttgctgaatcacatccgggcctattaacttagtctcgccaacatcaaaccaaccaataggtgatctgcacttcctcccatatatGGCCTCGTATggtgccatctggatactagaatggtagctattattattaggcaaactcaatgagcggcaagtggtcatcccaactgcctttgaagtcaataatacaggcccgcaacatatcttctagtgtctgaatagtacgctcagcctACCCATCAGTCTAAGGGTGAAATGctgtgctaaggttcacctatgtccccaatcccttctgaaatgatctccaaaagttggctgtaaattgagctcctctgtctgatataatggacgtgggaaccccatgaagtctcactatctccctgacatataacctcgcataatcttcagccgaataagtagtcctgactAGAAGAAAATAGGccgatttcgtcagcctatctacaataacccatatagagtcatacttccgttgagtgcaaggtaagcctgtaatgaagtccatattaatcatctcccattttcaagtcgggatctctatctcctgtaataatccaccaggcttttgatgttcgatcttgacttgttgacaatttgggcactgagaaacaaactctgctatgtcctttttcatgtcatcccaccaatataagcatctgaggtcatgatacatttttgttgaccctgtgtgaatagaataacgggcagagtgtgcctctcccataactTGCCGTCATAGCCCCGCAGTATtgggtacacacaatctgctttcatatcgtaacactccATCAGGTGTAAtcttaaatggggtcttttccttttgaagagctgcatctctatactgtgccagaatagggtctttgtattggtgtctctttacctcatctatgattgaggactcagcaacctctcgaatagaaactccactatcttccgaattagctagacggactccaaggctggatagctgctgaatctcccgaaccatatCCCTCCTTTCTGGTTGTAAATCTATCAAGCTACCCATGAACTTACGGCTAAGAGCATCtactacaacattcgctttccctggatgatataaaatatcaacatcataatcctttagcaactctaaccattgcctctgtcgtaagttcagctctttctatttaaagatatattggagactcttatgatctgtatagatgtccacatggataccatataaataatgtctccatatcttcaaggcatgaaccacgaccgccaactccagatcgtgagtaggatagttcttttcatgcttcctaagttgtcgggagtcataggctataactttgccatgctgcatcaatacacatcctagcccaacacccgaagcatcacaataaataacatagccgtctggtcCCTCCGGAAGAGTTAGGACTGG

# header: >AEKE03003135.1 Solanum lycopersicum cultivar Heinz 1706 SL3.00SC0003140, whole genome shotgun sequence
# Sequence: CGATCCTAAGAAGATCGAGGCAGTTAGAGATTGGGTCAGACCTACTTCAGTTACTGAGATTCGGAGTTTCTTGGGCCTTGCAGGTTATTATCGAcggtttgttgagggtttctcatccattgcatctccattaactagattgacacaaaaggaggtgacttttcagtggtctgacgaatgtgaggttagtttccaaaagctcaagactttattgactactgctCCAATTTTGACCCTACCCTTGGAGGGaaagggttttgttgtatattgtgatgcttctcagattggtcttggttgtgtgttgatgcagaagggaagGGTGATatcttatgcttcgaggcagttaaaggttcatgagaagaactaccctattcatgatttagagttggcgtctgttgtgtttgcattaaagatttgGAGGAATTATCTTTATGGTAtgcattgtgaggtgttcacggatcatcgtagtctccagtatatattcaatcagagggatctcaatttgaggcagaggagatggttggagttgctcaaagactacgatatgactattctttatcacccaggcaaagcaaatgttgtagcaAATGCCTTGAGTCGGaaggcggtaagtatgggtagtctagccaTGTTACAGGTTGGCGAGCGTCCTTTAGCTAGGGATGTCCAATCCTTGgccaatagctttgtgagacttgatatttcagaatctggtaaggtgttggcttatatggaggctaggtcatccttgttggagcagattcgggctcaacagtttgatgatggtgatttatgtaagattagggacaaggttttaaaaggagaagccaaggcttcaattcttgatagtgagggagttttgaggattaagggtcatatatgtgttcctcgtacaggtgatttgactagattgatcatggaggaggctcatagttcgaggtactctattcatccgggggctactaagatgtatcgtgacttgaagcaacattattggtggtgccgtatgaagagggacatagtagattttgtatcccAGTGtctgaattgtcagcaagtgaagtatgaacaccaaaatcCTGGAGGTGTGACACAGAGGATGCCTatacctgagtggaagtgggagcgtattgctatggactttgtggtaggatTGCCATGTActttgggtaagtttgatgctatatgggtcattgtggatcgactgactaagtctgcacactttgtaccagttCAGACAACCTATAattcagagaagttagccaaaatctatattcgagagatagttcgtttgcatggggttcctatatctattatttcagatcgtggcacccaatttacatctcatttctggCGGTCTATGCAGAAGGAGTTGGGTACtcgggtggatcttagtacagctttccaccctcagactgatggtcagtcagagcggactattcaggttcttgaggacatgttgcgagcatgtgtgattgactttggtggtcacTGGGATCAGTTCTTGCCATTAGCGGaattttcttacaataatagttatcattccaGCATCgagatggcaccatttgaggttCTGTACggtaggagatgtcgatctccaattggctggtttgatgcatttgaggttagaccatggggtacagatttgttgagggagtctttggacaaggtcaagttgatccaagatagacttatcatggctcaaagcaggcaaaagagTTACGCAGATAGGAAAGTTCGtgatttggagtttatggttggagagagggttctacttaaggtttcacccatgaagggtgtgatgagatttggaaagaagggaaagttgagtccaaggtacattggtcctttCGAGGTTGTGGAGAGTATTGGTGAGGTGGCATATCAGTTGGCTTTGCCACCTGGGTTGTCAGGTGtccatcctgtatttcatatttcaatgcttaagaagtatcatcagggtggtgatcatgtgattcaatgggattcagtgttacttga

# header: >AEKE03003136.1 Solanum lycopersicum cultivar Heinz 1706 SL3.00SC0003141, whole genome shotgun sequence
# Sequence: aagggaagggtatgtgtaccccgcgtcgatgatttgatcaacattattctgacagaggctcatagttcaaggtattctatacatccgggtgcaaccaagatgtatcgtgacctaaaacaacactttcggtggagtagaatgaagcgtgacattgtggattttattgccaaatgtccaaactgtcaacaagtaaagtatgaacaccaaaggcccggaggaacacttcagagaatgcccattccggaatggaagtgggaaagaattgcaatggactttgtggttggtcttccaaggacaatgggtaagtatgactccatttgggtgattgttgataggttaactaaatctgctcatttcattccgatgaaggtgacttacaatgcagaaaagttagccaaactttacatctcggaagtggtgtgattgcatggggttccactatccatcatatcatatagaggtatgcagtttacttctatgttttggaaaacattgcatgcagaattgggtactaggttggaccttagtactgcgttccatcctcagaccgatggtcagtctgagcgaatgattcaagtgttggaggatatgcttcgtgtgtgtgtgatagagtttggtggtcattgggataacttcctacccttagcggagtttttatacaataatagctatcactcaagcattgacaTGACTCCATtcgaagccttgtatggtaggagatgtaggtctcccattggttggtttgatgcatttgaggttaggccttggggtactgaccttttgagagattcgatagagaaagtgaagtctattcaagaaaagcttctagcggtgcaaagtagacaaaaagaatatgcagatcgaaatgTTAGGGACATAGAGTTCATGAAAGGTGAACATGTCTTGTtaaaggtttcgcccatgaaaggggtgatgcggttcggaAAAAGgtgtaaactaagtccaaggtacattggaccatttgaagtacttaagcgagtatgAGAGGTGGCTTATAAGCTAGCCTTGCCTctagggctgtccggagtacaccggtattccatgtgtcgatgttgaaaagataccatggggatgggaatTACATTATCCgatgggattcagttttgcttgatgggacttgtcttatgaggaggagcctgttgctattttagatagagaagttcgcaagttgaggtcaagagagattgcgtccatcaaggtgcaatggaagaatcgaccggttgaagaagccacttgggagaaggaggcggatatgcaagaaaaatacccacatctgtttacagattcaggtactccttctcgcccttgttttccttcttttgatcattcggggacgaacgatgggtaaattggtatctaatgtaatgacccgtttagtcgtcttgagcaacagacttcaattctggaaaaactggcagaagcgatggaccccacgacggaccgtcaagggcacgacggaccgtcgcagggtctcgtttcaaaacacttagaaaatctgaaattgggtactgaaaattgactctctgaacttcgtgactgaatggcaggacggaccgtcacggagacttcagtgaaaatccattctctgaactttgcgatgacctgcaggacggaccgtcgcagacacgacggcccgtcacaggttgcgcaaatcccaggcagaattggatttccttacacgttttaagggacgtttttggactattctttccttaattatagatttcgtgggtttatattaataactcaaattcttgggggttaaaagaggtaaccctaagttaattagtggggtattattgccatcttttattcttaattatatactaattagggtaaaagaaagagggtttgaataagaaaataagaaagaacaaaaagagacagaaaaaggAATAGAAAGAGTAGAAagagagggaaacgaagaggatagcaagggttctgagaagatagcttgttgatttcaattcttcggtgga
