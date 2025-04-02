correct_password = "ABCD"  
user_password = ""  
attempts = 3  

while attempts > 0 and user_password != correct_password:
    user_password = input("Enter the password: ")
    if user_password != correct_password:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect password. You have {attempts} attempts left. Try again.")
        else:
            print("Access denied. No attempts left.")
    else:
        print("Access granted!")