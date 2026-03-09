import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.geometry('300x400')

        self.entry = tk.Entry(root, font=('Arial', 18), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row = 1
        col = 0
        for btn in buttons:
            if btn == 'C':
                tk.Button(root, text=btn, font=('Arial', 18), command=self.clear).grid(
                    row=row, column=col, sticky='nsew', padx=5, pady=5)
            else:
                tk.Button(root, text=btn, font=('Arial', 18), 
                          command=lambda b=btn: self.on_button_click(b)).grid(
                    row=row, column=col, sticky='nsew', padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror('Error', 'Invalid input')
        else:
            self.entry.insert(tk.END, value)

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == __main__:
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()