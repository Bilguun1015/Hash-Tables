# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f'LinkedPair({self.key}, {self.value})'
    __repr__ = __str__


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


    # def _all_linked_pairs(self, linkpair):
    #     while linkpair:
    #         yield linkpair
    #         linkpair = linkpair.next


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # storage = storage or self.storage
        # hashed_key = self._hash_mod(key)
        # hash_value = LinkedPair(key, value)

        # if storage[hashed_key]:
        #     for old_hash_value in self._all_linked_pairs(storage[hashed_key]):
        #         if old_hash_value.key == key:
        #             old_hash_value.value = value
        #             return
        #     storage[hashed_key].next = hash_value
        # else:
        #     storage[hashed_key] = hash_value
        # current_node = storage[hashed_key]
        # while current_node:
        #     if current_node.key == key:
        #         current_node.value = value
        #     else:
        #         if current_node.next == None:
        #             current_node.next = hash_value
        # current_node = hash_value
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        last_pair = None
        while current_pair is not None and current_pair.key != key:
            last_pair = current_pair
            current_pair = last_pair.next
        if current_pair is not None:
            current_pair.value = value
        else:
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[index]
            self.storage[index] = new_pair
            

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hashed_key = self._hash_mod(key)

        # try:
        #     current_node = self.storage[hashed_key]
        #     first = True
        #     while current_node:
        #         if current_node.key == key:
        #             if first:
        #                 del self.storage[hashed_key]
        #             else:
        #                 previous_node.next = current_node.next
        #         else:
        #             previous_node = current_node
        #             current_node = current_node.next
        #         first = False
        # except IndexError:
        #     print('Key does not exist!')
        index = self._hash_mod(key)
        current_pair = self.storage[index]

        if current_pair is None:
            print('Key is not found')
            return
        searching = True
        while current_pair is not None and searching:
            if current_pair.key == key:
                self.storage[index] = None
                searching = False
            else:
                current_pair = current_pair.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # hashed_key = self._hash_mod(key)
        # try:
        #     current_node = self.storage[hashed_key]
        #     while current_node:
        #         if current_node.key == key:
        #             return current_node.value
        #         current_node = current_node.next
        #     return current_node
        # except IndexError:
        #     return None
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        while current_pair is not None:
            if current_pair.key == key:
                return current_pair.value
            else:
                current_pair = current_pair.next
        return None

    # def insert_special(self, hash_value, new_storage):
    #     if hash_value:
    #         self.insert(hash_value.key, hash_value.value, new_storage)
    #         if hash_value.next:
    #             self.insert_special(hash_value.next, new_storage)   

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        copy = self.storage
        self.storage = new_storage
        for pair in copy:
            current_pair = pair
            while current_pair is not None:
                self.insert(current_pair.key, current_pair.value)
                current_pair = current_pair.next

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
