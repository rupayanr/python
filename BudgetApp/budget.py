# To make a budget app where you track your expenses

class Category:

    def __init__(self,category):
        self.category = category
        self.ledger = []

    def __str__(self):
        self.heading = "***********"+self.category+"***********\n"
        self.transactions = ""
        for dict in self.ledger:
            self.transactions += dict["description"] +" "+ str(dict["amount"])+"\n"

        return self.heading + self.transactions + "Total: " + str(self.get_balance()) 

    def deposit(self,amount,description=""):
        self.ledger.append({"amount" : amount,"description" : description})

    def withdraw(self,amount,description=""):

        if self.ledger == []:
            print("Please deposit amount to withdraw")
            return False 

        if self.check_funds(amount) == True:
            amount = 0 - amount
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

                
    def get_balance(self):
        deposits = []
        withdrawls = []

        for dicts in self.ledger:
            if dicts["amount"] > 0:
                deposits.append(dicts["amount"])
            else:
                withdrawls.append(0 - dicts["amount"])

        total_deposit = sum(deposits)
        total_withdrawl = sum(withdrawls)

        balance = total_deposit - total_withdrawl
        return balance

    def transfer(self,amount,category_object):
        self.object = category_object

        if self.check_funds(amount) == True: 
            self.withdraw(amount,"Transfered to " + self.object.category)
            self.object.deposit(amount,"Transfered from " + self.category)
            return True
        else:
            return False

    def check_funds(self,amount):

        if amount > self.get_balance():
            return False
        else:
            return True             

def create_spend_chart(categories):
    print("***********************")
    print("Percentage Spend By Category")
    
    withdrawls = []
    category = []
    spends = []

    for object in categories:
        for dict in object.ledger:
            if dict["amount"] < 0:
                withdrawls.append(0 - dict["amount"])
                category.append(object.category)
    
    total = sum(withdrawls)

    for i in range(0,len(category)):
        spend_percentage = round((withdrawls[i] / total) * 100)
        print("Percentage spent in: "+category[i]+" = "+str(spend_percentage)+"%")
        spends.append(spend_percentage)

    for i in range(0,len(spends)):
        val = spends[i] 
        if val % 10 != 0:
            rem = val % 10
            if rem in range(1,5):
                val = val - rem
                spends[i] = val
            if rem in range(5,10):
                rem = rem // 2
                val = val + rem
                spends[i] = val    
                 
                    
    


