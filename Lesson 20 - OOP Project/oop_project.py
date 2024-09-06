from bank_account import BankAccount, InterestRewardsAcct, SavingsAcct

Mia = BankAccount(1000, "Mia")
Taylor = BankAccount(2000, "Taylor")

Mia.getBalance()
Taylor.getBalance()

Taylor.deposit(500)

Mia.withdraw(10000)
Mia.withdraw(10)

Mia.transfer(10000, Taylor)
Mia.transfer(100, Taylor)


Myca = InterestRewardsAcct(1000, "Myca")

Myca.getBalance()

Myca.deposit(100)

Myca.transfer(100, Mia)

Lohr = SavingsAcct(1000, "Lohr")

Lohr.getBalance()

Lohr.deposit(100)

Lohr.transfer(1000, Taylor)