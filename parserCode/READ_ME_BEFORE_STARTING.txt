
     	The XML_intron_parser program generates intron locations and sequences from Locus Reference Genomic (LRG) files that are in XML format in Python.
	This document provides information on how to implement the parser and also provides details of the functions used by the parser.

	To print this documentation from the command line, type the following:
				python documentationFunction.py
	--------------------------------------------------------------------------------------------------------------------------------------
	To use the XML_intron_parser, copy the XML_intron_parser.py file into the directory that contains all the LRG XML files
	that you wish to extract intronic sequences from. 
	
	The parser uses glob.glob() to search the current folder for all LRG files in the format LRG_*.xml, 
	ensuring that the LRG file names retain the original naming format.
	
	The parser can then be used by typing the following line at the command line:
				python XML_intron_parser
	---------------------------------------------------------------------------------------------------------------------------------------
	The XML_intron_parser is composed of the following functions:
	1.LRG_exon_coordinates, which parses a specified xml file then outputs a Python dictionary containing the exon numbers as the keys
	  together with the exon start and end coordinates;

	2.LRG_intron_coordinates, which creates a dictionary with the exon numbers as the keys together with the intron start and end coordinates;
	
	3.LRG_intron_sequence, which appends the intronic sequence to the LRG_intron_coordinates dictionary in 2 above.
