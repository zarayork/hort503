from sys import argv
import io
def get_read(fq):
sequence_id = fq.readline()
    if not sequence_id:
        return False
    sequence = fq.readline().strip()
    second_id = fq.readline()
    quality = fq.readline().strip()
    return [sequence_id, sequence, second_id, quality]

def trim_read_end(read, min_q, min_size):
    new_seq = read[1]
    rev_seq = new_seq[::-1]
    print(new_seq)
    print(rev_seq)
    quality = read[3]
    new_qual = quality
    pos = read[3]
    for pos in quality:
        q = ord(pos)- 33
        if q < min_q:
            new_seq = new_seq[1:]
            new_qual = new_qual[1:]
        elif q >=min_q and len(new_seq) >= min_size:
            return [read[0], new_seq + '\n', read[2], new_qual + '\n']
        else:
            return False
    return False

    def main(argv):
        script, in_file, out_file, min_q, min_size = argv
        min_q = int(min_q)
        min_size = int(min_size)
        print(f"Opening {outfile} file for writing...")
        output = open(out_file, 'w')
        print(f"Opening {in_file} file for reading...")
        with open(in_file, 'r') as textiobase_obj:
            total_reads = 0
            passed_reads = 0
            failed_reads = 0
            curr_read = get_read(fq=textiobase_obj)
            while curr_read:
                quality_read = trim_read_end(curr_read, min_q, min_size)
                if quality_read:
                    output.write(quality_read[0])
                    output.write(quality_read[1])
                    output.write(quality_read[2])
                    output.write(quality_read[3])
                    passed_reads += 1
                    total_reads += 1
                else:
                    failed_reads += 1
                    total_reads += 1
                curr_read = get_read(fq=textiobase_obj)
        print(f"""{total_reads} reads were found.
    {failed_reads} reads were removed.
    {passed_reads} reads were trimmed and kept.
    Done.""")
main()
