"""
Trammel May, Trent Dehart, Gene Evans
""" 

""" Problem 1 """ 

import random

class Craps:

  def play(self):
    self.__credits = 100
    self.__isPlaying = self.__wannaPlay()
    while self.__isPlaying:
        self.__handleInput()
        self.__update()
        self.__render()
    showInformation("You cashed out with " + str(int(self.__credits)) + " credits!")
 
  def __render(self):
    if self.__success:
      showInformation("Congratulations!, you now have " + str(int(self.__credits)) + " credits!")
    else:
      showInformation("Sorry, you lost that round. You now have " + str(int(self.__credits)) + " credits.")
    self.__keepPlaying()
    
  def __keepPlaying(self):
    if self.__credits != 0:
      userInput = requestString("Would you like to keep playing? (y/n)")
      if userInput == "n":
        self.__isPlaying = false
        showInformation("See you again soon!")
      elif userInput != "y":
        self.__keepPlaying()
    else:
      showInformation("Sorry, you are currently out of credits to bet.")
      self.__isPlaying = false
    
  def __handleInput(self):
    showInformation("You are the shooter with " + str(int(self.__credits)) + " credits.")
    self.__bet = self.__getBet()
    showInformation("You bet " + str(int(self.__bet)) + " credits! Time to Come Out!")
    
  def __update(self):
    roll = self.__rollPair()
    if roll == 7 or roll == 11:
      self.__success = true
    elif roll == 2 or roll == 3 or roll == 12:
      self.__success = false
    else:
      showInformation("During the point phase the shooter will re-roll until they roll a 7, or their original number: " + str(int(roll)))
      self.__success = self.__pointPhase(roll)
    if self.__success:
      self.__credits = self.__credits + int(self.__bet)
    else:
      self.__credits = self.__credits - int(self.__bet)
    
  def __pointPhase(self, roll):
    newRoll = self.__rollPair()
    if newRoll == roll:
      return true
    elif newRoll == 7:
      return false
    else:
      return self.__pointPhase(roll)
      
  def __getBet(self):
    bet = requestNumber("You have " + str(int(self.__credits)) + " credits. How much would you like to bet? (2-100)")
    if bet <=1 or bet > 100:
      showInformation("You must bet between the table minimum and maximum (2-100)")
      return self.__getBet()
    elif bet > self.__credits:
      showInformation("Sorry, you only have " + str(int(self.__credits)) + " credits")
      return self.__getBet()
    return bet
    
  def __wannaPlay(self):
    userInput = requestString("Welcome to the Crazy Craps Casino! Looks like you have 100 credits. Would you like to play? (y/n)")
    while userInput != "y" and userInput != "n":
      userInput = requestString("I am sorry, I did not understand. (y/n)")
    if userInput == "y":
      return true
    else:
      showInformation("Ok, we will keep a seat warm for you!")
      return false 
   
  def __rollPair(self):
    roll = self.__rollDie() + self.__rollDie()
    showInformation("You throw the dice accross the table landing a " + str(int(roll)) + "!")
    return roll

  def __rollDie(self):
    return random.randint(1, 6)

craps = Craps()
craps.play()
""" Problem 2 """
