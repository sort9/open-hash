import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import subprocess

def fileHashCompleteMessage():
    messagebox.showinfo("ALERT", "HASH SUCCESSFUL")  # Message box for when hash operation is complete

def fileHashErrorMessage():
    messagebox.showerror("ERROR", "NO FILE SELECTED")

def browse():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=(("All files", "*.*"), ("All files", "*.*")))
    entry_file_input.insert(tk.END, filepath)  # Insert the file path into the Entry widget

def hashFile():
    try:
        command = ['certutil', '-hashfile', filepath, 'SHA256']
        result = subprocess.run(command, capture_output=True, text=True)
        output_text_area.insert(tk.END, result.stdout)  # Insert the command output into the Text widget
    except Exception as e:
        print(e)
        fileHashErrorMessage()

def createFileShredTab(tab):
    label = ttk.Label(tab)
    label.pack(padx=20, pady=20)

    # Output Area (Text widget instead of Entry to handle multiple lines)
    global output_text_area
    output_text_area = tk.Text(tab, font=("Arial", 10), wrap=tk.WORD, height=10)
    output_text_area.pack(fill="both", side="top", ipady=10, expand=True)

    # File Input Entry Area
    global label_file_input
    label_file_input = tk.Label(tab, font=("Gill Sans MT", 11, "bold"), text="File to hash:")
    label_file_input.pack(side="left", padx=20, pady=10)
    label_file_input.config(bg="gray64")
    
    global entry_file_input
    entry_file_input = tk.Entry(tab, font=40, width=40)
    entry_file_input.pack(side="left", padx=5, pady=10)

    # Browse Button
    global browse_button
    browse_button = tk.Button(tab, text="Browse", font=40, command=browse)
    browse_button.pack(side="left", padx=5, pady=10)

    # Hash Button
    global shred_button
    shred_button = tk.Button(tab, text="Hash", font=40, command=hashFile)
    shred_button.pack(side="left", padx=5, pady=10)

def main():

    # Main window properties
    root = tk.Tk()
    root.title("Open Hash")
    root.geometry("670x430")
    root.resizable(False, False)
    root.config(bg="gray64")

    notebook = ttk.Notebook(root)

    tab1 = ttk.Frame(notebook)

    notebook.add(tab1, text="File Hasher")

    createFileShredTab(tab1)

    notebook.pack(padx=10, pady=10, fill="both", expand=True)

    # Program opens in the center of the screen
    root.eval('tk::PlaceWindow . center')

    root.mainloop()

if __name__ == "__main__":
    main()