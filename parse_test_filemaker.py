from sys import stdin, stdout
from struct import pack, unpack
from math import sin

def write(data):
    stdout.buffer.write(data)

def pack_2b_int(num):
    return pack("H", num)

def pack_4b_int(num):
    return pack("I", num)

def pack_8b_int(num):
    return pack("Q", num)

def pack_double(num):
    return pack("d", num)

# Header
write(pack_4b_int(42))
write(pack_8b_int(2))
write(pack("B", 43))

# Block 1
write(pack_2b_int(1))
write(pack_8b_int(20))
for x in range(20):
    write(pack_8b_int(x))
    write(pack_double(float(x*x)))

# Block 2
write(pack_2b_int(2))
write(pack_8b_int(99))
for x in range(99):
    write(pack_8b_int(2*x + 9))
    write(pack_double(float(sin(2 * x + 7))))
