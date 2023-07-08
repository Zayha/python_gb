class ATM:
    def __init__(self):
        self.operations_dict = {
            'Пополнить': self.put_to_account,
            'Снять': self.get_from_account,
            'Выход': self.exit_program,
        }
        self.key_list = list(self.operations_dict.keys())
        self.__account_amount = 0.0
        try:
            with open('account.txt', encoding='utf-8') as f:
                a = f.readline().split(' ')
                if self.__is_float(a[0]):
                    self.__account_amount = float(a[0])

        except FileNotFoundError:
            with open('account.txt', 'w', encoding='utf-8') as f:
                f.write(str(self.__account_amount) + " 0")

    def get_account_amount(self):
        return self.__account_amount

    def put_to_account(self):
        self.__minus_percents()
        amount = self.__get_amount('пополнения')
        if amount.isdigit() and int(amount) % 50 == 0:
            # # тут должно быть подтверждение от диспенсера
            # self.banknote_dispenser_receiving()
            self.__account_amount += int(amount)
            self.__write_to_acc()

    def get_from_account(self):
        self.__minus_percents()
        amount = self.__get_amount('снятия')
        if amount.isdigit() and int(amount) % 50 == 0:
            am = int(amount)
            withdrawal_fee = self.__commission(am)
            print(withdrawal_fee)
            am_plus_fee = withdrawal_fee + am
            if self.__account_amount >= am_plus_fee:
                self.__account_amount -= am_plus_fee
                self.__write_to_acc()
                # # тут должно быть подтверждение от диспенсера
                # self.banknote_dispenser_transfer(int(amount))

    @staticmethod
    def __is_float(string: str) -> bool:
        try:
            float(string)
            return True
        except ValueError:
            return False

    def __write_to_acc(self):
        with open('account.txt', 'r+', encoding='utf-8') as f:
            operation_counter_lst = f.readline().split(' ')
            operation_counter = int(operation_counter_lst[1]) + 1
            self.__plus_percents(operation_counter)
            f.seek(0)
            f.write(str(self.__account_amount) + f" {operation_counter}")
            f.truncate()

    def __plus_percents(self, num_operations: int):
        if num_operations % 3 == 0:
            self.__account_amount *= 1.03

    def __minus_percents(self):
        if self.__account_amount > 5_000_000:
            print(f'fee: {self.__account_amount * 0.1}')
            self.__account_amount -= self.__account_amount * 0.1

    @staticmethod
    def __commission(am):
        com = am * 1.5 / 100
        if com > 600:
            com = 600
        if com < 30:
            com = 30
        return com

    def menu(self):
        result = ""
        for i in range(len(self.key_list)):
            f = f'{i} - {self.key_list[i]} \n'
            result += f
        return result

    def make_operations(self, operation: str):
        if operation.isdigit() and 0 <= int(operation) <= len(self.key_list):
            selected_operation = self.operations_dict[self.key_list[int(operation)]]
            selected_operation()

    def exit_program(self):
        print(f'\nBye bye... Balance: {self.get_account_amount():.2f}')
        raise SystemExit

    @staticmethod
    def __get_amount(txt):
        return input(f'Введите сумму для {txt}, кратную 50: ')

    # # управление диспенсером купюр, проверка купюр, ведение логов, выдача и прием наличных, вынести в класс
    # def banknote_dispenser_transfer(self, amount) -> bool:
    #     pass
    #
    # def banknote_dispenser_receiving(self, amount) -> bool:
    #     pass


atm1 = ATM()
while True:
    print(f'Баланс: {atm1.get_account_amount():.2f}')
    print(atm1.menu())
    atm1.make_operations(input('Выберите пункт меню: '))
