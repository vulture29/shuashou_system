default_balance = 0
default_salary_balance = 0


class ShopStore:
    def __init__(self):
        self.store_id = "id"
        self.balance = default_balance
        self.salary_balance = default_salary_balance
        self.public_jobs = []
        self.finished_jobs = []
