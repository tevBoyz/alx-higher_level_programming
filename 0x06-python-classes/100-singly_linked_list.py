#!/usr/bin/python3
""" Node class """


class Node:
    """ Node definition"""

    def __init__(self, data, nextt=None):
        """constructor to new node

        Args:
            data(int): integer data stored in the node
            next_node (Node): next node reference

        Raises:
            TypeError: if data is not node and if next_node isn't Node
        """
        self.data = data
        self.next_node = nextt

    @property
    def data(self):
        """get the data of node object"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the next_node"""
        return self.__next_node

    @next_node.setter
    def next_data(self, value):
        if not isinstance(value, Node) and value is not None:
           raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ SLL definition"""

    def __init__(self):
        """constructor"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node to a correct sorted position

        Args:
            value (Node): new node to be inserted
        """
        new = Node(value)
        if (self.__head is None):
            new.next_node = None
            self.__head = new
        elif (self.__head.data > value):
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """string representattion of SLL"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return('\n'.join(values))
