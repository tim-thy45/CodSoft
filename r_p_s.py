from tkinter import *
import random

# for a win=2, for a loss=0, for a draw=1
rules = {"ROCK": {"ROCK": 1, "PAPER": 0, "SCISSORS": 2},
         "PAPER": {"ROCK": 2, "PAPER": 1, "SCISSORS": 0},
         "SCISSORS": {"ROCK": 0, "PAPER": 2, "SCISSORS": 1}}

ps = 0
cs = 0


def logic(choice):
    global ps, cs
    outcomes = ["ROCK", "PAPER", "SCISSORS"]
    random_num = random.randint(0, 2)
    comp_choice = outcomes[random_num]
    result = rules[choice][comp_choice]
    comp_c.config(text="Computer Choice: " + str(comp_choice))

    if result == 2:
        ps = ps + 1
        score.config(text="Your Score: " + str(ps))
        winner.config(text="YOU WON:)", fg="#3498db") 
    elif result == 1:
        winner.config(text="DRAWXD", fg="#f39c12")
    else:
        cs = cs + 1
        comp.config(text="Computer: " + str(cs))
        winner.config(text="YOU LOST :(", fg="#e74c3c")


root = Tk()
root.title("Rock Paper Scissors")

choice_label = Label(root, text="Welcome to the game!", width=18, height=2, font=("Arial", 14), fg="#2ecc71")
choice_label.grid(row=0, sticky=N, padx=200, pady=10)

Label(root, text="Please select an option:", font=("Arial", 14)).grid(row=1, sticky=N)

score = Label(root, text="Your Score: 0", font=("Arial", 10), fg="#2ecc71")
score.grid(row=2, sticky=W, pady=10)

comp = Label(root, text="Computer: 0", font=("Arial", 10), fg="#2ecc71")
comp.grid(row=2, sticky=E, pady=10)

player_c = Label(root, text="Player Choice:", font=("Arial", 12))
player_c.grid(row=3, sticky=W, pady=10)

comp_c = Label(root, font=("Arial", 12))
comp_c.grid(row=3, sticky=E, pady=10)

winner = Label(root, font=("Arial", 14))
winner.grid(row=3, sticky=N, pady=10)

Button(root, text="ROCK", width=10, command=lambda: logic("ROCK"), bg="#3498db").grid(row=5, sticky=W, padx=5, pady=10)
Button(root, text="PAPER", width=10, command=lambda: logic("PAPER"), bg="#f39c12").grid(row=5, sticky=N, padx=5, pady=10)
Button(root, text="SCISSORS", width=10, command=lambda: logic("SCISSORS"), bg="#e74c3c").grid(row=5, sticky=E, padx=5, pady=10)
Label(root).grid(row=6)

root.mainloop()