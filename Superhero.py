class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power} to fight crime!"

class Villain(Superhero):
    def __init__(self, name, power, city, weakness):
        super().__init__(name, power, city)
        self.weakness = weakness

    def use_power(self):
        return f"{self.name} spreads chaos in {self.city} with {self.power}!"

    def reveal_weakness(self):
        return f"{self.name}'s weakness is {self.weakness}."

hero = Superhero("Starflash", "Laser Eyes", "Neon City")
villain = Villain("Darkstorm", "Shadow Manipulation", "Neon City", "Sunlight")

print(hero.introduce())
print(hero.use_power())
print(villain.use_power())
print(villain.reveal_weakness())
