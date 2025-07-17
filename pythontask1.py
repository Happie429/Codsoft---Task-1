import random
print("welcome to rock ,paper scissors game!")

choices = ["rock","paper","scissors"]

user = input("Enter rock,paper, or scissors:").lower()
computer = random.choice(choices)


print("you chose:",user)
print("computer chose:",computer)

if user == computer:
    print("it is a tie!")
elif(user == "rock" and computer == "scissors")or\
    (user == "paper" and computer == "rock")or\
    (user == "scissors" and computer == "paper"):
    print("congratulations,you win!🥳")
else:
    print("Computer wins!💻")

    
    print("\n thanks for playing🤗")