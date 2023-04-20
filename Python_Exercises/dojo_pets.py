class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self): #walks the ninjas pet invoking pet play()
        self.pet.play()
        print(f"Good job for walking {self.pet.name}")
    def feed(self): #feeds ninjas pet invoking eat()
        self.pet.eat()
        print(f"Good job for feeding {self.pet.name}")
    def bathe(self): #cleans ninja's pet invoking noise()
        self.pet.noise()
        print(f"Uh oh! {self.pet.name} is being noisy!")

class Pet:
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound
    def sleep(self): #increases pets energy by 25
        self.energy = self.energy + 25
    def eat(self): #increase pets energy by 5 & health by 10
        self.energy = self.energy + 5
        self.health = self.health + 10
    def play(self): #increase pet's health by 5
        self.health = self.health + 5
    def noise(self): #prints out pet's sound
        print(f" {self.name} is being loud! {self.sound}")


pet1= Pet("Marley", "Labrador", ["Tug of War"], 200, 3000, "Woof")
ninja1 = Ninja("John", "Grogan", pet1, "Couches", "Kibble")

ninja1.feed()
ninja1.walk()
ninja1.bathe()

class Labrador(Pet):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()