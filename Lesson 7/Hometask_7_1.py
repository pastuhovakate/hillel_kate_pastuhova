class Car():
    
    def __init__(self, model, year_of_man, maker, volume, color, price):

        self.model = model
        self.year_of_man = year_of_man
        self.maker = maker
        self.volume = volume
        self.color = color
        self.price = price

    def print_description (self):
        print = (f"Short description: \nMaker:{self.maker}\nModel: {self.model}\nPrice: {self.price}")
        return print
    
    def print_full_description (self):
        print = (f"Full description: \nModel: {self.model} \nMaker: {self.maker}\nYaer of manufcture: {self.year_of_man}\
             \nPrice: {self.price}\nVolume: {self.volume}\nColor:{self.color}")
        return print
    
    def print_short_description (self):
        return self.print_description()

car1 = Car("Audi TT", 2019, "Audi", 400, "blue", 67000)
car2 = Car("MINI Cooper", 2013, "BMW", 200, "yellow", 9000)

print (car2.print_short_description())

print (car1.print_full_description())
