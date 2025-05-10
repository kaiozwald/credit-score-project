from dataclasses import dataclass

@dataclass
class UserCreditData:
    user_id: int
    payment_history_score: float  # 0 - 100
    current_debt: float
    monthly_income: float
    credit_history_length: int  # in months
    number_of_credit_types: int
    late_payments_count: int
