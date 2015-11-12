import xml.etree.ElementTree as tree #importing library. Calling it tree so we don't have to type the whole
# name of the library each time we want to use a function within that library

LRG_tree = tree.parse('LRG_1.xml')# parsing the LRG_1 file 

root = LRG_tree.getroot() # get the root node

print root.tag # prints root tag name

print root.attrib # prints root attribute

metadataDict = {'LRG_ID':root[0][0].text, 'Organism':root[0][3].text, 'Gene' : root[0][4][0].text}


