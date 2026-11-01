# SID/Name : 13526036/Levina Nirwasita
# Date : 28/09/2026
# Description : count greatest value of chests based on inputted gold coin

total_gold = int(input("Enter the total gold coins: "))
initial_total_gold = total_gold
M = int(input("Enter the price of a Mythic Chest: "))
E = int(input("Enter the price of an Epic Chest: "))
R = int(input("Enter the price of a Rare Chest: "))

mythic_number = total_gold//M
total_gold %= M
epic_number = total_gold//E
total_gold %= E
rare_number = total_gold//R
total_gold %= R

print(f"""
Mythic Chest: {mythic_number}
Epic Chest: {epic_number}
Rare Chest: {rare_number}
Leftover gold coins: {total_gold}
Total value of coins in chests: {initial_total_gold - total_gold}
""")