num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the arithmetic(eg. + - * etc): ")

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
    result = "Error: The second number can't be zero!!"
else:
  result ="Invalid input! Check your input again"
print(f"num1 {operation} num2 is: {result}")