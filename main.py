class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload 


class OrderSubmittedEvent(Event):
     def __init__(self, customer_name, product_name):
        super().__init__("order_submitted", {"customer_name": customer_name, "product_name": product_name})
