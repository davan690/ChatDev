'''
This file contains the Skateboard class.
'''
class Skateboard:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def get_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nPrice: ${self.price}"