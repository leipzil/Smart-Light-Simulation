p = int(input("Input payment amount(rupiah): "))
b = int(input("Input item price (rupiah): "))
change = p - b
fifty = change//50000
change = change % 50000
twenty = change//20000
change %= 20000
ten = change//10000
change %= 10000
five = change//5000
change %= 5000
one = change//1000
print(f"Ms. Sal needs to give {fifty} Rp50000 bill(s), {twenty} Rp20000 bill(s), {ten} Rp10000 bill(s), {five} Rp5000 bill(s), and {one} Rp1000 bill(s).")
print(fifty, "50000")