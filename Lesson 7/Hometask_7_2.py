class Book():
    
    def __init__(self, name, year, publisher, genre, author, price):

        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def print_description (self):
        print = (f"Short description: \nAuthor: {self.author}\nName: {self.name}\nPrice: {self.price}")
        return print
    
    def print_full_description (self):
        print = (f"Full description: \nName: {self.name} \nAuthor: {self.author}\nYaer: {self.year}\
             \nPrice: {self.price}\nGenre: {self.genre}\nPublisher: {self.publisher}")
        return print
    
    def print_short_description (self):
        return self.print_description()

book1 = Book("The Count of Monte Cristo", 1846, "Paris", "historical", "Alexandre Dumas", 3500)
book2 = Book("Mother Night", 1961, "АСТ", "realism" , "Kurt Vonnegut", 250)

print (book2.print_short_description())

print (book1.print_full_description())