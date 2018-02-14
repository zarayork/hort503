"""A Python script that performs simple read trimming of a FASTQ file.
.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.
.. moduleauthor:: Zara York
"""
from sys import argv
from os.path import splitext
from os.path import os
import io
#Set arguments as global variables. Minimums converted from strings to integers.
script, in_file, out_file, min_q, min_size = argv
print(argv)
min_q = int(min_q)
min_size = int(min_size)
def get_read(fq):
    """Extract a single read from a FASTQ file.
    Reads in a FASTQ file are stored in 4 lines that contain the
    sequence_id, nucleotide sequence, a second id, and a series of
    characters represeting quality scores. This function returns
    :param fq: A file handle for the FASTQ file
    :type fq: An io.TextIOBase object (created using the open() function).
    :return: a list containing 4 strings: the sequence ID, nucleotide sequence,
        second ID, and the quality score sequence. If there are no more
        sequences in the FASTQ file then this function returns False.
    :rtype: a list with four elements
    """
    sequence_id = fq.readline()
    if not sequence_id:
        return False
    sequence = fq.readline().strip()
    second_id = fq.readline()
    quality = fq.readline().strip()
    return [sequence_id, sequence, second_id, quality]

def trim_read_front(read, min_q, min_size):
    """Trims the low quality nucleotides from the front of a reads' sequences.
    This function examples the quality score of each nucleotide sequence
    starting from the first position of the sequence. When it encouters a
    high quality score it stops trimming and returns an updated read.
    :param read: A list containing four elements in this order: the sequence ID,
        the nucleotide sequence string, a secondary identifier string, and a
        quality score string.
    :type read: a list
    :param min_q:  The minimum quality score that a nucleotide must have to
        not be trimmed (e.g. 20).
    :type min_q:  integer
    :param min_size:  The minimum size that the sequence must have after
        trimming to keep the read (e.g. 25).
    :type min_size: integer
    :return: a list just like the the get_read() function returns but with the
       low-quality reads (and corresponding quality scores) trimmed off the
       front of the string. If the remaining trimmed read is smaller than the
       desired minimum read length then this function returns False.
    :rtype: a list with four elements
    """
    new_seq = read[1]
    quality = read[3]
    new_qual = quality
    pos = read[3]
    length = len(new_seq)
    for pos in quality:
        q = ord(pos)- 33
        print(q)
        if q < min_q:
            new_seq = new_seq[1:]
            new_qual = new_qual[1:]
        elif q >=min_q and length >= min_size:
            return [read[0], new_seq + '\n', read[2], new_qual + '\n']
        elif length < min_size:
            return ("Fail")
# The main function for the script.
#
def main():
    """The main function of this script.
    After trimming is completed, the function prints out three status lines. The
    first indicates the total number of reads that were found. The second
    indicates how many reads were removed for being too short after trimming and
    the third indicates how many reas were trimmed and kept.
    The script will create a new FASTQ file of just the trimmed reads and name
    it according to the argument provided by the user when running the script.
    :param argv:  The incoming arguments to this script as
       provided by the sys.argv variable.  There must be four total arguments
       provided to the script must be in the following order
       - The filename for the input FASTQ file
       - The filename for the new output FASTQ file that this script creates
       - An integer for the minimum quality score. Anything below this at the
         beginning of each read's nucleotide sequence is trimmed off.
       - An integer indicating how large a read's nucleotide sequence must
         be after trimming in order to keep it.
    """
    pass
    print("Opening SP1.trim.fq file for writing...")
    output = open(out_file, 'w')
    print("Opening SP1.fq file for reading...")
    with open(in_file, 'r') as textiobase_obj:
        total_reads = 0
        passed_reads = 0
        failed_reads = 0
        curr_read = get_read(fq=textiobase_obj)
        while curr_read:
            quality_read = trim_read_front(curr_read, min_q, min_size)
            if quality_read == "Fail":
                failed_reads += 1
                total_reads += 1
            else:
                output.write(quality_read[0])
                output.write(quality_read[1])
                output.write(quality_read[2])
                output.write(quality_read[3])
                passed_reads += 1
                total_reads += 1
                curr_read = get_read(fq=textiobase_obj)
    print(f"""{total_reads} reads were found.
        {failed_reads} reads were removed.
        {passed_reads} reads were trimmed and kept.
        Done.""")

# Begin the program by calling the main function.
main()
