# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value, next_pair=None):
        self.key = key
        self.value = value
        self.next = next_pair

    def __str__(self):
        return f"{self.key}, {self.value}, {self.next}"


class LinkedList:
    def __init__(self, set_head=None):
        self.head = set_head

    def __repr__(self):
        return f"{self.head}"

    # add to head
    def add_to_head(self, pair):
        if self.head is None:
            # new_pair = LinkedPair(key, value, self.head)
            self.head = pair

    # remove

    def list_remove(self, key):
        if not self.head:
            return None
        elif self.head.key == key:
            self.head = self.head.next
        else:
            parent = self.head
            current = self.head.next
            while current:
                if current.key == key:
                    parent.next = current.next
                    return
                else:
                    parent = parent.next
                    current = current.next
        return None

    # contains
    def list_contains(self, key):
        current_pair = self.head

        while current_pair:
            if current_pair.key == key:
                return current_pair.value
            else:
                current_pair = current_pair.next

        return None

    # insert

    # def list_insert(self, key, value):
    #     current_pair = self.head

    #     if current_pair is not None:


class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        # self.count = 0 # removing this for now
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def __str__(self):
        return f"{self.storage}"

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

        '''

        index = self._hash_mod(key)

        new_pair = LinkedPair(key, value)
        # new_linked_list = LinkedList(new_pair)

        # Check available storage
        # Omitting because this is happening manually in test file

        # if self.count >= self.capacity:
        #     print(f'We are at capacity')
        #     self.resize()

        # if index is empty, create new linked list with passed in pair
        if self.storage[index] is None:
            self.storage[index] = new_pair
        # otherwise, add new pair to next value
        else:
            new_pair.next = self.storage[index]
            self.storage[index] = new_pair
            # self.storage[index].add_to_head(new_pair)

        # self.count += 1

        # print(f"\n{self.storage[index]}")

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        else:
            current_pair = self.storage[index]
            while current_pair is not None:
                if current_pair.key == key:
                    self.storage[index] = current_pair.next
                current_pair = current_pair.next
            return None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None
        # elif self.storage[index].next is not None:
        #     self.storage.
        else:
            current_pair = self.storage[index]
            while current_pair is not None:
                if current_pair.key == key:
                    return current_pair.value
                current_pair = current_pair.next
            return None
            # return self.storage[index].list_contains(key)

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # print(self.storage)

        # double capacity
        self.capacity *= 2

        # create new array to the doubled size
        new_storage = [None] * self.capacity

        # set old storage to current storage
        old_storage = self.storage
        # print(f"old storage before point"({old_storage}))

        self.storage = new_storage

        # this is showing currently filled HT(2)
        # print(old_storage)
        # this is showing the 4x None's as created on line 181
        # print(self.storage)

        # go through existing/old storage and re-hash all keys
        # insert LL into new storage

        for i in range(len(old_storage)):
            if old_storage[i] is not None:
                current_list = old_storage[i]
                while current_list:
                    self.insert(current_list.key, current_list.value)
                    # index = self._hash_mod(l.key)
                    current_list = current_list.next


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
