class Node:

    def __init__(self, value):
        self.val = value
        self.parent = None
        self.child = None

    def __str__(self):
        return str(self.val)

    
class Llist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def string(self, node):
        if node == None:
            return ']'
        elif node == self.head:
            return str(node.val) + self.string(node.child)
        else:
            return ' => ' + str(node.val) + self.string(node.child)

    def __str__(self):
        return '[' + self.string(self.head)

    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.child = Node(value)
            self.tail.child.parent = self.tail
            self.tail = self.tail.child
        self.count += 1

    def exist(self, value):
        node = self.head
        while node != None:
            if node.val == value:
                return True
            else:
                node = node.child
        return False

    def kv_exist(self, key):
        node = self.head
        while node != None:
            if node.val[0] == key:
                return True
            else:
                node = node.child
        return False

    def kv_insert(self, key, value):
        if self.head == None:
            self.head = Node((key, value))
            self.tail = self.head
        elif self.kv_exist(key):
            node = self.head
            while node != None:
                if node.val[0] == key:
                    node.val = (key, value)
                    break
                node = node.child
        else:
            self.tail.child = Node((key, value))
            self.tail.child.parent = self.tail
            self.tail = self.tail.child
        self.count += 1


    def kv_delete(self, key):
        node = self.head
        while node != None:
            if node.val[0] == key:
                if node == self.head:
                    if self.count == 1:
                        self.head = None
                        self.tail = None
                    else:
                        node.child.parent = None
                        self.head = node.child
                elif node == self.tail:
                    node.parent.child = None
                    self.tail = node.parent
                else:
                    node.parent.child = node.child
                    node.child.parent = node.parent
                self.count -= 1
                return True
            node = node.child

    def delete(self, value):
        node = self.head
        while node != None:
            if node.val == value:
                if node == self.head:
                    if self.count == 1:
                        self.head = None
                        self.tail = None
                    else:
                        node.child.parent = None
                        self.head = node.child
                elif node == self.tail:
                    node.parent.child = None
                    self.tail = node.parent
                else:
                    node.parent.child = node.child
                    node.child.parent = node.parent
                self.count -= 1
            node = node.child

    def within(self, start, end):
        node = self.head
        result = []
        while node != None:
            if (node.val >= start) and (node.val <= end):
                result.append(node.val)
            node = node.child
        return result
