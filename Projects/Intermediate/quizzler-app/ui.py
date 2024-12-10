from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT_SIZE = 15
FONT = "Helvetica"
PADDING = 20

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=PADDING, pady=PADDING, bg=THEME_COLOR)

        # Creating Score label##

        self.score_label = Label(text = "Score: 0", fg = "white", bg=THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(width=300, height=250, bg= "white")

        # set up the size of the text using same image width (400) + height half of the existing 263 to show a little towards the top of the screen

        self.question_text = self.canvas.create_text(150, 125, text="some question text", font=(
        FONT, FONT_SIZE, "italic"), fill=THEME_COLOR, width=250)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # spread the image to two columns

        # //---------------------------------------------------------------------------------------------------//
        # creating buttons
        # //---------------------------------------------------------------------------------------------------//
        # creating the red button

        self.red_image = PhotoImage(file="images/false.png")  # capturing red image in a variable
        self.red_button = Button(image=self.red_image, highlightthickness=0, command=self.red_pressed)  # enabling the image as a button
        self.red_button.grid(column=0, row=2)  # set the position of the button on the screen.

        # creating the green button

        self.green_image = PhotoImage(file="images/true.png")  # capturing green image in a variable
        self.green_button = Button(image=self.green_image, highlightthickness=0
                             ,command=self.green_pressed)  # enabling the image as a button
        self.green_button.grid(column=1, row=2)  # set the position of the button on the screen.

        self.get_next_question()





        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")


    def green_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def red_pressed(self):
        is_right = self.quiz.check_answer("False")    # def green_pressed and red_pressed do the same thing, just a different way
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


