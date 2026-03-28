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

def cant_do_nothing():
    label = fn.Label(root, text="THATS WHY YOU SHOULD NOT ON YOUR PHONE ALL DAY", fg="red")
    label.pack()

root.mainloop()