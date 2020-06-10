from random import randint

# animals to practice classes, inheritence, and overriding/polymorphism

# the general animal class
class Animal:
    def __init__(self, name, age=randint(1,20), health=randint(20,100), happiness=randint(20,100)):
        self.name = name
        self.age = randint(1,20)
        self.health = randint(20,100)
        self.happiness = randint(20,100)

    def display_info(self):
        return (f"{self.name} is {self.age} years old, whose health is {self.health} and happiness is {self.happiness}")
        
    def feed(self):
        randHealth = randint(1,20)
        randHappy = randint(1,20)
        if self.health + randHealth <= 100:
            self.health += randHealth
        else:
            self.health = 100
        if self.happiness + randHappy <= 100:
            self.happiness += randHappy
        else:
            self.happiness = 100
        return self

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Lion"

    def display_info(self):
        myString = (f"Type: {self.type}, ")
        myString += super().display_info()
        print(myString)

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Tiger"

    def display_info(self):
        myString = (f"Type: {self.type}, ")
        myString += super().display_info()
        print(myString)

class Bear(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Bear"

    def display_info(self):
        myString = (f"Type: {self.type}, ")
        myString += super().display_info()
        print(myString)


# run this if calling this file directly
if __name__ == '__main__':
    tim_bear = Bear("Tim")
    tim_bear.display_info()
    tim_bear.feed()
    tim_bear.display_info()