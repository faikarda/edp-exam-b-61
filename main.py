# main.py

class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class OrderSubmittedEvent(Event):
    def __init__(self, customer_name, product_name):
        super().__init__("order_submitted", {"customer_name": customer_name, "product_name": product_name})

class OrderConfirmedEvent(Event):
    def __init__(self, customer_name, product_name):
        super().__init__("order_confirmed", {"customer_name": customer_name, "product_name": product_name})

class OrderRejectedEvent(Event):
    def __init__(self, customer_name, product_name, reason):
        super().__init__("order_rejected", {"customer_name": customer_name, "product_name": product_name, "reason": reason})

class Store:
    def __init__(self, name, inventory, event_queue):
        self.name = name
        self.inventory = inventory
        self.event_queue = event_queue

    def handle_order(self, event):
        product_name = event.payload['product_name']
        customer_name = event.payload['customer_name']

        if product_name in self.inventory and self.inventory[product_name] > 0:
            self.inventory[product_name] -= 1
            confirmation_event = OrderConfirmedEvent(customer_name, product_name)
            self.event_queue.append(confirmation_event)
            print(f"Order confirmed for {customer_name}: {product_name}")
        else:
            rejection_event = OrderRejectedEvent(customer_name, product_name, "Out of stock")
            self.event_queue.append(rejection_event)
            print(f"Order rejected for {customer_name}: {product_name} is out of stock.")

class Customer:
    def __init__(self, name, event_queue):
        self.name = name
        self.event_queue = event_queue

    def place_order(self, product_name):
        order_event = OrderSubmittedEvent(self.name, product_name)
        self.event_queue.append(order_event)
        print(f"Order submitted by {self.name} for {product_name}")

    def handle_order_response(self, event):
        if event.name == "order_confirmed":
            print(f"Great! {self.name} received confirmation for {event.payload['product_name']}")
        elif event.name == "order_rejected":
            print(f"Oh no! {self.name}'s order for {event.payload['product_name']} was rejected: {event.payload['reason']}")
