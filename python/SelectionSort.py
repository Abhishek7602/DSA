arr = [15,5,10,20,1]
for i in range(len(arr)-1):
    min = i
    for j in range(i+1,len(arr)):
        if (arr[j] < arr[min]):
            min = j
    arr[i],arr[min] = arr[min], arr[i]
print(arr)
         