#Python Program to find factorial of a number
num = int(input("Enter a number: "))
factorial = 1
if (num == 0):
print("factorial of 0 is 1")
elif (num < 0):
print("factorial of negative number does not exist")
else:
for i in range (1, num+1):
factorial=factorial*i
print("factorial of",num, "is", factorial)
