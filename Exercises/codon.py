from sys import argv

def get_sequence()
    seq_id = in_file.startswith('>')
    seq = in_file.startswith('A', 'T', 'G', 'C', 'a', 't', 'g', 'c')

    if not seq_id or seq:
        return False
    return
    for

def main(argv)
    script, in_file = argv
    get_sequence()
#     print("Opening SP1.trim.fq file for writing...")
#     output = open(out_file, 'w')
#     print("Opening SP1.fq file for reading...")
#     with open(in_file, 'r') as textiobase_obj:
#         total_reads = 0
#         passed_reads = 0
#         failed_reads = 0
#         curr_read = get_read(fq=textiobase_obj)
#         while curr_read:
#             quality_read = trim_read_front(curr_read, min_q, min_size)
#             if quality_read:
#                 output.write(quality_read[0])
#                 output.write(quality_read[1])
#                 output.write(quality_read[2])
#                 output.write(quality_read[3])
#                 passed_reads += 1
#                 total_reads += 1
#             else:
#                 failed_reads += 1
#                 total_reads += 1
#             curr_read = get_read(fq=textiobase_obj)
#     print(f"""{total_reads} reads were found.
# {failed_reads} reads were removed.
# {passed_reads} reads were trimmed and kept.
# Done.""")
