class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload 


class OrderSubmittedEvent(Event):
     def __init__(self, customer_name, product_name):
        super().__init__("order_submitted", {"customer_name": Arda  , "product_name":product1 })

class OrderConfirmedEvent(Event):
    def __init__(self, customer_name, product_name):
        super().__init__("order_confirmed", {"customer_name": Arda  , "product_name": product1 })

class OrderRejectedEvent(Event):
    def __init__(self, customer_name, product_name, reason):
        super().__init__("order_rejected", {"customer_name": customer_name, "product_name": product1 , "reason": wrong })

class Store:
    def __init__(self, name, inventory, event_queue):
        self.name = name
        self.inventory = inventory
        self.event_queue = event_queue
