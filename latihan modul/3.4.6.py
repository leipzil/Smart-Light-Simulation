lego = int(input("Enter the number of Lego pieces: "))
cube = 0
while lego != 0:
    x = 1
    while x*x*x < lego:
        x += 1
    x -= 1
    if x == 0:
        x = 1
    lego -= x*x*x
    print(lego)
    cube += 1
print(f"Mr. Kil can make {cube} cubes.")