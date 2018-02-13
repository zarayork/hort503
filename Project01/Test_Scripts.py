from sys import argv
from os.path import splitext
from os.path import os
import io



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
    pass
    print('Opening SP1.fq file for reading...')

    fq = open('SP1.fq', 'r')

    sequence_id = fq.readline()
    sequence = fq.readline()
    second_id = fq.readline()
    quality = fq.readline()

    indiv_read = [sequence_id, sequence, second_id, quality]

    print(indiv_read[])
get_read(0)

# Begin the program by calling the main function.
