#!/usr/bin/python3

"""Singly Linked List module"""


class Node:
    """Node class for a Singly Linked List"""

    def __init__(self, data,  next_node=None):
        """Initialize the node

        Args: data (int) - data to be stored in the node
             next_node (Node) - pointer to the next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data stored in the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class"""

    def __init__(self):
        """Initialize the linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node in the correct sorted position in the list

        Args: value (int) - data to be stored in the new node
        """
        node = Node(value)

        if self.__head is None:
            self.__head = node
            return
        if value < self.__head.data:
            node.next_node = self.__head
            self.__head = node
            return
        temp = self.__head
        while temp.next_node is not None:
            if value < temp.next_node.data:
                node.next_node = temp.next_node
                temp.next_node = node
                return
            temp = temp.next_node
        temp.next_node = node
        return

    def __str__(self):
        """Return a string representation of the list"""
        temp = self.__head
        string = ""
        while temp is not None:
            string += str(temp.data) + "\n"
            temp = temp.next_node
        return string[:len(string)-1]
