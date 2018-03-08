How to use ncd.py

"python ncd_calc.py data_folder compressor"
"compressors available: zlib or bz2"
"example: python ncd.py data/animals/ zlib"


This program uses the Normalized Compression Distance to evaluate the similarity degree the mtDNA of different animals, thus inferring their genetic similarity.

The results obtained from the ncd.py script are in the format required for post processing in Phylip (http://evolution.genetics.washington.edu/phylip.html).


To generate a phylogenetic tree from the example dataset using the zlib compressor, the following procedure shall be followed:

1) Execute the script
	
	python ncd.py data/animals/ zlib

	the output file, "q.phy" is a upper diagonal matrix

2) execute the Phylip program neighbor

	./phylip-3.695/neighbor

3) Choose "q.phy" as source and select Upper Triangular Data Matrix (R). Process the files and the program will output:

	Output written on file "outfile"
	Tree written on file "outtree"
	Done.

3) Execute the script "name_replace" to introduce the names of the animals in the outtree file

	python "name_replace.py"

4) Execute the Phylip program drawtree 
	
	./phylip-3.695/neighbor

5) Choose "outtree" as the input file and "font1" as the used font. Select option (B) to not use branch length and produce the output file.

6) the result phylogenetic tree will be saved in the newly created "plotfile"