from random import randint

choices = {0:"Rock", 1:"Paper", 2:"Scissors"}

computer = randint(0,2)
user = int(input("What is yor choice: select '1' for Rock, '2' for Paper and '3' for Scissors: ")) - 1

print("You chose--> ", choices[user])
print("Cumputer's choice --> ", choices[computer])

if computer == user:
    print("It is a draw")
elif computer - user == 2:
    print("You win")
elif computer - user == 1 and computer - user == -2:
    print("You loose")
else:
    print("You win")