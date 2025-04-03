
max_attempts = 5
user_attempts = 0

while True:
    user_answer = input("What is the capital city of Japan?\n")
    user_attempts += 1


    if (user_answer == "tokyo" or user_answer == "Tokyo"):
        print("Correct answer")
        break
    else:
        print(f"Incorrect answer. Attempt {user_attempts}/{max_attempts}")
        if user_attempts >= max_attempts:
            print("You reach the max attempts")
            break
    