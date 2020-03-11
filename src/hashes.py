import hashlib

n = 1
key1 = b"my_value"
key2 = "string".encode()
key3 = b"lunchtime"

index1 = hash(key1) % 8 # where 8 is the capacity in this example
index2 = hash(key2) % 8
index3 = hash(key3) % 8
print(index1)
print(index2)
print(index3)



    # for i in range(n):
    #     print(hash(key))
    #     print(hashlib.sha256(key).hexdigest())

    # for i in range(n):
    #     print(hash(key))

    # for i in range(n):
    #     print(hash(key2))

