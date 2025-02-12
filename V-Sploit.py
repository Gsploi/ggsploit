import subprocess
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog
import tkinter.filedialog

class MyTextEditor(tk.Tk):

    def __init__(self):
        super().__init__()
        
        # Set the window properties
        self.title("gsploit")
        self.geometry("500x400")

        # Ask for password on startup
        self.check_password()

        # Create a frame for the side bar and add it to the window
        sidebar = tk.Frame(self, width=30, bg="gray")
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Create the button for the main editor and add it to the side bar
        editor_button = tk.Button(sidebar, text="Editor", bg="gray", command=self.show_editor)
        editor_button.pack(side=tk.TOP, pady=10)

        # Create the button for the credits and add it to the side bar
        credits_button = tk.Button(sidebar, text="Credits", bg="gray", command=self.show_credits)
        credits_button.pack(side=tk.TOP, pady=10)

        # Create a frame for the main editor and add it to the window
        self.editor_frame = tk.Frame(self)
        self.editor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Create a text widget and add it to the editor frame
        self.text = tk.Text(self.editor_frame)
        self.text.pack(fill=tk.BOTH, expand=1)

        # Create a frame for the credits and add it to the window
        self.credits_frame = tk.Frame(self)
        self.credits_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Create a label for the credits and add it to the credits frame
        self.credits_label = tk.Label(self.credits_frame, text="Version 0.1")
        self.credits_label.pack(pady=10)

        # Create buttons and add them to the editor frame
        execute_button = tk.Button(self.editor_frame, text="Execute", command=self.execute)
        execute_button.pack(side=tk.LEFT)
        open_button = tk.Button(self.editor_frame, text="Roblox", command=self.open_file)
        open_button.pack(side=tk.LEFT)
        clear_button = tk.Button(self.editor_frame, text="Clear", command=self.clear)
        clear_button.pack(side=tk.LEFT)
        refresh_button = tk.Button(self.editor_frame, text="Refresh", command=self.refresh)
        refresh_button.pack(side=tk.LEFT)
        save_button = tk.Button(self.editor_frame, text="Save", command=self.save)
        save_button.pack(side=tk.RIGHT)

    def check_password(self):
        # Ask the user for a password
        password = simpledialog.askstring("key:", "Enter the key:", show='*')
        if password != "gsploitisthebest":  # Replace "your_password" with your desired password
            messagebox.showerror("Error", "its in the discord dumbass!")
            self.quit # Close the application if the password is incorrect
         
    def execute(self):
        pass

    def show_editor(self):
        # Show the main editor frame and hide the credits frame
        self.editor_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.credits_frame.pack_forget()

    def show_credits(self):
        # Show the credits frame and hide the main editor frame
        self.credits_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.editor_frame.pack_forget()

    def open_file(self):
        # Open the Roblox application on Mac
        roblox_path = '/Applications/Roblox.app'
        try:
            subprocess.Popen(['open', roblox_path])  # Open the application
        except Exception as e:
            print(f"Failed to open Roblox: {e}")

    def clear(self):
        # Display a confirmation dialog
        result = messagebox.askquestion("Confirm Clear", "Are you sure you want to clear the text?")
        if result == "yes":
            # Clear the contents of the text widget
            self.text.delete("1.0", "end")

    def refresh(self):
        # Refresh the window
        self.update()

    def save(self):
        # Get the contents of the text widget
        contents = self.text.get("1.0", "end-1c")
        # Open a file for writing and write the contents to it
        with open("saved_text.txt", "w") as f:
            f.write(contents)
        popup = messagebox.showinfo(title='Save', message='File saved successfully.')

editor = MyTextEditor()
editor.mainloop()
