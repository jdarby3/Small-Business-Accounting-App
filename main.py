from datetime import date

accounts = {}

journal_entries = {}

transactions = {}

#trans_data will be in form (acc_id, debit, credit)
def transaction(trans_data, trans_id, trans_self):

  trans_acc = accounts[trans_data[0]]
  debit = trans_data[1]
  credit = trans_data[2]

  if trans_acc.acc_type == 'liability' or trans_acc.acc_type == 'equity':
    trans_acc.acc_balance += credit
    trans_acc.acc_balance -= debit
  else:
    trans_acc.acc_balance -= credit
    trans_acc.acc_balance += debit  
  
  trans_acc.transactions[trans_id] = trans_self

class Account:
  def __init__(self, acc_id, acc_type, acc_name, acc_balance=0):

    accounts[acc_id] = self

    self.acc_id = acc_id
    self.acc_type = acc_type
    self.acc_name = acc_name
    self.acc_balance = acc_balance

    self.transactions = {}

class JournalEntry:
                # entry data will be of form ((trans_data), (trans_data), (trans_data)... etc)
  def __init__(self, entry_id, entry_data, date=date.today()):

    journal_entries[entry_id] = (self)

    self.entry_id = entry_id
    self.entry_data = entry_data
    self.date = date

    for entry in entry_data:
      transaction(entry, entry_id, self)

bv_checking = Account('1000', 'asset', 'bluevine checking', 100)

# a trailing comma is important for single element journal entries to run correctly, 
# but this should never happen in real accounting or debits and credits wouldnt be balanced
entry1 = JournalEntry('0021', (('1000', 0, 40), ))

print(bv_checking.transactions)