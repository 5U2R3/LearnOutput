flag = ''
data_array = []

def rol(value, shift, bit_size):
    value = value & ((1 << bit_size) - 1)
    return ((value << shift) | (value >> (bit_size - shift))) & (( 1 << bit_size) - 1)

memory = currentProgram.getMemory()
start_address = address_space.getAddress(0x140003238)
num_bytes = (0x14000325e - 0x140003238)

for i in range(num_bytes):
    byte_value = memory.getByte(start_address.add(i)) & 0xFF
    data_array.append(byte_value)

shift = 5
bit_size = 8

for i in range(len(data_array)):
    data_array[i] = rol(data_array[i], shift, bit_size)
    flag += chr(data_array[i])

print(flag)
