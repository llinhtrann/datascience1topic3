import bitarray
bit_array = bitarray.bitarray(60)
bit_array.setall(0)
bit_array[3] = 1

print(str(bit_array))