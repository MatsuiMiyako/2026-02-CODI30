def after_transaction(balance, transaction):
    global isBroke # global variables are all defined in functions and not outside you idiot
    if balance + transaction < 0:
        isBroke = True
        return balance
    else:
        return balance + transaction

user_balance = int(input("Enter your balance: "))
user_transaction = int(input("Enter the pending transaction: "))
isBroke = False

new_balance = str(after_transaction(user_balance, user_transaction))

if isBroke == True:
    print("You are too broke to proceed with the transation.") 
    print("Your new balance after the transaction is " + new_balance + ".")
else:
    print("Your new balance after the transaction is " + new_balance + ".")