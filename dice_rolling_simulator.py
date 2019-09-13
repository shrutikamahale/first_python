import random


min = 1
max = 6

N = int(input("enter the number of dice you want to roll?"))

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = int(input("Roll the dices again?"))
    


