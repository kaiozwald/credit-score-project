from core.domain.models import UserCreditData
from core.domain.score_calculator import ScoreCalculator

class CreditScoreUseCase:

    def __init__(self):
        self.calculator = ScoreCalculator()

    def calculate_i_score(self, user: UserCreditData) -> float:
        weights = {
            "payment_history": 0.35,
            "debt": 0.30,
            "history_length": 0.15,
            "credit_types": 0.10,
            "late_payments": 0.10
        }

        debt_score = self.calculator.calculate_debt_score(user.current_debt, user.monthly_income)
        history_score = self.calculator.calculate_history_length_score(user.credit_history_length)
        types_score = self.calculator.calculate_credit_type_score(user.number_of_credit_types)
        late_score = self.calculator.calculate_late_payment_score(user.late_payments_count)

        final_score = (
            user.payment_history_score * weights["payment_history"] +
            debt_score * weights["debt"] +
            history_score * weights["history_length"] +
            types_score * weights["credit_types"] +
            late_score * weights["late_payments"]
        )

        iscore = self.calculator.map_score_to_iscore(final_score)
        return iscore
