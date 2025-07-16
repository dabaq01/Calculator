# An Elementary Calculator
print("""++++++++++++++++++++
1. Addition
2. Subtraction
3. Multiplication
4. Divition
5. Exponential
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
print(f"{firstNumber} + {secondNumber}: {sum}")

print ("-----------")
print ("Subtraction")
print ("-----------")
print("Please enter two numbers to subtract")
#prompt the user for a number and store it
firstNumber = float (input ("first Number:"))
#prompt the user for another number and store it
secondNumber = float (input ("secondNumber:"))
sub = float (firstNumber - secondNumber)
print(f"{firstNumber} - {secondNumber}: {sub}")

print ("**************")
print ("Multiplication")
print ("**************")
print("Please enter two numbers to multiply")
#prompt the user for a number and store it
firstNumber = float (input ("first Number:"))
#prompt the user for another number and store it
secondNumber = float (input ("secondNumber:"))
mul = float (firstNumber * secondNumber)
print(f"{firstNumber} * {secondNumber}: {mul}")

print ("÷÷÷÷÷÷÷÷")
print ("Division")
print ("÷÷÷÷÷÷÷÷")
print("Please enter two numbers to divide")
#prompt the user for a number and store it
firstNumber = float (input ("first Number:"))
#prompt the user for another number and store it
secondNumber = float (input ("secondNumber:"))
div = float (firstNumber / secondNumber)
print(f"{firstNumber} / {secondNumber}: {div}")

print ("^^^^^^^^^^^")
print ("Exponential")
print ("^^^^^^^^^^^")
print("Please enter two numbers to run exponential")
#prompt the user for a number and store it
Number = float (input ("first Number:"))
exp = float (firstNumber **2)
print(f" Exponential of {Number} is {exp}")

