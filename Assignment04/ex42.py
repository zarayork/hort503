## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

#A dog is-a animal.
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

#A cat is-a animal.
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

# A person has-a object.
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

#An employee is-a person.
class Employee(Person):

    def __init__(self, name, salary):
        #Runs parent class reliably.
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

#A fish is-a object.
class Fish(object):
    pass

#A salmon is-a fish.
class Salmon(Fish):
    pass

##A halibut is-a fish.
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat.
satan = Cat("Satan")

## Mary is-a person.
mary = Person("Mary")

##Mary has-a pet, satan.
mary.pet = satan

##Frank is-a employee that has-a salary of 120000.
frank = Employee("Frank", 120000)

##Frank has-a pet, rover.
frank.pet = rover

##A fish has-a flipper.
flipper = Fish()

##Crouse has=a salmon.
crouse = Salmon()

##Harry has-a halibut.
harry = Halibut()
