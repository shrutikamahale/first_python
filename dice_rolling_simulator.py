import random


min_no = 1
max_no = 6

N = int(input("enter the number of dice you want to roll?"))

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min_no, max_no))
    print (random.randint(min_no, max_no))

    roll_again = int(input("Roll the dices again?"))
    


