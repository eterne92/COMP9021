# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    # def rearrange(self):
    #     # Replace pass above with your code
    #     node = self.head
    #     previous_node = None
    #     next_node = None
    #     while node:
    #         next_node = node.next_node
    #         if node.value % 2 == 1 and previous_node != None:
    #             newnode = self.head
    #             previous_newnode = None
    #             while newnode:
    #                 if newnode.value % 2 == 0:
    #                     break
    #                 previous_newnode = newnode
    #                 newnode = newnode.next_node
    #             # print(node.value,newnode.value)
    #             if previous_newnode == None:
    #                 previous_node.next_node = node.next_node
    #                 node.next_node = self.head
    #                 self.head = node
    #             elif previous_newnode == node:
    #                 break
    #             else:
    #                 previous_node.next_node = node.next_node
    #                 node.next_node = newnode
    #                 previous_newnode.next_node = node
    #         else:
    #             previous_node = node
    #         node = next_node
    def rearrange(self):
    # Replace pass above with your code
        self.prepend(1)
        node = self.head
        temp = LinkedList()
        while node and node.next_node:
            if node.next_node.value % 2 == 0:
                tempnode = node.next_node
                node.next_node = tempnode.next_node
                tempnode.next_node = None
                if temp.head == None:
                    temp.head = tempnode
                else:
                    newnode = temp.head
                    while newnode.next_node:
                        newnode = newnode.next_node
                    newnode.next_node = tempnode
            else:
                node = node.next_node
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = temp.head
        self.head = self.head.next_node

                    
