
#Node Class
class Node:
    def __init__(self,data=None): #Initialises the node object

        self.data=data #Assign data
        self.nextnode=None #Assign's reference to next data null until another element is added

#Main Class containing Node object
class LinkedList():

    def __init__(self): #Asssign's head of the Linked List

        self.head=None

    def Prepend(self,new_data): #Adds new elements to the start of the Linked List as the Head

        new_node=Node(new_data) #Using the Node Object Assign's the new element
        new_node.nextnode=self.head #Assign's the reference of the next element as the former Head
        self.head=new_node #Element takes place of the former Head(Not Replacing)

    def printlst(self): #Prints all nodes from Head till Tail

        printdata=self.head #First Data is the head as it contains the reference to the next data

        while printdata is not None: #Continues until Data is not Null
            print(printdata.data) #Prints the data
            printdata=printdata.nextnode #Moves to the next data using the assigned reference 

    def size(self): #Prints the size of the Linked List

        temp=self.head #Head of Linked List
        count=0 #count increases as it goes through each node

        while(temp): #continues until node isnt null
            count+=1 
            temp=temp.nextnode #moves to next node
        print(count)

    
LL=LinkedList() 

LL.Prepend(1)
LL.Prepend(200)
LL.Prepend(41)
LL.printlst()
LL.size()
