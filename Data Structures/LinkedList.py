# Implementing a linked list in Python

# Create a class Node comprising of Data and Address of next node
class Node:                     

    # Initiating the node with given data 
    def __init__(self,data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        # Setting the link to next node object
        self.__next = next_node            

# Create a class LinkedList to use Nodes 
class LinkedList:

    def __init__(self):
        # Initiate linkedlist with empty head and tail nodes
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def search(self,data):
        temp = self.__head
        while(temp is not None):
            list_data = temp.get_data()
            if data == list_data:
                print("Data Found")
                return temp
            temp = temp.get_next()
        
        print("Data Not Found")    
        return None                     
    
    def insert(self,data,data_before):
        new_node = Node(data)
        node_before = self.search(data_before)

        if node_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            new_node.set_next(node_before.get_next())
            node_before.set_next(new_node)
            
            if new_node.get_next() is None:
                self.__tail = new_node


    def add(self,data):
        # Create a new node with the given data
        new_node = Node(data)
        # If head node is empty
        if self.__head is None:
            self.__head = self.__tail = new_node
        # If LinkedList has some values in it already
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node    
    

    def delete(self,data):
        del_node = self.search(data)

        if del_node is not None:
            if del_node is self.get_head():
                self.__head = del_node.get_next()
                del_node = None

            else:
                temp = self.get_head()
                while(temp is not del_node):
                    print(temp.get_data())
                    prev = temp
                    temp = temp.get_next()

                prev.set_next(del_node.get_next())
                del_node = None

        else:
            return "Node not found"    

    def reverse(self):
        curr_node = self.get_head()
        prev_node = None
        while(curr_node is not None):
            next_node = curr_node.get_next()
            curr_node.set_next(prev_node)
            prev_node = curr_node
            curr_node = next_node
        self.__head = prev_node


    def display(self):
        temp = self.__head
        while(temp is not None):
            print(temp.get_data())
            temp = temp.get_next()
    
    def size(self):
        temp = self.__head
        count = 0
        while(temp is not None):
            count += 1
            temp = temp.get_next()

        return count    

    def __str__(self):
        temp = self.__head
        msg = []
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()

        msg = " --> ".join(msg)
        
        return msg


def replace_value(number_list,new_value):
    temp = number_list.get_head()
    max = 0 
    while(temp is not None):        

        if max < temp.get_data():
            max = temp.get_data()
            max_node = temp
        temp = temp.get_next()

    max_node.set_data(new_value)
    return number_list



input_list = input("Enter items to add in LinkedList: ")
input_list = input_list.split()

number_list = LinkedList()

for val in input_list:
    number_list.add(val)

print("Head --> Tail:",number_list)
print("Size:",number_list.size())

#data_input = input("Enter data to be found in Linkedlist: ")
#print(linkedlist.search(data_input))

#print(linkedlist)

#data_insert = input("Enter data to insert: ")
#data_before = input("Enter data before which prev data is to be inserted: ")

#linkedlist.insert(data_insert,data_before)
#print(linkedlist)

#data_del = input("Enter data to be deleted: ")
#linkedlist.delete(data_del)
#print(linkedlist)


#new_value = input("Enter value to replace max value in list: ") 
#print(replace_value(number_list,int(new_value)))

number_list.reverse()
print(number_list)
