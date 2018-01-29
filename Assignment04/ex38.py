ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar

#Study Drills
plant_tissues = ['Flower', 'Stem', 'Leaf', 'Flag_leaf', 'Whole_root', 'Mature_root', 'Root_tip', 'Above_ground', 'Seed', 'Pollen']
below_ground = plant_tissues[4:7]
vegetative = plant_tissues[0:4]
reproductive = plant_tissues[8:10]
print("Below ground:", below_ground)
print("Vegetative:", vegetative)
print("Reproductive:", reproductive)
print("Trial tissues:", ' '.join(plant_tissues[0:7]))
