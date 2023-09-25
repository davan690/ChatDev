'''
This file contains the GUI components of the application.
'''
import tkinter as tk
from skateboard import Skateboard
class SkateboardForm(tk.Frame):
    def __init__(self, parent, inventory):
        super().__init__(parent)
        self.inventory = inventory
        self.brand_label = tk.Label(self, text="Brand:")
        self.brand_entry = tk.Entry(self)
        self.model_label = tk.Label(self, text="Model:")
        self.model_entry = tk.Entry(self)
        self.price_label = tk.Label(self, text="Price:")
        self.price_entry = tk.Entry(self)
        self.add_button = tk.Button(self, text="Add Skateboard", command=self.add_skateboard)
        self.brand_label.pack()
        self.brand_entry.pack()
        self.model_label.pack()
        self.model_entry.pack()
        self.price_label.pack()
        self.price_entry.pack()
        self.add_button.pack()
    def add_skateboard(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        price = self.price_entry.get()
        skateboard = Skateboard(brand, model, price)
        self.inventory.add_skateboard(skateboard)
        app.show_message("Skateboard added successfully!")
        self.brand_entry.delete(0, tk.END)
        self.model_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)