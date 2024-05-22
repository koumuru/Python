class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = str(first_name)
    self.last_name = str(last_name)
    self.account_id = int(account_id)
    self.account_type = str(account_type)
    self.pin = int(pin)
    self.balance = float(balance)

  def deposit(self):
    dep = float(input("How much money you want to deposit: "))
    self.balance = self.balance + dep
    return self.balance

  def withdraw(self):
    wit = float(input("How much money you want to withdraw: "))
    self.balance = self.balance - wit
    return wit

  def display_balance(self):
    print(self.balance)
    return self.balance
    




szymon = BankAccount("Szymon","Gawel",54645659864,"Standard",1234,1000)

szymon.deposit()
szymon.withdraw()
szymon.display_balance()
