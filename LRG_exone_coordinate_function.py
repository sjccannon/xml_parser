#this function parses a specified xml file then outputs a dictionary containing the exon number as the key, value[0] as the exon start position and value[1] as the exon end position
#import relevant modules
import xml.etree.ElementTree as tree
import glob

#read in the exon file here
#filename =  #glob.glob("LRG*.xml")
LRG_tree = tree.parse("LRG_1.xml")
#identify the root of the xml file
LRG_root = LRG_tree.getroot()

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
					exon_dict[exon_number] = start_end_list
	#make the output of the function the exon dictionay that has been created
	return exon_dict

#execue the function on the parsed xml file 
LRG_exon_coordinates(LRG_tree)

