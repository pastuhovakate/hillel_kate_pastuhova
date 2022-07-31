class Product:
    def __init__(self, name, color, price, amount, discount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name}/{self.color}: {self.price} | {self.amount}"

    def show_description(self):
        print(f"Description: {self.get_product_description()}")

    def  get_price(self):   
         dis_price = self.price - ((self.price * self.discount)/100)
         print(self.name + " Discounted price: " + str(dis_price))

class Phone(Product):
    def __init__(self, name, color, price, amount, discount, lte=False,):
        super().__init__(name, color, price, amount, discount)
        self.lte = lte

    def get_product_description(self):
        additional = ", LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional

        return message

    # def show_description(self):
    #     # if self.lte is True:
    #     #     additional = "LTE"
    #     # else:
    #     #     additional = ""
    #     additional = "LTE" if self.lte else ""
    #     print(f"Description: {self.name}/{self.color}: {self.price} | {self.amount}, {additional}")


class Laptop(Product):
    def __init__(self, name, color, price, amount, discount, motherboard_type, material ):
        super().__init__(name, color, price, amount, discount)
        self.motherboard_type = motherboard_type
        self.material = material

    
    def show_details(self):
        print(f"Description: {self.name}/{self.color}, {self.motherboard_type}, {self.material}: {self.price} | {self.amount}")
         


iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1, discount = 5.0 )
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, lte=True, discount = 10.2)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1, discount = 7.4, motherboard_type="ATX", material="plastic")

iphone13.show_description()
iphone7.show_description()
lenovo.show_details()
iphone13.get_price()
iphone7.get_price()
lenovo.get_price()