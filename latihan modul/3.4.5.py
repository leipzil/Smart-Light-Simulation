lenstring = int(input("Input string length: "))
string = input("Input string: ")
arr = []
palindrome = True
for char in string:
    arr.append(char)
for i in range(int(lenstring//2)):
    if arr[i] != arr[lenstring-1-i]:
        palindrome = False
if palindrome:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")