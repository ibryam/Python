from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=100, height=100)
window.config(padx = 15, pady = 15)

def miles_to_km():
    """Convert miles to kilometers by multiplying the number of miles by 1.6, since there are 1.6 kilometers in a mile.\n So, 20 miles is 32 kilometers because 20 x 1.6 = 32 kilometers. If you need a more accurate number, multiply by 1.60934 instead.\n Using the more accurate method, 20 miles would equal 32.1868 kilometers."""
    converted = round(float(miles_input.get()) * 1.60934,1)
    km_result.config(text = converted)

# Creating "is equal to" label

is_equal_to = Label(text = "is equal to", font = ("Arial", 10, "normal"))
is_equal_to.grid(column = 0, row = 1)

# Creating "result_km" label

km_result = Label(text = int(), font = ("Arial", 10, "bold"))
km_result.grid(column = 1, row = 1)

# Creating "km" label

km_label = Label(text = "km", font = ("Arial", 10, "normal"))
km_label.grid(column = 2, row = 1)

# Creating "miles_label" label

miles_label = Label(text = "miles", font = ("Arial", 10, "normal"))
miles_label.grid(column = 2, row = 0)

# Creating an entry for miles

miles_input = Entry(width= 10)
miles_input.get()
miles_input.grid(column = 1, row = 0)

# Button
button = Button(text = "calculate", command=miles_to_km)
button.grid(column = 1, row = 2)














window.mainloop()