#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:08:46 2021

@author: alina

Resources:
    https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python
    
    https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python


    https://stackoverflow.com/questions/2365100/converting-bytes-to-megabytes
    
    megabytes=bytes/1000000
    megabytes=bytes/1024/1024
    megabytes=bytes/1024/1000
    
    
    
    https://stackoverflow.com/questions/1704458/get-uncompressed-size-of-a-gz-file-in-python/22348071
    https://stackoverflow.com/questions/24332295/how-to-determine-the-content-length-of-a-gzipped-file-in-python
    
    
    https://superuser.com/questions/619591/how-can-i-get-the-uncompressed-size-of-gzip-file-without-actually-decompressing/619659
    
    
    https://stackoverflow.com/questions/2712173/check-the-total-content-size-of-a-tar-gz-file
    https://unix.stackexchange.com/questions/183465/fastest-way-of-working-out-uncompressed-size-of-large-gzipped-file
    https://unix.stackexchange.com/questions/472013/uncompressed-file-estimation-wrong




"""

# I need to check 2 things now:
    # 1- the size of the .vcf file that contains the SNPs data
    # (and estimate how big it would be after extracting it)
    
    # 2- the available memory to inform the user and ask if they want to continue

############# # 1 - check file size:

from pathlib import Path

### REMOVE THIS LATER ###
# # for 1024 multiplier
# def get_human_readable(size, precision=2):
#     suffixes=['B','KB','MB','GB','TB']
#     suffixIndex = 0
#     while size >= 1024 and suffixIndex < len(suffixes):
#         suffixIndex += 1 # increment the index of the suffix
#         size = size/1024.0 # apply the division
#     return "%.*f%s"%(precision, size, suffixes[suffixIndex])

# get_human_readable(info.st_size)


# for 1000 multiplier >>> USE THIS ONE
units = {1000: ['KB', 'MB', 'GB'],
         1024: ['KiB', 'MiB', 'GiB']}

def approximate_size(size, flag_1024_or_1000=True):
    mult = 1024 if flag_1024_or_1000 else 1000
    for unit in units[mult]:
        size = size / mult
        if size < mult:
            return '{0:.2f} {1}'.format(size, unit)

filepath = input("Please enter the file's path XXXXXX: ")
info = Path(filepath).stat()

approximate_size(info, False)


# $$$$$$$$$$$$$$$$$$$ BASH $$$$$$$$$$$$$$$$$$$

# (base) alina@Mini:/media/alina/Pen/Genome$ time zcat 20219-tomato-snps.vcf.gz | wc -c
# 23967925790

# real	3m16.538s
# user	2m34.459s
# sys	0m28.921s

# Real Time is the actual, real world, time that the step takes to run and will be the same as if you timed it with a stopwatch 
# (not possible as you won't know the precise moment the step starts and stops).
# CPU Time is the amount of time the step utilises CPU resources.

# With this command I have the file's uncompressed size, now I can inform the user about how much space they'll need
# to extract it, if they choose to do so

# $$$$$$$$$$$$$$$$$$$ BASH $$$$$$$$$$$$$$$$$$$




### ### ### To Do: ### ### ###

# Now, how to run this on Python? >>> learn the subprocess module:
    # https://janakiev.com/blog/python-shell-commands/
    # https://docs.python.org/3/library/subprocess.html#module-subprocess
    # https://docs.python.org/3/library/subprocess.html#subprocess-replacements


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

############# # 2 - check available memory:

# https://stackoverflow.com/questions/11615591/available-and-used-system-memory-in-python
# https://github.com/giampaolo/psutil
# https://psutil.readthedocs.io/en/latest/

import psutil
psutil.virtual_memory() # it returns a named tuple
# Out[9]: svmem(total=3951124480, available=616099840, percent=84.4, used=2691055616, free=187158528, active=2572746752, inactive=936222720, buffers=106459136, cached=966451200, shared=400666624, slab=120938496)

# total=3951124480
approximate_size(3951124480)

# available=616099840 >>> this is the one I need (https://psutil.readthedocs.io/en/latest/index.html?highlight=virtual_memory()#psutil.virtual_memory)
approximate_size(616099840)

available_memory = psutil.virtual_memory()[1]

### I'm here:
    
    # write a function to compare the available memory with the space needed 
    # to extract the SNPs and create the dataframe
    
    # Inform the user and let them decide if they want to continue



    























##### ##### ##### testing "approximate_size":

# 1.1 kB
small = '/home/alina/Learning_to_Code/My_Projects/vcf/LICENSE.txt'
# 1.8 MB
medium = '/home/alina/Learning_to_Code/PowerfulPython.pdf'
# 2.7 MB
medium2 = '/media/alina/MiniBackUp/BOOKS_n_other_resources/byte_of_python.pdf'
# 40.4 MB
big = '/media/alina/MiniBackUp/BOOKS_n_other_resources/eBOOK_Biological_Data_Exploration/Biological data exploration with Python pandas and seaborn.pdf'
# 86.7 MB
big_zip = '/media/alina/MiniBackUp/BOOKS_n_other_resources/eBOOK_Biological_Data_Exploration/Biological_data_exploration_ebook.zip'
# 838.4 MB
bigger = '/media/alina/Pen/Genome/GCA_000188115.3_SL3.0_genomic.fna'
# 4.3 GB
very_big = '/media/alina/Pen/Genome/20219-tomato-snps.vcf.gz'


# very_big: 23967925790   >>> zcat 20219-tomato-snps.vcf.gz | wc -c

approximate_size(23967925790, False)
# Out[7]: '23.97 GB' >>> uncompressed file

approximate_size(4289010456, False)
# Out[8]: '4.29 GB'  >>> compressed file



print('LICENSE.txt')
print(approximate_size(Path(small).stat().st_size, False))
print('PowerfulPython.pdf')
print(approximate_size(Path(medium).stat().st_size, False))
print('byte_of_python.pdf')
print(approximate_size(Path(medium2).stat().st_size, False))
print('eBOOK_Biological_Data_Exploration/Biological data exploration with Python pandas and seaborn.pdf')
print(approximate_size(Path(big).stat().st_size, False))
print('Biological_data_exploration_ebook.zip')
print(approximate_size(Path(big_zip).stat().st_size, False))
print('GCA_000188115.3_SL3.0_genomic.fna')
print(approximate_size(Path(bigger).stat().st_size, False))
print('20219-tomato-snps.vcf.gz')
print(approximate_size(Path(very_big).stat().st_size, False))

##### ##### ##### end tests







