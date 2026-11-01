# SID/Name : 13526036/Levina Nirwasita
# Date : 26/10/26
# Description : find segments that accumulate the most power and output range too

N = int(input("Enter the number of track segments (N): "))
segment = []
for x in range(N):
    temp = int(input(f"Enter the power of segment {x+1}: "))
    segment.append(temp)

max = 0
max_L = 0
max_R= 0
for L in range(N):
    sum = 0
    for R in range(L, N):
        sum += segment[R]
        if sum > max:
            max = sum
            max_L, max_R = L, R
        elif sum == max:
            if max_R-max_L < R-L:
                max = sum
                max_L, max_R = L, R
print(f"Best segment rage: Segment {max_L+1} through Segment {max_R + 1}")
print(f"Range length: {max_R-max_L+1} segments")
print(f"Maximum total accumulated power: {max} kWh")