import tkinter as fn
from tkinter import messagebox as nf

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

def clicking():
    global score, points_per_click, upgrade_cost
    if score >= upgrade_cost:
        score -= upgrade_cost
        points_per_click += 1
        upgrade_cost *= 2
        score_label.config(text=f"Score: {score}")
        upgrade_button.config(text=f"Upgrade (Cost: {upgrade_cost})")
    else:
        nf.showinfo("you are poor", "click more man you are broke")

#4. creating buttons
click_button = fn.Button(root, text="smash me", command=click)
click_button.pack(pady=20)

upgrade_button = fn.Button(root, text=f"Upgrade (Cost: {upgrade_cost})", command=clicking)
upgrade_button.pack(pady=20)

root.mainloop()