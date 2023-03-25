import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Basic Arithmetic Calculator")

        # Entry widget to display the results
        self.result = tk.Entry(master, width=25, font=('Arial', 12))
        self.result.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons for the calculator operations
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "%", "="
        ]
        row = 1
        col = 0
        for button in buttons:
            # Define the function that will be called when the button is pressed
            if button == "=":
                cmd = self.calculate
            elif button == "C":
                cmd = self.clear
            else:
                cmd = lambda x=button: self.add_to_expression(x)

            # Create the button with the corresponding function
            btn = tk.Button(master, text=button, width=5, height=2, command=cmd)
            btn.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

        self.expression = ""

    def add_to_expression(self, char):
        self.expression += str(char)
        self.result.insert(tk.END, char)

    def calculate(self):
        try:
            self.result.delete(0, tk.END)
            self.result.insert(tk.END, str(eval(self.expression)))
        except:
            self.result.delete(0, tk.END)
            self.result.insert(tk.END, "Error")
        self.expression = ""

    def clear(self):
        self.result.delete(0, tk.END)
        self.expression = ""

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
