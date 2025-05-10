from core.domain.models import UserCreditData
from core.use_cases.calculate_score import CreditScoreUseCase

if __name__ == "__main__":
    sample_user = UserCreditData(
        user_id=1,
        payment_history_score=85.0,
        current_debt=12000.0,
        monthly_income=8000.0,
        credit_history_length=36,
        number_of_credit_types=3,
        late_payments_count=2
    )

    use_case = CreditScoreUseCase()
    score = use_case.calculate_i_score(sample_user)

    print(f"User {sample_user.user_id} iScore: {score}")