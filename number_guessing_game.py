import tkinter as tk
import random
secret_number = random.randint(1, 100)
attempts = 0
game_finished = False
def check_guess(event=None):
    """
    This function runs every time the user
    clicks the 'Check Guess' button or presses Enter.
    It compares the user's guess with the secret number.
    """
    global attempts, game_finished
    if game_finished:
        return
    try:

        user_guess = int(guess_entry.get())
        attempts += 1
        if user_guess < secret_number:
            result_label.config(
                text="📉 Too low! Aim a little higher."
            )

        elif user_guess > secret_number:
            result_label.config(
                text="📈 Too high! Come down a bit."
            )

        else:
     
            result_label.config(
                text=f"🎉 Well done! You guessed it in {attempts} tries."
            )
            game_finished = True
            check_button.config(state="disabled")


        guess_entry.delete(0, tk.END)

    except ValueError:
 
        result_label.config(
            text="Oops! Please enter a number only."
        )
        guess_entry.delete(0, tk.END)


def restart_game():
    """
    Resets everything so the user can play again.
    """
    global secret_number, attempts, game_finished

    secret_number = random.randint(1, 100)
    attempts = 0
    game_finished = False

    guess_entry.delete(0, tk.END)
    result_label.config(
        text="Game reset. Let’s go again!"
    )
    check_button.config(state="normal")


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x520")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="🎯 Number Guessing Game",
    font=("Arial", 18, "bold"),
    bg="#f4f6f8"
)
title_label.pack(pady=12)

instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 11),
    bg="#f4f6f8"
)
instruction_label.pack()


guess_entry = tk.Entry(
    root,
    font=("Arial", 13),
    width=15,
    justify="center"
)
guess_entry.pack(pady=15)
guess_entry.focus()


root.bind("<Return>", check_guess)


button_frame = tk.Frame(root, bg="#f4f6f8")
button_frame.pack(pady=5)


check_button = tk.Button(
    button_frame,
    text="Check Guess",
    font=("Arial", 11),
    width=12,
    bg="#4CAF50",
    fg="white",
    command=check_guess
)
check_button.grid(row=0, column=0, padx=5)


restart_button = tk.Button(
    button_frame,
    text="Restart",
    font=("Arial", 11),
    width=10,
    bg="#2196F3",
    fg="white",
    command=restart_game
)
restart_button.grid(row=0, column=1, padx=5)


result_label = tk.Label(
    root,
    text="🤔 I’m thinking of a number...",
    font=("Arial", 11),
    bg="#f4f6f8"
)
result_label.pack(pady=20)


footer_label = tk.Label(
    root,
    text="Tip: Press Enter to submit your guess",
    font=("Arial", 9),
    fg="gray",
    bg="#f4f6f8"
)
footer_label.pack(side="bottom", pady=8)


credit_label = tk.Label(
    root,
    text="Made by Naksh Garg",
    font=("Arial", 9, "italic"),
    fg="gray",
    bg="#f4f6f8"
)
credit_label.pack(side="bottom", pady=2)

root.mainloop()
