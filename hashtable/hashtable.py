class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    FNV_OFFSET_BASIS = 0x1f
    FNV_PRIME = 0x3B8BBA37

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.list = [None] * capacity
        self.item_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.item_count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        curr_hash = HashTable.FNV_OFFSET_BASIS
        for letter in key.encode():
            curr_hash *= HashTable.FNV_PRIME
            curr_hash ^= letter
            curr_hash &= 0xffffffffffffffff

        return curr_hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        pass


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity


    def __put_sans_check(self, new_entry: HashTableEntry):
        index = self.hash_index(new_entry.key)
        entry = self.list[index]
        if entry is None:
            self.list[index] = new_entry
        else:
            while entry.next is not None and entry.key != new_entry.key:
                entry = entry.next
            if entry.key == new_entry.key:
                entry.value = new_entry.value
            else:
                entry.next = new_entry


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.item_count += 1
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)

        entry = HashTableEntry(key, value)

        self.__put_sans_check(entry)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        entry = self.list[index]
        if entry.key == key:
            self.list[index] = entry.next
        else:
            while entry.next.key != key and entry.next is not None:
                entry = entry.next
            if entry.next is None:
                print(f'key "{key}" is not in table to delete')
            else:
                entry.next = entry.next.next
                self.item_count -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        entry = self.list[self.hash_index(key)]
        while entry is not None and entry.key != key:
            entry = entry.next

        return entry.value if entry is not None else None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_list = self.list
        self.capacity = new_capacity
        self.list = [None] * self.capacity

        def place_entry(entry: HashTableEntry) -> None:
            nonlocal self

            if entry is None:
                return
            else:
                old_next = entry.next
                entry.next = None
                self.__put_sans_check(entry)
                place_entry(old_next)


        for entry in old_list:
            place_entry(entry)





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
