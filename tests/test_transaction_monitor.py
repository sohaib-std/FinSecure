import unittest
from services.transaction_monitor import TransactionMonitor

class TestTransactionMonitor(unittest.TestCase):
    def test_fraud_detection(self):
        monitor = TransactionMonitor()
        tx = monitor.add_transaction("C001", 6000)
        self.assertEqual(tx['flag'], "FRAUD")

    def test_normal_transaction(self):
        monitor = TransactionMonitor()
        tx = monitor.add_transaction("C001", 1500)
        self.assertEqual(tx['flag'], "OK")

if __name__ == '__main__':
    unittest.main()