# Outlive25
# by: Edu371
# exibe secções e suas posições
# shows sections and their offsets

file_name = 'header.bin'

content = open(file_name, 'rb')
content = content.read()
content = content[:5636]

l = []

chunk = 44
chunks = int.from_bytes(content[:4], 'little')

for n in range(chunks):
    a = content[chunk*n+4:chunk*n+chunk+4]
    string = str(a[:32], 'utf-8')
    offset = int.from_bytes(a[32:36], 'little')
    compressed_size = int.from_bytes(a[36:40], 'little')
    size = int.from_bytes(a[40:44], 'little')
    l.append([string, offset, compressed_size, size])

l = sorted(l, key=lambda x: x[1])

for x in l:
    print(x[0], x[1], x[2], x[3])

