import random
### gauss number
for x in range(1,6):
    geussNumber=input("Enter Your gauss between 1 to 5 : ")

    randomNumber = random.randint(1,5)  # random import 

    if geussNumber == randomNumber:
        print("You Have Win")
    else:
        print("You are lost")
        print("Random number was : ",randomNumber)


##user input from 

n=input(":Enter list item : ")

list=n.split()
print(list)
