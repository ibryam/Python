from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Helvetica"
current_card = {}
to_learn = {}

try:

    data = pandas.read_csv("data/word_to_learn.csv") #read the data we need to use. Formats the data in columns and rows (german & english).
except FileNotFoundError:
    original_data = pandas.read_csv("data/top_german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") # converts the data to a dictionary


# What "orient" does? - Previously the dict looked as "German" is the key to the word and respectively "English" is the other key to access the words.
# 'German': {0; 'ich', 1: 'ja', 2: 'nein', 'English': {0: 'i', 1:'yes', 2: 'no'}

# "Orient" changes the structure of the dictionary for every single item they become a list of dictionaries:
# [{'German': 'ich', 'English': 'i'}, {'German': 'ja', 'English': 'yes'}, {'German': 'nein', 'English': 'no'}]



#//---------------------------------------------------------------------------------------------------//
# creating different functions
#//---------------------------------------------------------------------------------------------------//

#next card - picks are random word from the data, when a button is clicked, changes the word that appears on the screen.
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer) #cancels the existing flip_timer that is a global and that starts when the program starts
    current_card = random.choice(to_learn) # picks a random record from the dictionary when any button is clicked.
    canvas.itemconfig(card_title, text="German", fill="black") # changes the text "Title" to "German" when clicked
    canvas.itemconfig(card_word, text=current_card["German"], fill="black") # changes the text below "Title" to a random word
    canvas.itemconfig(card_background, image=card_front_img) # changes the background to front image once a button is clicked ( ie German screen)
    flip_timer = window.after(3000, func=flip_card) # after 3 seconds flips to english card to show translation, restarts the flip timer 3 seconds




#//---------------------------------------------------------------------------------------------------//
# change the card to show the english translation for the current word, will change the image on the screen from yellow to white, change the color of the text.
# this will automatically happen in 3 seconds
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill="white") # Change the text from "German" to "English"
    canvas.itemconfig(card_word, text = current_card["English"], fill="white") # configures the translation
    canvas.itemconfig(card_background, image = card_back_img)  # change card background


# function that removes the current card from the data
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_card()



# Window setup
window = Tk() # create window item
window.title("Flash Card App") # set the name of the window title (appears on top)
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR) # set padding of the window and background color

flip_timer = window.after(3000, func = flip_card) # do this after 3 seconds. This activates the function flip card to change the card to english after 3 seconds.

#creating a canvas. This will allow us to put items on top of it. Text, images etc.
# width + height should be equal to the image size(sizes of the card_front
canvas = Canvas(width = 800, height = 526)


card_front_img = PhotoImage(file="images/card_front.png") # capture the front image in a variable
card_back_img = PhotoImage(file="images/card_back.png") # capture the back image in a variable
# add the image in the canvas.
# The image has to go in the CENTER of the canvas, it must have the half of the canvas size. 800/2; 526/2
card_background = canvas.create_image(400, 263, image = card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0) #remove the white background from the image by setting up the same background color. + remove borders.

# adding first label "Title" + set font
# set up the size of the text using same image width (400) + height half of the existing 263 to show a little towards the top of the screen
card_title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))

card_word = canvas.create_text(400, 263, text = "", font=(FONT, 60, "bold")) # adding second label german word + set font, set in the center - 400 and 263.

canvas.grid(row = 0, column = 0, columnspan = 2) # spread the image to two columns


#//---------------------------------------------------------------------------------------------------//
# creating buttons
#//---------------------------------------------------------------------------------------------------//
#creating the red button

red_image = PhotoImage(file = "images/wrong.png") # capturing red image in a variable
red_button = Button(image=red_image, highlightthickness=0, command=next_card) # enabling the image as a button
red_button.grid(column = 0, row = 1) # set the position of the button on the screen.

#creating the green button

green_image = PhotoImage(file = "images/right.png") # capturing green image in a variable
green_button = Button(image=green_image, highlightthickness=0, command=is_known) # enabling the image as a button
green_button.grid(column = 1, row = 1) # set the position of the button on the screen.

next_card()

window.mainloop() # window to start of the mainloop