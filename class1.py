#inheritance

#multiple class (parent and child)

class Animal:
    def __init__(self,species):
        self.species=species

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self,name):
        super().__init__(Dog)
        self.name=name

    def make_sound(self):
        return "woof"
    

class Cat(Animal):
    def __init__(self, name):
        super().__init__(Cat)
        self.name=name


    def make_sound(self):
        return "meow"
    

d=Dog("buddy")
c=Cat("tommy")

print(d.species)
print(d.name)
print(d.make_sound())

print(c.species)
print(c.name)
print(c.make_sound())