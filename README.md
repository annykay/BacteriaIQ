# BacteriaIQ

Here are my scripts to calculate bacterial IQ. It is calculated as:

IQ = amount_of_signaling_proteins/amount_of_all_proteins 

To do it, you should run script 'hmm_script_all.sh'. It takes two arguments:
- first is the name of bacteria we want to explore. This argument should correspond to the name of a folder from (ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/). 
- second is the name of a version we want to explore. 

For example, I want to explore Chroococcidiopsis Thermalis, because it can servive in extremal enviroAnd, suppose, I decided use  GCF_000317125.1_ASM31712v1. Here is the command, that will do the calculation: 

./hmm_script_all.sh Chroococcidiopsis_thermalis GCF_000317125.1_ASM31712v1

Also, some additional files should be in the directory:
- in 'protein' folder should be aligments of families of proteins
- in domains.txt he information for each family should contain. This information is protein type and domain. In my file this information is provided by numbers. 
- hmm-program should be installed. Also, the path to this program should be defined inside'hmm_script_all_proteins.sh' (the line for this is marked inside the script)

The results will be printed on the screen. The last value is the IQ of bacteria, other ones are printed in the order of  the columns in resulting table(Total number of proteins,	#of histidin kinases,	# of methyl-acc chemotaxis prot,	# of Ser/Thr/Tyr kinases,	# of diguanylate cyclases, # of adenylate cyclases,	# of c-di-GMP phosphodiesterases)

Here is output of my command:
6018
96
11
36
20
1
20
IQ of  Chroococcidiopsis_thermalis : 0.030574941841143236
