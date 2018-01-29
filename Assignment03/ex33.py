print("Please set maximum:")
max_n = int(input())
print("Please specify incremental increase")
increment = int(input())

def while_loop(max_n):
    i = 0
    numbers = []
    while i < max_n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")

    for num in numbers:
        print(num)

while_loop(max_n)

#Study Drills
numbers = []
for i in range(0, 9, 2):
    print(f"Adding increment to the list.")
    i = i + int(increment)
    numbers.append(i)
    print(numbers)
