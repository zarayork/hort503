#creates a string for open variables
formatter = "{} {} {} {}"
#uses 1-4 as variables
print(formatter.format(1, 2, 3, 4))
#puts strings in to the variables
print(formatter.format("one", "two", "three", "four"))
#inserts "concepts of true and false" not just the word
print(formatter.format(True, False, False, True))
#formatter variable into other strings (will learn more about this later, not clear yet)
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
