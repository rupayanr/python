# To implement Queue data structure

class Queue:

    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1
        self.__front = 0
    
    def get_max_size(self):
        return self.__max_size


    def is_full(self):
        if(self.__rear == self.__max_size -1):
            return True
        else:
            return False
    
    def is_empty(self):
        if(self.__rear == -1 or self.__front == self.get_max_size()):
            return True
        else:
            return False


    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
            return None
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data


    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data
    
    def __str__(self):
        msg = []
        index = self.__front
        while(index <= self.__rear):
            msg.append(str(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue Data(Front To Rear): "+msg
        return msg

