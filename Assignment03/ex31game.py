print("""You find $100,000. What do you do?
1. Turn it in to authorities
2. Deposit it into an off shore account
3. Splurge""")

choice = input("~ ")

if choice == "1":
    print("You are an individual with high morals, and that is now a wealthy precinct.")
    print("How do you feel?")
    print("1. That it was the right thing to do.")
    print("2. Maybe I'll take that coice back.")

    morality = input("~ ")

    if morality == "1":
        print("You are free to go about your life and are not at risk of nefarious individuals tracking you down and extracting it from you.")
    elif morality == "2":
        print("""Options: 2. Deposit it into an off shore account
        3. Splurge""")
        choice = input("~ ")
    else:
        print("You have to face your choices sooner or later, you should have made a choice.")


elif choice == "2":
    print("1. Leave the offshore account to accrue interest")
    print("2. Slowly withdraw money and try to avoid getting caught and paying taxes")

    offshore = input("> ")

    if offshore == "1":
        print("You will probably die without ever using it, you should have kept your conscience clear and turned it in.")
    elif offshore == "2":
        print("Have fun with the stress.")
    else:
        print("Not doing anything was not an option. You might need to work on being decisive.")

elif choice == "3":
    print("Splurge")
    print("""1. Buy a fancy car.
    2. Buy a house.
    3. Buy fancy clothes and accessories.
    4. Set up a rescue for animals""")

    spending = input("~")
    if spending == "1":
        print("Ostentatious. You had better hope that it was not money from an unsavory individual.")
    elif spending == "2":
        print("That is not even close to enough for a decent house, maybe property, but the government will notice.")
    elif spending == "3":
        print("Ostentatious. You had better hope that it was not money from an unsavory individual. Now you look like competition that stole the money on purpose.")
    elif spending == "4":
        print("Probably safest, and you can help animals. Good job picking something that won't draw attention.")

else:
    print("You delayed long enough that now you can't turn it in. Your best option is an anonymous donation.")
