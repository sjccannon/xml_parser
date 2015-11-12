#this function parses a specified xml file then outputs a dictionary containing the exon number as the key, value[0] as the exon start position and value[1] as the exon end position
#import relevant modules
import xml.etree.ElementTree as tree
import glob

#read in the exon file here
#filename =  #glob.glob("LRG*.xml")
LRG_tree = tree.parse("LRG_1.xml")
#identify the root of the xml file
LRG_root = LRG_tree.getroot()

#this line of code extracts the required metadata and saves it into a dictionary
metadataDict = {'LRG_ID':root[0][0].text, 'Organism':root[0][3].text, 'Gene' : root[0][4][0].text}

#this line of code extracts the genomic sequence of gene in the LRG file and stores it as a list (CM)
GeneSequence = list(LRG_root[0][7].text)

#create a dictionary with the exon number as the key and the "startcoordinate"  as value [0] and the "endcoordinate" a$
def LRG_exon_coordinates(LRG_tree):
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
			#pull out the exon number from the atribute dictionary
			exon_number = (exon_attribute[exon_label]) 
			#iterate through the elements within the elements that pass the for loop i.e. only the exon numbers
	                for child in element:
				#this is the coordinate system we require of the three available
				coordinate_label = "LRG_1"
				coordinate_attribute = child.attrib
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

def LRG_intron_coordinates(exon_dict):
	intron_dict = {}
	for exon_number in exon_dict:
		if exon_number != exon_dict.keys()[-1]:
			intron_number = exon_number
			if intron_number in exon_dict.keys(): 
				value = (exon_dict[intron_number])
				intron_start = int(value[1]) + 1
				#print intron_start
				exon_exclude_1 = intron_number + 1
				if exon_exclude_1 in exon_dict.keys():
					value = exon_dict[exon_exclude_1]
					#print value
					intron_end = int(value[0]) -1
					#print intron_end
					intron_start_end_list = [intron_start, intron_end]
					intron_dict[int(intron_number)] = intron_start_end_list
	return intron_dict

def LRG_intron_sequence(intron_dict):
        for intron_number in intron_dict:
		value = (intron_dict[intron_number])
		intron_sequence_start = int(value[0]) -1
		intron_sequence_end = int(value[1])
		intron_sequence = (GeneSequence[intron_sequence_start:intron_sequence_end])
		intron_sequence = ''.join(intron_sequence)
		intron_dict[intron_number].append(intron_sequence)
		print intron_dict
	return intron_dict

def intron_sequence_output(intron_dict) 



#execue the function on the parsed xml file 
exon_dict = LRG_exon_coordinates(LRG_tree)
intron_dict = LRG_intron_coordinates(exon_dict)
intron_sequences = LRG_intron_sequence(intron_dict)
