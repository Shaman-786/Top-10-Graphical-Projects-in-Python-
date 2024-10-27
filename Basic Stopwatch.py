import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.running = False
        self.time_elapsed = 0

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 48))
        self.label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=20)

    def update(self):
        if self.running:
            self.time_elapsed += 1
            hours, remainder = divmod(self.time_elapsed, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update)

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
