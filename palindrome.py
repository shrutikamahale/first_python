#Python Program to check if a string is Palindrome or not
name = str(input("Enter a name "))
s = ""
for ch in name:
  s = ch + s
if(s == name):
  print("String is palindrome")
else:
  print("String is not palindrome")