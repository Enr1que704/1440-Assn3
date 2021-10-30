import Deck
import Menu
import math


class UserInterface():
    def __init__(self):
        self.__m_currentDeck = 0

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False

    def __createDeck(self):
        """Command to create a new Deck"""
        cardSize = self.__getIntegerInput("Enter the size of the card [3, 16]: ", 3, 16)
        maxNumber = self.__getIntegerInput("Enter the highest possible value [" + str((3*cardSize*cardSize)) + ", " +
                                           str(math.floor(3.9*cardSize*cardSize)) + "]: ", 3*cardSize*cardSize,
                                           math.floor(3.9*cardSize*cardSize))
        numOfCards = self.__getIntegerInput("Enter the amount of cards [2, 8192]: ", 2, 8192)
        self.__m_currentDeck = Deck.Deck(cardSize, numOfCards, maxNumber)
        self.__deckMenu()


    def __getIntegerInput(self, prompt, m, n):
        """
        Prompt the user for an integer in the range [m, n] INCLUSIVE
        If the provided input is NOT an integer NOR in the range, repeat the prompt
        Otherwise, convert the user's value to an integer and return it.
        """
        min = m
        max = n
        keepGoing = True
        while keepGoing:
            val = input(prompt)
            if val.isdigit():
                val = int(val)
                if val < min or val > max:
                    print("Please enter integer within the range.")
                    keepGoing = True
                else:
                    return val
            else:
                keepGoing = True

    def __getStringInput(self, prompt):
        """
        Prompt the user for a string and return it
        """
        file = input(prompt)
        return file

    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getIntegerInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)

    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name")
        if fileName != "":
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")
