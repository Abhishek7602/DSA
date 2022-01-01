def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0

    while(low <= high):

        mid = (low + high) // 2

        if(arr[mid] < x):
            low = mid +1
        
        elif(arr[mid] > x):
            high = mid -1

        else:
            return mid
    return -1

arr = [10,20,30,40,50]
x = 60

result = binary_search(arr, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found")