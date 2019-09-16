print("Welcome to Text Based Adventure Game!!!")

name = input("Enter your name: ")

print("Hi! " + name + " Welcome to room no 704")

selection = input(print(name + " Do you want to take left or right?\n"))

if (selection == "right"):
    print("keep walking......\n Open the door in front of you...")
    answer = input("you have entered in hall!! what would you like to have....\n Tea \n Coffee\n")
    
    if (answer == "Tea"):
        print("Enjoy your tea")
    elif (answer == "Coffee"):
        suger = input("How many Tea spoons....\n 1 \ 2 \ 3\n")
        
        if(suger == "1"):
            print("Enjoy your coffee")
        else:
    
            print("GOODBYE!!!") 
    else:
        print("you are done!!")


else:
    print("I am sorry no directions for you......")