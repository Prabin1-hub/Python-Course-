marks = []

while True:
    mark = input("Enter your mark or press enter to stop \n")  
    if mark == "": 
        break
    else:
        marks.append(float(mark))
  
if marks:
    total = sum(marks)
    average = total / len(marks)
    print(f"Total marks: {total}")
    print(f"Average marks: {average}")
else:
    print("No marks entered.")
    