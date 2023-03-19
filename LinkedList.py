"""
Peter Demachkie
pdemachk@uscs.edu
https://github.com/PeterDemachkie/LinkedList.py
LinkedList.py
"""

class Node:
    def __init__(self, x):
        self.data = x #any
        self.next = None #Node
        self.prev = None #Node
        
class List:
    def __init__(self):
        self.front = None #Node
        self.back = None #Node
        self.cursor = None #Node
        self.length = 0 #int
        self.index = -1 #int

    # Access functions
    def getFront(self):
        if not self.front:
            return None
        return self.front.data
    
    def getBack(self):
        if not self.back:
            return None
        return self.back.data
    
    def getCursor(self):
        if not self.cursor:
            return None
        return self.cursor.data

    def getNext(self):
        if not self.cursor.next:
            return None
        return self.cursor.next.data
    
    def getPrev(self):
        if not self.cursor.prev:
            return None
        return cursor.prev.data

    def Index(self):
        return self.index

    def Length(self):
        return self.length

    def Equals(self, List L):
        A = self.front
        B = L.front

        if L.Length() != self.length:
            return False
        while B != None:
            if A.data != B.data:
                return False
            A = A.next
            B = B.next
        return True


    # Manipulation Functions
    # Adds a node to the back of the list
    def append(self, x):
        new = Node(x)
        if self.length == 0:
            self.front = self.back = self.cursor = new
        
        else:
            self.back.next = new
            new.prev = self.back
            self.back = new

        self.length += 1
    
    # Adds a node to the front of the list
    def prepend(self, x):
        new = Node(x)
        if self.length == 0:
            self.front = self.back = self.cursor = new

        else:
            self.front.prev = new
            new.next = self.front
            self.front = new

        self.length += 1
        self.index += 1

    # Inserts a node right after the cursor
    def insertAfter(self, x):
        if self.cursor:
            new = Node(x)
            cursor.prev.next = new
            new.prev = cursor.prev
            new.next = cursor
            cursor.prev = new

            self.length += 1

    # Inserts a node right before the cursor
    def insertBefore(self, x):
        if self.cursor:
            new = Node(x)
            cursor.next.prev = new
            new.next = cursor.next
            new.prev = cursor
            cursor.next = new

            self.length += 1
            self.index += 1

    # Removes node under cursor from the list
    def delete(self):
        if self.cursor == self.front:
            self.deleteFront()
            return
        if self.cursor == self.back:
            self.deleteBack()
            return
        if length > 0 and self.cursor:
            self.cursor.prev.next = self.cursor.next
            self.cursor.next.prev = self.cursor.prev

            self.cursor = None
            self.index = -1
            self.length -= 1

    # Removes the current front node and sets the next to front
    def deleteFront(self):
        if self.length > 0 and self.cursor != self.front:
            self.front.next.prev = None
            self.front = self.front.next
            self.length -= 1
            self.index -= 1

        elif self.length > 0 and self.cursor == self.front:
            self.front.next.prev = None
            self.front = self.front.next
            self.cursor = None
            self.length -= 1
            self.index = -1
        
        if self.length == 0:
            self.front = self.back = self.cursor = None
            self.index = -1

    # Removes the current back node and sets the prev to back
    def deleteBack(self):
        if self.length > 0 and self.cursor != self.back:
            self.back.prev.next = None
            self.back = self.back.prev
            self.length -= 1

        elif self.length > 0 and self.cursor == self.front:
            self.back.prev.next = None
            self.back = self.back.prev
            self.cursor = None
            self.length -= 1
            self.index = -1

        if self.length == 0:
            self.front = self.back = self.cursor = None
            self.index = -1

    # Returns the list to empty state
    def clear(self):
        while self.length > 0:
            self.deleteFront()

    # Moves cursor to the front of the list
    def moveFront(self):
        if self.length > 1:
            self.cursor = self.front
            self.index = 1

    # Moves cursor to the back of the list
    def moveBack(self):
        if self.length > 1:
            self.cursor = self.back
            self.index = self.length

    # Moves cursor forward one Node
    def moveNext(self):
        if self.cursor:
            if self.cursor != self.back:
                self.cursor = self.cursor.next
                self.index += 1
            else:
                self.cursor = None
                self.index = -1
    
    # Moves the cursor backwards one Node
    def movePrev(self):
        if self.cursor:
            if self.cursor != self.front:
                self.cursor = self.cursor.prev
                self.index += 1
            else:
                self.cursor = None
                self.index = -1

    # Sets the data in the Node under the cursor to x
    def setCursor(self, x):
        if self.cursor:
            self.cursor.data = x

    # Other functions
    def __str__(self):
        s = "["
        x = self.front
        while x != None:
            s += str(x.data)
            if x.next != None:
                s += ", "
            x = x.next
        s += "]"
        return s

    def __repr__(self):
        return self.__str__()
