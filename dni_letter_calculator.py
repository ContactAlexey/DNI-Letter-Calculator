import tkinter as tk
from tkinter import messagebox, ttk

def get_dni_letter(number):
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    if number >= 0:
        return letters[number % 23]
    else:
        return None

def calculate_letter():
    try:
        dni_number = int(entry.get())
        letter = get_dni_letter(dni_number)
        if letter:
            result_label.config(text=f"The corresponding letter is: {letter}", foreground="#333333")
        else:
            messagebox.showerror("Error", "Invalid DNI number. Must be non-negative.")
            result_label.config(text="")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        result_label.config(text="")

# Create main window
root = tk.Tk()
root.title("DNI Letter Calculator")
root.geometry("400x250")  # Fixed window size
root.resizable(False, False)  # Disable window resizing

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

# ttk style for the button with a modern theme
style = ttk.Style(root)
style.theme_use('clam')  # Cleaner, more modern theme
style.configure('TButton', 
                font=('Helvetica', 12, 'bold'), 
                foreground='white',
                background='#007ACC',
                padding=10)
style.map('TButton',
          background=[('active', '#005F99')])

# Set window background color
root.configure(bg="#f0f4f8")

# Main label asking for DNI number input
label = tk.Label(root, 
                 text="Enter your DNI number without the letter:", 
                 bg="#f0f4f8",
                 font=("Helvetica", 14),
                 fg="#333333")
label.pack(pady=(20, 10))

# Entry widget for DNI number with font and padding
entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
entry.pack(ipady=6, ipadx=10)

# Calculate button
button = ttk.Button(root, text="Calculate Letter", command=calculate_letter)
button.pack(pady=20)

# Label to display the result with highlighted font
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#007ACC")
result_label.pack(pady=10)

# Run the application
root.mainloop()
