class Hashtable:

    def __init__(self, size=50):
        self.size = size
        self.arr = range(0, self.size)
        self.count = 0
        for i in range(0, self.size):
            self.arr[i] = Llist()

    def __str__(self):
        result = ''
        for i in range(0, len(self.arr)):
            result = result + str(self.arr[i]) + '\n'
        return result

    def hf(self, string, size):
        if type(string) != str:
            raise Exception('Value must be a string.')
        else:
            result = 0
            for i in range(0, len(string)):
                result += ord(string[i])**2
            return result%size

    def modify_size(self):
        if self.count >= 0.7*len(self.arr):
            new_table = Hashtable(len(self.arr)*2)
        elif (self.count <= 0.3*len(self.arr)) and (len(self.arr) > self.size):
            new_table = Hashtable(int(round(len(self.arr)/2.0)))
        else:
            return
        for i in range(0, len(self.arr)):
            node = self.arr[i].head
            while node != None:
                new_table.arr[self.hf(node.val[0], len(new_table.arr))].kv_insert(node.val[0], node.val[1])
                node = node.child
        self.arr = new_table.arr

    def put(self, key, value):
        self.arr[self.hf(key, len(self.arr))].kv_insert(key, value)
        self.count += 1
        self.modify_size()

    def get(self, key):
        my_list = self.arr[self.hf(key, len(self.arr))]
        node = my_list.head
        while node != None:
            if node.val[0] == key:
                return node.val[1]
            node = node.child
        return None

    def remove(self, key):
        for i in range(0, len(self.arr)):
            if self.arr[i].kv_delete(key):
                self.count -= 1
                break
        self.modify_size()
            
