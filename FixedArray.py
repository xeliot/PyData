class FArray:
    
    def __init__(self, size=100):
        self.count = 0
        self.arr = range(0, size)
    
    # print out fixed array not including blanks
    def __str__(self):
        return str(self.arr[0:self.count])
    
    # insert value at the end of the unsorted fixed array
    def insert(self, value):
        if self.count == len(self.arr):
            raise Exception('No more space in fixed array')
        self.arr[self.count] = value
        self.count += 1
    
    # return index of first occurence of value
    def index_of(self, value):
        for i in range(0, self.count):
            if self.arr[i] == value:
                return i
        return None
    
    # delete all occurences of specified value from fixed array by shifting elements
    def delete(self, value):
        while (self.index_of(value) != None):
            for i in range(self.index_of(value), self.count-1):
                self.arr[i] = self.arr[i+1]
            self.count -= 1
    
    # delete all occurences of specified value from fixed array by making new copy of elements
    def delete_copy(self, value):
        new_array = FArray(len(self.arr))
        for i in range(0, self.count):
            if self.arr[i] != value:
                new_array.insert(self.arr[i])
        self.arr = new_array.arr
        self.count = new_array.count
    
    # returns boolean based on the existence of the given value
    def exist(self, value):
        return self.index_of(value) != None
    
    # returns all values within the range from start to end    
    def within(self, start, end):
        result = []
        for i in range(0, self.count):
            if (self.arr[i] >= start) and (self.arr[i] <= end):
                result.append(self.arr[i])
        return result
