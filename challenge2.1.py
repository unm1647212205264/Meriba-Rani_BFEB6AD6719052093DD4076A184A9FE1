class Bank_Account:
  def __init__(self):
    self.balance=0
    print("Hello!!! Welcome to the Deposit & Withdraw Machine")
  def deposit(self):
    amount=float(input("Enter amount to be Deposited: "))
    print("\n Amount Deposited: ", amount)
  def withdrawal (self): 
    amount=float(input("Enter amount to be Withdrawn: "))
    if self. balance>=amount:
      self.balance-=amount
      print("\n You Withdrew: ", amount)
    else:
      print("Insufficient balance")
  def display(self):
    print("\n Net Available Balance=", self.balance)
s=Bank_Account()
s.deposit()
s.withdrawal()
s.display()