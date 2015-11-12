import xml.etree.ElementTree as tree

LRGfile_tree = tree.parse('LRG_1.xml')

root = LRGfile_tree.getroot()

GeneSequence = list(root[0][7].text) 
#this line of code extracts the genomic sequence of gene in the LRG file and stores it as a list (CM)
