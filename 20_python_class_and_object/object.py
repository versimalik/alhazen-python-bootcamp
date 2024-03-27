class Animal:
    name = ""
    color =""

    def makeSound(self, sound):
        print(f"{self.name} is {sound}")

cat = Animal()
cat.name = "Max"
cat.color = "Yellow"

print(f"My cat's name is {cat.name}")
print(f"Its color is {cat.color}")
cat.makeSound("Meowing")

