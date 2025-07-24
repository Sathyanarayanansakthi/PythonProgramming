fruits = ["apple", "banana", "orange"]
print(fruits)

# Accessing the elements
print(fruits[0])    # First element (Ascending order)
print(fruits[-1])   # Last element (Reverse indexing)

# Finding the length of the array
y = len(fruits)
print(y)

# Append – Adding a new element to the end
fruits.append("pineapple")
print(fruits)

# Pop – Removing element by index (remove "orange" at index 2)
fruits.pop(2)
print(fruits)

# Remove – Removing by value (let's remove "banana" instead)
fruits.remove("banana")
print(fruits)

