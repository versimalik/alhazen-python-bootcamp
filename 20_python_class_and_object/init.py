class Animal:
    name = color = ""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def makeSound(self, sound):
        print(f"{self.name} is {sound}")

    def eat(self, food):
        print(f"{self.name} is eating {food}")

cat = Animal("Max", "White")
print(cat.name)
cat.makeSound("meowing")
cat.eat("fish")

bird = Animal("Tweety", "Blue")
bird.makeSound("chirping")
bird.eat("corn")

