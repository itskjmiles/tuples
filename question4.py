# Sample order data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 1),
    ("David", "Headphones", 3),
    ("Emma", "Tablet", 2),
]

for index, (customer, product, quantity) in enumerate(orders, 1):
    print(f"Order {index}:")
    print(f"Customer: {customer}")
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print() 
