class Math:
    def add(self, a, b):  # Instance method (self is required)
        return a + b

# Create an instance of the Math class
math_instance = Math()

# Call the add method through the instance
result = math_instance.add(1, 2)

# Print the result
print(result)






class Math:
    @staticmethod
    def add(a, b):
        return a + b
result = Math.add(1, 2)
print(result)



import math

class Circle:
    @staticmethod
    def area(radius):
        return math.pi * radius ** 2

# Using static method without creating an object
print(Circle.area(5))  # Output: 78.53981633974483


class MathOperations:
    @staticmethod
    def multiply(a, b):
        return a * b

# Using the static method without creating an instance
result = MathOperations.multiply(3, 4)
print(result)
