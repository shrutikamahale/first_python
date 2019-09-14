import random

guess = random.randint(1,20)

user_ip =  int(input("Hi, Guess the number between 1 to 20\n"))

while user_ip != guess:
    print
    if user_ip < guess:
        print("your guess is too low... guess again")
        user_ip = int(input("guess the number betweem 1, 20\n"))
    elif user_ip > guess:
        print("Your guess is too high guess again...")
        user_ip = int(input("guess the number between 1, 20\n")) 
    elif user_ip == guess:
        print("you are correct! Congratulations!!!!")
   
    
