import random

"""initiate global variables"""

#open file of 4k words
f = open("4000-most-common-english-words-csv.csv","r")
hangman_dictionary = f.read().splitlines()

#array of wrong letters guessed
letters_wrong = []
#array of right letters guessed
letters_right = []
#number of wrong gueses
num_wrong = 0
#maximum number of wrong guesses allowed
max_wrong = 6
#total guesses
total_guesses = 0
#current word
current_word = ""

for word in hangman_dictionary:
	if len(word)<3:
		hangman_dictionary.remove(word)


"""Pick a new word and initiate letters_guessed,
num_wrong, """

def new_word():
	global num_wrong
	global total_guesses
	global letters_guessed
	global current_word
	global letters_right
	global letters_wrong

	num_wrong = 0
	total_guesses = 0

	word_index = random.randint(0, len(hangman_dictionary)-1)
	current_word = hangman_dictionary[word_index]

	if (len(current_word)<3):
		new_word()

	letters_right = ["_"] * len(current_word)
	letters_wrong = []

	guess()


"""Preconditions: a word has been chosen and a guess has been made
Check if the letter is part of the chosen word
and return the word with all correct letters and blanks
Postconditions: num_wrong and total guesses updated, letters_wrong or letters_right updated"""
def guess():
	global total_guesses
	global current_word
	global letters_right
	global num_wrong

	print "============== GUESS NUMBER " + str(total_guesses + 1) + " =============="
	
	if (num_wrong > 0):
		#print the wrong letters
		print "The following letters are not in your word: " + " ".join(letters_wrong)

	#show the word so far
	print "Your word so far is: " + " ".join(letters_right)
	
	#display remaining moves
	print "You have " + str(max_wrong - num_wrong) + " wrong moves left"

	#prompt the letter input
	letter = raw_input("Guess a letter: ").lower()
	
	#check for valid input
	if (len(letter) != 1 or not letter.isalpha()):
		print "ATTN: You must enter exactly one letter at a time"
		guess()

	#check if letter has already been guessed
	elif(letter in letters_right or letter in letters_wrong):
		print "ATTN: You need to guess a new letter"
		guess()

	#check if letter is in the current word
	elif (letter in current_word):
		# print "The letter " + letter + " is in the word " + str(current_word.count(letter)) + " times"

		#add letter to the letters_right list
		word_substring = current_word
		start_index = 0
		while (letter in word_substring):
			substring_index = word_substring.index(letter)
			index = start_index + substring_index
			letters_right[index] = letter
			start_index = index + 1
			word_substring = word_substring[substring_index + 1:]

		total_guesses += 1

		if ("_" not in letters_right):
			print "Congrats! You won! The word is: " + "".join(current_word)
			print "It took you " + str(total_guesses) + " guesses"
			play_again = raw_input("Want to play again? (Y/N): ").lower()
			if(play_again == "y"): 
				print"Here we go!"
				new_word()
			else: 
				exit()

		else: guess()
	
	#check if letter isn't in word
	elif (letter not in current_word):
		print "The letter '" + letter + "' is not in the word"
		num_wrong += 1
		#check if the user has lost
		if (num_wrong >= max_wrong):
			print "You lost"
			print "The word was: " + current_word
			play_again = raw_input("Want to play again? (Y/N): ").lower()
			if(play_again == "y"): 
				print"Here we go!"
				new_word()
			else: 
				exit()
		
		#the user has not lost, so keep playing
		else:
			letters_wrong.append(letter)
			total_guesses += 1
			guess()


	else: print "something went wrong"

"""initiate game"""
new_word()

