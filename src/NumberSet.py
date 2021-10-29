import random



class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.__maxNum = size
        self.__cardNumbers = []
        self.__placeHolder = 0
        for i in range(1, self.__maxNum+1):
            self.__cardNumbers.append(i)
        self.randomize()



    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return len(self.__cardNumbers)

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        if index >= 0 and index < self.getSize():
            return self.__cardNumbers[index]
        else:
            return None


    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.__cardNumbers)

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        if self.__placeHolder < self.getSize():
            val = self.__cardNumbers[self.__placeHolder]
            self.__placeHolder += 1
            return val
        else:
            return None

    def resetIndex(self):
        self.__placeHolder = 0

