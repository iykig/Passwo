import tkinter as tk
from string import *
from itertools import product

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.is_paused = False

        self.generate_button = tk.Button(root, text="Play", command=self.generate_passwords)
        self.generate_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.toggle_pause)
        self.pause_button.pack()
        self.pause_button["state"] = "disabled"

        self.display = tk.Text(root, wrap="word")
        self.display.pack()

        self.value = ascii_letters + digits + punctuation
        self.cancel_generation = False

    def generate_passwords(self):
        self.generate_button["state"] = "disabled"
        self.pause_button["state"] = "normal"
        self.is_paused = False

        for i in range(8, 9):
            if self.cancel_generation:
                self.cancel_generation = False
                break

            for j in product(self.value, repeat=i):
                word = "".join(j)
                self.display.insert(tk.END, word + '\n')
                self.display.see(tk.END)
                self.root.update()
                if self.is_paused:
                    self.generate_button["state"] = "normal"
                    self.pause_button["state"] = "disabled"
                    return

        self.generate_button["state"] = "normal"
        self.pause_button["state"] = "disabled"

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def cancel_generation(self):
        self.cancel_generation = True

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
