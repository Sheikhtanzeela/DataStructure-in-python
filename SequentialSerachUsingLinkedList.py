class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.key = None

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def setKey(self, key):
        self.key = key

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getKey(self):
        return self.key

    def searchValue(self, key):
        current = self.head
        while current != None:
            if current.key == key:
                current.data
            current = current.next
        return None

    def updateList(self, key, val):
        current = self.head
        while current != None:
            if current.key == key:
                current.data = val
                return
            current = current.next
        first = Node()
        first.setData(val)
        first.setKey(key)


setData(2)
setData(8)
setData(5)
setData(3)
setData(90)
setData(21)
setData(34)

setKey(1)
setKey(2)
setKey(3)
setKey(4)
setKey(5)
setKey(6)

sv = searchValue(4)
print(sv)

up = updateList(7, 9)
print(up)
