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
    A hash table with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def __repr__(self):
        return f"({self.storage})"

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

        Hash collisions should be handled with Linked List Chaining. set 

        ###############

        Check if there is room in storage

        If not return an error, or call resize function to double capacity

        If there is, 

        check if there is already key value pair stored at hash index

        if there is, set new key, value paired linkedpair to current pair next value

        If there is not,
        store linkedpaired at hashed index


        '''
        index = self._hash_mod(key)
        # print(f"index")
        new_pair = LinkedPair(key, value)

        # Check storage available
        # if self.count >= self.capacity:
        #     print(f'We are at capacity')
        #     self.resize()

        # If we have room, check if index is occupied
        if self.storage[index] is not None:
            # if occupied, add new pair to next value
            self.storage[index].next = new_pair
        else:
            self.storage[index] = new_pair

        self.count += 1

        # print(f"\n{self.storage[index]}")

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            print("There is no spoon")
            # return
        else:
            self.storage[index].value = None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            # for pair in self.storage[index]:
            # if self.storage[index][0] == key and self.storage[index].next is None:
            #     return self.storage[index][1]
            return self.storage[index].value
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # old_storage = self.storage
        # self.capacity *= 2
        # new_storage = [None * self.capacity]
        # for pair in old_storage:
        #     if pair is not None:
        #         index = self._hash_mod(pair.key)
        #         new_storage[index] = pair
        # self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    # print(ht)

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
