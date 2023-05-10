import random
import time

print("""**********************
      
Game of guess a number

Know the number between of 1 to 40

If you want to quit, enter the 0...

**************************
""")

randomNumber = random.randint(1,40)
geuessing_right = 5

while True:
    
    guess = int(input("Please enter the guess number : "))
    
    if (guess == 0):
        print ("game ending..")
        time.sleep(1)
        break 
    
    if (guess < randomNumber):
        print("Number check...")
        time.sleep(1)
        print("Please enter more higher another number.")
        geuessing_right -= 1
        
    elif (guess > randomNumber):
        print("Number check...")
        time.sleep(1)
        print("Please enter more lower another number.")
        geuessing_right -= 1
    else:
        print("Number check...")
        time.sleep(1)
        print("!!!COGULARITIONS!!! You found the number... Your number is : ",guess)
    if (geuessing_right == 0):
        print("YOU LOST THE GAME.. NO MORE CHANCE TO KNOW.. TRY AGAIN..")
       
