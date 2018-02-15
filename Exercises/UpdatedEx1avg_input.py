#Need to import mean function from library, which is listed at the top of the page.
from statistics import mean
from sys import argv

def Sets1to10():
    i = 1
    numbers = []
    while i < 10.1:
        print("Input Set", i, "value")
        x = float(input())
        numbers.append(x)

        i = i + 1

    print("Set Totals:", numbers)
    return numbers
#Assigns the returned number to a variable.
Seed_Sets = Sets1to10()

#for i, x in enumerate(z): #creates an index
#Make sure to include both ([]), because the brackets make it a list.
#The variable is a list, so the mean function does not need brackets.
average = mean(Seed_Sets)
print("Average is: ", average)
