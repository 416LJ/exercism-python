def to_rna(dna_strand):
    pairs = {"A":"U","T":"A","C":"G","G":"C"}

    if dna_strand == "":
        return ""
    else:
        return ''.join([pairs[i] for i in dna_strand ])
