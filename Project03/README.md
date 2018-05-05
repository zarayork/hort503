This file is designed to run on WSU's Kamiak system.
The script splits a FASTA file into multiple smaller files that undergo individual BLAST searches and are later recombined.
It performs a BLAST search for a FASTA file that contains multiple protein names and sequences.
The summary file will contain a list of the proteins and their respective number of BLAST hits.
  It will be sorted based on the number of hits, and will be displayed highest to lowest.

Before any scripts can be ran: assign the directory that contains the programs and then add: java, nextflow, blast.
  In Dr. Ficklin's account these can be accessed using the commands:
  $ module use /data/ficklin/modulefiles
  $ module add java nextflow blast

The scripts needs to be ran in the same directory as the file that contains the query sequences.
  The params will need to changed so they are specific for the project and account you are using.
  The file path for the file containing the query protein sequences will go in params.inf and the file path for the database (such as Swiss-Prot) goes in params.db. 
  The second script uses the output directory, so it is best not to change params.out unless it is also changed in the bash script.

Script 1: Project03.1.nf
  Any number of sequences can be specified for the split, the script does not depend on the number of files.
  To run: $ nextflow Project03.1.nf --divideby [number of desired sequences per file]
  For 10 Files: First use the command "grep -c '>' your_file_name" to determine the total number of sequences.
    Divide that number by 10 and round up to the nearest whole number. This will be your --divideby number.
  For 5000 sequences per file: $ nextflow Project03.1.nf --divideby 5000

  Output: BLAST results for all files in the params.out directory.

Script 2: Project03.2.sh
  When Script 1 has finished running, Script 2 can be used to concatente the files, isolate the names, and display the number of BLAST hits in descending order.
  *Script 1 must be completely finished*
  To run: $ ./Project03.2.sh

  Output: 
    blastConcat.txt file that contains all the BLAST results in one file, not sorted.
    ProteinNames.txt file with a list of the protein names (duplicated based on number of hits; used for counting, not for displaying results).
    P3SummaryFile.txt file with names and number of hits in descending order.

The results file is P3SummaryFile.txt.
