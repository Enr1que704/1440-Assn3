Given from Braxton Francom:
This is a great UML! You have accounted for all the appropriate functions/
    methods and from my limited expertise, it appears that all of your data
    return types are accurate. Overall I thought your UML design had very good
    flow. It was hard to find any flaws or things to improve on. I did find
    several minor points that you could implement into your next draft that
    will make your UML all the better!
   
    One small recommendation you could possibly implement is regarding your
    options attribute in the 'Menu' class. You have the data type listed as
    a list, but I believe that instead of putting 'list', the proper UML syntax
    is to put 'list[]'. Again, I'm not totally sure about this, but I thought
    I remember Professor Falor mentioning this in class. Again, take it for what
    it is, but one other thing I did in my UML was I created a boolean isOddNumbered
    attribute in my Card class. I did this to determine if the card needed a free
    space to be printed. If the number given by the user is odd, there will be a
    free space printed, and the opposite is true for even numbers.
   
    Something else I actually noticed as a flaw in my own UML design was that
    in the instructions it states to use 'dotted lines with open arrows'. In my
    own UML, I used solid arrows to connect my classes. I noticed that your design
    also used solid arrows. The good news is this is a very easy fix!

Given from Christian Howell:
Your UML is pretty well done. You have the six classes that were given to us in the starter code clearly outlined and spaced out in an easy to understand fashion. You have the class names clearly labeled, along with the given data members and methods listed out. You also have the data types for the members listed out in the appropriate member: type format. The arrows clearly show how you anticipate each class to interact with the other classes. You have used the plus and minus signs to indicate which methods inside each class are private and which methods are public. Overall, it is a comprehensive and well done UML.

As far as points of improvement, don’t forget to include the plus and minus visibility indicators on the data fields so that you can keep track of which members can be altered from outside the class. Also, there are some methods you have listed that will need to intake arguments and return certain data. It is  important to make sure you state the data type of the arguments inside the parenthesis of the methods, and the data types of the outputting data after a colon; i.e. visibility methodName(argument data types): return data type. This will help to keep track of how data is being transferred between the classes and methods.

I also think the order you have your classes listed is slight off (unless you are deliberately deciding to do it another way). While UserInterface -> Menu -> MenuOption is correct, and Deck -> Card -> NumberSet is correct, I believe that Deck should be used by UserInterface rather than MenuOption. So UserInterface will use both Menu and Deck.

Overall, good UML.

Christian Howell 

