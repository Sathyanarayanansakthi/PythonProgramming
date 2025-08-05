# Square Every Digit
"""Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!"""

def square_digits(num):
 return int(''.join(str(int(digit)**2) for digit in str(num)))



# Another way for to do this
 def square_digits(num):
     result = ""  # ✅ Step 1: Initialize an empty string
     for i in str(num):  # ✅ Step 2: Loop through each digit
         square = int(i) ** 2  # ✅ Step 3: Square the digit
         result += str(square)  # ✅ Step 4: Add it to result as string
     return int(result)  # ✅ Step 5: Convert final result to integer
