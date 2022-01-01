arr = [15,5,10,25,20]
for i in range (len(arr)-1):
    for j in range(len(arr)-1-i):
        if(arr[j]>arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1]= temp
print(arr)