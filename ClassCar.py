class Car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

        
def get_type(self):
    return self.type

def get_manufacturer(self):
    return self.manufacturer

def fullspecs(self):
    return f"Model: {self.model}, Year: {self.year}, Color: {self.color}, " \
            f"Type: {self.type}, Manufacturer: {self.manufacturer}"

car1 = Car("Sports", 2012, "Blue", "Coupe", "Tesla")
car2 = Car("Sedan", 2020, "Black", "Sedan", "Toyota")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color()
print(car1.fullspecs())
print(car2.fullspecs())
