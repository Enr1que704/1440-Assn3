# Bingo! User Manual

**Your instructions go here**
How to run the program:
Open git bash, and using the command cd DIRECTORY, navigate to the directory that the bingo.py file is located in
type "python bingo.py"
The program will start

Menus:
You will be presented with multiple menus in the following order:
NOTE: all of the following commands are case sensitive
	Main menu:
	Enter a main command:
		Options (C, X)
			C - create new deck
			X - Exit program
	Enter card size:
		Integer from [3, 16]
	Enter max number:
		Integer from [(3 * cardSize * cardSize),floor(3.9*cardSize*cardSize)]
	Enter number of cards:
		Integer from [2,8192]
	Deck menu:
		P - print card to screen
		D - display whole deck
		S - save whole deck to file
		X - exit

		if "P" is entered, it will ask which card in the range of the deck size you will wish to print
		if "D" is entered, it will display all the cards in the deck to the screen
		if "S" is entered, it will ask what what the file input name is
			you will then enter the file name. The file will be saved in the CWD.
		if "X" is selected, user will be directed to Main Menu, and will be presented with the option to create new card, or exit program.

		NOTE: All deck and card data will be lost if you leave the deck menu

for the menus such as card size, max number, and number of cards, a range of possible values will be presented. 
	proper input consists of an integer number within the range presented
Possible error messages can only be presented if invalid characters are used when a file name contains invalid characters (these limitations are from the system)
	If this error is presented, the program will crash naturally.

