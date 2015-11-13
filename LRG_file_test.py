'''Test that the input file is an LRG file'''

def LRG_file_test():
	if LRG_root.tag=="lrg":
		print 'This is an LRG file'
	else:
		return 'This is not an LRG file'


LRG_file_test()
