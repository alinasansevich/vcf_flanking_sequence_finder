# vcf_flanking_sequence_finder

The program extracts several columns ('Chromosome ID', 'Position', 'REF_SNP', 'ALT_SNP', 'is_snp') from a .vcf file (Variant Call Format). It parses a genomic fasta file, searches for SNPs from the .vcf and returns each SNP with its flanking sequences (50 nucleotides on each side).

It is run from the command line, it informs the user how much memory is needed to save the results and if that memory is available or not.
