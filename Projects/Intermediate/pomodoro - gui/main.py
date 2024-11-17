from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#7AB2D3"
FONT_NAME = "Helvetica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Ready to learn❓🔥", font = (FONT_NAME, 18, "normal"), fg = BLUE)
    check_label.config(text = "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break⏳", font = (FONT_NAME, 18, "normal"), fg = RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text = "Short Break ☕",font = (FONT_NAME, 18, "normal"), fg = PINK)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        timer_label.config(text = "Work...🔎✍️", font = (FONT_NAME, 18, "normal"), fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions =math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✓"
        check_label.config(text = marks)





# ---------------------------- UI SETUP ------------------------------- #

# creating the tomato/background config
window = Tk()
window.title("Pomodoro App")
window.config(padx=100,
              pady= 50,
              bg=YELLOW)



canvas = Canvas(width=200,
                height=224,
                bg=YELLOW,
                highlightthickness=False)

photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,
                    image=photo)
timer_text = canvas.create_text(100,130,
                   text="00:00",
                   fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 1,
            row = 1)

# creating timer_label
timer_label = Label(text = "Ready to learn❓🔥",
                    font = (FONT_NAME, 18, "normal"),
                    fg=BLUE,
                    highlightthickness=False,
                    bg=YELLOW)
timer_label.grid(column = 1,
                 row = 0)

# creating check_mark
check_label = Label(fg=GREEN,
                    highlightthickness=False,
                    bg=YELLOW)
check_label.grid(column = 1,
                 row = 2)

# creating "start" button

start_button = Button(text = "GO!",
                      font = (FONT_NAME, 15, "normal"),
                      highlightthickness=False,
                      command=start_timer)
start_button.grid(column = 0,
                  row = 2)

# creating "reset" button

reset_button = Button(text = "reset",
                      font = (FONT_NAME, 15, "normal"),
                      highlightthickness=False,
                      fg=BLUE,
                      command = reset_timer)
reset_button.grid(column = 2,
                  row = 2)



window.mainloop()












