class TransactionMonitor:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, customer_id, amount):
        flag = "FRAUD" if amount > 5000 else "OK"
        tx = {'id': customer_id, 'amount': amount, 'flag': flag}
        self.transactions.append(tx)
        return tx

    def get_summary(self):
        return self.transactions