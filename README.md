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
  
## Mini Lab
Background:
So far, the html pages that we've been creating are pretty boring: black text on a white background.  We can make things a little more exciting by changing up the color and size of the font that we use.  First we need to introduce the <p> tag.  In html <p> defines a paragraph.  No big deal.  However, we can combine the <p> tag with a little css (cascading style sheet) code to start to format our output a little more. Let's look at an example:

<p style="color:#339900; font-size:50px; font-weight:bold">GREEN EGGS!</p>

Here I have the <p> tag with some extra stuff inside the opening tag:

style="    this part alerts us that there is some style information coming up.  All the style information will be inside the double quotes

color=#339900   this sets the color of the text for the paragraph tag that we are currently using. Notice that the color is specified as a wierd number.  This number is actually a set of RGB values specified in hexadecimal (base 16).  Don't worry, you don' t need to know hexadecimal color codes, you can just look them up on line.  Here are a couple of resources:

http://html-color-codes.com/
http://www.colorpicker.com/
font-size:50px     this sets the size of the text

font-weight:bold     this part says to make the text in this paragraph bold.

Notice that all the style components are insdie the same set of double quotes and each part is separated from the next by a semi-colon.  The text between the <p> and </p> tags will be affected by the formatting and will be the text that shows up on your webpage.

There are actually a ton of different ways that you can use CSS to modify the look of text on your page, but these three options should be more than enough for today's lab.  To learn more about CSS and font you can check out this page from W3 Schools (make sure you click some of the additional links to learn more)

Lab Problem for Today:
Start with the Green Eggs and Ham word count lab.  In this lab, you printed to the screen a list of every word in Green Eggs and Ham and how often it appeared. For today's lab, 

  1. First, modify your Green Eggs and Ham lab so that instead of printing the words and counts to the screen, it writes them out to an .html file.  You should be able to open your html file in a browser to see the results of your word count

  2.  Now, instead of printing the counts for each word, modify the color/size/weight of the word to reflect its frequency in the file.  You will probably want to break the counts into ranges for this (e.g. words with a count between 30 and 40 have one color/size, etc).  

Here is a screen shot showing part of one potential outcome (be creative, this is by no means *the* answer, hopefully every group will have a different product for this lab)

hams
