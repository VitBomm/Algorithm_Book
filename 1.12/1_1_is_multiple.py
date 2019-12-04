# Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n
# is a multiple of m, n = mi for some integer i, and False otherwise
# 

def is_multiple(n, m):
    if n/m % 1 == 0:
        return True
    return False

n = eval(input("Input your n: "))
m = eval(input("Input your m: "))
print(str(is_multiple(n,m)))