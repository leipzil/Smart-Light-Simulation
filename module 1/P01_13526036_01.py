# SID/Name : 13526036/Levina Nirwasita
# Date : 28/09/2026
# Description : each payment of wifi according to proportion of use

monthly_wifi = int(input("Enter the monthly WiFi price (rupiah): "))
g1 = float(input("Enter Mr. Mik’s data usage (GB): "))
g2 = float(input("Enter Mr. Vin’s data usage (GB): "))
g3 = float(input("Enter Mr. Joji’s data usage (GB): "))
total = g1 + g2 + g3
g1_payment = (g1/total)*monthly_wifi
g2_payment = (g2/total)*monthly_wifi
g3_payment = (g3/total)*monthly_wifi
print(f"""
Mr. Mik pays Rp{int(g1_payment)}
Mr. Vin pays Rp{int(g2_payment)}
Mr. Joji pays Rp{int(g3_payment)}
""")