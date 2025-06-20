class Inventory:
    def __init__(self):
        self.products = {} 
    def add_product(self, product_id, name, quantity, price):
        """Adds or updates a product."""
        if product_id in self.products:
            self.products[product_id]["quantity"] += quantity
            print(f"Updated {name}: New quantity is {self.products[product_id]['quantity']}")
        else:
            self.products[product_id] = {"name": name, "quantity": quantity, "price": price}
            print(f"Added product: {name}")

    def get_product(self, product_id):
        """Get details of a specific product."""
        return self.products.get(product_id, "Product not found")

    def get_low_stock(self, threshold):
        """Get products with stock below a threshold."""
        return {pid: data for pid, data in self.products.items() if data["quantity"] < threshold}

inventory = Inventory()
inventory.add_product(101, "Laptop", 10, 70000)
inventory.add_product(102, "Mouse", 50, 500)
inventory.add_product(103, "Keyboard", 5, 1500)
inventory.add_product(104,"Monitor", 9, 5000)

print(inventory.get_product(101))  
low_stock = inventory.get_low_stock(10)
print(low_stock)  
