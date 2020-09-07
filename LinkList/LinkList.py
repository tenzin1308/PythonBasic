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


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode



    def pop(self):
        if self.head is None:
            print("The list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            currentNode = self.head
            while currentNode.next.next is not None:
                currentNode = currentNode.next
            currentNode.next = None

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
    linkedList.insert(5)
    linkedList.insert(25)
    linkedList.insert(100)
    linkedList.printList()

    linkedList.pop()
    linkedList.pop()
    linkedList.printList()
