
class Node:
    # default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    def updateData(self, data):
        self.data = data

    def setLink(self, node):
        self.link = node

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.link


# LinkedList class
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    # method adds elements to the left of the Linked List
    def addToStart(self, data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    # method adds elements to the right of the Linked List
    def addToEnd(self, data):
        start = self.head
        tempNode = Node(data)

        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return True

    # method displays Linked List
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # method returns length of linked list
    def length(self):
        start = self.head
        size = 0
        while start  :# start != None
            size += 1
            start = start.getNextNode()
        # print(size)
        return size


    # method removes item passed from the Linked List
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        # search element in list
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        # if previous is None then the data is found at first position
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return found

    # method returns max element from the List
    def Max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest

    # method returns minimum element of Linked list
    def Min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    # method pushes element to the Linked List
    def push(self, data):
        self.addToEnd(data)
        return True

    # method removes and returns the last element from the Linked List
    def pop(self):
        start = self.head
        previous = None

        while start.getNextNode():
            previous = start
            start = start.getNextNode()

        if previous is None:
            self.head = None
        else:
            previous.setLink(None)
            data = start.getData()
            del start
            return data


while True:
    print(" ")
    print(" +++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" 1. Create List ")
    print(" 2. Insert in the Beginning ")
    print(" 3. Insert in the Ending ")
    print(" 4. Remove from Head ")
    print(" 5. Remove form Tail ")
    print(" 6. Count Element in the List and Display Size ")
    print(" 7. Find and Display the Max Element in the Linked List ")
    print(" 8. Find and Display the Min Element in the Linked LIst ")
    print(" 9. Print all the Elements in the List ")
    print(" 10. Exit ")
    print(" +++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    choice = int(input("Enter your choice: "))

    if choice ==1:
        myLList = LinkedList()
        print("The linked list has been created.")
        print("")

    elif choice == 2:
        item = int(input("Enter number to add at the Beginning of the list: "))
        myLList.addToStart(item)

    elif choice == 3:
        item = int(input("Enter number to add at the End of the list: "))
        myLList.addToEnd(item)

    elif choice == 4:
        number = int(input("Enter number you want to want to Delete: "))
        myLList.remove(number)

    elif choice == 5:
        number = int(input("Enter number you want to Delete from the Tail: "))
        myLList.pop(number)

    elif choice == 6:
        print("Number of element(s) in the linked list: " ,myLList.length())

    elif choice == 7:
        print("The Maximum Element in the List is: " ,myLList.Max())

    elif choice == 8:
        print("The Minimum Element in the List is: " ,myLList.Min())

    elif choice == 9:
        print("List of element(s):")
        myLList.display()

    else:
        break






