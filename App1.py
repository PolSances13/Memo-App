import tkinter as tk
import random
from tkinter import messagebox

class MemorizeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memo App")
        self.root.geometry("500x500")
        self.root.iconbitmap("Brain.ico")

        self.letters = self.generate_letters()

        self.label = tk.Label(self.root, text="", font=("Arial", 24))
        self.label.pack(pady=20)

        self.time_entry = tk.Entry(self.root, font=("Arial", 14))
        self.time_entry.insert(0, "Write time in seconds")
        self.time_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_memorize)
        self.start_button.pack(pady=5)

        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answers)
        self.submit_button.pack(pady=5)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=5)

        self.answer_entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.reset_button.config(state="disabled")

    def generate_letters(self):
        letters = []
        for _ in range(20):
            letter = chr(random.randint(65, 90))
            letters.append(letter)
        return letters

    def start_memorize(self):
        self.start_button.config(state="disabled")
        self.label.config(text="".join(self.letters))
        time_delay = int(self.time_entry.get()) * 1000  # Convert seconds to milliseconds
        self.root.after(time_delay, self.show_entry)
        self.time_entry.pack_forget()  # Ocultar el cuadro de entrada de tiempo

    def show_entry(self):
        self.label.config(text="")
        self.answer_entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.reset_button.config(state="normal")
        self.answer_entry.focus_set()

    def check_answers(self):
        user_answers = self.answer_entry.get().upper()
        correct_answers = "".join(self.letters)

        if user_answers == correct_answers:
            messagebox.showinfo("Result", "Correct answers!")
        else:
            messagebox.showinfo("Result", "Incorrect answers. Try again.")

        self.reset()

    def reset(self):
        self.letters = self.generate_letters()
        self.answer_entry.delete(0, tk.END)
        self.label.config(text="")
        self.start_button.config(state="normal")
        self.answer_entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.reset_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemorizeApp(root)
    root.mainloop()
