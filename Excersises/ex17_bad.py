from sys import argv
from os.path import exists
# Originally did not have "script"
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

 # we could do these two on one line, how?
in_file = open(from_file)
#Did not have .read()
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
#() Was empty
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
