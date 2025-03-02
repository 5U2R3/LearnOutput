#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra


#TODO Add User Code Here
from struct import unpack
def init_rc4(key):
    index1 = 0
    index2 = 0
    table = list(range(256))
    for i in range(256):
        index2 = (key[index1 % len(key)] + table[i] + index2) & 0xFF
        table[i], table[index2] = table[index2], table[i]
        index1 += 1
    return table

def rc4(encrypted_data, table):
    x = 0
    y = 0
    for i in range(len(encrypted_data)):
        x = (x + 1) & 0xFF
        y = (table[x] + y) & 0xFF
        table[x], table[y] = table[y], table[x]
        enc[i] ^= table[(table[x] + table[y]) & 0xFF]
    return bytes(encrypted_data)

def do_rc4(encrypted_data, key):
    table = init_rc4(key)
    return rc4(encrypted_data, table)

key = getBytes(toAddr(0x00416000), 0x4)
enc = bytearray(getBytes(toAddr(0x00416008), 0x146))
decrypted_conf = do_rc4(enc, key)
print("hostname:{}".format(decrypted_conf[:128].decode('utf-16').rstrip('\x00')))
print("port:{}".format(unpack("<h", decrypted_conf[128:130])[0]))
print("path:{}".format(decrypted_conf[130:258].decode('utf-16').rstrip('\x00')))
print("rc4key:{}".format(decrypted_conf[258:322].rstrip(b'\x00').decode('utf-8')))
print("sleep_sec:{}".format(unpack("<i", decrypted_conf[322:326])[0]))
