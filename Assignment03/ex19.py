#This defines the function.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#This prints the string after substituting the variable into it.
    print(f"You have {cheese_count} cheeses!")
#This prints the string after substituting the variable into it.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
#This prints the string.
    print("Man that's enough for a party!")
#This prints the string and creates a line break after it.
    print("Get a blanket.\n")

#This prints a string.
print("We can just give the function numbers directly:")
#This prints the function with the variables substituted in
cheese_and_crackers(20, 30)

#This prints the string.
print("OR, we can use variables from our script:")
#This line establishes the first variable, even though it has a different name.
amount_of_cheese = 10
#This line establishes the second variable, which also has a different name.
amount_of_crackers = 50
#This line runs the function and assigns the two new variables as the function's variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#This prints the string
print("We can even do math inside too:")
#This assigns the two variables after the calculation is performed.
cheese_and_crackers(10 + 20, 5 + 6)

#This prints the string.
print("And we can combine the two, variables and math:")
#This performs a calculation with a variable, the substitutes the variable into the function.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#Study Drills
def Amount_of_food(people_attending):
    total_pizzas = people_attending / 4
    print("The event will need at least", total_pizzas, "pizzas" )
    print("How many guests are vegetarian?"); veg = float(input())
    print("The event will need", int(total_pizzas - veg), "meat pizzas and", ((veg / 4) + int(0.1 * people_attending)), "vegetarian pizzas")

print("\nHow many people will be attending the event?"); people_attending = int(input())
Amount_of_food(people_attending)
