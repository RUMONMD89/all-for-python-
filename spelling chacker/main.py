import tkinter as tk
import re


# copyright@rumon


class SpellingCheckerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Spelling Checker")

        # Create the dictionary
        self.dictionary = ["hello", "world", "python", "programming", "language", "model"]

        # Create the text entry
        self.text_entry = tk.Text(self.master, height=15, width=30)
        self.text_entry.pack()

        # Create the check spelling button
        self.check_button = tk.Button(self.master, text="Check Spelling", command=self.check_spelling)

        heading = tk.Label(root, text="spelling checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
        heading.pack(pady=(50, 0))
        self.check_button.pack()

        # Create the result label
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def check_spelling(self):
        # Get the text from the text entry
        text = self.text_entry.get("1.0", "end-1c")

        # Split the text into words
        words = re.findall(r'\w+', text)

        # Check each word against the dictionary
        for word in words:
            if word.lower() not in self.dictionary:
                self.result_label.config(text=f"Incorrect spelling: {word}")
                return

        self.result_label.config(text="Correct spelling")


# Create the Tkinter app
root = tk.Tk()
app = SpellingCheckerApp(root)
root.mainloop()
