def sum(num1, num2) :
  return num1 + num2
  
def sub(num1, num2) :
  return num1 - num2

def mul(num1, num2) :
  return num1 * num2

def div(num1, num2) :
  if num2 != 0 :
    return num1 / num2
  else :
    return "Can not divided by zero."

num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))

print("Enter operation choice")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")
option = input("Enter operation : ")

if option == "1" :
  print(sum(num1, num2))
elif option == "2" :
  print(sub(num1, num2))
elif option == "3" :
  print(mul(num1, num2))
elif option == "4" :
  print(div(num1, num2))
else :
  print("Please Enter valid input")