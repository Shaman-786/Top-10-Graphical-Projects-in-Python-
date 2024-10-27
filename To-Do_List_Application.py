import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=20)

        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=10)

        self.button_add = tk.Button(root, text="Add Task", command=self.add_task)
        self.button_add.pack(pady=10)

        self.button_delete = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.button_delete.pack(pady=10)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.entry_task.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
