#this programme extracts intronic sequences from LRG files.
#run within the directory containg the LRG files you wish to be analysed

import xml.etree.ElementTree as tree
import glob

#function to define the metadata to be extracted from the file
#ensures the user is analysing the correct file. I think we should just take it all
def LRG_metadata(LRG_file):
	#insert an asscertion - check the file is the correct one? e.g. is the LRG_root 'lrg'?
	#choose the metadata to be included and assign to a variable (this could also be a dictionary with the tag as a key and the text as the value)
	#insert ascertion - do we have all of the correct data?
	#return the the metadata dictionary

#function to identify the genomic sequence tag and store the data in a list of characters
def LRG_genomic_sequence(LRG_file):
	LRGfile_tree = tree.parse('LRG_1.xml')

	root = LRGfile_tree.getroot()

	GeneSequence = list(root[0][7].text)

#this line of code extracts the genomic sequence of gene in the LRG file and stores it as a list (CM)
	#identify genomic sequence tag and generate a list with one nucleotide per element 
	#assign list to a dictionary with the gene_name and LRG concatenated as the key and the nucleotide as the list of values
	#note - exons start at 5001, genomic sequence starts at 1 and ends 2000 bases after the final exon.
	#note - the list is 0 indexed
	#assertion - check length of list is same as final exon coordinate + 2000
	#return genomic_sequence_dictionary

#create a dictionary with the exon number as the key and the "startcoordinate"  as value [0] and the "endcoordinate" as value [1]
def LRG_exon_coordinates(LRG_file):
	exon_dict = {}
	#need to figure out how to reference every exon attribute's text 
	for element in LRG_tree.iter(tag='exon'):
		exon_number = element.text
		#append dictionary key as exon_number
		exon_start =  
		#take the values add it to a dictionary as teh key
		#then for the same exon take the forst row coordinates attribute "start"'s test and "end" test 
		#and add it as values
		#return the dictionary

#create a dictionary with the intron number as the key, intron_start as value [0], and intron_end as value [1] 
def LRG_intron_coordinates(exon_dict):
	intron_dict = {}
	for every key in the exon_ dictionary:
		assign the value to the new intron_dictionary as the key
		take the end value + 1 to create the intron start value
		then move to the key + 1 take the start -1 and assign it as the intron end value
	retun intron_dict
#note -there is going to be one less intron than there are exon:
# assertion? if else statement to control this. check there is another exon after it

#function to generate 
def LRG_intron_sequence(intron_dict, genomic_sequence_dict):
	for every value in intron_dict:
		if the nucleodide is >= start value and <= end value in the list of nucleotides
			extract (slice) every element and convert to a single string
			assertion - check number of elements and length of string are the same  	
			append the nucleotide sequence to intron_dict as value [2]
		else:
			print an informative error message
	return appended intron_dict

def LRG_intron_output(intron_dict, metadata_dict):
	create an xml file from the output of the other functions - bonus points for this. 

	
#this code then calls of the fucntions in sequence to make them work
#assign all of the LRG.xml within current directory to the variable filename
filename = glob.glob("LRG*.xml)
#loop through the identified LRGs calling functions 
for LRG_file in filename:
	LRG_tree = tree.parse(LRG_file)
	LRG_root = LRG_tree.getroot()
	#run the metadata function
	LRG_metadata(LRG_file)
	LRG_genomic_sequence(LRG_file)
	LRG_exon_coordinates(LRG_file)
	LRG_intron_coordinates(exon_dict)
	LRG_intron_sequence(intron_dict, genomic_sequence_dict)
	LRG_intron_output(intron_dict, metadata_dict)




#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#below here is useful code:

#you can use this to identify particular elements 
#for element in LRG_tree.iter(tag='period'):
#        print element.text

#this is a way to refer to one specific section
#now we are going to find all of the nodes listed within the root node 
#using a for loop
#for child in root:
#        print "tag =", child[0].tag
#        print "attribute =", child[0].attrib #could also do itlike child.attrib['name']
#        print "text =", child[0].text


#create an output function
#from lxml import etree
#def intron_xml_output:
	# create XML 
#	root = etree.Element('root')
#	root.append(etree.Element('child'))
	# another child with text
#	child = etree.Element('child')
#	child.text = 'some text'
#	root.append(child)

	# pretty string
#	s = etree.tostring(root, pretty_print=True)
	#write this to outfile
	



