-python 2.7
--The XML_intron_parser program is intended to parse Locus reference Genomic xml files into memory to be used for further analysis as required.
--Directory structure should be set out as:

    #    parent directory/
    #        lrgs/
    #           LRG_1/
    #               LRG_1.xml
    #           LRG_2/
    #               LRG_2.xml

useage: python lrg_xml_parser.py
"__main__" statement prints the exon coordinates as a dictionary but also:
    models the workspace in the above format
    iterates through each LRG_n.xml file to create an array of LRG instancesin the workspace class
    for each lrg instances the folowing occurs:
        file extension is used to deduce file format
        lrg file name is extracted
        ensures the lrg_format is xml and prints exception message if not
        lrg_id id extraced 'LRG_n' where n is lrg number
        exon coordinates are read into memeory {'exon_number' : ['start', 'end']}
        intron coordinates {'exon_number' : ['start', 'end']}
        genomic sequence, transcript sequence and protein sequences are read into memory for each lrg ['genomic', 'transcript', 'protein']
