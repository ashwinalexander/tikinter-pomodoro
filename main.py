# since we are working with many classes, import them all.
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """when the timer begins, increase the reps value,
    decide whether to go on short break, long break or work"""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
    # take a short break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        # get to work
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# input: count in seconds
# output: timer shows countdown mm:ss format
# this func converts count from seconds to mm:ss and displays it on the label
# if sec < 10, it prepends a 0
# once the count reaches 0, re-trigger the timer.


def count_down(count):
    min_count = math.floor(count/60)
    sec_count = count % 60

    if sec_count < 10:
        sec_count = f"0{sec_count}"

    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        window.after(2, count_down, count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
# since we have imported all classes, we do not need to tkinter.Tk() to access the Tk class
window = Tk()
window.title("pomodoro")
# first configure the window
window.config(padx=100, pady=50, bg=YELLOW)


# next add the Timer label
lblTimer = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
lblTimer.grid(row=0,column=1)

# next configure the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# next configure the image on the canvas
filename = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=filename)

# next add some text over the image
timer_text = canvas.create_text(100,130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


def btnReset_Click():
    print("button reset clicked")


# next add the two buttons
btnStart = Button(text="Start", command= start_timer)
btnStart.grid(row=2, column=0)

btnReset = Button(text="Reset", command= btnReset_Click)
btnReset.grid(row=2, column=2)

# finally add the Check label
lblTimer = Label(text="✔", font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
lblTimer.grid(row=3,column=1)






window.mainloop()
