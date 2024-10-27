import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Quiz App")

        self.questions = [
            "What is the capital of France?",
            "What is 2 + 2?",
            "What is the color of the sky?",
        ]
        self.answers = ["Paris", "4", "Blue"]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text=self.questions[self.current_question])
        self.question_label.pack(pady=20)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

    def submit_answer(self):
        user_answer = self.entry.get()
        if user_answer.lower() == self.answers[self.current_question].lower():
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
            self.entry.delete(0, tk.END)
            self.result_label.config(text="")
        else:
            self.question_label.config(text="Quiz Finished!")
            self.result_label.config(text=f"Score: {self.score}/{len(self.questions)}")

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
