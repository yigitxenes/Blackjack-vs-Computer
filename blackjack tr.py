import random
player = 0
computer = 0
card = random.randint(1,11)
player += card
print("your number: ", player)
card = random.randint(1,11)
computer += card
print("house is: ", computer)
card = random.randint(1,11)
player += card
card = random.randint(1,11)
computer += card
print()
print("your card is: ",player)

while True and player < 21:
    decide = input("Hit or Stand  ")
    card = random.randint(1, 11)
    print()
    if player == 21 and computer != 21:
        print("you won")
        break

    elif player > 21:
        print("lost")

    elif decide.lower() == "stand":
        break

    elif decide.lower() == "hit":
        player += card
    print("your card is: ", player)
if player>21:
    print("you lost")
    quit()
while True:
    card = random.randint(1, 11)

    if computer<=16:
        computer += card
        if computer>16 and player<=21 and player>computer:
            print("you won")


    elif computer == 21 and player != 21:
        print("house is ", computer)
        print("House always wins ")
        break

    elif computer>21 and player <21:
        print("You won")
        print("house is", computer)
        break

    elif player >21 and computer<21:
        print("house is : ", computer)
        print("House always wins ")
        break

    elif player<21 and computer<21 and computer>player:
        print("house is: ",computer)
        print("House always wins")
        break

    else:
        print("house is: ", computer)
        break
if computer == player:
    print("Draw ")
