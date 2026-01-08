🎯 Number Guessing Game (Tkinter GUI)

A simple and user-friendly Number Guessing Game built using Python and Tkinter.
The application generates a random number between 1 and 100, and the user tries to guess it with helpful feedback after each attempt.

This project demonstrates GUI design, event handling, and basic game logic in Python.

📌 Features

🎲 Random number generation (1–100)

🧠 Intelligent feedback: Too High / Too Low / Correct

⌨️ Enter key support for quick guessing

🔄 Restart game functionality

📱 Mobile-style (portrait) window layout

🎨 Clean and user-friendly interface

🧾 Attempt counter

👤 Credit displayed in UI

🛠️ Technologies Used

Python 3

Tkinter (Python’s standard GUI library)

Random module

▶️ How to Run the Project

Make sure Python 3.x is installed on your system.

Save the program file as:

number_guessing_game.py


Open terminal / command prompt in the file location.

Run the command:

python number_guessing_game.py


The game window will open.

🎮 How to Play

The computer selects a random number between 1 and 100.

Enter your guess in the input box.

Click Check Guess or press Enter.

The game will guide you whether your guess is:

Too Low 📉

Too High 📈

Correct 🎉

Once guessed correctly, the game stops.

Click Restart to play again.

🧠 Project Logic Overview

random.randint(1, 100) generates the secret number.

User input is taken via a Tkinter Entry widget.

Button click or Enter key triggers guess validation.

UI updates dynamically using Label.config().

Game state is controlled using flags and counters.


👤 Author
Naksh Garg
Made as a Python GUI mini-project using Tkinter.

📜 License
This project is free to use for learning, academic, and personal purposes.
