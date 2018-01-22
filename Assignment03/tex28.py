#Study Drills
def Amount_of_food(people_attending):
    total_pizzas = people_attending / 4
    print("The event will need at least", total_pizzas, "pizzas" )
    print("How many guests are vegetarian?"); veg = float(input())
    print("The event will need", int(total_pizzas - veg), "meat pizzas and", ((veg / 4) + int(0.1 * people_attending)), "vegetarian pizzas")

print("\nHow many people will be attending?"); people_attending = int(input())
Amount_of_food(people_attending)
