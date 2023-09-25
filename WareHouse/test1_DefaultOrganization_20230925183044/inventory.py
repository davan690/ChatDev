'''
This file contains the Inventory class.
'''
class Inventory:
    def __init__(self):
        self.skateboards = []
    def add_skateboard(self, skateboard):
        self.skateboards.append(skateboard)
    def remove_skateboard(self, skateboard):
        self.skateboards.remove(skateboard)
    def get_skateboards(self):
        return self.skateboards