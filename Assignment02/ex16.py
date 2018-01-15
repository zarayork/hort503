#user specifies arguments
from sys import argv
#order of arguments
script, filename = argv
#print precautions and get user initiation
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#needs input from user to proceed
input(" ")

print("Opening and erasing file...")
#erases the file by opening in "write mode"
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")
#user input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#writes the 3 input lines to the file
target.write(line1 + "\n" + line2 + "\n" + line3)

print("And finally, we close it.")
target.close()

print("Input txt filename to view content")
txt_file = input("txt file: ")
otxt = open(txt_file)
print("\n")
print(otxt.read())
otxt.close()
