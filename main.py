class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload 

class Store:
    def __init__(self, inventory):
        self.inventory = inventory
