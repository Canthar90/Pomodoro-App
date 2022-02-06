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
reps = 0
timer = None
mark = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global mark, reps
    tomato_label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        reps = 0
        tomato_label.config(text="Break", fg=RED)
        start_of_timer(long_break)


    elif reps % 2 == 0 and reps < 8:
        tomato_label.config(text="Break", fg=PINK)
        start_of_timer(short_break)

    else :
        tomato_label.config(text="Work", fg=GREEN)
        start_of_timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time
import math


def start_of_timer(count):

    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes <10:
        minutes = f"0{minutes}"
    if count == 0 :
        window.attributes('-topmost', True)
        window.update()
        window.attributes('-topmost', False)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, start_of_timer, count-1)
    else:
        global mark
        start_countdown()
        mark=""
        work_sessions = math.floor(reps/2)
        for e in range(work_sessions):
            mark += "✓"
        checkmark_label.config(text=mark)


    pass



# ---------------------------- UI SETUP ------------------------------- #
interruption = False




def reset_of_timer():
    global interruption
    interruption = True
    pass


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

def say_something(thing):
    print(thing)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

tomato_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
tomato_label.grid(column=1, row=0)

checkmark_label = Label(text="", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_countdown )
start_button.grid(column=0, row=2)



reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=2)





window.mainloop()