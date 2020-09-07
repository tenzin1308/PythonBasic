# LinkList is a user defined data structure.
# Steps:  (1) Create Node
#             (a) Data
#             (b) Pointer
#         (2) Create linked list
#         (3) Add nodes to linked list


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.min = None
        self.max = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        newNode = Node(data)
        newNode.min = data
        newNode.max = data
        if self.head is None:
            self.head = newNode
            self.size = 1
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            if currentNode.max > newNode.max:
                newNode.max = currentNode.max
            if currentNode.min < newNode.min:
                newNode.min = currentNode.min
            currentNode.next = newNode

            self.size += 1


    def pop(self):
        if self.head is None:
            print("The list is empty")
            self.size = 0
        elif self.head.next is None:
            self.head = None
            self.size -= 1
        else:
            currentNode = self.head
            while currentNode.next.next is not None:
                currentNode = currentNode.next
            currentNode.next = None
            self.size -= 1

    def remove(self, index):
        if index < 0 or index > (self.size - 1):
            print("Sorry invalid index")
        elif self.size is 0:
            print("Sorry the list is empty")
        else:
            currentNode = self.head
            while currentNode.next.next is not None:
                currentNode = currentNode.next
            currentNode.next = None

    def sizeof(self):
        return self.size

    def getMin(self):
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        return currentNode.min

    def getMax(self):
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        return currentNode.max

    def printList(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            currentNode = self.head
            while currentNode.next is not None:
                print(f"{currentNode.data}", end=" ")
                currentNode = currentNode.next
            print(f"{currentNode.data}")


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insert(15)
    linkedList.printList()
    print(f"Max = {linkedList.getMax()}")
    print(f"Min = {linkedList.getMin()}")

    linkedList.insert(5)
    linkedList.printList()
    print(f"Max = {linkedList.getMax()}")
    print(f"Min = {linkedList.getMin()}")

    linkedList.insert(25)
    linkedList.printList()
    print(f"Max = {linkedList.getMax()}")
    print(f"Min = {linkedList.getMin()}")

    linkedList.pop()
    linkedList.printList()
    print(f"Max = {linkedList.getMax()}")
    print(f"Min = {linkedList.getMin()}")

    linkedList.pop()
    linkedList.printList()
    print(f"Max = {linkedList.getMax()}")
    print(f"Min = {linkedList.getMin()}")
    # linkedList.pop()
    # print((linkedList.getMax()))
    # print((linkedList.getMin()))
