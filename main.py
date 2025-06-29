from datetime import date

accounts = ()

transactions = ()

class Account:
  def __init__(self, acc_name, acc_id, acc_type, acc_balance):
    self.acc_name = acc_name
    self.acc_id = acc_id
    self.acc_type = acc_type
    self.acc_balance = acc_balance
    self.transactions = ()

class Transaction:
  def __init__(self, trans_date, trans_num, acc_id, debit, credit, trans_desc):
    self.trans_date = date.today()
    self.trans_num = len(transactions) + 1
    self.acc_id = acc_id
    self.trans_acc_num = trans_acc_num
    self.debit = debit
    self.credit = credit
    self.trans_desc = trans_desc

def add_transaction(trans, acc):
  if trans.acc_id() == acc.acc_id()
    





