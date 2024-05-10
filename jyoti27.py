from random import randint

comp_num = randint(0,10)
guess_num = int(input("Enter a number between 1 to 10 :  "))


if (guess_num==comp_num):
 print("Congratulations you have guessed correct")
elif(guess_num < comp_num):
 print("You guessed a smaller number")
elif(guess_num > comp_num):
 print("You guessed a higher number")
else:
 print("Try again......")

