class GroceryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.quantity} items)"
    
class Cart:
    
    def __init__(self):
        self.inventory = []
    
    def add_item(self, name, quantity):
        for item in self.inventory:
            if item.name == name:
                item += quantity
                return
        
        new_item = GroceryItem(name,quantity)
        self.inventory.append(new_item)
    
    def show_cart(self):
        if not self.inventory:
            print("🛒 Your cart is empty.")
        else:
            print("🛒 Your grocery cart contains:")
            for item in self.inventory:
                print(f" - {item}")
    
    def remove_item(self, name):
        self.inventory = [item for item in self.items if item.name != name]
        
    def clear_cart(self):
        self.inventory = []
        
cart = Cart()

cart.add_item("BBW Perfume", 4)

cart.show_cart()
cart.clear_cart()
cart.show_cart()