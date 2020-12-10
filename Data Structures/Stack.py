
class Stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__top = -1

    def push(self,data):
        if self.is_full():
            print("Stack is Full")
            return None
        else:
            self.__top += 1
            self.__elements[self.__top] = data
         
    def is_empty(self):
        if self.__top == -1:
            return True
        else:
            return False
        
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data


    def is_full(self):
        if self.__top == self.get_max_size() - 1:
            return True
        else:
            return False

    def get_max_size(self):
        return self.__max_size 

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
                
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg    



