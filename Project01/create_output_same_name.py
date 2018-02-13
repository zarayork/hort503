from sys import argv
from os.path import splitext
from os.path import os

script, in_file = argv
def create_out_file():
    in_name = os.path.splitext(in_file)[0]
    results_file = open(f'{in_name}.trimmed.fq', 'a+')
    results_file.seek(0)
    results_file.write('Test Successful')
    results_file.close()

out_file = create_out_file

create_out_file()
