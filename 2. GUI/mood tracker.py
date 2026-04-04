import tkinter as fn #It's a library
#library is toolbox for programmers, it is a pre made code that we can use, so we doesnt need to write in from zero

#1. setup the windows
root = fn.Tk()
root.title("mood tracker by puddle")
root.geometry("500x500")

#2. creating functions for buttons
def smile():
    labels.config(text="keep smiling 😁😁", fg="blue")
    root.configure(bg="lightblue")
    #this code ^^ will generate a new label every time we click the button
    #labeln = fn.Label(root, text="keep smiling 😁😁", fg="blue")
    #labeln.pack()
    #this code ^^ will create a new label every time we click the button

def unmotivated():
    labels.config(text="search motivation dude dont ask me 😔😔", fg="black")
    root.configure(bg="lightyellow")
def cant_move():
    labels.config(text="NOW PUT YOUR PHONE AWAY", fg="red")
    root.configure(bg="lightgray")


#3. LABEL 1 TIMEEEE (man the "1" ruined)
labelnau=fn.Label(root, text="How did you do today?", fg="orange", font=("algerian", 20))
labelnau.pack(pady=7)

#4. TIME FOR THEEEE BUTTONSSSSSS
buttons = fn.Button(root, text="😁😁😁", width=30, command=smile)
buttons.pack(pady=7)

unmotivated_button = fn.Button(root, text="😔😔😔", width=30, command=unmotivated)
unmotivated_button.pack(pady=7)

cant_move_button = fn.Button(root, text="😴😴😴", width=30, command=cant_move)
cant_move_button.pack(pady=7)


root.mainloop()