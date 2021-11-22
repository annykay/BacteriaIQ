#!/bin/bash

HOMEDIR="$(pwd)"
#echo "${HOMEDIR}"
wget https://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/$1/latest_assembly_versions/$2/$2_protein.faa.gz
mkdir -p profiles/$1
mkdir -p results/$1
for file in $HOMEDIR/proteins/*
do
#echo $file
str="$file"
IFS='/'
read -ra ADDR <<< "$str"  
str="${ADDR[-1]}"
IFS='_' 
read -ra ADDR <<< "$str" 
res="${ADDR[0]}"

IFS=' ' 
#echo $str
../hmmer-3.3.2/src/hmmbuild   profiles/$1/$res.hmm $file #here the directory for hmm program should be specified
../hmmer-3.3.2/src/hmmsearch --notextw -E 0.0001  profiles/$1/$res.hmm $HOMEDIR/$2_protein.faa.gz > results/$1/$res.txt #here the directory for hmm program should be specified

done

gunzip -k $2_protein.faa.gz 
NUMPROTEINS="$(grep '^>' $2_protein.faa | wc -l)"
echo $NUMPROTEINS
rm $2_protein.faa
python3 pythonScript.py $1 $HOMEDIR $NUMPROTEINS
