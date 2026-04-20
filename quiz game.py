print("Welcome to the Quiz Game")

name = input("Enter Your Name: ")

score = 0

q1 = input("1.What's 5 + 3? ")
if q1.lower() == "8":
  print("Correct")
  score += 1
else:
  print("Wrong, The correct answer is 8")

q2 = input("2.How many days in a week? ")
if q2.lower() == "7":
  print("Correct")
  score += 1
else:
  print("Wrong, The correct answer is 7")

q3 = input("3.What is the capital of UK? ")
if q3.lower() == "London":
  print("Correct")
  score += 1
else:
  print("Wrong, The correct answer is London")

q4 = input("4.What's 10 + 10? ")
if q4.lower() == "20":
  print("Correct")
  score += 1
else:
  print("Wrong, The correct answer is 20")

print(name + ", Your Final Score is:", score, "/4")

if score == 4:
  print("Excellent")
elif score == 3:
  print("Very Good")
elif score == 2:
  print("Good")
elif score == 1:
  print("Not bad")
else:
  print("Try again")
