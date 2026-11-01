print("Input value of N: ", end="")
N = int(input())
if (N > 0):
    if N % 2 == 0:
        print(f"{N} is an even positive integer")
    else:
        print(f"{N} is an odd positive integer")
elif (N < 0):
    print(str(N) + " is not positive number")
else:
    print(str(N) + " is zero")