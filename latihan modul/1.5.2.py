n = int(input("Input number of seat rows (n): "))
m = int(input("Input number of seat columns (m): "))
k = int(input("Input chosen seat number (k): "))
row = k%m
column = k%n
mirror = n*m-k+1
print(mirror)