# SID/Name : 13526036/Levina Nirwasita
# Date : 12/10/2026
# Description : determine if a year is a leap year
year = int(input("Enter the year: "))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")