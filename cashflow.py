# A Simulation of personal cash flow
#Personal Allowance
money = 2000
print ("Allowance is ₦2,000.00k")

#Expenditure on Books
print ("₦400.00k was spent on books")
books = 400
money -= books
print (f"New Balance is: ₦{money:,.2f}k")

#Lost But Found Funds
print ("₦100 was found under the bed")
lostButFound = 100
money += lostButFound
print (f"New Balance is: ₦{money:,.2f}k")

##Expenditure on Snacks
print ("₦250 was spent on snacks")
snacks = 250
money -= snacks
print (f"New Balance is: ₦{money:,.2f}k")

#Expenditure on Gifting
print ("25% of the current balance was gifted to siblings")
percentage = 0.25 * money
money -= percentage
print (f"New Balance is: ₦{money:,.2f}k")

#Expenditure on Data
print ("⅓ of the allowance was spent on data")
oneThird = 1/3 * money
money -= oneThird
print (f"New Balance is: ₦{money:,.2f}k")

#Expenditure on Savings & Tithing
print ("Current ballance was split equally between savings and tithing")
tithe = money / 2
money -= tithe
print (f"New Balance is: ₦{money:,.2f}k")

#Balance After withdrawing All ₦100 notes
print ("Balance after removing all ₦100 notes")
money %= 100
print (f"New Balance is: ₦{money:,.2f}k")
