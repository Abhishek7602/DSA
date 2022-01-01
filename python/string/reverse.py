s = str(input("Enter your Name:"))
l = len(s)
newStr = ""
for i in range (l-1, -1, -1):
    newStr += s[i]
print(newStr)
