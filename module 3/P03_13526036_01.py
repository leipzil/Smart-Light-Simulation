# SID/Name : 13526036/Levina Nirwasita
# Date : 26/10/26
# Description : find if mr.mik's raffle number will be drawn + at which index and how many other participants have larger raffle numbers

N = int(input("Enter the name of participants (N): "))
M = int(input("Enter Mr. Mik's raffle number (M): "))
participants = []
for x in range(N):
    temp = int(input(f"Enter participant {x+1}'s number: "))
    participants.append(temp)

count = 0 #to count how many numbers are larger
found = False
for y in range(N):
    if M == participants[y]:
        found = True
    if participants[y] > M:
        count+= 1
if found:
    print("Mr. Mik's raffle number was found at position", y+1)
else:
    print("Mr. Mik’s raffle number was not found in the list.")
print(f"There are {count} other participants with a raffle number larger than Mr. Mik's.")
