import tkinter as tk
import random

# ---------------- GAME STATE ----------------
secret_number = random.randint(1, 100)
attempts = 0
game_finished = False

# ---------------- FUNCTIONS ----------------
def check_guess(event=None):
    global attempts, game_finished

    if game_finished:
        return

    try:
        user_guess = int(guess_entry.get())
        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        if user_guess < secret_number:
            result_label.config(text="⬆️ Too Low! Go Higher", fg="#ff9800")

        elif user_guess > secret_number:
            result_label.config(text="⬇️ Too High! Come Down", fg="#ff9800")

        else:
            result_label.config(
                text=f"🎉 YOU WON!\nGuessed in {attempts} attempts",
                fg="#4CAF50"
            )
            game_finished = True
            check_button.config(state="disabled", bg="#9e9e9e")

        guess_entry.delete(0, tk.END)

    except ValueError:
        result_label.config(text="⚠️ Enter numbers only!", fg="#f44336")
        guess_entry.delete(0, tk.END)


def restart_game():
    global secret_number, attempts, game_finished

    secret_number = random.randint(1, 100)
    attempts = 0
    game_finished = False

    attempts_label.config(text="Attempts: 0")
    result_label.config(text="🤔 I’m thinking of a number...", fg="#333")
    guess_entry.delete(0, tk.END)
    check_button.config(state="normal", bg="#4CAF50")


# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x560")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# ---------------- CARD CONTAINER ----------------
card = tk.Frame(root, bg="#ffffff", bd=0)
card.pack(padx=15, pady=15, fill="both", expand=True)

# ---------------- TITLE ----------------
title_label = tk.Label(
    card,
    text="🎯 Guess The Number",
    font=("Segoe UI", 20, "bold"),
    bg="white",
    fg="#222"
)
title_label.pack(pady=(25, 5))

subtitle = tk.Label(
    card,
    text="Between 1 and 100",
    font=("Segoe UI", 11),
    bg="white",
    fg="#666"
)
subtitle.pack()

# ---------------- ATTEMPTS ----------------
attempts_label = tk.Label(
    card,
    text="Attempts: 0",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="#2196F3"
)
attempts_label.pack(pady=10)

# ---------------- INPUT ----------------
guess_entry = tk.Entry(
    card,
    font=("Segoe UI", 16),
    justify="center",
    width=10,
    relief="solid",
    bd=1
)
guess_entry.pack(pady=20)
guess_entry.focus()

root.bind("<Return>", check_guess)

# ---------------- BUTTONS ----------------
check_button = tk.Button(
    card,
    text="CHECK",
    font=("Segoe UI", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=18,
    height=1,
    bd=0,
    command=check_guess
)
check_button.pack(pady=8)

restart_button = tk.Button(
    card,
    text="RESTART",
    font=("Segoe UI", 11),
    bg="#2196F3",
    fg="white",
    width=18,
    height=1,
    bd=0,
    command=restart_game
)
restart_button.pack(pady=5)

# ---------------- RESULT ----------------
result_label = tk.Label(
    card,
    text="🤔 I’m thinking of a number...",
    font=("Segoe UI", 13),
    bg="white",
    fg="#333",
    justify="center"
)
result_label.pack(pady=25)

# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    text="Made by Naksh Garg",
    font=("Segoe UI", 9),
    fg="#bbbbbb",
    bg="#1e1e2f"
)
footer.pack(pady=5)

# ---------------- START ----------------
root.mainloop()
