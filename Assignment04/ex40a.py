mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# this goes in mystuff.py
def apple():
    print("I AM APPLES!")

import mystuff
mystuff.apple()

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"

import mystuff

mystuff.apple()
print(mystuff.tangerine)

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable
