import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x350")
        self.root.configure(padx=20, pady=20)
        
        self.secret_number = random.randint(1, 100)
        self.attempts_left = 7
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        self.title_label = tk.Label(self.root, text="Guess the Number (1-100)", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=(0, 15))
        
        # Info about attempts
        self.info_label = tk.Label(self.root, text=f"Attempts remaining: {self.attempts_left}", font=("Helvetica", 12))
        self.info_label.pack(pady=5)
        
        # Entry field for guesses
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 16), width=10, justify="center")
        self.guess_entry.pack(pady=10)
        # Bind the Enter key to submit guess
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())
        
        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit Guess", font=("Helvetica", 12, "bold"), 
                                       command=self.check_guess, bg="#4CAF50", fg="white", cursor="hand2")
        self.submit_button.pack(pady=10)
        
        # Feedback label
        self.feedback_label = tk.Label(self.root, text="Enter your first guess!", font=("Helvetica", 12, "italic"))
        self.feedback_label.pack(pady=15)
        
        # Restart button
        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Helvetica", 11), 
                                        command=self.restart_game, state=tk.DISABLED, cursor="hand2")
        self.restart_button.pack(pady=5)
        
        # Focus the entry widget on start
        self.guess_entry.focus()
        
    def check_guess(self):
        if self.attempts_left <= 0:
            return
            
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a valid integer.", fg="red")
            return
            
        if guess < 1 or guess > 100:
            self.feedback_label.config(text="Number must be between 1 and 100.", fg="red")
            return
            
        # Valid guess entered
        self.attempts_left -= 1
        self.info_label.config(text=f"Attempts remaining: {self.attempts_left}")
        
        if guess == self.secret_number:
            self.feedback_label.config(text=f"Correct! {guess} is the number!", fg="green", font=("Helvetica", 13, "bold"))
            self.game_over(True)
        elif guess < self.secret_number:
            self.feedback_label.config(text=f"{guess} is too low! Try higher.", fg="blue")
            if self.attempts_left == 0:
                self.game_over(False)
        else:
            self.feedback_label.config(text=f"{guess} is too high! Try lower.", fg="#e67e22") # Orange color
            if self.attempts_left == 0:
                self.game_over(False)
                
        # Clear the entry field for the next guess
        self.guess_entry.delete(0, tk.END)
        
    def game_over(self, won):
        # Disable inputs
        self.submit_button.config(state=tk.DISABLED)
        self.guess_entry.config(state=tk.DISABLED)
        # Enable restart
        self.restart_button.config(state=tk.NORMAL)
        
        if not won:
            self.feedback_label.config(text=f"Game Over! The number was {self.secret_number}.", fg="red", font=("Helvetica", 13, "bold"))
            messagebox.showinfo("Game Over", f"You ran out of attempts!\nThe secret number was {self.secret_number}.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number!\nYou had {self.attempts_left} attempts left to spare.")

    def restart_game(self):
        # Reset variables
        self.secret_number = random.randint(1, 100)
        self.attempts_left = 7
        
        # Reset UI
        self.info_label.config(text=f"Attempts remaining: {self.attempts_left}")
        self.feedback_label.config(text="Enter your first guess!", fg="black", font=("Helvetica", 12, "italic"))
        
        self.submit_button.config(state=tk.NORMAL)
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)
        self.restart_button.config(state=tk.DISABLED)
        
        self.guess_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    # Start the GUI event loop
    root.mainloop()
