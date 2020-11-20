Budget Tracking Application 

-> Made using OOP Concepts by making a Category Class with attributes and behaviors.
-> Category class is instantiated by the name of the category and an empty ledger list wherein all the transactions are stored.
-> Object of Category class looks like this: object = Category("Food")
-> Class independent method create_spend_chart() prints out the %spend in each category according to the withdrawal amount.

Attributes:
-> category : <Name of the category>
-> ledger : [list of transactions in that category]

Methods:
-> deposit(amount,descritpion="")
    1) Creates a dictionary object {"amount" : <amount given by user>, "description" :"<string entered by user>"}
    2) Appends this object to ledger list

-> withdraw(amount,description="")
    1) Similar to deposit method 
    2) Dictionary object looks like {"amount" : <negative of amount entered by user>,"description":<string entered by user>}
    3) Appends this object to ledger list

-> transfer(amount,category_object)
    1) Withraws amount from base category and deposits that amount to the ledger of category_object
    2) Description for base category "Trasferred to <category_object>" and for category_object "Transferred from <base category>"

-> get_balance()
    1) Calculates ledger balance by subtracting total withdrawals with total deposits
    2) Only when ledger balance is more than the withdrawn amount can any more money with withdrawn -> check_funds() method

-> check_funds()
    1) Checks if current ledger balance is enough to withdraw funds

-> create_spend_chart()
    1) Class independent method that provides %spend in each category according to the withdrawals for each category
   *2) Plot the values on a bar graph (In Progress...) 