class Account:
  def __init__(self, id, type, balance):
    self.id = id
    self.type = type
    self.balance = balance

  def transaction(self, creditdebit, amount):
    self.balance += amount
    return self.balance

#class Transaction
 # def __init__(self, account_id, creditdebit, amount)
  #  self.account_id = account_id
   # self.creditdebit = creditdebit
    #self.amount = amount

  #def 

BluevineChecking = Account('1010', 'Asset', 0)

print(BluevineChecking.transaction('debit', 25))
