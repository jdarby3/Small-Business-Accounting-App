from datetime import date
import streamlit as st
import pandas as pd

st.title("Small Business Accounting System")

uploaded_file = st.file_uploader("Upload Chart of Accounts", type=['csv', 'xlsx'])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)

# the initial ui will prompt user to upload a general journal and chart of accounts
# or just to add a journal entry or a new account

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
        self.acc_balance += balance_changes.get((self.acc_type, d_c), 0)
        # Record the transaction
        self.transactions[entry_num] = (d_c, amount, entity, proj_num, note, date)

# TODO: Implement journal entry processing
# def journal_entry(my_csv_file):
#     # Add logic to process CSV file and create transactions
#     pass

bv_checking = Account("asset", 1000, "Bluevine Checking")

# bv_checking.transaction("debit", 1000, "John Doe", 1, "Initial balance")
