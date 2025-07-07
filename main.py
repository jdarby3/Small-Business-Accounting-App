from datetime import date

#goal is to input coa, hournal and ledger and have them be updated

chart_of_accounts = {}
# can add logic to auto populate this dict from coa excel or csv whenever script is called

transaction_tracker = {}
# updates need to be made to the transaction function to properly populate this

class Account:
  def __init__(self, acc_type, acc_id, acc_name, acc_balance=0):
    self.acc_type = acc_type
    self.acc_balance = acc_balance
    self.acc_id = acc_id
    self.acc_name = acc_name
    self.transactions = {}
    chart_of_accounts[acc_id] = self

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

def journal_entry(my_csv_file):
  for rows in rows(my_csv)
    if 
    # add logic to assign debit credit variable based on if that column has data or empty
    #this logic also assigns amount variable with amount that was in the populated column
  ### chart_of_accounts[my_csv(column1)].transaction(my_csv(column_2), dc_variable, amount_cariable, my_csv(entity_column), etc....
    
    
    
   # chart_of_accounts[acc_id].transaction(mycsv[0] ... etc
   # for every line calls .transaction on the applicable account
  pass

bv_checking = Account("asset", 1000, "Bluevine Checking")

bv_checking.transaction("debit", 1000, "John Doe", 1, "Initial balance")
