import random

#271
class Account:
    # class variable
    account_count = 0

    # class function
    def __init__(self, 예금주, 초기잔액):
        self.bank = "SC은행"
        self.name = 예금주
        self.account_number = str(random.randint(0, 999)) + "-" + str(random.randint(0, 99)) + "-" + str(random.randint(0, 999999))
        self.balance = 초기잔액
        Account.account_count += 1

kim = Account("김민수", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)

#272
kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)

#273
class Account:
    # class variable
    account_count = 0

    # class function
    def __init__(self, 예금주, 초기잔액):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.bank = "SC은행"
        self.name = 예금주
        self.account_number = str(random.randint(0, 999)) + "-" + str(random.randint(0, 99)) + "-" + str(random.randint(0, 999999))
        self.balance = 초기잔액
        Account.account_count += 1

    def get_account_num(self):
        return self.account_count

    #274
    def deposit(self, value):
        if value >= 1:
            self.deposit_count += 1
            self.balance += value
            if self.deposit_count % 5 == 0:
                self.balance += self.balance * 0.01
                self.deposit_log.append(value + self.balance * 0.01)
            else:
                self.deposit_log.append(value)
        else:
            print("입금할 금액이 부족합니다")

    #275
    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
            self.withdraw_log.append(value)
        else:
            print("출금할 금액이 부족합니다")

    #276
    def display_info(self):
        print("은행이름:", self.bank, end=" ")
        print("예금주:", self.name, end=" ")
        print("계좌번호:", self.account_number, end= " ")
        print("잔고:", "{:,}".format(self.balance), end=" ")

    #280
    def deposit_history(self):
        for i in self.deposit_log:
            print(i)

    def withdraw_history(self):
        for i in self.withdraw_log:
            print(i)

k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print(k.balance)

p = Account("파이썬", 10000)
p.display_info()
print()

#277
u = Account("파이썬", 10000)
u.deposit(10000)
u.deposit(10000)
u.deposit(10000)
u.deposit(5000)
u.deposit(5000)
print(u.balance)

#278
계좌 = []
계좌.append(k)
계좌.append(u)
계좌.append(p)

for i in 계좌:
    i.display_info()
    print()

#279
for i in 계좌:
    if i.balance >= 10000:
        i.display_info()
        print()

#280
O = Account("Kim", 1000)
O.deposit(100)
O.deposit(200)
O.deposit(300)
O.deposit_history()
print()

O.withdraw(100)
O.withdraw(200)
O.withdraw_history()