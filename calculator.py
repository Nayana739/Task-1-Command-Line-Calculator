#addition function
def add(num1,num2):
   return num1+num2

#subtraction function
def sub(num1,num2):
   return num1-num2

#multiplication function 
def mul(num1,num2):
   return num1*num2

#division function
def div(num1,num2):
   return num1/num2

#Print Command Line Calculator
print("Command Line Calculator")
choice=1
while(choice!=0):
  print("1. PERFORM ADDITION")
  print("2. PERFORM SUBTRACTION")
  print("3. PERFORM MULTIPLICATION")
  print("4. PERFORM DIVISION")
  print("5. Exit Loop")
  choice = int(input("Enter your choice :"))
  if choice==5:
     print("Exit Loop")
     break
  x = int(input(" Enter the first number : "))
  y = int(input(" Enter the second number : "))
  if choice == 1:
     print(x, "+" ,y ,"=" ,add(x,y))
  elif choice == 2:
     print(x, "-" ,y ,"=" ,sub(x,y))
  elif choice == 3:
     print(x, "*" ,y ,"=" ,mul(x,y))
  elif choice == 4:
       res=div(x,y)
       print("%d  / %d = %.2f" %(x,y,res))
  else:
    print("Invalid Choice, try again");
