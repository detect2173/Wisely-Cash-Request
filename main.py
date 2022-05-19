import tkinter as tk
from tkinter import ttk, messagebox
#tk._test()
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def display():
    messagebox.showinfo('Display Box', 'This message was successfully displayed using the tkinter messagebox widget!')


reasons = {
    1: 'SHRO Student of the Month',
    2: 'CPP Completion - 60 days',
    3: 'Outstanding show of integrity',
    4: 'Outstanding Improvement/Achievement-Past 60 Days',
    5: 'Excellent Student Modeling/Mentoring',
    6: 'Above and beyond selfless contribution to the center',
    7: 'Other'
}

amounts = {
    5.00: '$5.00',
    10.00: '$10.00',
    15.00: '$15.00',
    20.00: '$20.00',
    25.00: '$25.00',
    30.00: '$30.00',
    35.00: '$35.00',
    40.00: '$40.00',
    45.00: '$45.00',
    50.00: '$50.00',

}

root = tk.Tk()
root.title('Student Wisely Request')
root.geometry('500x400')
root.resizable(width=False, height=False)
student_name = ttk.Label(root, text="Student Name:", padding=(10, 50, 20, 10))
student_name.grid(row=0, column=0, padx=(10, 0))
student_id = ttk.Label(root, text="   Student ID:", padding=(10, 10, 20, 10))
student_id.grid(row=1, column=0, padx=(10, 0))
student_amt = ttk.Label(root, text="       Amount:", padding=(10, 10, 20, 10))
student_amt.grid(row=2, column=0, padx=(10, 0))
student_reason = ttk.Label(root, text="       Reason:", padding=(10, 10, 20, 10))
student_reason.grid(row=3, column=0, padx=(10, 0))
# frame_left = ttk.Frame(root)
# frame_right = ttk.Frame(root)
# frame_right.pack(side='right')
# frame_left.pack(side='left')
# label_1 = ttk.Label(frame_left, text="\n\nStudent Name: \n\n\n\nStudent ID: \n\n\n\nAmount: \n\n\n\nReason: ", justify='right')
# label_1.grid(row=0, column=0, padx=10, pady=10)
root.grid_columnconfigure(1, weight=1)
name = tk.StringVar()
student_name = ttk.Combobox(root, width=50, justify="left", textvariable=name)
student_name.grid(row=0, column=1, padx=(10,20), pady=(50,10))
student_id = ttk.Entry(root, width=53)
student_id.grid(row=1, column=1, padx=0, pady=10)
var_reason = tk.StringVar()
var_amount = tk.DoubleVar()
student_amount = ttk.Combobox(root, width=50, values=list(amounts.values()), justify="left", textvariable=var_amount)
student_amount.grid(row=2, column=1, padx=0, pady=10)
student_reason = ttk.Combobox(root, width=50,values=list(reasons.values()), justify="left", textvariable=var_reason)
student_reason.grid(row=3, column=1, padx=0, pady=10)
#display_button = ttk.Button(root, text="Display", command=display).grid(row=8, column=1, padx=10, pady=10)


root.mainloop()
