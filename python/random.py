import random

randNum = random.randint(1,20)
userNum = 0
i = 0

while i < 5:
  userNum = int(input("input a number between 1 and 20: "))

  print("My number is " + str(randNum))
  print("Your number is " + str(userNum))

  if randNum == userNum:
    print("You guessed correctly!")
    break
  else: 
    print("wrong number")
    i += 1

if i >= 5:
  print("game over")
