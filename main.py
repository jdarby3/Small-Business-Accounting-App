# input:
#   current general journal + chart of accounts + old ledger
# output:
#   new ledger, financial statements, plus graphs and visuals etc...

accounts = {}

class Account:
  def __init__(self, id, balance, type = 'asset'):

    accounts[id] = self

    self.id = id
    self.type = type
    self.balance = balance

    self.transactions = { }

  def transact(self, date, entry_num, debit, credit):

    self.transactions[entry_num] = (date, debit, credit)

    if self.type == 'equity' or self.type == 'liability':

      self.balance += credit
      self.balance -= debit

    else:

      self.balance -= credit
      self.balance += debit

    return None


def journal_entry(date, entry_num, entry_data):

  for row in entry_data:  # row will have account, debit, credit
      
      accounts[row[0]].transact(date, entry_num, row[1], row[2])

  return None






# testing

# bvc = Account(123, 0, 'liability')

# print (accounts)

# journal_entry('1/04/2023', 1000, ((123, 0, 20), ))

# print (accounts[123].transactions)