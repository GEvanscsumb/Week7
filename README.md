# Week7
Week 7 contains our lab work for labs 15 and 16

## Lab 15

**Problem 1**:

Use a function from the random library to simulate rolling dice.  Write a function that rolls a single die and then use that function to build a program that let's the user play craps. The basic rules of craps are:

1. A player rolls two six-sided dice and adds the numbers rolled together.
2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12 automatically loses, and play is over. If a 4, 5, 6, 8, 9, or 10 are rolled on this first roll, that number becomes the "point.”
3. The player continues to roll the two dice again until one of two things happens: either they roll the "point" again, in which case they win; or they roll a 7, in which case they lose.

Playing craps can include a number of variations on this game, and also typically involves betting on various outcomes; those aspects of the game are not required for this lab, however have some fun writing this game.

**Problem 2**:

Have some fun with different library functions by figuring out how to get Python to:

Print out a calendar of the month you were born
Tell you how many days it is until your next birthday
What day of the week was the Declaration of Independence ratified by the Continental Congress? (write a program that prints out Monday, Tuesday, etc)
[Check point] Submit to assignment your python code as a lab15_LastName.py file. Please add your name and your partner's name as a comment in the beginning of your program. And submit the screen capture of your running program and the output as a imge file (.jpg, or .png). 

## Lab 16

**Scraping HTML from existing sites**
In the headline lab, we saved a local, static copy of the Otter Realm website to get the featured headlines. But the web is always changing so we'd like to be able to get live data from the current version of a website.  Luckily the urllib module (<- LINK) lets us open, read and then close a URL.  
The Lab
Ok, now that we can read from a URL, get data out of the html (Just like in the headline lab), and write a page, we can finally get started on the lab itself.  For today's lab
  1. Choose a website that you frequent that has data (text) that could be scraped from it's HTML (this could be Facebook, CNN, Kitty Pictures, whatever)
  2. Write some code that collects at least 10 pieces of information from the webiste (e.g. friends from Facebook, or headlines from CNN, comments on kitty pictures, etc)
  3. Create a new web page that displays ONLY the information you collected in step 2
The page you create can be very simple. You only need to display the information in a readable format.  No fancy formatting required ... we'll save that for next time :)
To get checked off, be prepared to show:
  1. The original website you got your data from
  2. Your code in lab16_LastName.py format (Please add your name and your partner's name as a comment in the beginning of your program. )
  3. Your resulting html page that you created
