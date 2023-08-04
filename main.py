# since we are working with many classes, import them all.
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# since we have imported all classes, we do not need to tkinter.Tk() to access the Tk class
window = Tk()
window.title("pomodoro")
# first configure the window
window.config(padx=100, pady=50, bg=YELLOW)

# next configure the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# next configure the image on the canvas
filename = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=filename)

# next add some text over the image
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.pack()


window.mainloop()
