#Assign a value to the variable.
people = 30
#Assign a value to the variable.
cars = 40
#Assign a value to the variable.
trucks = 35

#Compare the two variables, if True (cars has a higher value than people), it
#will print the string and not move on through the rest of the block.
if cars > people:
    print("We should take the cars.")
#If the "if" statement is False, then it moves to the alternate "if" statement.
#The alternate if statement is evaluated, and it will move on if False, or finish
#with this block if the statement is True.
elif cars < people:
    print("We should not take the cars.")
#When both "if" statements are False, it will print the following string.
else:
    print("We can't decide.")

#Compare the two variables, if True (trucks has a higher value than cars), it
#will print the string and not move on through the rest of this block.
if trucks > cars:
    print("That's too many trucks.")
#If the "if" statement is False, then it moves to the alternate "if" statement.
#The alternate if statement is evaluated, and it will move on if False, or finish
#with this block if the statement is True.
elif trucks < cars:
    print("Maybe we could take the trucks.")
#When both "if" statements are False, it will print the following string.
else:
    print("We still can't decide.")


#Compare the two variables, if True (people has a higher value than truck), it
#will print the string and not move on through the rest of this block.
if people > trucks:
    print("Alright, let's just take the trucks.")
#Additional, more complex boolean expression for the Study Drills.
elif cars > people or trucks < cars:
    print("We will have enough space.")
#If the "if" statement was False, it will print the following string.
else:
    print("Fine, let's stay home then.")
