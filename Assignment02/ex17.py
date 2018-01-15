#semicolon after every command can be used to shorten this to a single line, but it is not user-friendly for me as a beginner.
#I shortned it into similar command types, but I am leaving this longer so that I can easily break it down into different processes/functions.
from sys import argv; from os.path import exists; script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file); indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

out_file = open(to_file, 'w'); out_file.write(indata)

print("Alright, all done.")

out_file.close(); in_file.close()
