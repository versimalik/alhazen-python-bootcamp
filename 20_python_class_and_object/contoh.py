class Vehicle:

    name = ""
    brand = ""
    color = ""
    year = ""
    origin = ""
    
    def __init__(self, v_name, v_brand, v_color, v_year, v_origin):
        self.name = v_name
        self.brand = v_brand
        self.color = v_color
        self.year = v_year
        self.origin = v_origin

    def move_forward(self, speed):
        print(f"{self.name} is moving forward {speed} km/h")

    def move_backward(self):
        print(f"{self.name} is moving backward")

    def turn(self, direction):
        print(f"{self.name} is turning {direction}")

monster = Vehicle("Monster", "Ford", "Red", 2010, "America")

monster.move_forward(100)
monster.turn("left")
monster.move_forward(100)
monster.turn("right")
monster.move_backward()