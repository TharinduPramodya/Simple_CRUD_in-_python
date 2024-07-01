import tkinter as tk
from tkinter import messagebox

class CRUDApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Application")
        
        # Variables to store data temporarily in RAM
        self.data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        
        # Labels and Entries
        tk.Label(root, text="First Name:").pack(pady=5)
        self.first_name_entry = tk.Entry(root, width=50)
        self.first_name_entry.pack(pady=5)

        tk.Label(root, text="Last Name:").pack(pady=5)
        self.last_name_entry = tk.Entry(root, width=50)
        self.last_name_entry.pack(pady=5)

        tk.Label(root, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack(pady=5)

        # Buttons
        self.create_button = tk.Button(root, text="Create", command=self.create)
        self.create_button.pack(pady=10)

        self.read_button = tk.Button(root, text="Read", command=self.read)
        self.read_button.pack(pady=10)

        self.update_button = tk.Button(root, text="Update", command=self.update)
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete", command=self.delete)
        self.delete_button.pack(pady=10)

    def create(self):
        self.data['first_name'] = self.first_name_entry.get()
        self.data['last_name'] = self.last_name_entry.get()
        self.data['email'] = self.email_entry.get()
        messagebox.showinfo("Create", "Record created and stored in memory.")

    def read(self):
        messagebox.showinfo("Read", f"First Name: {self.data['first_name']}\nLast Name: {self.data['last_name']}\nEmail: {self.data['email']}")

    def update(self):
        self.first_name_entry.insert(0, self.data['first_name'])
        self.last_name_entry.insert(0, self.data['last_name'])
        self.email_entry.insert(0, self.data['email'])
        messagebox.showinfo("Update", "Data auto-filled for update.")

    def delete(self):
        self.data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        messagebox.showinfo("Delete", "Data deleted from memory.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApplication(root)
    root.mainloop()
