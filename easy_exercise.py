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

for index, product in enumerate(products):
    print(f"{product["name"]} press {index}")

while True:
    product_index = input("please enter the product number:\n")
    try:
        product_index = int(product_index)
        if product_index >0 and product_index < len(products):
            break
        else:
            print("This product does not exist")
    except ValueError:
        print("please enter a number")

selected_product = products[product_index]



while True:
    product_index = input("please enter the product number:\n")
    try:
        product_index = int(product_index)
        if product_index >0 and product_index < len(products):
            break
        else:
            print("This product does not exist")
    except ValueError:
        print("please enter a number")

selected_product = product[product_index]
