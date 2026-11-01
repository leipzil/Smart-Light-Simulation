N = abs(int(input("Enter N: ")))
factors = []
#find factors of 110
#find if each factor is a prime factor
for x in range (1, N//2):
    if  N//x== N/x:
        factors.append(x)
primefactor = []
for i in range(len(factors)):
    prime = True
    for y in range(2, len(factors)):
        if (factors[i] // y == factors[i]/y and factors[i] != y) or factors[i] == 1:
            prime = False
    if prime:
        primefactor.append(factors[i])
print("The prime factors are ", primefactor)