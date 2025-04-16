class Animal:
    def move(self):
        return "The animal moves."

class Bird(Animal):
    def move(self):
        return "Flying in the sky. 🐦"

class Fish(Animal):
    def move(self):
        return "Swimming in the water. 🐟"

class Cheetah(Animal):
    def move(self):
        return "Running fast on land. 🐆"

animals = [Bird(), Fish(), Cheetah()]

for a in animals:
    print(a.move())
