# bigger picture - do you want to play again
play_again = "y"

while play_again != "n":
	# This is a guessing game
	import random

	# computer picks a number from 1 to 10
	random = random.randint(1,10)

	number = int(input("Pick a number between 1 and 10: "))

	# keep going until number is guessed
	while number != random:
		if number > random:
			print("You're too high!")
			number = int(input("Try again: "))
		else:
			print("You're too low!")
			number = int(input("Try again: "))

	print("You guessed it correctly!")

	play_again = input("Do you want to play again? (y/n): ")

	if play_again == "y":
		random = 0
	elif play_again == "n":
		break