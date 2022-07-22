class Stadium():
    
    def __init__(self, name, year, country, city, place):

        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.place = place

    def print_description (self):
        print = (f"Short description: \nName: {self.name}\nCountry: {self.country}\nCity: {self.city}")
        return print
    
    def print_full_description (self):
        print = (f"Full description: \nName: {self.name} \nCounty: {self.country}\nCity: {self.city}\
             \nPlace: {self.place}\nYear: {self.year}")
        return print
    
    def print_short_description (self):
        return self.print_description()

Stadium1 = Stadium("Dinamo", 1933, "Ukraine", "Kyiv", "Velika Vasilkivska, 55")
Stadium2 = Stadium("Old Trafford", 1933, "UK", "Manchester", "Ashton New Rd, Manchester M11 3FF")

print (Stadium2.print_short_description())

print (Stadium1.print_full_description())