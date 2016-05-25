#import modules
import xml.etree.ElementTree as tree
from xml.etree.ElementTree import Element
from lxml import etree
import os, re

#model the local workspace
class Workspace(object):
    lrg_instances = []
      	
    #initialise workspace to current working directory. Should be immediate parent directory of directory containing lrg directories
    #workspace diagram:

    #    parent directory/
    #        lrgs/
    #	        LRG_1/
    #               LRG_1.xml
    #           LRG_2/
    #               LRG_2.xml


    def __init__(self, root_dir=None):
	if root_dir is None:
	    self.root_dir = os.getcwd()
	elif root_dir:
	    self.root_dir = root_dir
	else:
	    print 'root directory not recognised by workspace __init__'


    #find all lrg pathnames in child directories and returns array of lrg_instances,
    def lrg_array(self):
	#path to 'lrgs' directory containing all LRG directories
	lrg_root = os.path.join(self.root_dir, 'lrgs')
	#iterate_through subdirectories, directories and files in the lrg_root
	for subdirs, dirs, files in os.walk(lrg_root):
	    #iterate through the files in each dirs
	    for file in files:
		#basic regular expression to match default names for lrg xml files
		if re.match("LRG_.*xml", str(file)):
		    #join file name to absolute path (subdirs)
		    file = os.path.join(subdirs, file)
		    #initialise and append an LRG instance for each file found
		    self.lrg_instances.append(Lrg(file))
		#basic regular expression to match default names for lrg fasta files
		elif re.match("LRG_.*fasta", str(file)):
		    file = os.path.join(subdirs, file)
		    self.lrg_instances.append(Lrg(file))
	#return array of LRG instances
	return self.lrg_instances

#models sections of an lrg_file
class Lrg:
    #requires the path to an lrg_file. Uses lxml to read the xml file into memeory and get the root
    #all other instance variables are updateable using the appropriate functions as required
    def __init__(self, lrg_path):
	self.path = lrg_path
	self.lrg_tree = tree.parse(self.path)
	self.lrg_root = self.lrg_tree.getroot()
	self.name = ""
	self.format = ""
	self.id = ""
	self.exon_coord = {}
	self.intron_coord = {}
	self.sequence = []
    
    #get filename without extension
    def get_name(self):
	base = os.path.basename(self.path)
	no_ext = os.path.splitext(base)
	self.name = no_ext[0]
	return self.name

    #return format of lrg file
    def get_format(self):
	base = os.path.basename(self.path)
	ext = os.path.splitext(base)[1].strip(".")
	if ext == 'xml':
	    self.format = ext
	elif ext == 'fasta':
	    self.format = ext
        return self.format
    
    #return the lrg id/name from within the lrg file
    def get_id(self):
	for id in self.lrg_root.iter('id'):
	    self.id = id.text
	return self.id

    #return {exon_number : [exon_start, exon_end]}
    def get_exon_coords(self):
	#string used in lrg files to label the exon number 
	exon_label = 'label'
	#iterate through ever element called 'exon'
	for exon in self.lrg_root.iter('exon'):
	    if 'label' in exon.attrib.keys():
		#extract exon_number
		exon_number = (exon.attrib['label'])
		#iterate through coordinates in the child elements of each exon
	        for coords in exon:
		    #pull out coordinates used in the exon LRG genomic sequence as opposed to a transcript sequence
		    if self.id in coords.attrib.values():
			#update the instance variable dictionary with the extracted coordinates
			self.exon_coord[exon_number] = [coords.attrib['start'], coords.attrib['end']]
	return self.exon_coord 

    #return {intron_number : [intron_start, intron_end]
    def get_intron_coords(self):
	#iterate through the exon dictionary - include conditional to ensure exon dictionary is created
	for exon_number, exon_coord_list in self.exon_coord.iteritems():
	    exon_number = int(exon_number)
	    #list to be updated for each iteraion
	    intron_coord_list = []
	    #intron start is the last based of the preceeding exon +1 with the exception of the final exon
	    if exon_number < len(self.exon_coord.keys()):
		intron_number = exon_number
		intron_start = int(exon_coord_list[1]) + 1
		intron_coord_list.append(str(intron_start))
	    #intron end is the first base of the subsequent exon -1 with the exception of the first exon
	    if exon_number:
		exon_above = exon_number + 1 
		try:
   	            exon_above_coord = (self.exon_coord[str(exon_above)])
		    intron_end = int(exon_above_coord[0]) - 1
		    intron_coord_list.append(str(intron_end))
		except:
		    pass
	    #update the instance dictionary with introns where the number of introns is exon number -1
	    if exon_number < len(self.exon_coord.keys()):
	        self.intron_coord[exon_number] = intron_coord_list
	return self.intron_coord

    #function to retun the genomic, transctipt and protein sequences as an array
    def get_sequences(self):
	for sequence in self.lrg_root.iter('sequence'):
	    self.sequence.append(sequence.text)
	return self.sequence    

#main statment to initialise lrg instances in an array and loop through each to perform functions
if __name__ == "__main__":
    WS = Workspace()
    lrg_instances = WS.lrg_array()
    for lrg in lrg_instances:
	print lrg.get_name()
	print lrg.get_format()
	lrg.get_id()
	print lrg.get_exon_coords()
	print lrg.get_intron_coords()
	lrg.get_sequences()
	

