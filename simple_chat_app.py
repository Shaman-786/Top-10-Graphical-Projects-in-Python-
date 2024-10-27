import tkinter as tk
from tkinter import scrolledtext
import random

class SimpleChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Chat App")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word')
        self.chat_area.pack(pady=10, padx=10, fill='both', expand=True)

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(pady=10, padx=10, fill='x', expand=True)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        # Sample responses to simulate dynamic conversation
        self.response_options = [
            "That's interesting! Tell me more.",
            "Why do you think that is?",
            "I see! What else can you say about it?",
            "Hmm, that's a thought. How do you feel?",
            "Oh, really? Could you elaborate?",
            "Sounds intriguing! What's next?",
            "Is there something specific you want to ask?"
        ]

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.display_message("You: " + message)
            response = self.get_response(message)
            self.display_message("Bot: " + response)
            self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)  # Automatically scroll to the bottom

    def get_response(self, message):
        # Generate a more interesting dynamic response
        return random.choice(self.response_options)

if __name__ == "__main__":
    root = tk.Tk()
    chat_app = SimpleChatApp(root)
    root.mainloop()
