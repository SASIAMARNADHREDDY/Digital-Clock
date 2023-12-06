import tkinter as tk
from tkinter import ttk
from time import strftime

class DigitalClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.setup_ui()

    def setup_ui(self):
        # Configure root window
        self.root.geometry("400x200")
        self.root.configure(bg="black")

        # Create and configure label
        self.label = ttk.Label(
            self.root,
            font=("Helvetica", 40, "bold"),
            background="black",
            foreground="cyan",
        )
        self.label.pack(expand=True, anchor="center")

        # Update time periodically
        self.update_time()

    def update_time(self):
        current_time = strftime("%H:%M:%S %p")
        self.label.config(text=current_time)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClockApp(root)
    root.mainloop()
