#email = input("Please enter your email address: ")

#print(f"Your email address is: {email}")

#username = input("Enter your username: ")
#age = input("Enter your age: ")
#print(f"Welcome {username} {age}")

#games = ["GTA", "Overwatch", "Clash of Clan", "COD"]

#for game in games:
    #print(game)

#manga_list = [
        #{"title": "One Piece", "volumes": 108},
        #{"title": "Attack On Titan", "volumes": 34},
        #{"title": "One-Punch Man", "volumes": 30}
    #]

#for index, manga in enumerate(manga_list):
        #print(f"{index}. {manga['title']} = {manga['volumes']} volumes")



#numbers = []

#while True:
        #user_input = input("Enter a number or press enter to stop: ")
        #if user_input == "":
            #break
        #try:
           # numbers.append(float(user_input))
        #except ValueError:
            #print("Please enter a valid number.")

#if numbers:
        #choice = input("print max number (press 1) or min number (press 2)? ")
        #if choice == "1":
            #print(f"The max is: {max(numbers)}")
        #elif choice == "2":
            #print(f"The min is: {min(numbers)}")
        #else:
            #print("Invalid choice.")
#else:
    #print("No numbers were entered.")

    # PIN-based ATM system
#pin = "6666"
#balance = 800.00
#attempts = 3

#while attempts > 0:
        #entered_pin = input("Enter your PIN: ")
        #if entered_pin == pin:
            #while True:
              #  print("\nChoose an option:")
             #   print("1. Deposit")
             #   print("2. Withdraw")
             #   print("3. Check Balance")
            #    print("4. Exit")
             #   choice = input("Enter your choice (1/2/3/4): ")

             #   if choice == "1":
               #     amount = float(input("Enter amount to deposit: $"))
              #      balance += amount
                #    print(f"Deposited: ${amount:}")
              #  elif choice == "2":
                #    amount = float(input("Enter amount to withdraw: $"))
                  #  if amount > balance:
                  #      print("Insufficient funds.")

    
# Inventory storage
#inventory = []

#def add_item():
    #name = input("Enter item name: ")
   # quantity = int(input("Enter item quantity: "))
    #price = float(input("Enter item price: "))

   # print(f"Added item: {name} with quantity: {quantity} and price: ${price:}\n")

   # inventory.append({"name": name, "quantity": quantity, "price": price})


#def main():
   # while True:
    #    print("Choose an option:")
#        print("1. Add Item")
    #    print("2. View Inventory")
     #   print("3. Calculate Total Inventory Value")
     #   print("4. Exit")

      #  choice = input("Enter your choice (1/2/3/4): ")

      #  if choice == '1':
           # add_item()
       # elif choice == '2':
           # view_inventory()
       # elif choice == '3':
           # calculate_total_value()
      #  elif choice == '4':
          #  print("Exiting the program. Goodbye!")
          #  break
      #  else:
        #    print("Invalid choice. Please try again.\n")






                 
       
