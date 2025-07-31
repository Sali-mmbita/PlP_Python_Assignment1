#prompting the user to enter the numbers and operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the arithmetic operations( eg. + - * /): ")

#chection the user's input performing the calculation based on them
if operation == '+':
  result = num1 + num2
elif operation == '-':
  result = num1 - num2
elif operation == '*':
  result = num1 * num2
elif operation == '/':
  if num2 != 0:
   result = num1 / num2
  else:
    result = "Undefined: Please ensure that your second number is not zero!"
else:
  result ="Invalid input! Check your input again"
  
  #the result if the user enters the correct input
print(f"{num1} {operation} {num2} = {result}")