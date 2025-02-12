import tkinter as tk
from tkinter import messagebox
from scipy.optimize import newton
from datetime import datetime

class XIRRCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("XIRR Calculator")
        self.root.geometry("600x400")

        # Add a permanent label to the main window
        self.label = tk.Label(self.root, text="Kaushik's XIRR Calculator", font=("Comic Sans MS", 20))
        self.label.pack(pady=20)  # Add some padding for better appearance
        
        self.investments = []  # Stores investment data as (amount, date)

        self.ask_for_investment()

    def ask_for_investment(self):
        """Initial GUI to ask if user wants to enter an investment."""
        answer = messagebox.askyesno("Investment Entry", "Do you want to enter an investment?")
        if answer:
            self.investment_window()
        else:
            self.return_window()

    def investment_window(self):
        """Window to enter investment amount and date."""
        self.investment_win = tk.Toplevel(self.root)
        self.investment_win.title("Enter Investment")
        self.investment_win.geometry("450x300")  # Set the window to be three times bigger
        
        tk.Label(self.investment_win, text="Amount:", font=("Comic Sans MS", 12)).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.investment_win, text="Date (YYYY-MM-DD):", font=("Comic Sans MS", 12)).grid(row=1, column=0, padx=5, pady=5)

        self.amount_entry = tk.Entry(self.investment_win, width=30, font=("Comic Sans MS", 12))
        self.date_entry = tk.Entry(self.investment_win, width=30, font=("Comic Sans MS", 12))
        
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.investment_win, text="Submit", command=self.submit_investment, font=("Comic Sans MS", 12)).grid(row=2, columnspan=2, pady=10)

    def submit_investment(self):
        """Handles the submission of an investment entry."""
        try:
            amount = float(self.amount_entry.get())
            date_str = self.date_entry.get()
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            
            # Add the investment to the list and close the window
            self.investments.append((amount, date))
            self.investment_win.destroy()
            
            # Prompt to add another investment
            self.ask_for_investment()
        except ValueError as ve:
            messagebox.showerror("Input Error", f"Invalid input: {ve}")

    def return_window(self):
        """Window to enter the return amount."""
        self.return_win = tk.Toplevel(self.root)
        self.return_win.title("Enter Return")
        self.return_win.geometry("450x300")  # Set the window to be three times bigger

        tk.Label(self.return_win, text="Return Amount on Present Day:", font=("Comic Sans MS", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.return_entry = tk.Entry(self.return_win, width=30, font=("Comic Sans MS", 12))
        self.return_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.return_win, text="Calculate XIRR", command=self.calculate_xirr, font=("Comic Sans MS", 12)).grid(row=1, columnspan=2, pady=10)

    def calculate_xirr(self):
        """Calculates the XIRR based on entered data and displays results."""
        try:
            return_amount = float(self.return_entry.get())
            today_date = datetime.today().date()
            
            # Append the return as a cash flow
            cash_flows = [-investment[0] for investment in self.investments] + [return_amount]
            dates = [investment[1] for investment in self.investments] + [today_date]
            
            # Calculate XIRR
            xirr_value = self.xirr(cash_flows, dates) * 100  # XIRR in percentage
            
            # Print data and XIRR
            result_text = "Investments and Dates:\n"
            for amount, date in self.investments:
                result_text += f"Amount: {amount}, Date: {date}\n"
            result_text += f"\nReturn Amount on {today_date}: {return_amount}\n"
            result_text += f"\nCalculated XIRR: {xirr_value:.2f}%"

            # Create a larger result window
            result_window = tk.Toplevel(self.root)
            result_window.title("XIRR Result")
            result_window.geometry("600x400")  # Set the result window to be larger
            result_label = tk.Label(result_window, text=result_text, font=("Comic Sans MS", 12), justify="left")
            result_label.pack(pady=20)

            tk.Button(result_window, text="Close", command=result_window.destroy, font=("Comic Sans MS", 12)).pack(pady=10)

            # Close the return window after calculation
            self.return_win.destroy()
            
            # Ensure the root window stays open until the user closes it
            self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        except ValueError as ve:
            messagebox.showerror("Calculation Error", f"Invalid input for return amount: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def on_close(self):
        """Callback to handle window closing."""
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def xirr(self, cash_flows, dates):
        """Calculates XIRR using Newton's method."""

        # Calculate the day differences from the first date
        days = [(date - dates[0]).days for date in dates]
        
        # XIRR objective function
        def npv(rate):
            return sum([cf / (1 + rate)**(day / 365) for cf, day in zip(cash_flows, days)])
        
        # Use Newton's method to solve for the rate that makes NPV = 0
        try:
            return newton(npv, 0.1)  # Initial guess of 10% (0.1)
        except RuntimeError:
            raise ValueError("XIRR calculation did not converge.")

# Initialize the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = XIRRCalculator(root)
    root.mainloop()
