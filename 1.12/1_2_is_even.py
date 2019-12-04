# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, False otherwise, However, your function
# cannot use the multiplication, modulo, or division operators
def is_even(k):
    return (not (k & 1))
k = eval(input())
print(is_even(k))
# 101
#   1
# 001