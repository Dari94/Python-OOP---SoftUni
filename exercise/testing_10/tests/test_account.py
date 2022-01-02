import unittest
from polymorfism_06.account_2 import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('John', 100)

    def test_addTransaction_InvalidType(self):
        with self.assertRaises(ValueError):
            self.account.add_transaction(50.20)

    def test_addTransaction_ValidType(self):
        self.assertEqual(len(self.account._transactions), 0)
        self.account.add_transaction(50)
        self.assertEqual(len(self.account._transactions), 1)

    def test_balance(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(50)
        self.assertEqual(self.account.balance, 150)

    def test_validateTransactionRaiseException(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account, -102)

    def test_validateTransactionCorrect(self):
        result = Account.validate_transaction(self.account, 100)
        self.assertEqual(result, 'New balance: 200')

    def test_validateTransaction_shouldBeStatic(self):
        import types
        self.assertTrue(isinstance(self.account.validate_transaction, types.FunctionType))

    def test_validateTransaction_invalidAmount(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account, 50.60)

    def test_accountStr(self):
        result = str(self.account)
        self.assertEqual(result, 'Account of John with starting amount: 100')

    def test_accountRepr(self):
        result = repr(self.account)
        self.assertEqual(result, 'Account(John, 100)')

    def test_accountLenTransactions(self):
        self.account.add_transaction(50)
        result = len(self.account._transactions)
        self.assertEqual(result, 1)


    def test_accountGetItem(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        result = self.account[1]
        self.assertEqual(result, 150)

    def test_account_gt(self):
        account_2 = Account('test', 50)
        self.assertGreater(self.account, account_2)
        self.assertTrue(self.account > account_2)


    def test_account_ge(self):
        account_2 = Account('test', 100)
        self.assertGreaterEqual(self.account, account_2)
        self.assertTrue(self.account >= account_2)
        self.assertEqual(self.account, account_2)

    def test_account_lt(self):
        account_2 = Account('test', 150)
        self.assertLess(self.account, account_2)
        self.assertTrue(self.account < account_2)

    def test_account_le(self):
        account_2 = Account('test', 100)
        self.assertLessEqual(self.account, account_2)
        self.assertTrue(self.account <= account_2)
        self.assertEqual(self.account, account_2)

    def test_accountReversedTransactions(self):
        self.account.add_transaction(50)
        self.account.add_transaction(10)
        result = list(reversed(self.account._transactions))

        self.assertEqual(result, [10, 50])

    def test_accountAdd(self):
        account_2 = Account('test', 50)
        account_3 = self.account + account_2
        self.assertEqual(repr(account_3), f'Account(John&test, 150)')
        self.assertEqual(account_3.balance, 150)
        self.assertEqual(account_3.owner, 'John&test')

    def test_accountEqual(self):
        account_2 = Account('test', 100)
        result = self.account == account_2
        self.assertTrue(result)
        self.assertEqual(self.account.amount,100)
        self.assertEqual(account_2.amount,100)

    def test_accountNotEqual(self):
        account_2 = Account('test', 50)
        result = self.account != account_2
        self.assertTrue(result)
        self.assertEqual(self.account.amount, 100)
        self.assertEqual(account_2.amount, 50)
if __name__ == '__main__':
    unittest.main()
