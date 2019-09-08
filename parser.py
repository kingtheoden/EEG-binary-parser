from struct import pack, unpack
from typing import List, Tuple
from sys import stdin

def main():
    byte_data = stdin.buffer.read()
    pointer = 0

    flags = [False, False, False]
    header_data, pointer = read_bytes(pointer, byte_data, 13)
    file_id, number_of_blocks, flags[0], flags[1], flags[2] = parse_header(header_data)
    print_header_info(file_id, number_of_blocks, [flags[0], flags[1], flags[2]])

    for x in range(number_of_blocks):
        block_head, pointer = read_bytes(pointer, byte_data, 10)
        number_of_samples = parse_block_head(block_head)
        print_block_head_info(x + 1, number_of_samples)

        for y in range(number_of_samples):
            sample_data, pointer = read_bytes(pointer, byte_data, 16)
            time, value = parse_sample(sample_data)
            print_sample_data(time, value)
        print()

# Helper Functions

# Reads bytes from the buffer, keeps track of the pointer
def read_bytes(pointer: int, data: bytes, number_of_bytes: int) -> Tuple[bytes, int]:
    new_pointer = pointer + number_of_bytes
    if len(data) < new_pointer:
        raise Exception("Less bytes than expected are available.")
    return (data[pointer : new_pointer], new_pointer)

# Takes header binary string, seperates and converts the individual info.
def parse_header(data: bytes) -> Tuple[int, int, bool, bool, bool]:
    file_id = unpack("I", data[0:4])[0]
    number_of_blocks = unpack("Q", data[4:12])[0]
    flag_byte = data[12:13]
    flag_bits = byte_to_binstr(flag_byte)
    flags = [False, False, False]
    for x in range(3):
        if flag_bits[x] == "1":
            flags[x] = True

    return (file_id, number_of_blocks, flags[0], flags[1], flags[2])

# prints the header info to stdout.
def print_header_info(file_id: int, number_of_blocks: int, flags: List[bool]):
    print("File Identifier:", file_id)
    print("Number of Blocks:", number_of_blocks)
    for x in range(3):
        bool_string = "true" if flags[x] else "false"
        print("Flag {}:".format(x + 1), bool_string)
    print()
    return

# Takes the first 10 bytes of a block and parses the number of samples.
def parse_block_head(data: bytes) -> int:
    return unpack("Q", data[2:10])[0]

# Prints the block header info
def print_block_head_info(block_number: int, number_of_samples: int):
    print("Block", block_number)
    print("Number of Samples:", number_of_samples)
    return

# Takes block binary string, seperates and converts the individual info.
def parse_sample(data: bytes) -> Tuple[int, float]:
    time = unpack("Q", data[0:8])[0]
    value = unpack("d", data[8:16])[0]
    return (time, value)

# Prints sample info.
def print_sample_data(time: int, value: float):
    print(str(time) + ",", value)
    return

# converts a byte to a 8-bit binary number as a string.
def byte_to_binstr(byte: bytes) -> str:
    hex_number = byte.hex()
    return bin(int(hex_number, 16))[2:].zfill(8)

# Run it!
if __name__ == "__main__":
    main()
