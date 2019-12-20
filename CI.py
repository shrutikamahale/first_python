#Python Program for compound interest
prnc = float(input("Enter prnc"))
rate = float(input("Enter rate"))
nofyr = float(input("Enter no. of year"))
amount = prnc * (pow((1+rate/100),nofyr))
print("Amount")
print(amount)
print("Compound intrest on compounded amount")
CI = amount - prnc
print(CI)