import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")

        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
