# linked lists:

# class for node
class Node:
    # on init the pointer shows to none
    def __init__(self, data):
        self.data = data
        self.next = None


# class for linked list, used to link objects
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:  # or while temp --> false for last node
            print(temp.data)
            temp = temp.next

    def push(self, new_data):    # insert new node as head
        new_node = Node(new_data)
        new_node.next = self.head  # new node next linked to head
        self.head = new_node  # move the head

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:  # check if there is a list. If not, new node is head
            self.head = new_node
            return
        else:
            last = self.head
            while last.next is not None:  # or last.next --> true until last node
                last = last.next
            last.next = new_node

    def insert_after(self, prev_node, new_data):  # insert new node
        if prev_node is None:    # check that node exists
            print("Node not found")
            return
        new_node = Node(new_data)
        temp = prev_node.next  # save the link to the rest of the list
        prev_node.next = new_node  # insert new node
        new_node.next = temp  # link the rest of the list to the new node

    # def insert_after_data(self, user_data, new_data):
    #     new_node = Node(new_data)
    #     if self.head is None:  # check if there is a list. If not, new node is head
    #         self.head = new_node
    #     else:
    #         temp = self.head
    #         node_not_present = True
    #         while node_not_present:
    #             if temp.data == user_data:
    #                 new_node = Node(new_data)
    #                 after_node = temp.next
    #                 temp.next = new_node
    #                 new_node.next = after_node
    #                 node_not_present = False
    #             temp = temp.next
    #         if node_not_present:
    #             print("Data not present")


    def pull(self):  # removes head
        if self.head is None:
            print("Node not found")
        else:
            self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            print("Node not found")
        else:
            second_last = self.head
            while second_last.next is not None:
                temp = second_last
                second_last = second_last.next
            temp.next = None

    def remove_specific(self,point):
        if point is None:
            print("Node not found")
        else:
            temp = self.head
            while temp.next is not point:
                temp = temp.next
            temp.next = point.next

    # def remove_specific_data(self, user_data):
    #     point = Node(user_data)
    #     if point is None:
    #         print("Node not found")
    #     else:
    #         temp = self.head
    #         while temp.next is not point:
    #             temp = temp.next
    #         temp.next = point.next




if __name__ == "__main__":
    # create simple linked list
    SimpleList = LinkedList()
    SimpleList.head = Node(1)
    SecondNode = Node(2)
    ThirdNode = Node(3)
    SimpleList.head.next = SecondNode
    SecondNode.next = ThirdNode
    print("Initial list:")
    SimpleList.print_list()
    SimpleList.push(0)
    print("New head after push:")
    SimpleList.print_list()
    SimpleList.append(4)
    print("List after append:")
    SimpleList.print_list()
    SimpleList.insert_after(SecondNode,1)
    print("List after insert:")
    SimpleList.print_list()
    # SimpleList.insert_after_data(3,5)
    # print("List after insert after data:")
    # SimpleList.print_list()
    SimpleList.pull()
    print("List after head removal:")
    SimpleList.print_list()
    SimpleList.remove_last()
    print("List after tail removal:")
    SimpleList.print_list()
    SimpleList.remove_specific(SecondNode)
    print("List after specific removal:")
    SimpleList.print_list()
    # SimpleList.remove_specific_data(3)
    # print("List after specific data removal:")
    # SimpleList.print_list()


# How do we address the new nodes as we only init SecondNode and ThirdNode
# Using data
