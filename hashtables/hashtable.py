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
        '''
        return hash(key)


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        '''
        i = self._hash_mod(key)
        next_pair = LinkedPair(key, value)
        next_pair.next = self.storage[i]
        self.storage[i] = next_pair



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        '''
        i = self._hash_mod(key)
        if self.storage[i] is None:
            print("There is no queen of england, https://www.youtube.com/watch?v=2A3HLWtHYWA") #There is no Key
        remove = self.storage[i]
        self.storage[i] = remove.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        '''
        i = self._hash_mod(key)
        this_pair = self.storage[i]
        while this_pair:
            if this_pair.key == key:
                return this_pair.value
            this_pair = this_pair.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        for storage in range(self.capacity):
            self.storage.append(None)



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

    print(f"\nResized from {old_capacity}(old) to {new_capacity}(new).\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

