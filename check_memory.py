#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:08:46 2021

@author: alina

Resources:
    https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python
    
    https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python


    megabytes=bytes/1000000
    megabytes=bytes/1024/1024
    megabytes=bytes/1024/1000
    
    https://stackoverflow.com/questions/2365100/converting-bytes-to-megabytes



"""

# I need to check 2 things now:
    # 1- the size of the .vcf file that contains the SNPs data
    # (and estimate how big it would be after extracting it)
    
    # 2- the available memory to inform the user and ask if they want to continue

# Start with # 1 - check file size:
    
from pathlib import Path

filepath = input("Please enter the file's path XXXXXX: ")


info = Path(filepath).stat()

# for 1024 multiplier
def get_human_readable(size, precision=2):
    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size >= 1024 and suffixIndex < len(suffixes):
        suffixIndex += 1 # increment the index of the suffix
        size = size/1024.0 # apply the division
    return "%.*f%s"%(precision, size, suffixes[suffixIndex])

get_human_readable(info.st_size)


# for 1000 multiplier
UNITS = {1000: ['KB', 'MB', 'GB'],
         1024: ['KiB', 'MiB', 'GiB']}

def approximate_size(size, flag_1024_or_1000=True):
    mult = 1024 if flag_1024_or_1000 else 1000
    for unit in UNITS[mult]:
        size = size / mult
        if size < mult:
            return '{0:.2f} {1}'.format(size, unit)

approximate_size(2123, False)






# testing:

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


##### I'm here, test this function and continue with number 2!