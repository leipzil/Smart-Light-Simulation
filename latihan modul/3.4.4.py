lenA = int(input("Input number of elements in A: "))
A = [0 for x in range(10)]
print(len(A))
for a in range(lenA):
    number = int(input(f"Input element A number {a+1}: "))
    A[number-1] += 1

lenB = int(input("Input number of elements in B: "))
B = [0 for i in range(10)]
for b in range(lenB):
    number = int(input(f"Input element B number {b+1}: "))
    B[number-1] += 1

if B == A:
    print("B is an anagram of A")
else:
    print("B is not an anagram of A")