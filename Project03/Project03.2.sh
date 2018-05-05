#!/bin/bash

### Concatenate all BLAST output files.
cat ./BlastOut/*.blastp.out > blastConcat.txt

### Isolate the protein names using awk, and count the number of occurances using uniq.
awk '{ print $1 }' blastConcat.txt | uniq -ci > ProteinNames.txt 

### Re-order the file to protein names then number of BLAST hits, in a tab-delimited format.
### Sort the file by largest to smallest number of BLAST hits.
awk '{ print $2 "\t" $1 }' ProteinNames.txt | sort -nrk2 > P3SummaryFile.txt

