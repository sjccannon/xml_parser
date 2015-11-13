""" Check whether the genomic sequence seq contains ONLY the characters ACTG. """

ACTG = ["A", "C", "T", "G"]

def GenomicSequence_ACTG_test(GeneSequence, ACTG):
    for character in GeneSequence:
        if character not in ACTG: 
	    return 'This sequence has other letters that are not ACTG'
        else:
    	    return 'This is a genomic sequence'

GenomicSequence_ACTG_test(GeneSequence, ACTG)
