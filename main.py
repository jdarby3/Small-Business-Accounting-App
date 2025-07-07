from datetime import date

chart_of_accounts = #should hold all accounts in a dict with the acc_id being the
                          # key and the value being the instance

class Account:
  def __init__(self, acc_type, acc_id, acc_name, acc_balance=0):
    self.acc_type = acc_type
    self.acc_balance = acc_balance
    self.acc_id = acc_id
    self.acc_name = acc_name
    self.transactions = {}
    #add code to add each new account to my chart of accounts dict

  def transaction(self, entry_num, d_c, amount, entity, proj_num, note, date=date.today()):
    # Define the balance change rules
    balance_changes = {
      ("asset", "debit"): amount,
      ("asset", "credit"): -amount,
      ("liability", "debit"): -amount,
      ("liability", "credit"): amount
    }
    # Apply the balance change
    self.acc_balance += balance_changes.get((self.acc_type, d_c))
    # Record the transaction
    self.transactions[entry_num] = (d_c, amount, entity, proj_num, note, date)

def journal_entry(my_csv):
  for lines in my_csv
   # chart_of_accounts[acc_id].transaction(mycsv[0] ... etc
   # for every line calls .transaction on the applicable account
  pass

bv_checking = Account("asset", 1000, "Bluevine Checking")

bv_checking.transaction("debit", 1000, "John Doe", 1, "Initial balance")
