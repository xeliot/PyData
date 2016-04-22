class SArray:
    
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
        else:
            for i in range(0, self.count+1):
                if (self.count - i - 1) < 0 :
                    self.arr[0] = value
                elif self.arr[self.count - i - 1] > value:
                    self.arr[self.count - i] = self.arr[self.count - i - 1]
                else:
                    self.arr[self.count - i] = value
                    break
        self.count += 1

    def insert_bubble(self, value):
        if self.count == len(self.arr):
            raise Exception('No more space in fixed array')
        self.arr[self.count] = value
        for i in range(0, self.count):
            if self.arr[self.count - i] < self.arr[self.count - i - 1]:
                self.arr[self.count - i] = self.arr[self.count - i - 1]
                self.arr[self.count - i - 1] = value
            else:
                break
        self.count += 1
        
    
    # return index of first occurence of value
    def find_edge(self, pos, left_most):
        array = self.arr[:self.count]
        if left_most:
            for i in range(1, pos+1):
                if array[pos - i] != array[pos]:
                    return pos - i + 1
            return 0
        else:
            for i in range(1, len(array)- pos):
                if array[pos + i] != array[pos]:
                    return pos + i
            return len(array)

    def index_of(self, value, left_most=True):
        array = self.arr[:self.count]
        low = 0 # inclusive; left most boundary
        high = len(array) # exclusive; right most boundary
        if len(array) == 0:
            return (False, 0)
        while low < high:
            if low == (high - 1): # One element needed to be check within the boundary
                if array[low] == value:
                    return (True, self.find_edge(low, left_most))
                elif array[low] > value:
                    return (False, low)
                elif array[low] < value:
                    return (False, high)
            else: # More than one element needed to be check within the boundary
                mid = (low + high) // 2
                if array[mid] == value:
                    return (True, self.find_edge(mid, left_most))
                elif array[mid] > value:
                    high = mid
                elif array[mid] < value:
                    low = mid
    
    # delete all occurences of specified value from fixed array by shifting elements
    def delete(self, value):
        if self.index_of(value)[0] != False:
            right_most_pos = self.index_of(value, False)[1]
            left_most_pos = self.index_of(value)[1]
            for i in range(right_most_pos, self.count):
                self.arr[i - right_most_pos + left_most_pos] = self.arr[i]
            self.count -= right_most_pos - left_most_pos
            
    # delete all occurences of specified value from fixed array by making new copy of elements
    def delete_copy(self, value):
        new_array = SArray(len(self.arr))
        for i in range(0, self.count):
            if self.arr[i] != value:
                new_array.insert(self.arr[i])
        self.arr = new_array.arr
        self.count = new_array.count
    
    # returns boolean based on the existence of the given value
    def exist(self, value):
        return self.index_of(value)[0]
    
    # returns all values within the range from start to end    
    def within(self, start, end):
        if end < start:
            raise Exception('Start must be less than or equal to end')
        array = self.arr[0:self.count]
        return array[self.index_of(start, left_most=True)[1]:self.index_of(end, left_most=False)[1]]
