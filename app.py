
weight=float(input("Enter your weight : "))
value=input("Is your weight in Kg or Pounds ? Type K for Kg and P for pounds : ")
if value.upper() =="K":
    answer=float(weight)/0.45
    print("Your weight in Pounds = "+str(answer)+" "+ "pounds.")
elif value.upper() =="P":
    answer=float(weight)*0.45
    print("Your weight in kg = "+str(answer)+" "+ "kg.")
else:
    print("Enter valid input")