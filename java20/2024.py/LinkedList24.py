class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        def insertAtIndex(self, data, Index):
            if Index < 0:
                print("Invalid index. Cannot insert.")
                return

            new_node = Node(data)
            if Index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                for _ in range(Index - 1):
                    if current is None:
                        print("Index out of bounds. Cannot insert.")
                        return
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def remove_node(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        print(f"{data} not found in the list.")

    def sizeofLL(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def printLL(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBegin(int(input("Entre a first number:")))
    ll.insertAtBegin(int(input("Entre a second number:")))
    ll.insertAtBegin(int(input("Entre a Third number:")))
    ll.insertAtIndex(15, 2)
    ll.printLL()
    ll.remove_node(int(input("Enter a you want to delete:")))
    ll.printLL()
    print(f"Size of linked list: {ll.sizeofLL()}")