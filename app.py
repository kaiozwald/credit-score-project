# app.py

import tkinter as tk
from tkinter import ttk, messagebox
from core.domain.models import UserCreditData
from core.use_cases.calculate_score import CreditScoreUseCase

class CreditScoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("iScore Calculator")
        self.root.geometry("400x500")
        self.use_case = CreditScoreUseCase()

        self.create_widgets()

    def create_widgets(self):
        self.entries = {}

        fields = [
            ("User ID", int),
            ("Payment History Score", float),
            ("Current Debt", float),
            ("Monthly Income", float),
            ("Credit History Length (months)", int),
            ("Number of Credit Types", int),
            ("Late Payments Count", int)
        ]

        for i, (label, _) in enumerate(fields):
            ttk.Label(self.root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(self.root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry

        ttk.Button(self.root, text="Calculate iScore", command=self.calculate_score).grid(
            row=len(fields), column=0, columnspan=2, pady=20
        )

        self.result_label = ttk.Label(self.root, text="iScore: N/A", font=("Arial", 14, "bold"))
        self.result_label.grid(row=len(fields)+1, column=0, columnspan=2)

    def calculate_score(self):
        try:
            user = UserCreditData(
                user_id=int(self.entries["User ID"].get()),
                payment_history_score=float(self.entries["Payment History Score"].get()),
                current_debt=float(self.entries["Current Debt"].get()),
                monthly_income=float(self.entries["Monthly Income"].get()),
                credit_history_length=int(self.entries["Credit History Length (months)"].get()),
                number_of_credit_types=int(self.entries["Number of Credit Types"].get()),
                late_payments_count=int(self.entries["Late Payments Count"].get())
            )
            score = self.use_case.calculate_i_score(user)
            self.result_label.config(text=f"iScore: {score}")
        except Exception as e:
            messagebox.showerror("Input Error", f"Check your inputs: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CreditScoreApp(root)
    root.mainloop()
