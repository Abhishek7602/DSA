def Binary_Rec(arr, low, high, x):
    
    if (low <= high):
        mid = (low + high)//2
    
        if(arr[mid] == x):
      
           return mid
    
        elif(arr[mid] < x):
            
            return Binary_Rec(arr, mid+1, high, x)
    
        else:
            return Binary_Rec(arr, low, mid-1, x)
    return -1
    
arr = [10,20,30,40,50]
x = 5
low = 0
high = len(arr)
result = Binary_Rec(arr, low, high, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found")



