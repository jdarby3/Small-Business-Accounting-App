class Account:
  def __init__(self, id, name, atype, balance):
    self.id = id
    self.type = atype
    self.name = name
    self.balance = balance

class Transaction:
  def __init__(self, id, account, creditdebit, amount, description):
    self.id = id
    self.creditdebit = creditdebit
    self.account = account
    self.amount = amount
    #f 1000 <= int(self.account) <= 3999
      #write so credit an debit gets properly added and subtracted from proper accounts

def New_Account():
  #function that will be called when new account button pressed
  pass

def New_Transaction(Account, id, account, creditdebit, amount, description):
  #make this function create a new transaction object
  if Account.id == Transaction.account:
    Account.balance += Transaction.amount
    print (f'{Account.name} balance is now {Account.balance}')
  else:
    print ('Acount ID does not match')

BluevineChecking = Account('1010', 'BlueVine Checking', 'Asset', 0)

ToolPurchase = Transaction('1234', '1010', 'credit', 90)

New_Transaction(BluevineChecking, ToolPurchase)
