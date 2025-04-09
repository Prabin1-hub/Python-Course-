products = [
    {"name": "ASUS_Laptop", "price": 1000},
    {"name": "Samsung", "price": 500},
    {"name": "Headphones", "price": 100},
    {"name": "Keyboard", "price": 50}
]


delivery_companies = [
    {"name": "Standard Delivery", "fee": 20},
    {"name": "overnight Delivery", "fee": 50},
    {"name": "Premium Delivery", "fee": 100}
]

print("Available Products:\n")
for index, product in enumerate(products):
    print(f"{index}. {product['name']} - ${product['price']}")

product_index = int(input("Enter the index of the product you want to buy: "))
selected_product = products[product_index]

print("Delivery Options:\n")
for index, company in enumerate(delivery_companies):
    print(f"{index}. {company['name']} - ${company['fee']}")

delivery_index = int(input("Enter the index of the delivery option you want to choose: "))
selected_delivery = delivery_companies[delivery_index]

total_cost = selected_product["price"] + selected_delivery["fee"]
print(f"total cost is ${total_cost}")

print(f"you have selected {selected_product["name"]} with {selected_delivery["name"]}")


