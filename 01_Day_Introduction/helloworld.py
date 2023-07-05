# Introduction
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('JJ'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'John'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# Writing script for exercise 3 with points (2,3) and (10,8)

x = 2
y = 3
x2 = 10
y2 = 8
function1 = (x2 - x)**2 + (y2 - y)**2
function2 = function1**(1/2)
print (function2)