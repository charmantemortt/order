class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name{self.name}-Price{self.price}"

class Order(Item):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items.remove(item_name)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += total + item.price
        return total

    def display_order(self):
        for i in self.items:
            print(i.name)
        print(self.calculate_total())

class Customer:
    def __init__(self, client_name, name, price):
        self.__client_name = client_name
        self.order = Order(name, price)

    def create_order(self): pass

    def add_to_order(self, item):
        self.order.add_item(item)

    def finalize_order(self):
        print("Client name:", self.__client_name, "Item: ", self.order.name, "Price: ", self.order.price)

item1 = Item("Капучино", 3.50)
item2 = Item("Сэндвич", 5.00)
item3 = Item("Торт", 4.75)

customer = Customer("Анна", "Сэндвич", 120, )
# customer.create_order()

customer.add_to_order(item1)
# customer.add_to_order(item2)
# customer.add_to_order(item3)

# customer.order.remove_item("Сэндвич")

print(customer.finalize_order())