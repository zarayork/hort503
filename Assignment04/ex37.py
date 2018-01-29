from sys import exit

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


# Side note, I must be given credit should any cat names be used for future pets.
def end():
    exit(0)

def date_tree():
    def resource_usage():
        print("Do you use your resources to A) produce dates or B) use all resources to keep growing larger?")
        answer = input()
        return answer

    def dt_else():
        print("You wither and dye from Graphiola because you did not choose an option that continues your lifecycle.")
        end()

    answerA = "People let you keep living because you are producing food."

    print("Happily photosynthesise in the Mediterranean sun for your sixth year.")
    resources1 = resource_usage()
    if resources1 == "A":
        print(answerA)
    elif resources1 == "B":
        print("Year 7:")
        resources2 = resource_usage()
        if resources2 == "A":
            print(answerA)
        elif resources2 == "B":
            print("""People are wondering if you will ever bear fruit.\n
            Year 8:""")
            resources3 = resource_usage()
            if resources3 == "A":
                print(answerA)
            elif resources3 == "B":
                print("The people lost patience and cut you down for firewood so you can finally be useful to them.")
            else:
                dt_else()
        else:
            dt_else()
    else:
        dt_else()

print(True and True)
print(False and True)
print(1 == 1 and 2 == 1)
print("test" == "test")
print(1 == 1 or 2 != 1)

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
