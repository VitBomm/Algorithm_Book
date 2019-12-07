# Write a short python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use
# the built-in functions min or max in implementing your solution

def minmax(data):
    temp = sorted(data)
    return temp[0], temp[-1]

list_temp = [3 ,5 ,6 ,1 ,6]
tuple_temp = (3, 5, 6 ,1 ,7)

print(minmax(list_temp))
print(minmax(tuple_temp))
