from sys import exit
# Side note, I must be given credit should any cat names be used for future pets.
def end():
    exit(0)

def cat():
    print("Welcome to Caterini! Do you want surf or turf?")

    name = input()

    if name == "surf":
        print("Hello Pusseidon. Do you want cod, flounder, or tuna?")
        fish = input()
        if fish == "cod" or fish =="flounder":
            print("Bon appetit, I hope it's divine!")
            end()
        elif fish == "tuna":
            print("Be careful, tuna contains thiaminase which can be lethal through the destruction of vitamin B1.")
            end()
        else:
            print("You may be divine, but that was not on the menu.")
            end()
    elif name == "turf":
        print("Hello Purrseus. Will it be Gorgon-zola mice, or Andromeata?")
        land_meat = input()
        if land_meat == "Gorgon-zola mice":
            print("Enjoy, and watch out for snakes!")
            end()
        elif land_meat == "Andromeata":
            print("Eat quickly and prepare for a cat fight!")
            end()
        else:
            print("You may be divine, but that was not on the menu.")
            end()
    else:
        print("Cats are carnivores, anything else is unacceptable.")
        end()

def dog():
    print("""Hello, Cerberus. It's a lovely day in the underworld.
    Pawsephone has told you to do something. Do you listen, yes or no?""")
    task = input()
    if task == "yes":
        print("Travel to the Roman Empire. Defeat Hannibal Barka in Cannae!")
        end()
    elif task == "no":
        print("Who is a good dog? Not you. Now you will be destined to lose Cleopawtra to Bark Anthony.")
        end()
    else:
        print("Labrathor came to save the day while you hesitated.")
        end()




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
            print("""People are wondering if you will ever bear fruit.
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

def organisms():
    print("Welcome to ancient Greece! Are you a cat, dog, or date tree?")
    org = input()

    if org == "cat":
        cat()
    elif org == "dog":
        dog()
    elif org == "date tree":
        date_tree()
    else:
        print("That was not a recognized option. Please try again.")
        return "Z"
repeat = organisms()

def start_game():
    organisms()
    if repeat == "Z":
        organisms()

start_game()
