# vcf_flanking_sequence_finder

## Overview
[A VCF file][1] is a text file used in bioinformatics to store information about variant genetic sequences. It contains metadata that describes the file's format, source, created on date, and reference genome, and it contains column-formatted genetic sequencing data. VCF files are used as part of large-scale genotyping and DNA sequencing projects.

This format allows the user to catalog variants of a genome without recording those variants' genetic data in their entirety. Instead, one default reference copy of the genome is saved in a .FASTA or another file, and then the genome's variants are described in a VCF file. This allows the user to quickly review and analyze genetic variants, without sifting through redundant data.

.vcf files are usually very large, so accessing them and working with the information they store has high memory usage, which can make your computer become sluggish or even crash. This means that finding every SNP with its flanking sequences in the reference genome to design primers for it can be pretty complicated, time consuming or even impossible due to a lack of memory. _This problem is what inspired this project._ 

[1]: https://fileinfo.com/extension/vcf
***

## Table of contents
- [vcf_flanking_sequence_finder](#vcf_flanking_sequence_finder)
- [Overview](#overview)
- [Table of contents](#table-of-contents)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description
[(Back to top)](#table-of-contents)
_What is the project?_ The program extracts several columns ('Chromosome ID', 'Position', 'REF_SNP', 'ALT_SNP', 'is_snp') from a .vcf file (Variant Call Format). It parses a genomic .fasta file, finds the SNPs and returns each SNP with its flanking sequences (50 nucleotides on each side). It is run from the command line, it informs the user how much memory is needed to save the results and if that memory is available or not.

_What is the Minimal Viable Product (MVP)?_ A program that extracts data from the .vcf file, finds the SNPs in the genome and returns them with their flanking sequences.

_What are the Nice-to-Haves?_ Check memory available before running. Check that the SNP found at 'REF' is the same as the one found in that position in the genome. Check if the ALT sequence is actually a SNP.

_When will the project be complete?_ The project will be complete once all the MVP and Nice-to_Haves features have been implemented.
***

## Installation
[(Back to top)](#table-of-contents)
If your project is software or an app that needs installation, you should include the steps required to install your project. Provide a step-by-step description of how to get the development environment running.
***

## Usage
[(Back to top)](#table-of-contents)
Provide instructions and examples so users/contributors can use the project. This will make it easy for them in case they encounter a problem – they will always have a place of reference.
You can also include screenshots to show examples of the running project.
***

## License
[(Back to top)](#table-of-contents)

This repository contains content developed by Alina Sansevich and is distributed under the MIT license.<br>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
***
