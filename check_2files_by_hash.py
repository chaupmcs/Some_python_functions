import hashlib
BLOCKSIZE = 65536
hasher_1 = hashlib.sha1()
hasher_2 = hashlib.sha1()

with open('/Users/minhchau/Downloads/file_1.pdf', 'rb') as file_1:
    buf_f1 = file_1.read(BLOCKSIZE)
    while len(buf_f1) > 0:
        hasher_1.update(buf_f1)
        buf_f1 = file_1.read(BLOCKSIZE)

with open('/Users/minhchau/Downloads/file_2.pdf', 'rb') as file_2:
    buf_f2 = file_2.read(BLOCKSIZE)
    while len(buf_f2) > 0:
        hasher_2.update(buf_f2)
        buf_f2 = file_2.read(BLOCKSIZE)


if (hasher_2.hexdigest() == hasher_1.hexdigest()):
    print("The two files are identical!")
else:
    print("They are different!")


# OUTPUT:
# The two files are identical!