import random
target=random.randint(1,100)
print("******************************")
while True:
    userchoice=int(input("Guess a number(1 to 100)  ❔ :"))
    if userchoice == target:
        print("Your Guessed number is correct !")
        break
    elif (userchoice < target):
        print("Guess a bigger number.")
    else:
        print("Guess a smaller number.")
print("*****GAME OVER*****")
