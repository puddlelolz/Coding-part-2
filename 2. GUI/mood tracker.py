import tkinter as fn #It's a library
#library is toolbox for programmers, it is a pre made code that we can use, so we doesnt need to write in from zero

#1. setup the windows
root = fn.Tk()
root.title("mood tracker by puddle")
root.geometry("500x500")

#2. creating functions for buttons
def smile():
    label = fn.Label(root, text="keep smiling 😁😁", fg="yellow")
    label.pack()


def unmotivated():
    label = fn.Label(root, text="search motivation online dude dont ask me", fg="gray")
    label.pack()

def cant_move():
    label = fn.Label(root, text="THATS WHY YOU SHOULD NOT ON YOUR PHONE ALL DAY", fg="red")
    label.pack()


#3. LABEL 1 TIMEEEE (man the "1" ruined)
labels=fn.Label(root, text="How did you do today?", fg="orange", font=("algerian", 20))
labels.pack(pady=7)

#4. TIME FOR THEEEE BUTTONSSSSSS
buttons = fn.Button(root, text="😁😁😁", width=30, command=smile)
buttons.pack(pady=7)

unmotivated_button = fn.Button(root, text="😔😔😔", width=30, command=unmotivated)
unmotivated_button.pack(pady=7)

cant_move_button = fn.Button(root, text="😴😴😴", width=30, command=cant_move)
cant_move_button.pack(pady=7)


root.mainloop()