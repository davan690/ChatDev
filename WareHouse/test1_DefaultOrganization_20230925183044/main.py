'''
This is the main file of the skateboard company software.
'''
import tkinter as tk
from tkinter import messagebox
from gui import SkateboardForm
from inventory import Inventory
class SkateboardCompanyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Skateboard Company")
        self.geometry("800x600")
        self.inventory = Inventory()
        self.create_widgets()
    def create_widgets(self):
        self.skateboard_form = SkateboardForm(self, self.inventory)
        self.skateboard_form.pack()
    def show_message(self, message):
        messagebox.showinfo("Message", message)
if __name__ == "__main__":
    app = SkateboardCompanyApp()
    app.mainloop()