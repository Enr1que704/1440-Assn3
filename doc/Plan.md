# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

*   A detailed written description of the problem this program aims to solve.
*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
_____________________________________________________________________________
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

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).
_____________________________________________________________________________
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

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.
_________________________________________________________________________________
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

**Deliver:**

*   (More or less) working Python code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to
        *   anybody besides yourself?
        *   yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading
        *   your computer's hardware?
        *   the operating system?
        *   to the next version of Python?
