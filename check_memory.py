#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:08:46 2021

@author: alina

Resources:
    https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python
    
    https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
"""

# I need to check 2 things now:
    # 1- the size of the .vcf file that contains the SNPs data
    # (and estimate how big it would be after extracting it)
    
    # 2- the available memory to inform the user and ask if they want to continue

# Start with # 1 - check file size:
    
from pathlib import Path

filepath = input("Please enter the file's path XXXXXX: ")

small = '/home/alina/Learning_to_Code/My_Projects/vcf/LICENSE.txt'

big = '/home/alina/Learning_to_Code/My_Projects/vcf/vcf_sample_2.vcf'

info = Path(filepath).stat()


def get_human_readable(size, precision=2):
    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size >= 1024 and suffixIndex < len(suffixes):
        suffixIndex += 1 # increment the index of the suffix
        size = size/1024.0 # apply the division
    return "%.*f%s"%(precision, size, suffixes[suffixIndex])

get_human_readable(info.st_size)

##### I'm here, test this function and continue with number 2!