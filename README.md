# vcf_flanking_sequence_finder

The program extracts several columns ('Chromosome ID', 'Position', 'REF_SNP', 'ALT_SNP', 'is_snp') from a .vcf file (Variant Call Format). It parses a genomic fasta file, searches for SNPs from the .vcf and returns each SNP with its flanking sequences (50 nucleotides on each side).

It is run from the command line, it informs the user how much memory is needed to save the results and if that memory is available or not.

*********



[A VCF file][1] is a text file used in bioinformatics to store information about variant genetic sequences. It contains metadata that describes the file's format, source, created on date, and reference genome, and it contains column-formatted genetic sequencing data. VCF files are used as part of large-scale genotyping and DNA sequencing projects, such as the 1000 Genomes Project.

To streamline the storage of variant genetic information, the 1000 Genomes Project created the Variant Call Format (VCF). This format allows bioinformaticians to catalog variants of a genome without recording those variants' genetic data in their entirety. Instead, bioinformaticians save one default reference copy of the genome in a .FASTA or another file, and then they describe the genome's variants in a VCF file. This allows bioinformaticians to quickly review and analyze genetic variants, without sifting through redundant data.

(include/remove this?)
In its header, the VCF file describes its own file format, created on date, source, and other relevant metadata. The most important piece of metadata is the VCF file's ##reference, which describes where the VCF file's reference genome is stored.

In its body, the VCF file contains variant genetic sequencing data that is separated into eight mandatory columns, including:

    CHROM: The name of the sequence on which the variation is being called
    POS: The 1-based position of the variation on the given sequence
    ID: The identifier of the variation or . if the identifier is unknown
    REF: The reference base at the given position on the reference sequence
    ALT: This list of alternative alleles at this position
    QUAL: A quality score associated with the inference of the given alleles
    FILTER: A flag indicating which of a given set of filters the variation has passed
    INFO: An extensible list of key-value pairs describing the variation

Some VCF files may contain additional columns of data, including FORMAT and SAMPLE.


[1]: https://fileinfo.com/extension/vcf
