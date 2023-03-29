from nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def get(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.val

    def set(self, index, val):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        current_node.val = val

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next

    def __str__(self):
        current_node = self.head
        values = []
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
        return str(values)
    
