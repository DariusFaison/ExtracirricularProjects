import random

play = input("Do you want to play Rock, Paper, Scissors? Y or N: ")
while play == "Y":  #While loop that starts the game
	print("First to 3 wins!")
	p1_score = 0
	cpu_score = 0
	
	while (p1_score != 3) and (cpu_score != 3): #While that begins once the game starts, keep track of scores
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
				cpu_score += 1
			elif choice2=="scissors":
				print("Player 1 wins")
				p1_score += 1
		elif choice1 == "paper":
			if choice2=="scissors":
				print("Computer wins")
				cpu_score += 1
			elif choice2=="rock":
				print("Player 1 wins")
				p1_score += 1
		elif choice1 == "scissors":
			if choice2=="rock":
				print("Computer wins")
				cpu_score += 1
			elif choice2=="paper":
				print("Player 1 wins")
				p1_score += 1
		else:
			print("Something went wrong.")
			
		print(f"PLAYER 1: {p1_score} \n CPU: {cpu_score}")
		#End of second while loop
		if p1_score == 3:
			print("YOU WIN!")
		elif cpu_score == 3:
			print("CPU WINS!")
	play = input("Would you like to play again? Y or N: ")
	#End of first while loop