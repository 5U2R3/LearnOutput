#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra

flag = ''

memory = currentProgram.getMemory()
start_address = toAddr(0x40004e)
num_bytes = 0x26

key_array = []

for i in range(num_bytes):
    byte_value = memory.getByte(start_address.add(i)) & 0xFF
    key_array.append(byte_value)

flag_array = []
addr = toAddr(0x00402284)
inst = getInstructionAt(addr)
for i in range(0x24):
    flag_array.append(inst.getDefaultOperandRepresentation(1))
    inst = inst.getNext()

flag_array = [int(i, 0) for i in flag_array]

for i in range(len(flag_array)):
    flag_array[i] = flag_array[i] ^ key_array[i]
    flag += chr(flag_array[i])

print(flag)