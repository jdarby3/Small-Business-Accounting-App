from datetime import date

global_transactions = []

class Account:
  def __init__(self, acc_type, acc_balance, acc_id, acc_name):
    self.acc_type = acc_type
    self.acc_balance = acc_balance
    self.acc_id = acc_id
    self.acc_name = acc_name
    self.transactions = []

  def transaction(self, d_c, amount, entity, proj_num, note, date=date.today()):
    # Define the balance change rules
    balance_changes = {
      ("asset", "debit"): amount,
      ("asset", "credit"): -amount,
      ("liability", "debit"): -amount,
      ("liability", "credit"): amount
    }
    
    # Apply the balance change
    self.acc_balance += balance_changes.get((self.acc_type, d_c), 0)
    
    # Record the transaction
    self.transactions.append((d_c, amount, entity, proj_num, note, date))
    global_transactions.append((d_c, amount, entity, proj_num, note, date))

checking = Account("asset", 0, '0001', "Checking")

checking.transaction("debit", 1000, "John Doe", 1, "Initial balance")

print(checking.transactions[0][3])