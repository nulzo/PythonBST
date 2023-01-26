"""

Name :: Nolan Gregory

Course :: CSCI3320 - Data Structures

Desc :: Simple Binary Search Tree

Version :: 2.1

Updates :: Reformatted for clarity - Modified methods for final project

"""


#Node class - Added parent value to the constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

#BST class
class BST:
    def __init__(self):
        self.root = None

    #add function; checks if tree is empty
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            #call recursive add
            self._add(value, self.root)
        return self

    def _add(self, value, current):
        #checks to see where to place the new node
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                current.left.parent = current
            else:
                self._add(value, current.left)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                current.right.parent = current
            else:
                self._add(value, current.right)

    #basic height method
    def height(self):
        if self.root is not None:
            #calls recursive method
            return self._height(self.root, 0)
        else:
            return 0

    #recursive height method
    def _height(self, node, current=0):
        #base case
        if node is None:
            return current

        #my junky printer for debugging :)
        # if (node.left is not None) and (node.right is not None):
        #     print("Two children:     ",node.value)
        # elif node.left is not None:
        #     print("Has left child:   ",node.value)
        # elif node.right is not None:
        #     print("Has right child:  ",node.value)
        # else:
        #     print("Has no children:  ",node.value)

        #recurse down the tree
        leftvalue = self._height(node.left, current+1)
        rightvalue = self._height(node.right, current+1)

        #returning larger of two values
        if leftvalue > rightvalue:
            return leftvalue
        else:
            return rightvalue

    #bane of my existence function
    def remove(self, value):
        data = self.root
        #if tree is empty
        if not data:
            return self
        if (not data.left and not data.right) and (data.value == value):
            self.root = None
            return self
        #recurse through and perform removal
        else:
            self.remove_node(self.root, value)
        #return self
        return self

    #sleepless night function
    def remove_node(self, data, value):
        #return data from argument
        if not data:
            return data
        #recurse to find the value [FIND METHOD IMPLEMENTED FOR MY FINAL PROJECT]
        if data.value < value:
            data.right = self.remove_node(data.right, value)
        elif data.value > value:
            data.left = self.remove_node(data.left, value)
        else:
            #if the node has zero children (like the "pony express" workers) :)
            if not data.left and not data.right:
                data = None
            #if the node has only one left child
            elif not data.right:
                if data == self.root:
                    self.root = data.left
                else:
                    data = data.left
            #if the node has only one right child
            elif not data.left:
                if data == self.root:
                    self.root = data.right
                else:
                    data = data.right
            #if the node has two children... so sad :(
            else:
                # maximum value of left subtree
                max_rln = self.min_value(data.left)
                #left most child of the node that is being deleted
                new_root = self.remove_node(data.left, value)
                #node that is directly to the right of the node to be deleted
                temp_node = data.right

                if max_rln == new_root:
                    data.value = max_rln.value
                    data.left = new_root.left
                    return data

                #do the swap outlined in class and in the slides
                data.left = new_root.left
                data.value = new_root.value
                max_rln.right = temp_node
                data.right = max_rln
                #swap completed like a boss
        #return the acquired data
        return data

    #returns number of children a node has [FOR FINAL PROJECT]
    def num_child(self, new_root):
        num = 0
        #simply counts the nodes
        if new_root.left is not None:
            num += 1
        if new_root.right is not None:
            num += 1
        return num

    #minimum value method; Finds right most value in provided tree
    def min_value(self, new_root):
        current = new_root
        if current is None:
            return None
        #loops through until bottommost max value is found
        while current.right is not None:
            current = current.right
        return current

    #For final project! (similar to contains)
    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    #recurses through to find value of a given node (similar to contains)
    def _find(self, value, current):
        if current.value == value:
            return current

        elif (current.value > value) and (current.left is not None):
            return self._find(value, current.left)

        elif (current.value < value) and (current.right is not None):
            return self._find(value, current.right)

    #Simple contains call
    def contains(self, value):
        if self.root is not None:
            return self._contains(value, self.root)
        else:
            return False

    #Recursive implementation of contains. Very straightforward.
    def _contains(self, value, current):
        if current.value == value:
            return True

        elif (current.value > value) and (current.left is not None):
            return self._contains(value, current.left)

        elif (current.value < value) and (current.right is not None):
            return self._contains(value, current.right)

        return False

    # size function
    def size(self):
        if self.root is None:
            return 0
        else:
            return int(self._size(self.root))

    #recursive size function that recurses through, and finds the size
    def _size(self, node):
        if node is None:
            return 0
        else:
            if node.left is not None and node.right is not None:
                return self._size(node.left) + self._size(node.right) + 1
            if node.left is None and node.right is None:
                return 1
            if node.left is None:
                return self._size(node.right) + 1
            if node.right is None:
                return self._size(node.left) + 1

    #pre-order list
    def asList(self):
        returnlist = []
        if self.root is not None:
            self._asList(self.root, returnlist)
        return returnlist

    #pre-order list
    def _asList(self, node, returnlist):
        if node is not None:
            returnlist.append(node.value)
            self._asList(node.left, returnlist)
            self._asList(node.right, returnlist)
            