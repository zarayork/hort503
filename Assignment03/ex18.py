# this one is like your scripts with argv
#Set a definition to print two arguments.
def print_two(*args):
    #Assign arguments.
    arg1, arg2 = args
    #Print a string that states what the arguments are.
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
#Define a function to assign and print two arguments.
def print_two_again(arg1, arg2):
    #Print a string that states what the arguments are.
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
#Define a function to assign and print one argument.
def print_one(arg1):
    #Print a string that states what the argument is.
    print(f"arg1: {arg1}")

# this one takes no arguments
#Define what to print when there are no arguments.
def print_none():
    #Print a string.
    print("I got nothin'.")

#Run the two-argument, two-assigning-steps function.
print_two("Zed","Shaw")
#Run the two-argument function.
print_two_again("Zed","Shaw")
#Run the single argument function.
print_one("First!")
#Run the function that does not have an argument.
print_none()
