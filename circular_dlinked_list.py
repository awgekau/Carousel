class CircularDLinkedListNode:
    
    def __init__(self, initData, initNext = None, initPrevious = None):
        '''
        This function helps us by initializing a new instance of the CircularDLinkedListNode class.
        '''

        self.data = initData
        self.next = initNext 
        self.previous = initPrevious

    def getData(self):
        '''
        This function returns the data stored in the node
        '''
        return self.data

    def getNext(self):
        '''
        This function returns the next node in cdlinkedlist
        '''
        return self.next

    def getPrevious(self):
        '''
        This function returns the previous node in cdlinkedlist
        '''
        return self.previous

    def setData(self, newData):
        '''
        This function sets the data of a node.
        '''
        self.data = newData

    def setNext(self, newNext):
        '''
        This function sets the next node of a node and also updates the previous reference of the new next node.
        '''
        self.next = newNext
        newNext.previous = self

    def setPrevious(self, newPrevious):
        '''
        This function sets the previous node of a node and also updates the next reference of the new previous node.
        '''
        self.previous = newPrevious
        newPrevious.next = self
    


class CircularDoublyLinkedList:

    def __init__(self, maxSize = 5):
        '''
        This function helps us by initializing a new instance of the CircularDoublyLinkedList class.
        '''

        self.head = None
        self.tail = None
        self.current = None 
        self.size = 0
        self.maxSize = maxSize
    
    def isFull(self):
        '''
        This function returns true if the cdLinkedlist is full.
        '''
        return self.size >= self.maxSize

    def isEmpty(self):
        '''
        This function returns false if the cdLinkedList is full.
        '''
        return self.size == 0

    def length(self):
        '''
        This function returns the number of nodes in cdLinkedList
        '''
        return self.size

    def getCurrentNode(self):
        '''
        This function helps us get the current node
        '''
        return self.current
    
    def getPreviousNode(self):
        '''
        This function helps us get the previous node of the current node
        '''
        if self.current is not None:  
            return self.current.getPrevious()
        return None   
    def getNextNode(self):
        '''
        This function helps us get the next node of the current node
        '''
        if self.current is not None: 
            return self.current.getNext()
        return None 

    def add(self, item):
        '''
        This function helps us add a node at the end of the cdLinkedList and sets it as the current node
        '''
        newNode = CircularDLinkedListNode(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode 
            newNode.previous = newNode
            
        else:
            newNode.next = self.head 
            newNode.previous = self.tail 
            self.tail.next = newNode  
            self.head.previous = newNode  
            self.tail = newNode 

        self.current = newNode 
        self.size += 1

    def addLeft(self, item):
        '''
        This function adds a new node to the left of the current node and sets it as the current node
        '''
        if self.isEmpty():
            self.add(item) 
        else:
            newNode = CircularDLinkedListNode(item, self.current, self.current.previous)
            self.current.previous.next = newNode 
            self.current.previous = newNode 
            if self.current == self.head:  
                self.head = newNode 
            self.current = newNode 
            self.size += 1

    def addRight(self, item):
        '''
        This function adds a new node to the right of the current node and sets it as the current node
        '''
        if self.isEmpty():
            self.add(item)
        else:
            newNode = CircularDLinkedListNode(item, self.current.next, self.current)
            self.current.next.previous = newNode 
            self.current.next = newNode 
            if self.current == self.tail:
                self.tail = newNode
            self.current = newNode 
            self.size += 1

    def remove(self, item):
        '''
        This function helps us remove the current node from the cdLinkedList and sets the previous node of the deleted node as the current node
        '''
        current = self.head
        if self.size == 0:
            return 

        for i in range(self.size):  
            if current.getData() == item:
                if self.size == 1: 
                    self.head = None
                    self.tail = None
                    self.current = None
                else:
                    current.getPrevious().setNext(current.getNext())
                    current.getNext().setPrevious(current.getPrevious())
                    if current == self.head:
                        self.head = current.getNext()
                    if current == self.tail:
                        self.tail = current.getPrevious()
                    if current == self.current:
                        self.current = current.getNext()
                self.size -= 1
                return 
            current = current.getNext()



