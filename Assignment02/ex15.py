#sets that the arguments are imported by the system/user
from sys import argv
#sets the order/names for the arguments
script, filename = argv
#opens the specific text file based on the argument
txt = open(filename)
#print confirmation of file argument
print(f"Here's your file {filename}:")
#prints contents of the file
print(txt.read())
close()
#first method is my preference because you can use the tab key to make sure your file name is correct

#Alternate method for calling the file
print("Type the filename again:")
#file name input follows the >
file_again = input("> ")
#opens the txt file
txt_again = open(file_again)
#prints contents of txt file
print(txt_again.read())
close()
