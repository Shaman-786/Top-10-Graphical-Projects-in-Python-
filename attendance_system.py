import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            status TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    ''')
    conn.commit()
    conn.close()

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")

        # Create a main frame
        self.main_frame = tk.Frame(self.root, bg="#ffffff", bd=5, relief=tk.RAISED)
        self.main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.create_widgets()
        self.populate_students()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.main_frame, text="Attendance Management System", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#4CAF50")
        self.title_label.pack(pady=10)

        # Add Student Section
        self.add_student_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.add_student_frame.pack(pady=10)

        self.name_label = tk.Label(self.add_student_frame, text="Student Name:", font=("Helvetica", 12), bg="#ffffff")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.add_student_frame, font=("Helvetica", 12), bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.name_entry.grid(row=0, column=1, padx=5)
        self.add_student_btn = tk.Button(self.add_student_frame, text="Add Student", command=self.add_student, bg="#4CAF50", fg="white", font=("Helvetica", 12), activebackground="#45a049")
        self.add_student_btn.grid(row=0, column=2, padx=5)

        # Remove Student Section
        self.remove_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.remove_frame.pack(pady=10)

        self.remove_label = tk.Label(self.remove_frame, text="Remove Student ID:", font=("Helvetica", 12), bg="#ffffff")
        self.remove_label.grid(row=0, column=0)
        self.remove_entry = tk.Entry(self.remove_frame, font=("Helvetica", 12), bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.remove_entry.grid(row=0, column=1, padx=5)
        self.remove_student_btn = tk.Button(self.remove_frame, text="Remove Student", command=self.remove_student, bg="#F44336", fg="white", font=("Helvetica", 12), activebackground="#e53935")
        self.remove_student_btn.grid(row=0, column=2, padx=5)

        # Mark Attendance Section
        self.mark_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.mark_frame.pack(pady=10)

        self.mark_label = tk.Label(self.mark_frame, text="Mark Attendance for Student ID:", font=("Helvetica", 12), bg="#ffffff")
        self.mark_label.grid(row=0, column=0)
        self.mark_entry = tk.Entry(self.mark_frame, font=("Helvetica", 12), bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.mark_entry.grid(row=0, column=1, padx=5)
        self.mark_attendance_btn = tk.Button(self.mark_frame, text="Mark Present", command=lambda: self.mark_attendance("Present"), bg="#2196F3", fg="white", font=("Helvetica", 12), activebackground="#1976D2")
        self.mark_attendance_btn.grid(row=0, column=2, padx=5)
        self.mark_absent_btn = tk.Button(self.mark_frame, text="Mark Absent", command=lambda: self.mark_attendance("Absent"), bg="#FFC107", fg="white", font=("Helvetica", 12), activebackground="#FFA000")
        self.mark_absent_btn.grid(row=0, column=3, padx=5)

        # View Attendance Sheet Button
        self.view_btn = tk.Button(self.main_frame, text="View Attendance Sheet", command=self.view_attendance, bg="#9C27B0", fg="white", font=("Helvetica", 12), activebackground="#7B1FA2")
        self.view_btn.pack(pady=10)

        # Students List
        self.students_list = ttk.Treeview(self.main_frame, columns=("ID", "Name"), show="headings", height=8)
        self.students_list.heading("ID", text="ID")
        self.students_list.heading("Name", text="Name")
        self.students_list.pack(pady=10, fill=tk.BOTH, expand=True)

        # Attendance List
        self.attendance_list = ttk.Treeview(self.main_frame, columns=("ID", "Student ID", "Date", "Status"), show="headings", height=8)
        self.attendance_list.heading("ID", text="ID")
        self.attendance_list.heading("Student ID", text="Student ID")
        self.attendance_list.heading("Date", text="Date")
        self.attendance_list.heading("Status", text="Status")
        self.attendance_list.pack(pady=10, fill=tk.BOTH, expand=True)

        # Style the Treeview
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.map("Treeview", background=[("selected", "#4CAF50")], foreground=[("selected", "white")])

        # Animate the Treeview
        self.students_list.bind('<Button-1>', self.on_click)
        self.attendance_list.bind('<Button-1>', self.on_click)

    def add_student(self):
        name = self.name_entry.get()
        if name:
            conn = sqlite3.connect('attendance.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO students (name) VALUES (?)', (name,))
            conn.commit()
            conn.close()
            self.name_entry.delete(0, tk.END)
            self.populate_students()
            messagebox.showinfo("Success", "Student added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a student name.")

    def remove_student(self):
        student_id = self.remove_entry.get()
        if student_id:
            conn = sqlite3.connect('attendance.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
            conn.commit()
            conn.close()
            self.remove_entry.delete(0, tk.END)
            self.populate_students()
            messagebox.showinfo("Success", "Student removed successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a student ID.")

    def mark_attendance(self, status):
        student_id = self.mark_entry.get()
        if student_id:
            conn = sqlite3.connect('attendance.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO attendance (student_id, date, status) VALUES (?, DATE("now"), ?)', (student_id, status))
            conn.commit()
            conn.close()
            self.mark_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Attendance marked as {status}.")
        else:
            messagebox.showwarning("Warning", "Please enter a student ID.")

    def view_attendance(self):
        for row in self.attendance_list.get_children():
            self.attendance_list.delete(row)
        
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM attendance')
        records = cursor.fetchall()
        for record in records:
            self.attendance_list.insert('', 'end', values=record)
        conn.close()

    def populate_students(self):
        for row in self.students_list.get_children():
            self.students_list.delete(row)

        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        records = cursor.fetchall()
        for record in records:
            self.students_list.insert('', 'end', values=record)
        conn.close()

    def on_click(self, event):
        # Animate the row selection
        item = self.students_list.identify_row(event.y)
        if item:
            self.students_list.selection_set(item)
            self.students_list.item(item, tags='selected')
            self.root.after(100, lambda: self.students_list.item(item, tags=''))

        item = self.attendance_list.identify_row(event.y)
        if item:
            self.attendance_list.selection_set(item)
            self.attendance_list.item(item, tags='selected')
            self.root.after(100, lambda: self.attendance_list.item(item, tags=''))

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = AttendanceSystem(root)
    root.mainloop()
