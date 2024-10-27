import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.image_path = None
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=20)

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            image = Image.open(self.image_path)
            image = image.resize((400, 400), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

root = tk.Tk()
app = ImageViewer(root)
root.mainloop()
