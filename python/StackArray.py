class Stack:
    def __init__(self,size):
        self.__top = -1
        self._arr = [0]*size
    
    def push(self, element):
        if(self.isFull()):
            print("Stack Overflow")
            return
        self.__top +=1
        self._arr[self.__top] = element
        
    def isEmpty(self):
        if(self.__top == -1):
            return True
        return False
    
    def isFull(self):
        if(self__top == len(self._arr)-1):
            return True
        return False
    
    def display(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        print('Stack: ', end=" ")
        for i in range(self.__top+1):    
            print(self._arr[i], end=" ")
        print()
     
    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        lastElement = self.arr[self.__top] 
        self.__top -= 1
        return lastElement
            

n = int(input())
s = Stack(n)
s.push(10)
s.push(20)
s.push(30)
s.display()


