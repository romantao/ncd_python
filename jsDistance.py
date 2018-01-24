# Jensen-Shannon distance calculation
# Last modified by: 
# Romulo Antao
# 4 January 2017

import sys
import numpy as np
from datetime import datetime
from itertools import combinations

startTime = datetime.now()

def windowCount(data, seq):

	count = 0
	for k in range(len(data)):
	    if data[k:k+3] == seq:
	        count += 1
	return count        

def jensen_shannon(data_x, data_y):

	from itertools import product
	ACTGbase = {'a','c','t','g'}
	
	bucket_x = [0]*64;
	bucket_y = [0]*64;

	i = 0
	for combo in list(product(ACTGbase,repeat = 3)):
		seq = ''.join(combo[0:])
		
		bucket_x[i] = windowCount(data_x,seq)
		bucket_y[i] = windowCount(data_y,seq)

		i = i + 1

	total_bucket_x = sum(bucket_x)
	total_bucket_y = sum(bucket_y)

	p = np.array(bucket_x, dtype='f') / total_bucket_x
	q = np.array(bucket_y, dtype='f') / total_bucket_y
	m = 0.5*(p + q)
	
	sum1 = 0.0
	sum2 = 0.0

	for i in range(len(p)):
		if p[i] == 0.0:
			sum1 = sum1
		else:
			sum1 = sum1 + p[i]*np.log(p[i]/m[i])
		
		if q[i] == 0.0: 
				sum2 = sum2
		else:	
			sum2 = sum2 + q[i]*np.log(q[i]/m[i])

	return 0.5*(sum1+sum2)

def jsDistance_calc(glob_files):
	from glob import glob
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
		
			#Write item_name 9 times for Phylip compatibility
			f.write('\n'+item_name*9)
			item_name = chr(ord(item_name) +1)
			
			combo_prev = combo[0]

		js_distance = jensen_shannon(file_datas[combo[0]], file_datas[combo[1]])
		f.write(' '+str(js_distance))

	#Last item of the list
	f.write('\n'+item_name*9+' ')
	f.close()
	
	print "Script execution time:", str(datetime.now()-startTime)[0:7]

if len(sys.argv) < 2:
	print "syntax error: python jsDistance.py data_folder"
	print "example: python jsDistance.py data/animals/"
else:
	jsDistance_calc(sys.argv[1])
