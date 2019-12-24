#Python Program to find the largest element in the given array
arr = [23,45,12,89,45]
max = arr[0]
for i in range(0,len(arr)):
  if (arr[i] > max):
    max = arr[i]
print("Largest element: " +str(max))
