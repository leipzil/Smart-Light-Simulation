N = int(input("Enter the value of N: "))
list = []
for x in range(N):
    temp = int(input(f"Enter the number for index {x+1}: "))
    list.append(temp)

even = 0
for j in range(N):
    sum = 0
    for i in range(j, N):
        sum += list[i]
        if sum%2 == 0:
            even += 1
print(f"There are {even} sublists with an even sum")