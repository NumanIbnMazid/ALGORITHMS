"""
Keywords: Key-Value Pairs
Terms:
    - Key: Unique integers that is used for indexing the values.
    - Value: Data that are associated with keys.
    - Hashing: A new index is processed using the keys. Element corresponding to that key is stored in the index. This processed is called Hashing.
    - Hash Collision: When the hash function generates the same index for multiple keys there will be conflict. This is called a hash collision.
Resolving Hash Collision:
    - Collision resolution by chaining.
    - Open Addressing: Linear/Quadratic Probing and Double Hashing.
"""

class HashTable():
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
    
    # create buckets for hash table
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # insert values into hash table
    def set_value(self, key, value):
        # get index from the key using hash function
        hashed_key = hash(key) % self.size
        
        # get the bucket corresponding to the index
        bucket = self.hash_table[hashed_key]
        
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            
            # check if the bucket has the same key as the key to be inserted
            if record_key == key:
                found_key = True
                break
        
        # if the bucket has the same key to be inserted then update the key value otherwise append the new key value pair to the bucket
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))
            
    # get value of a specific key from the bucket
    def get_value(self, key):
        # get index of the key using the hash function
        hashed_key = hash(key) % self.size
        
        # get the bucket corresponding to the index
        bucket = self.hash_table[hashed_key]
        
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            
            # check if the bucket has the same key as the key's value to be retrieved
            if record_key == key:
                found_key = True
                break
            
        # if the bucket has the key that is searching then return the value of the corresponding key, otherwise indicate that there was no record found
        if found_key:
            return record_value
        else:
            return "No record found!"
        
    # delete a value with a specific key
    def delete_value(self, key):
        # get the index of the key using the hash function
        hashed_key = hash(key) % self.size
        
        # get the bucket corresponding to the key
        bucket = self.hash_table[hashed_key]
        
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            
            # chek if the bucket has the same key as the key to be deleted
            if record_key == key:
                found_key = True
                break
        
        # remove the key if the key is found otherwise indicate that the key is not found
        if found_key:
            return bucket.pop(index)
        else:
            return "Key not found!"
        
    # display the hash table
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
    
    
hash_table = HashTable(50)

# insert some values
hash_table.set_value('gfg@example.com', 'some value')
print(hash_table)
print()

hash_table.set_value('portal@example.com', 'some other value')
print(hash_table)
print()

# search/access a record with key
print(hash_table.get_value('portal@example.com'))
print()

# delete or remove a value
hash_table.delete_value('portal@example.com')
print(hash_table)
