class Invoice:
    def __init__(self, client_name: str, amount: float):
        self.client_name = client_name
        self.amount = amount

    def generate_invoice(self):
        return f"Invoice for {self.client_name} | Amount: {self.amount}"


inv = Invoice("Riya", 5000)

print(inv.generate_invoice())