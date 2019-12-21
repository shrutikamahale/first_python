#Python Program to reverse a String
name = str(input("Enter a name "))
s = ""
for ch in name:
  s = ch + s
print(s)