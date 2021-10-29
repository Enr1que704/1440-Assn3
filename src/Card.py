import sys

import NumberSet


class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.__idNum = idnum
        self.__size = size
        self.numberSet = NumberSet.NumberSet(numberSet)


    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.__idNum

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.__size

    def getSquare(self, row, col):
        """Return the value in the Bingo square at (row, col) """
        index = (row * self.getSize() + col)
        if self.getSize() % 2 == 1:
            if row == self.getSize() // 2 and col == self.getSize() // 2:
                return "Free"
        return self.numberSet.get(index)

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        print("Deck #" + str(self.getId() + 1), file=file)
        spacingSize = len(str(self.getSize()*self.getSize())) + 2
        stringFormat = "{:^" + str(spacingSize) + "s}"
        for i in range(0, self.getSize()):
            for j in range(0, self.getSize()):
                if self.getSize() % 2 == 1:
                    if j == self.getSize() // 2 and i == self.getSize() // 2:
                        freeSpace = "Free"
                        print(stringFormat.format(freeSpace), end='', file=file)
                    else:
                        val = str(self.numberSet.getNext())
                        print(stringFormat.format(val), end='', file=file)
                else:
                    val = str(self.numberSet.getNext())
                    print(stringFormat.format(val), end='', file=file)
            print(file=file)
            print(file=file)
        self.numberSet.resetIndex()

# c1 = Card(1, 5, 200)
# c1.print(file=sys.stdout)