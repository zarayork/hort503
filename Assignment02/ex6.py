#variable
types_of_people = 10
#creates a string containing variable
x = f"There are {types_of_people} types of people."
#Next 2 lines establish variables
binary = "binary"
do_not = "don't"
#creates a second string containing different variables
#string inside string 1/2
y = f"Those who know {binary} and those who {do_not}."
#Next 2 lines prints the two strings
print(x)
print(y)
#Next 2 lines prints string within string
#string inside string 3
print(f"I said: {x}")
#string inside string 4
print(f"I also said: '{y}'")
#creates variable
hilarious = False
#string with open variable
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
#Next 2 lines create variable containing a string
w = "This is the left side of..."
e = "a string with a right side."
#combines the two strings
print(w + e)
