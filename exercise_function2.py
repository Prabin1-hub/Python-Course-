def get_price_with_vat(price):
    return price + (price * 20 / 100)


price = 200 
price_with_vat = get_price_with_vat(price)

print(f"The price including VAT is: {price_with_vat}")

user_price = int(input("Enter the price without VAT:\n"))
# we call the function passing parameters
user_price_with_vat  = get_price_with_vat(user_price)

print(f"Price with vat: {user_price_with_vat}")