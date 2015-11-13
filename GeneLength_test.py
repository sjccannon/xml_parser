'''This function checkes that the genomic sequence is the correct length'''

transcriptDetails = LRG_root[0][8][0].attrib
geneLength = int(transcriptDetails.values()[1]) + 2000


def GeneLength_test(GeneSequence, geneLength):
	if len(GeneSequence) != geneLength:
		return 'This sequence is not the right length'
	else:
		return 'The sequence length is correct'

GeneLength_test(GeneSequence, geneLength)

