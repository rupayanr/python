
import budget
from budget import create_spend_chart
from budget import Category

food = Category("Food")
food.deposit(4000,"deposit")
food.withdraw(2000,"bbq nation")

petrol = Category("Petrol")
petrol.deposit(10000,"deposit")
petrol.withdraw(5000,"petrol")


print(food)
print(petrol)

create_spend_chart([food,petrol])