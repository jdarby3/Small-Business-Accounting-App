from datetime import date

accounts = {}

journal_entries = {}

transactions = {}

#trans_data will be in form (acc_id, debit, credit)
def transaction(trans_data):

  trans_acc = accounts[trans_data[0]]
  debit = accounts[trans_data[1]]
  credit = accounts[trans_data[2]]

  if trans_acc.acc_type() == 'liability' or 'equity':
    trans_acc.acc_balance += credit
    trans_acc.acc_balance -= debit
  else:
    trans_acc.acc_balance -= credit
    trans_acc.acc_balance += debit
  
class Account:
  def __init__(self, acc_id, acc_type, acc_name, acc_balance=0):

    self.acc_id = acc_id
    self.acc_type = acc_type
    self.acc_name = acc_name
    self.acc_balance = acc_balance

    self.transactions = {}

  accounts[acc_id] = self

class JournalEntry:
  # entry data will be of form ((trans_data), (trans_data), (trans_data)... etc)
  def __init__(self, entry_id, entry_data, date=date.today()):

    journal_entries[entry_id] = (self)

    self.entry_id = entry_id
    self.entry_data = entry_data
    self.date = date

    for entry in entry_data:
      transaction(entry)

bv_checking = Account('1000', 'asset', 'bluevine checking', 100)

print(accounts)

entry1 = JournalEntry('0021', (('1000', 0, 40)))