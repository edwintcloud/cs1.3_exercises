def hash_str(string):
    """hash_str uses the djb2 algorithm to compute the hash
       value of a string http://www.cse.yorku.ca/~oz/hash.html"""
    hash = 5381
    for char in string[1:]:
        # (hash << 5) + hash is equivalent to hash * 33
        hash = (hash << 5) + hash + ord(char)
    return hash


# test
result = hash_str("test")
print(result)
print(hash_str("estt"))
