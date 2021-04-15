#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:37:58 2021

@author: alina
"""

import allel
import pandas as pd
import os

def extract_data_from_vcf(filepath):
    '''
    Extracts data from .vcf file, stores it in a pd.dataframe and
    returns the dataframe.
    '''
    return allel.vcf_to_dataframe(filepath, fields='*')

def create_working_dataframe(raw_df):
    '''
    Takes a pandas.dataframe with the raw data from the .vcf file,
    creates a sub-dataframe with columns: 'CHROM', 'POS', 'REF', 'ALT_1', 'is_snp',
    saves this sub-dataframe to a .csv file, and
    returns a dataframe from the .csv to continue working with.
    '''
    # create subdf with columns of interest only
    sub_df = raw_df[['CHROM', 'POS', 'REF', 'ALT_1', 'is_snp']]
    
    # save sub_df as .csv
    cwd = os.getcwd()
    sub_df_filepath = cwd + '/sub_df.csv'
    sub_df.to_csv(path_or_buf=sub_df_filepath, index=False)
    
    return sub_df

if __name__ == "__main__":
    filepath = input("Please enter the absolute filepath to the .vcf file: ")
    raw_df = extract_data_from_vcf(filepath)
    data = create_working_dataframe(raw_df)
    print("All data from columns\n\t'CHROM', \n\t'POS', \n\t'REF', \n\t'ALT_1', \n\t'is_snp' \n from the .vcf file provided is now available as a .csv file,")
    print("'sub_df.csv', located in the current working directory.")
   