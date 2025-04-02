correct_answer = "tokyo"
min_attempt = 0
max_attempt = 5

while min_attempt < max_attempt:  
    answer = input("What is the capital of Japan?\n ")
    
    if answer == correct_answer:  
        print("Correct! Well done.")
        break  
    else:
        min_attempt += 1  
        print(f"Incorrect answer. Number of attempts {min_attempt}/{max_attempt}")

if min_attempt == max_attempt:
    print("Sorry, The correct answer is Tokyo.")
