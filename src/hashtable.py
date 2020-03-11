# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # Collision
        if self.storage[index] is not None:
            node = self.storage[index]
            while node.next != None:
                if node.key == key:
                    break
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = LinkedPair(key, value)
        # No collision
        else:
            self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # No entry for given key
        if self.storage[index] is None:
            print("ERROR: Key not found.")
            return

        # One item in chain
        if self.storage[index].next is None:
            # Double check to make sure this isn't a collision
            if self.storage[index].key == key:
                self.storage[index] = None
                return
            else:
                print("ERROR: Key not found.")
                return

        prev_node = self.storage[index]
        curr_node = prev_node.next
        next_node = curr_node.next

        while True:
            if curr_node.key == key or curr_node.next is None:
                break

            prev_node = curr_node
            curr_node = next_node
            next_node = curr_node.next

        prev_node.next = next_node


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            node = self.storage[index]
            while True:
                if node is None:
                    print("ERROR: Value not found")
                    return None
                if node.key == key:                    
                    return node.value
                node = node.next
                

        
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for bucket_item in old_storage:
            node = bucket_item
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next
                

            



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
