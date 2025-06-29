class Account:
  def __init__(self, id, name, type, balance):
    self.id = id
    self.type = type
    self.balance = balance

  def transaction(self, creditdebit, amount):
    ##creates a transaction in the account
    if creditdebit.upper() == 'CREDIT'

    self.balance += amount
    return self.balance

BluevineChecking = Account('1010', 'BlueVine Checking', 'Asset', 0)

print(BluevineChecking.transaction('debit', 25))
