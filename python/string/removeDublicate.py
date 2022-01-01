s = 'xxyyzz' 
a = []
for i in range(len(s)-1):
    if(s[i] == s[i+1]):
        i = +1
    else:
        a.append(s[i])
        print(a)
if(len(a) == 0):
    print("Empty String")
else:   
    print(a)