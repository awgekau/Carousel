'''
Author: Kaustubh Khilari
Assignment 4
CMPUT 175
References: https://stackoverflow.com/questions/37774983/clearing-the-screen-by-printing-a-character for ANSI ESC COMMANDS
'''

import json
from circular_dlinked_list import CircularDoublyLinkedList
from art import art
import time

class Carousel:
    
    clearTerminal = "\033[2J" # clears the terminal
    resetCursor = "\033[H" # resets the cursor position to top left of the terminal


    def __init__(self):
        '''
        This function is a constructor method that sets up the carousel list as a CircularDoublyLinkedList.
        '''

        self.carouselList = CircularDoublyLinkedList()


    def readEmojis():
        '''
        This function helps us read the json file and store the data in a dictonary "data, in which we store emojiClass, emojiName
        and emojiSymbol.
        '''

        with open('emojis.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data


    def resetTerminal():
        '''
        This function helps us clear the terminal and reset the cursor to the default position which is top left.
        It does this by combining two ANSI esc commands that we have mentioned before.
        '''

        print(Carousel.clearTerminal + Carousel.resetCursor, end='')


    def getUserInput(self, data):
        '''
        This function helps us get the user input and basically runs the code futher based on various user inputs.
        It does so by tracking the number of times a user inputs something. When the user input = 0, it prompts the user to either add or quit the program.
        Further, if the user inputs something it increments the userInputCount and promts more options which are add, del, info or quit.
        As the user inputs more emojis the count keeps incrementing and once the userInputCout is more than 1, it gives the user option to move left or right in the carousel.

        Max size of the carousel is 5, so this function also helps us by not letting user add more than 5 elements using the isFull() function.
        
        In short, this function helps us add, delete or get info of an emoji in the carousel. It also helps us to move left and right or quit the program.
        
        '''

        userInputCount = 0 
        exitLoop = False
        Carousel.resetTerminal()
        
        while not exitLoop:
            if userInputCount == 0: # no frames in carousel
                userInput = input("Type any of the following commands to perform the action:\n"
                                   "         ADD: Add an emoji frame\n"
                                   "         Q: Quit the program\n").strip().upper()

                if userInput == "ADD":
                    selectedEmoji = False
                    while not selectedEmoji:
                        emojiUserSelected = input("What do you want to add? ").lower()

                        for item in data: 
                            if not selectedEmoji:  
                                if emojiUserSelected in item['emojis'].keys():
                                    selectedEmoji = True

                        if selectedEmoji:
                            for item in data:
                                for emojiName, emojiSymbol in item['emojis'].items():
                                    if emojiName == emojiUserSelected:
                                        self.carouselList.add(emojiSymbol)
                                        currentEmoji = self.carouselList.getCurrentNode().getData()
                                        
                                        Carousel.resetTerminal()
                                        print(art.addingFrame())
                                        time.sleep(1) # helps us display the ASCII art for 1 second before reseting the terminal
                                        Carousel.resetTerminal()
                                        print(art.singleFrame(currentEmoji))
                            userInputCount += 1
                        else:
                            print("Invalid emoji name. Please enter a valid emoji name.")

                elif userInput == "Q":
                    exitLoop = True

                else:
                    print("Invalid menu option. Please choose a valid option from the menu.")
        

            elif userInputCount == 1: # One frame in the carousel
                userInput = input("Type any of the following commands to perform the action:\n"
                                "         ADD: Add another emoji frame\n"
                                "         DEL: Delete the last emoji frame\n"
                                "         INFO: Show frame information\n"
                                "         Q: Quit the program\n>> ").strip().upper()
            
                if userInput == "ADD":
                    selectedEmoji = False
                    while not selectedEmoji:
                        emojiUserSelected = input("What do you want to add? ").lower()

            

                        for item in data:
                            if not selectedEmoji: 
                                if emojiUserSelected in item['emojis'].keys():
                                    selectedEmoji = True

                        if selectedEmoji:
                            selectedSide = False
                            while not selectedSide:
                                side = input("On which side do you want to add the emoji frame (left/right)? ").strip().lower()
                                if side in ["left","right"]:
                                    selectedSide = True
                                else:
                                    print("Invalid side. Please enter either 'left' or 'right'.")
                            
                            Carousel.resetTerminal()
                          
                            for item in data:
                                for emojiName, emojiSymbol in item['emojis'].items():
                                    if emojiName == emojiUserSelected:
                                        if side == "left":
                                            self.carouselList.addLeft(emojiSymbol)
                                        elif side == "right":
                                            self.carouselList.addRight(emojiSymbol)



                                        if side == 'left':
                                            print(art.addSingleLeft())
                                            time.sleep(1)
                                            Carousel.resetTerminal()
                                        elif side == 'right':
                                            print(art.addSingleRight())
                                            time.sleep(1)
                                            Carousel.resetTerminal()

                                        currentEmoji = self.carouselList.getCurrentNode().getData()
                                        previousEmoji = self.carouselList.getPreviousNode().getData()
                                        nextEmoji = self.carouselList.getNextNode().getData()
                                       
                               
                                        print (art.multipleFrames(previousEmoji, currentEmoji, nextEmoji))
                                        userInputCount += 1
                        else:
                            print("Invalid emoji name. Please enter a valid emoji name.")

                elif userInput == "DEL":
                    Carousel.resetTerminal()
                    print(art.singleDeletion())
                    time.sleep(1)

                    Carousel.resetTerminal()
                    if not self.carouselList.isEmpty():
                        self.carouselList.remove(self.carouselList.getCurrentNode().getData())
                        
                        if self.carouselList.isEmpty():
                            Carousel.resetTerminal()
                        else:
                            Carousel.resetTerminal()
                            self.carouselList.current = self.carouselList.getCurrentNode().getPrevious()

                            currentEmoji = self.carouselList.getCurrentNode().getData()
                            previousEmoji = None
                            nextEmoji = None

    
                            if self.carouselList.getCurrentNode().getPrevious() is not None:
                                previousEmoji = self.carouselList.getPreviousNode().getData()
                            else:
                                previousEmoji = None

                            if self.carouselList.getCurrentNode().getNext() is not None:
                                nextEmoji = self.carouselList.getNextNode().getData()
                            else:
                                nextEmoji = None
                            
                            if self.carouselList.size == 1:
                                print (art.singleFrame(currentEmoji))
                            else:
                                print (art.multipleFrames(previousEmoji, currentEmoji, nextEmoji))
                    userInputCount -= 1

                elif userInput == "INFO":
                    if self.carouselList.getCurrentNode() is not None:
                        currentEmoji = self.carouselList.getCurrentNode().getData()
                    else:
                        currentEmoji = None
                    if currentEmoji:
                        found = False 
                        for item in data:
                            emojiClass = item['class']
                            for emojiName, emojiSymbol in item['emojis'].items():
                                if emojiSymbol == currentEmoji and not found:
                                    print(f"Object: {emojiName}\n"
                                        f"Sym: {emojiSymbol}\n"
                                        f"Class: {emojiClass}\n")
                                    found = True 
                        input("Click any button to continue.")

                        Carousel.resetTerminal()
                        
                        print(art.singleFrame(currentEmoji))
                                                       
                elif userInput == "Q":
                    exitLoop = True

                else:
                    print("Invalid menu option. Please choose a valid option from the menu.")
                
            elif userInputCount > 1: # more than one frame in carousel
                if not self.carouselList.isFull(): 
                    userInput = input("Type any of the following commands to perform the action:\n"
                                    "         L : Move Left\n"
                                    "         R : Move Right\n"
                                    "         ADD: Add another emoji frame\n"
                                    "         DEL: Delete the last emoji frame\n"
                                    "         INFO: Show frame information\n"
                                    "         Q: Quit the program\n>> ").strip().upper()
                
                elif self.carouselList.isFull():
                    userInput = input("Type any of the following commands to perform the action:\n"
                                    "         L : Move Left\n"
                                    "         R : Move Right\n"
                                    "         DEL: Delete the last emoji frame\n"
                                    "         INFO: Show frame information\n"
                                    "         Q: Quit the program\n>> ").strip().upper()

                    
                if userInput == "ADD":
                    if self.carouselList.isFull():
                        print("You cannot add emojis! Carousel is Full.")
                    else:
                        selectedEmoji = False
                        while not selectedEmoji:
                            emojiUserSelected = input("What do you want to add? ").lower()


                            for item in data:
                                if not selectedEmoji:
                                    if emojiUserSelected in item['emojis'].keys():
                                        selectedEmoji = True

                            if selectedEmoji:
                                selectedSide = False
                                while not selectedSide:
                                    side = input("On which side do you want to add the emoji frame (left/right)? ").strip().lower()
                                    if side in ["left","right"]:
                                        selectedSide = True
                                    else:
                                        print("Invalid side. Please enter either 'left' or 'right'.")
                                
                                Carousel.resetTerminal()
                            
                                for item in data:
                                    for emojiName, emojiSymbol in item['emojis'].items():
                                        if emojiName == emojiUserSelected:
                                            if side == "left":
                                                self.carouselList.addLeft(emojiSymbol)
                                            elif side == "right":
                                                self.carouselList.addRight(emojiSymbol)


                                            if side == 'left':
                                                print(art.addMultipleLeft(previousEmoji, nextEmoji))
                                                time.sleep(1)
                                                Carousel.resetTerminal()
                                            elif side == 'right':
                                                print(art.addMultipleRight(previousEmoji, nextEmoji))
                                                time.sleep(1)
                                                Carousel.resetTerminal()



                                            currentEmoji = self.carouselList.getCurrentNode().getData()
                                            previousEmoji = self.carouselList.getPreviousNode().getData()
                                            nextEmoji = self.carouselList.getNextNode().getData()
                                            
                                            print (art.multipleFrames(previousEmoji, currentEmoji, nextEmoji))
                                            userInputCount += 1
                            else:
                                print("Invalid emoji name. Please enter a valid emoji name.")

                elif userInput == "DEL":
                    Carousel.resetTerminal()
                    print(art.multipleDeletion(previousEmoji, nextEmoji))
                    time.sleep(1)

                    Carousel.resetTerminal()

                    if not self.carouselList.isEmpty():
                        self.carouselList.remove(self.carouselList.getCurrentNode().getData())
                        
                        if self.carouselList.isEmpty():
                            Carousel.resetTerminal()
                        else:
                            Carousel.resetTerminal()
                            self.carouselList.current = self.carouselList.getCurrentNode().getPrevious()

                            currentEmoji = self.carouselList.getCurrentNode().getData()
                            previousEmoji = None
                            nextEmoji = None


                            if self.carouselList.getCurrentNode().getPrevious() is not None:
                                previousEmoji = self.carouselList.getPreviousNode().getData()
                            else:
                                previousEmoji = None

                            if self.carouselList.getCurrentNode().getNext() is not None:
                                nextEmoji = self.carouselList.getNextNode().getData()
                            else:
                                nextEmoji = None
                            
                            if self.carouselList.size == 1:
                                print(art.singleFrame(currentEmoji))
                            else:
                                print (art.multipleFrames(previousEmoji, currentEmoji, nextEmoji))

                    userInputCount -= 1

                elif userInput == "INFO":
                    if self.carouselList.getCurrentNode() is not None:
                        currentEmoji = self.carouselList.getCurrentNode().getData()
                    else:
                        currentEmoji = None
                    if currentEmoji:
                        found = False
                        for item in data:
                            emojiClass = item['class']
                            for emojiName, emojiSymbol in item['emojis'].items():
                                if emojiSymbol == currentEmoji and not found:
                                    print(f"Object: {emojiName}\n"
                                        f"Sym: {emojiSymbol}\n"
                                        f"Class: {emojiClass}\n")
                                    found = True 
                        input("Click any button to continue.")
                        
                        Carousel.resetTerminal()
                        
                        print(art.multipleFrames(previousEmoji, currentEmoji, nextEmoji))

                elif userInput == "L":
                    Carousel.resetTerminal()
                    print(art.movingLeft(previousEmoji, nextEmoji))
                    time.sleep(1)
                    Carousel.resetTerminal()

                    self.carouselList.current = self.carouselList.getCurrentNode().getPrevious()
                    
                    previousEmoji = None
                    nextEmoji = None

                    if self.carouselList.getCurrentNode().getPrevious() is not None:
                        previousEmoji = self.carouselList.getPreviousNode().getData()


                    if self.carouselList.getCurrentNode().getNext() is not None:
                        nextEmoji = self.carouselList.getNextNode().getData()

                    currentEmoji = self.carouselList.getCurrentNode().getData()
                    
                    Carousel.resetTerminal

                    print(art.multipleFrames(previousEmoji, currentEmoji, nextEmoji))
                
                elif userInput == "R":
                    Carousel.resetTerminal()
                    print(art.movingRight(previousEmoji, nextEmoji))
                    time.sleep(1)
                    Carousel.resetTerminal()


                    self.carouselList.current = self.carouselList.getCurrentNode().getNext()
                    

                    previousEmoji = None
                    nextEmoji = None


                    if self.carouselList.getCurrentNode().getPrevious() is not None:
                        previousEmoji = self.carouselList.getPreviousNode().getData()

                    if self.carouselList.getCurrentNode().getNext() is not None:
                        nextEmoji = self.carouselList.getNextNode().getData()


                    currentEmoji = self.carouselList.getCurrentNode().getData()
                   
                    Carousel.resetTerminal()

                    print(art.multipleFrames(previousEmoji, currentEmoji, nextEmoji))

                elif userInput == "Q":
                    exitLoop = True
                else:
                    print("Invalid menu option. Please choose a valid option from the menu.")


if __name__ == "__main__":
    emojiData = Carousel.readEmojis()
    myCarousel = Carousel()
    myCarousel.getUserInput(emojiData)

