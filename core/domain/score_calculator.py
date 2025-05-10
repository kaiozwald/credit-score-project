class ScoreCalculator:

    def calculate_debt_score(self, current_debt: float, monthly_income: float) -> float:
        if monthly_income == 0:
            return 0.0
        ratio = current_debt / monthly_income
        if ratio > 1:
            return 0
        elif ratio > 0.75:
            return 20
        elif ratio > 0.5:
            return 50
        elif ratio > 0.25:
            return 80
        else:
            return 100

    def calculate_history_length_score(self, months: int) -> float:
        if months < 6:
            return 10
        elif months < 12:
            return 30
        elif months < 24:
            return 60
        elif months < 60:
            return 80
        else:
            return 100

    def calculate_credit_type_score(self, types_count: int) -> float:
        if types_count >= 3:
            return 100
        elif types_count == 2:
            return 60
        elif types_count == 1:
            return 30
        else:
            return 0

    def calculate_late_payment_score(self, late_count: int) -> float:
        if late_count == 0:
            return 100
        elif late_count <= 2:
            return 60
        elif late_count <= 4:
            return 30
        else:
            return 0

    def map_score_to_iscore(self,raw_score):
        return round(300 + ((raw_score / 100) * 550), 2)
