#print string
print("Mary had a little lamb.")
#print string with variable
print("Its fleece was white as {}.".format('snow'))
#print string
print("And everywhere that Mary went.")
#print . 10 times
print("." * 10) # what'd that do?
#lines 10-21 creates a set of strings
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. Comma is needed because you are creating a new string; if end=' ' is moved up with the other "cheese burger" string creations, then a comma is not needed, just + end
#print strings back to back, creates string that is a space
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
