class LoanApplicant:
    def __init__(self, name: str, salary: float, credit_score: float):
        self.name = name
        self.salary = salary
        self.credit_score = credit_score

    def is_eligible(self):
        return self.salary > 50000 and self.credit_score > 700


applicant = LoanApplicant("Riya", 80000, 750)

print(applicant.is_eligible())