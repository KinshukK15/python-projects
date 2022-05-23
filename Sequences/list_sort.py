even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
# even += odd
print(even)

even.sort()  # for sorting
print(even)

even.sort(reverse=True)
print(even)
