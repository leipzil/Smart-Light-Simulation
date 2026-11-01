# SID/Name : 13526036/Levina Nirwasita
# Date : 26/10/26
# Description : alternating between tables + time taken for each and total

N = int(input("Enter the number of tables (N): "))
table = []
for x in range(N):
    temp = int(input(f"Enter the time for table {x+1}: "))
    table.append(temp)

left = 0
right = N - 1
time_v = 0
time_m = 0
v = 0
m = 0

while left <= right:
    if time_v <= time_m:
        time_v += table[left]
        v += 1
        left += 1
    else:
        time_m += table[right]
        m += 1
        right -= 1

print(f"Mr. Vin clears {v} tables")
print(f"Mr. Mik clears {m} tables")
print(f"All tables are cleared in {max(time_v, time_m)} minutes")