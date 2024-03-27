class Person:
    name = ""
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print(f"This person's name is {self.name}")

class Student(Person):
    nis=""
    def __init__(self, name, nis):
        super().__init__(name)
        self.nis = nis

    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    def getInfo(self):
        super().getInfo()
        print(f"{self.name} is a student")
        print(f"{self.name}'s nis is {self.nis}")

student1 = Student("Jaka", "100023424")
print(student1.name, "=", student1.nis)
student1.getInfo()
student1.study("science")