total = 0

while True:
    try:
        number = int(input("Enter a number (0 to stop): "))
        if number == 0:
            break
        total += number
    except ValueError:
        print("Invalid, please enter only numbers")

print("total sum:", total)
