from python.usecases.oops import Mask
from python.usecases.oops import EnDecode

#Execution
objmask = Mask()
objendecode = EnDecode()

# Create a list with 3 names like ["Alan","Jake","Charlie"] loop the elements using map function and apply hashMask for all 3 elements and print the masked values.

nameslist = ["Alan","Jake","Charlie"]
print('Names:',nameslist)

"""
Names: ['Alan', 'Jake', 'Charlie']
"""

print('#1.Getting Hash Mask Value:')
hasMash_value_dict = {}
for name in nameslist:
    hasMash_value_dict[name] = objmask.hashMask(name)

print(hasMash_value_dict)

"""
#1.Getting Hash Mask Value:
{'Alan': -6767629245512748524, 'Jake': 6013411149039668558, 'Charlie': 896875423019824000}
"""

# Loop the list created in the above step and apply the revEncode function for all the 3 elements and print of the encoded values.
print('#2. Encode the Masked Value:')
encoded_value_dict = {}
for name, hashvalue in hasMash_value_dict.items():
    encoded_value_dict[name] = objendecode.revEncode(hashvalue)
    print(f"{name} = {encoded_value_dict[name]}")

"""
#2. Encode the Masked Value:
Alan = aix4258472155429267676-
Jake = aix8558669309411143106
Charlie = aix000428910324578698
"""

# Create a decode function inside endecodeclass as revDecode and write a logic to decode the encoded string we got in the above step
print('#3. Decode the Encoded Value:')
decoded_value_dict = {}
for name, value in encoded_value_dict.items():
    decoded_value_dict[name] = objendecode.revDecode(value)
    print(f"{name} = {decoded_value_dict[name]}")


"""
#3. Decode the Encoded Value:
Alan = -6767629245512748524
Jake = 6013411149039668558
Charlie = 896875423019824000
"""