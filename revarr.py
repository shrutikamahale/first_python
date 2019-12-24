def revarr(arr, start, end): 
    while start < end: 
        arr[start], arr[end] = arr[end], arr[start] 
        start += 1
        end -= 1 
arr = [1, 2, 3, 4, 5, 6] 
print(arr) 
revarr(arr, 0, 5) 
print(arr) 
