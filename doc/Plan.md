# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

This problem aims to create a deck of bingo cards (min: 2, max: 8192) based on user input
Each card will have between (3, 16) rows, based on user input
Each card will be a square, so if 3 is input, then it would be 3x3. I'm not sure how to do this yet. Maybe print row by row?
Every card is assigned a unique integer. Assign it the value of whatever card it is eg. 1,4,6... whatever the iteration is
Use getter to retrieve card based on unique ID
Numbers on card must be between 1 and (max val) based on user input
A card cannot contain duplicates of numbers, but cards in a deck can have same numbers
Previous card gets overwritten
"Free" in center of odd number row decks. Find the middle val of both row and column, place there?
Menu options are case sensitive, stick to it
Prompts must display available range for ints
Validate user input
Continue to display prompt until correct format is given
Program cannot construct anything if bad input is given

The biggest problem I can see myself having in this assignment is not knowing how to do the ascii art for the bingo cards

Everything else seems pretty straight forward

## Phase 1: System Analysis *(10%)*

Data needed by the program:
	Size of a card: User input
	Rows in a card: User input
	Maximum number: User input
The output will be pythons standard out, unless they want to save the card to a file--in that case there will be no output

Algorithms and formulas:
class Card()
	getId()
	getSize()
	getSquare(row, col)
	print()

class Deck()
	getCardCount()
	getCard()
	print()

class Menu()
	addOption()
	__isValidCommand()
	getOption()
	getHeader()
	getOptionCount()
	show()

class MenuOption()
	getCommand()
	getDescription()

class NumberSet()
	getSize()
	get()
	randomize()
	getNext()

class UserInterface()
	run()
	createDeck()
	getIntegerInput()
	getStringInput()
	deckMenu()
	printCard()
	saveDeck()
		

## Phase 2: Design *(30%)*

**Deliver:**

UserInterface():
__createDeck():
	prompt user to input card size (int)
	prompt user to input max number (int)
	prompt user to input number of cards (int)
	
	deck = Deck(cardSize, cardCount, numberMax)
	command = menu.show()
__getIntegerInput(prompt, m, n):
	prompt user for integer input
	if is digit and <m and >n, convert to int and return
__getStringInput(prompt):
	promput user for string
	return it
__saveDeck():
	i'm unsure how to create a file, will research

NumberSet():
getSize():
	card.getSize() ** 2
get(index):
	unsure of necessity of get and getNext
randomzie():
	random.shuffle(index)
getNext():
	pop?

Deck():
getCardCount():
	return cardCount

Card():
getId():
	return card number
getSize():
	return card row length
getSquare():
	unsure, will ask
print():
	unsure, will ask

## Phase 3: Implementation *(15%)*

I learned a lot more about interaction between classes, especially passing different class objects in as parameters
Something that didn't go to plan was when I initially designed my get next, everytime I would call a card to print, it would change
because it would pick up where it left off in the list instead of starting over at the beginning of the index. 
Something else that didn't go to plan was my printCard. I learned a lot about format strings so that the numbers would print out in
an even grid despite being different character lengths.

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
____________________________________________________________________________________________________________
The test cases that are included in the starter code ran on my computer. Since I didn't change the class structure or any of the method
functionality, the test cases applied. 
NumberSet Tests:
	Tests if the number size is the same as what was passed in: Passed
	Tests out of bound numbers, if the number is out of bounds, returns none, passed.
	Tests getNext function by pulling numbers out of numberlist, and then returns none when it runs out of numbers. Passed
	Tests duplicates: Tests if there are any duplicates. Passed
Card Tests:
	Setup failed, as the way numberSet would get called was the actually object. Number set was coded to create the set in the initilizer, and then pass the actual object.
	problem was resolved by just passing in the max number to NumberSet
	Tests get size: Passed
	Tests getID: Passed
	Tests free square: Failed at first, as I incorporated free square into the print function, so it wasn't getting detected. I just copy pasted my code into getSquare and it passed.
	Tests duplicates: Passed
Deck Tests:
	Tests get card count: Passed
	Tests getting individual card from deck: Passed
Menu Tests:
	I didn't modify menu at all, so the tests passed without problem.

## Phase 5: Deployment *(5%)*

## Phase 6: Maintenance

The sloppiest part of my program is getting integer input, and printing a card to the screen. These were 2 functions I struggled with, so
its not as well written and thought out as I might have hoped.
However, there are no parts of the program that I don't understand. 
If a bug was reported, it would be very easy to find, as I used all the different classes and methods included, so no method or class does
everything, making it easy to locate where the issue may be

My documentation should make sense, as I tried to write it in as plain of language as possible. 
It should still make sense to me in 6 months.

It will be very easy to add new features, since as mentioned above, it was all made using the classes. All it would take is adding a new
class or method

Since everything was written using standard python, it will still work despite any changes that may get made. If anything, it will run
faster if upgrading the hardware. 