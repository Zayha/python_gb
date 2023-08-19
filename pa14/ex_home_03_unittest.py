import unittest
from unittest.mock import patch

from atm import ATM


class TestATM(unittest.TestCase):

    def setUp(self) -> None:
        self.atm = ATM()

    def test_ex_exit(self):
        with self.assertRaises(SystemExit) as ex:
            self.atm.exit_program()
        self.assertEqual(str(ex.exception), 'BB')

    def test_start_amount(self):
        self.assertAlmostEqual(self.atm.get_account_amount(), 0, places=3)

    @patch('builtins.input', lambda *args: '50')
    def test_plus_to_acc(self):
        start_balance = 0.0
        amount = input('')
        if amount.isdigit() and int(amount) % 50 == 0:
            self.atm._ATM__account_amount += int(amount)
            self.atm._ATM__write_to_acc()
            self.atm.operations_list.append(f'+{amount}')
            self.atm._ATM__write_dump()
        self.assertAlmostEqual(50, self.atm.get_account_amount(), places=3)


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()
