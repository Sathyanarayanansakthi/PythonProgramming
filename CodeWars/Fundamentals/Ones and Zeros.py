# Ones and Zeros
"""Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
However, the arrays can have varying lengths, not just limited to 4."""

def binary_array_to_number(arr):
    # Step 1: Create an empty string to store binary digits
    binary_string = ""

    # Step 2: Loop through each bit in the array
    for bit in arr:
        # Convert bit to string and add it to binary_string
        binary_string += str(bit)

    # Step 3: Convert binary string to decimal using int with base 2
    decimal_number = int(binary_string, 2)

    # Step 4: Return the decimal result
    return decimal_number
r