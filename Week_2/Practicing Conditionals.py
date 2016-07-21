number = 79
user_guess = input("Guess the number: ")
while number != int(user_guess):
	if number < int(user_guess) or number > int(user_guess):
		print("Your guess is wrong.")
		user_guess = input("try again: ")

if number == int(user_guess):
	print("Yeah!")
	print("Nope.")