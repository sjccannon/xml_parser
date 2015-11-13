#import relevant modules
import xml.etree.ElementTree as tree
from xml.etree.ElementTree import Element, tostring, SubElement
from lxml import etree
import glob 

#create a dictionary with the exon number as the key and the "startcoordinate"  as value [0] and the "endcoordinate" a$
def LRG_exon_coordinates(LRG_tree, tag):
	#create an empty dictionary to be later appended
        exon_dict = {}
        #use for loop to identify all elements with the tag 'exon' 
        for element in LRG_root.iter('exon'):
		#assign the exon tag to a variable
		exon_tag = element.tag
		#assign the exon attibute dictionary to a variable
		exon_attribute = element.attrib
		#assign the string 'label' to a variable which can be used to ensure the code only pulls through the exons
		exon_label = 'label'
		#if statement to see if the exon_label is in the key of the exon attribute dictionary
		if exon_label in exon_attribute.keys():
			#assert number of keys in dictionary is equal to the number of exons 
			#pull out the exon number from the atribute dictionary
			exon_number = (exon_attribute[exon_label]) 
			#iterate through the elements within the elements that pass the for loop i.e. only the exon numbers
	                for child in element:
				#this is the coordinate system we require of the three available
				coordinate_label = tag
				coordinate_attribute = child.attrib
				#ASSERT - check there are the same number of coordinate attributes as there are exons
				#if statement to pull out only the LRG_1 coordinate system data by checking the label against the values in the generated dictionary
				if coordinate_label in coordinate_attribute.values():
					#assigning each coordinate start attribute to a variable
					exon_start = coordinate_attribute['start']
					#assigning each coordinate end attribute to a variable
					exon_end = coordinate_attribute['end']
					#generate a list of exon_start and exon_end for each exon
					start_end_list = [exon_start, exon_end]
					#append the exon_dictionary with the exon number as a key and the exon_start, exon_end as the values
					exon_dict[int(exon_number)] = start_end_list
	#make the output of the function the exon dictionay that has been created
	return exon_dict

""" Includes as function to infer the intron number, start and end coordinates by taking a dictionary in the format {'exon_number': 'exon_ start_ coordinate', 'exon_end_coordinate'}.
Returns the intron dictionary in the format {'intron_number' : 'intron_start_coordinate', 'intron_end_coordinate'} for introns in between the exons in the given exon dictionary"""
def LRG_intron_coordinates(exon_dict):
	#generate the empty intron dictionary which will be later updated with intron number as the key and intron start, intron end coordinates as
	#the values
	intron_dict = {}
	#iterates through every key in the exon_dictionary
	for exon_number in exon_dict:
		#if statement to exclude the final exon (as there will be one less introns than exons)
		if exon_number != exon_dict.keys()[-1]:
			#assign the new list of keys to the variable intron_number which will later become the key in the intron_dictionary
			intron_number = exon_number
			#ASSERT - check the number of introns is one less than the number of exons
			#if statement to identify intron start value
			if intron_number in exon_dict.keys(): 
				#using intron number to only pull out values in the exon dictionary required to identify intron start (i.e. doesn't pull out the end values associated with the final exon)
				value = (exon_dict[intron_number])
				#intron start is the exon end coordinate(2nd value in the exon_dict) plus 1
				intron_start = int(value[1]) + 1
				#this excludes the first exon in the exon dictionary to enable the intron end values to be calculated. we do not want to know the start value of the last exon
				exon_exclude_1 = intron_number + 1 
				#if statement to identify intron end value by using the exon_exclude list to reference the exon_dictionary
				if exon_exclude_1 in exon_dict.keys():
					value = exon_dict[exon_exclude_1]
					#the end intron is the intron start -1 (excludes the first intron as stated previously)
					intron_end = int(value[0]) -1
					#concatenate the intron start and end values for each intron into a list 
					intron_start_end_list = [intron_start, intron_end]
					#create a dictionary with intron number (1:n-1) as the key and intron start, intron end as the values.  
					intron_dict[int(intron_number)] = intron_start_end_list
	#assert - check the number of introns in the dictionary is one less than the number of exons in the exon dictionary 
	return intron_dict

"""Includes a function to parse the genomic intron sequences from an xml file by taking the genomic sequence and a dictionary in the format {'intron_number' : 'intron_start_coordinate', 'intron_end_coordinate'}"""
def LRG_intron_sequence(intron_dict):
        for intron_number in intron_dict:
		value = (intron_dict[intron_number])
		intron_sequence_start = int(value[0]) -1
		intron_sequence_end = int(value[1])
		intron_sequence = (GeneSequence[intron_sequence_start:intron_sequence_end])
		intron_sequence = ''.join(intron_sequence)
		intron_dict[intron_number].append(intron_sequence)
 		# check the length of the sequence == (end - start) + 1
#		print intron_dict
	return intron_dict

def xml_from_dict(tag, intron_dict):
	filename = tag + "_intron_sequences.xml"
	with open(filename, "wb") as outfile:
		root = etree.Element(tag)
		for key, value in intron_dict.items():
			intron_attribute = {"intron_start" : str(value[0]), "intron_number" : str(key), "intron_end" : str(value[1])}
			intron_tag = etree.SubElement(root, 'intron', intron_attribute)
			intron_tag.text = value[2]
		s = etree.tostring(root, pretty_print=True)
		outfile.write(s)

"""uses glob.glob() to search the current folder for all LRG files in the format LRG_*.xml. Ensure LRG files retain t$
will run the program on every LRG_file within the dictionary""" 

#read in the exon file here
for filename in glob.glob('LRG_*.xml'):
        LRG_tree = tree.parse(filename)
	#identify the root of the xml file
        LRG_root = LRG_tree.getroot()
	print LRG_root
        #this line of code extracts the required metadata and saves it into a dictionary
        metadataDict = {'LRG_ID':LRG_root[0][0].text, 'Organism':LRG_root[0][3].text, 'Gene' : LRG_root[0][4][0].text}
        #check if the value generated by the LRG_ID is 'lrg'
        tag = str(metadataDict.values()[0])
        print tag
        #this line of code extracts the genomic sequence of gene in the LRG file and stores it as a list (CM)
        GeneSequence = list(LRG_root[0][7].text)
        #check - there are only ATCGs
        #assertion - check the length of the list is the same as the length of the genomic sequence by
        #checking that the end of the coordinate tag 0 and attribute 2 plus 2000 is equal the length 
	"""The code then executes all of the above functions on every LRG_n.xml file within the current directory"""
	#execue the functions on each the parsed xml files, these function calls are within the initial for loop
	exon_dict = LRG_exon_coordinates(LRG_tree, tag)
	intron_dict = LRG_intron_coordinates(exon_dict)
	intron_sequences = LRG_intron_sequence(intron_dict)
	xml_output = xml_from_dict(tag, intron_sequences)
	
'''This function checkes that the genomic sequence is the correct length'''

transcriptDetails = LRG_root[0][8][0].attrib
geneLength = int(transcriptDetails.values()[1]) + 2000


def GeneLength_test(GeneSequence, geneLength):
        if len(GeneSequence) != geneLength:
                return 'This sequence is not the right length'
        else:
                return 'The sequence length is correct'

GeneLength_test(GeneSequence, geneLength)

""" Check whether the genomic sequence seq contains ONLY the characters ACTG. """

ACTG = ["A", "C", "T", "G"]

def GenomicSequence_ACTG_test(GeneSequence, ACTG):
    for character in GeneSequence:
        if character not in ACTG:
            return 'This sequence has other letters that are not ACTG'
        else:
            return 'This is a genomic sequence'

GenomicSequence_ACTG_test(GeneSequence, ACTG)

""" Check whether the genomic sequence seq contains ONLY the characters ACTG. """

ACTG = ["A", "C", "T", "G"]

def GenomicSequence_ACTG_test(GeneSequence, ACTG):
    for character in GeneSequence:
        if character not in ACTG:
            return 'This sequence has other letters that are not ACTG'
        else:
            return 'This is a genomic sequence'

GenomicSequence_ACTG_test(GeneSequence, ACTG)

