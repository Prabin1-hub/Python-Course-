correct_answer = "Tokyo"
attempts = 0
max_attempts = 5

while True:
    answer = input("What is the capital of Japan?\n ")
    attempts += 1  

    if answer == correct_answer:  
        print("Correct! Well done.")
        break  

    if attempts == max_attempts:  
        print("Sorry, the correct answer is Tokyo.")  
        break  

    print(f"Incorrect. Attempts: {attempts}/{max_attempts}")