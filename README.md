# vcf_flanking_sequence_finder
Extract data from .vcf, find SNPs in genomic .fasta file and return each SNP with its flanking sequences.

WIP:

open .vcf file >>> extract 4 columns ['chomosome', 'position', 'ref snp', 'alt snp'] ONLY for snps (No deletions, insertions, etc.)

open genome.fasta >>> read with Biopython SimpleFastaParser

for snp in .vcf_df:
  find in genome DONE
  get 5'- + 3'- flanking sequences DONE
  create a result_str = 5'-flanking[REF/ALT]'3-flanking (50bp on each side) DONE 
  append to final_df (['chomosome', 'position', 'ref snp', 'alt snp', 5'-flanking[REF/ALT]'3-flanking]) DONE
