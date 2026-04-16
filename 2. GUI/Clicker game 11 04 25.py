import tkinter as fn

#1. variables
score = 0
points_per_click = 1
upgrade_cost = 10

#2. setup the windows
root = fn.Tk()
root.title("Clicker Game by Puddle")
root.geometry("400x500")

#3. creating label and fuctions
score_label = fn.Label(root, text=f"Score: {score}", font=("Arial", 24))
score_label.pack(pady=20)

def click():
    global score #using this code will make th program understand which variable do i need to change
    score += points_per_click
    score_label.config(text=f"Score: {score}")



root.mainloop()