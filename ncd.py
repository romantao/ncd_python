# Normalized Compression Distance calculation
# Last modified by: 
# Romulo Antao
# 31 December 2017

import sys
from datetime import datetime
startTime = datetime.now()

def compression_distance(data_x, data_y, compressor = "zlib", level = 6, precompressed = 0):
	if compressor == "zlib":
		#print "Using ZLIB"
		from zlib import compress
		from zlib import decompress
	if compressor == "bz2":
		#print "Using BZIP"
		from bz2 import compress
		from bz2 import decompress
	if precompressed == 0:
		c_x = len(compress(data_x, level))
		c_y = len(compress(data_y, level))
		c_x_y = len(compress(data_x + " " + data_y, level))
	else:
		c_x = len(data_x)
		c_y = len(data_y)
		c_x_y = len(compress(decompress(data_x) + " " + decompress(data_y), level))
	ncd = (c_x_y - min(c_x, c_y)) / float(max(c_x, c_y))
	return ncd

def ncd_calc(glob_files, compressor = "zlib", level = 6, precompressed = 0):
	from glob import glob
	from itertools import combinations
	file_datas = {}
	files = glob(glob_files+'*')

	for filec in files:
		file_datas[filec] = open(filec).read()

	f = open('q.phy','w')

	f.write(str(len(files)))

	item_name = 'A'
	combo_prev = ''

	for combo in combinations(files, 2):

		if combo[0] != combo_prev:
			
			#f.write('\n'+str(item1))
		
			#Write item_name 9 times for Phylip compatibility
			f.write('\n'+item_name*9)
			item_name = chr(ord(item_name) +1)
			
			combo_prev = combo[0]

		ncd_distance = compression_distance(file_datas[combo[0]], file_datas[combo[1]], compressor, level)
		f.write(' '+str(ncd_distance))

	#Last item of the list
	f.write('\n'+item_name*9+' ')

	f.close()
	
	print "Using compressor:", compressor

	print "Script execution time:", str(datetime.now()-startTime)[0:7]

if len(sys.argv) < 3:
	print "syntax error: python ncd_calc.py data_folder compressor"
	print "compressors available: zlib or bz2"
	print "example: python ncd.py data/animals/ zlib"
else:
	ncd_calc(sys.argv[1], str(sys.argv[2]), 9)	

