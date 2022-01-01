from array import*
arr = array("i", [])
x = int(input("Enter the length of array"))
for i in range (x):
    n = int(input("Enter the element"))
    arr.append(n)
print(arr)
for i in range(0,x):
    for j in range(i+1,x):
        if arr[i] == arr[j]:
            print("Dublicate element is",arr[j])
        

