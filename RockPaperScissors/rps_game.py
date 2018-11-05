print("choose rock, paper, or scissors")
choice1 = input("Player one chooses: ").lower()
print("****ANTI-CHEATING BUFFER****\n" * 60)
choice2 = input("Player two chooses: ").lower()

print("Rock...Paper...Scissors...SHOOT!")

if choice1 == choice2:
	print("It is a draw!")
elif choice1 == "paper":
	if choice2=="scissors":
		print("Player 2 wins")
	elif choice2=="rock":
		print("Player 1 wins")
elif choice1 == "scissors":
	if choice2=="rock":
		print("Player 2 wins")
	elif choice2=="paper":
		print("Player 1 wins")
elif choice1 == "rock":
	if choice2=="paper":
		print("Player 2 wins")
	elif choice2=="scissors":
		print("Player 1 wins")
else:
	print("Something went wrong.")