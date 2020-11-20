import unittest
import budget

from budget import Category

class TestBudget(unittest.TestCase):

    def setUp(self):
        self.food = Category("Food")
        self.laundry = Category("Laundry")

    def tearDown(self):
        pass    
    
    def test_deposit(self):
        self.food.deposit(1000,"Initial Deposit")
        actual = self.food.ledger[0]
        expected = {"amount":1000,"description":"Initial Deposit"}
        self.assertEqual(actual,expected,"Expected deposit method to create a specific object in ledger")

    def test_deposit_no_description(self):
        self.laundry.deposit(1000)
        actual = self.laundry.ledger[0]
        expected = {"amount":1000,"description":""}
        self.assertEqual(actual,expected,'Expected deposit method to create a specific object in ledger')

    def test_withdraw(self):
        self.food.deposit(2000,"Initial Deposit")
        good_withdraw = self.food.withdraw(1000,"BBQ Nation")
        actual = self.food.ledger[1]
        expected = {"amount":-1000,"description":"BBQ Nation"}
        self.assertTrue(good_withdraw,'Expected method to return true')
        self.assertEqual(actual,expected,"Expected withdraw method to create a specific object in ledger")

    def test_withdraw_no_description(self):
        self.laundry.deposit(2000,"Initial deposit")
        good_withdraw = self.laundry.withdraw(1000)
        actual = self.laundry.ledger[1]
        expected = {"amount":-1000,"description":""}
        self.assertTrue(good_withdraw,'Expected method to return true')
        self.assertEqual(actual,expected,'Expected withdraw method to create a specific object in ledger')        
        
    def test_transfer(self):
        self.food.deposit(1000,"deposit")
        self.laundry.deposit(1000,"Initial deposit")
        good_transfer = self.laundry.transfer(500,self.food)
        actual = self.food.ledger[1]
        expected = {"amount":500,"description":"Transfered from "+self.laundry.category}
        self.assertEqual(actual,expected,'Expected trasnfer method to create a specific object in ledger')
        self.assertTrue(good_transfer,'Expected method to return true')

if __name__ == '__main__':
    unittest.main()        
