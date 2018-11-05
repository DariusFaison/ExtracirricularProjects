import random
print("choose rock, paper, or scissors")
choice1 = input("Player one chooses: ").lower()
computer = random.randint(0,2)

if computer == 0:
	choice2 = "rock"
elif computer == 1:
	choice2 = "paper"
elif computer == 2:
	choice2 = "scissors"

print("Rock...Paper...Scissors...SHOOT!")

print("Computer chooses " + choice2 + "!")
	

if choice1 == choice2:
	print("It is a draw!")
elif choice1 == "rock":
	if choice2=="paper":
		print("Computer wins")
	elif choice2=="scissors":
		print("Player 1 wins")
elif choice1 == "paper":
	if choice2=="scissors":
		print("Computer wins")
	elif choice2=="rock":
		print("Player 1 wins")
elif choice1 == "scissors":
	if choice2=="rock":
		print("Computer wins")
	elif choice2=="paper":
		print("Player 1 wins")
else:
	print("Something went wrong.")