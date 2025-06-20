class Product:
    """Base class to represent a product."""
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_details(self):
        """Get product details."""
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}"

class Sales:
    """Class to track sales of products."""
    def __init__(self):
        self.sales = []  

    def add_sale(self, product, quantity):
        """Add a sale record."""
        total_price = product.price * quantity
        self.sales.append({"product": product, "quantity": quantity, "total_price": total_price})
        print(f"Sale added: {product.name} x {quantity} for {total_price}")

    def get_total_sales(self):
        """Calculate total sales amount."""
        return sum(sale["total_price"] for sale in self.sales)

    def get_sales_report(self):
        """Generate sales report."""
        report = "Sales Report:\n"
        for sale in self.sales:
            report += f"{sale['product'].name}: {sale['quantity']} units - {sale['total_price']} total\n"
        return report


if __name__ == "__main__":
    # Create products
    product1 = Product(1, "Laptop", 70000)
    product2 = Product(2, "Smartphone", 30000)

    sales_tracker = Sales()

    sales_tracker.add_sale(product1, 3)
    sales_tracker.add_sale(product2, 5)

    print("\n" + sales_tracker.get_sales_report())
    print(f"Total Sales: {sales_tracker.get_total_sales()}")
