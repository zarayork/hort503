#Instantiates the class "Parent."
class Parent(object):
    #Override.
    def override(self):
        print("PARENT override()")
    #Not an override.
    def implicit(self):
        print("PARENT implicit()")
    #This alters the function.
    def altered(self):
        print("PARENT altered()")
#Instantiates the class "Child."
class Child(Parent):
    #Override.
    def override(self):
        print("CHILD override()")
    #This alters the function.
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        #This inherits from two classes and alters to ensure the functions still work.
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
#Instantiates object "dad" that runs the function "Parent".
dad = Parent()
#Instantiates object "son" that runs function "Child."
son = Child()
#These automatically inherit the function.
dad.implicit()
son.implicit()
#These override the function which causes a different behavior.
dad.override()
son.override()
#These alter the function.
dad.altered()
son.altered()
