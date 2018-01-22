#Import argv from the sys module.
from sys import argv
#Set up the arguments.
script, input_file = argv
#Set the definition for printing the file.
def print_all(f):
    #Prints out the file contents.
    print(f.read())
#Set the function to go back to the beginning.
def rewind(f):
    #Uses the seek function within the file to go to a specific location.
    #In this case, position, or byte, 0. Replacing with 1 prints "his is line 1" instead of "This."
    f.seek(0)
#Set the function to print the line numbers of the file, then the line contents.
def print_a_line(line_count, f):
    print(line_count, f.readline())
#Creates an object that opens the input file specified in the arguments.
current_file = open(input_file)
#Print the string followed by a line break.
print("First let's print the whole file:\n")
#Reads and prints the current input file from the arguments.
print_all(current_file)
#Print the string.
print("Now let's rewind, kind of like a tape.")
#Go back to the beginning of the current input file.
rewind(current_file)
#Print the string.
print("Let's print three lines:")
#Creates a variable for the line that is being read.
current_line = 1
#Print the line then the contents of that line in the input file.
#Current_line equals 1.
print_a_line(current_line, current_file)
#Creates a variable for the next line that will now be read.
current_line += 1
#Print the line then the contents of that line in the input file.
#Current_line equals 2.
print_a_line(current_line, current_file)
#Creates a variable for the next line that will now be read.
current_line += 1
#Print the line then the contents of that line in the input file.
#Current_line equals 3.
print_a_line(current_line, current_file)
