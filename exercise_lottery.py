user_numbers = set()

while len(user_numbers) < 7:
    try:
        num = int(input(f"Enter number: {len(user_numbers)+1}/7\n"))
        
        if num in user_numbers:
            print("Error: This number already exists in the set.")
        else:
            user_numbers.add(num)
    except ValueError:
        print("Error: Please try again.")


for num in user_numbers:
  print(num)
