import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_PATH = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = self.load_tasks()

        self.create_widgets()

    def load_tasks(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                return json.load(file)
        return {}

    def save_tasks(self):
        with open(FILE_PATH, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def create_widgets(self):
        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.mark_button = tk.Button(self.root, text="Mark Completed", command=self.mark_completed)
        self.mark_button.pack(side=tk.LEFT, padx=5)

        self.populate_listbox()

    def populate_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task_id, task_info in self.tasks.items():
            status = "Completed" if task_info["completed"] else "Pending"
            self.task_listbox.insert(tk.END, f"ID: {task_id} | Task: {task_info['description']} | Status: {status}")

    def add_task(self):
        task_description = self.entry.get()
        if task_description:
            task_id = str(len(self.tasks) + 1)
            self.tasks[task_id] = {"description": task_description, "completed": False}
            self.save_tasks()
            self.populate_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    def update_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_id = str(selected_task[0] + 1)
            new_description = self.entry.get()
            if new_description:
                if task_id in self.tasks:
                    self.tasks[task_id]["description"] = new_description
                    self.save_tasks()
                    self.populate_listbox()
                    self.entry.delete(0, tk.END)
                else:
                    messagebox.showwarning("Update Error", "Task ID not found.")
            else:
                messagebox.showwarning("Input Error", "Please enter a new description.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_id = str(selected_task[0] + 1)
            if task_id in self.tasks:
                del self.tasks[task_id]
                self.save_tasks()
                self.populate_listbox()
            else:
                messagebox.showwarning("Deletion Error", "Task ID not found.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_completed(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_id = str(selected_task[0] + 1)
            if task_id in self.tasks:
                self.tasks[task_id]["completed"] = True
                self.save_tasks()
                self.populate_listbox()
            else:
                messagebox.showwarning("Completion Error", "Task ID not found.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
