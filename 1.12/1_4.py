# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n

def shortFunction(n):
    return sum([i**2 for i in range(1,n)])

n = int(input("Input your integer"))
print(shortFunction(n))