class DynamicArray():
    # my_array = [4]
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        # Emulate allocation of memory using Python list
        self.storage = [None] * self.capacity
    
    def __len__(self):
        return self.count

    def insert(self, index, value):
        # Make sure we have open space
        if self.count >= self.capacity:
            # TODO: Make array dynamically resize
            # print("ERROR: Array is full.")
            self.double_size()
            
            
        # Make sure index is in range
        if index > self.count:
            print("ERROR: Index is out of range.")

        # Shift everything over to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]


        # Insert value
        self.storage[index] = value
        self.count += 1
        
    def append(self, value):
        self.insert(self.count, value)
    
    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


my_array = DynamicArray(4)
my_array.insert(0,1)
my_array.insert(0,2)
my_array.insert(1,3)
my_array.insert(3,4)
my_array.insert(0,5)
my_array.append(20)
print(my_array.storage)
