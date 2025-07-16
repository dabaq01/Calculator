# An Elementary Calculator
print("""++++++++++++++++++++
1. Addition
2. Subtraction
3. Multiplication
4. Divition
5. Exponential
6. Floor Division
++++++++++++++++++++""")

print ("++++++++")
print ("Addition")
print ("++++++++")
print ("Please enter two numbers to sum")
#prompt the user for a number and store it
firstNumber = float (input ("first Number:"))
#prompt the user for another number and store it
secondNumber = float (input ("secondNumber:"))
sum = float (firstNumber + secondNumber)
print(f"{firstNumber} + {secondNumber}: {sum:.2f}")

print ("-----------")
print ("Subtraction")
print ("-----------")
print("Please enter two numbers to subtract")
#prompt the user for a number and store it
firstNumber = float (input ("First Number:"))
#prompt the user for another number and store it
secondNumber = float (input ("Second Number:"))
sub = float (firstNumber - secondNumber)
print(f"{firstNumber} - {secondNumber}: {sub:.2f}")

print ("**************")
print ("Multiplication")
print ("**************")
print("Please enter two numbers to multiply")
#prompt the user for a number and store it
firstNumber = float (input ("First Number:"))
#prompt the user for another number and store it
secondNumber = float (input ("Second Number:"))
mul = float (firstNumber * secondNumber)
print(f"{firstNumber} * {secondNumber}: {mul:.2f}")

print ("÷÷÷÷÷÷÷÷")
print ("Division")
print ("÷÷÷÷÷÷÷÷")
print("Please enter two numbers to divide")
#prompt the user for a number and store it
firstNumber = float (input ("First Number:"))
#prompt the user for another number and store it
secondNumber = float (input ("Second Number:"))
div = float (firstNumber / secondNumber)
print(f"{firstNumber} / {secondNumber}: {div:.2f}")

print ("^^^^^^^^^^^")
print ("Exponential")
print ("^^^^^^^^^^^")
print("Please enter two numbers to run exponential")
#prompt the user for a number and store it
firstNumber = float (input ("First Number:"))
#prompt the user for another number and store it
SecondNumber = float (input ("Second Number:"))
exp = float (firstNumber ** SecondNumber)
print(f" Exponential of {firstNumber} ** {SecondNumber} is {exp:.2f}")

print ("^^^^^^^^^^^")
print ("Floor Division")
print ("^^^^^^^^^^^")
print("Please enter two numbers to run exponential")
#prompt the user for a number and store it
firstNumber = float (input ("First Number:"))
SecondNumber = float (input ("Second Number:"))
floor = float (firstNumber // SecondNumber)
print(f" Exponential of {firstNumber} // {SecondNumber} is {floor}")

