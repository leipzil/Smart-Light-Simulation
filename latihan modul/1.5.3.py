#every day late fee 800k
#after full day, every hour 25k
#after hour, every 5 mins 1k
#if less than 5 minutes, no extra 

late_minutes = int(input("Total minutes late: "))
days = late_minutes//1440
late_minutes %= 1440
hours = late_minutes//60
minutes = late_minutes%60
fee = days*800000 + hours*25000 + (minutes//5)*1000
print(fee)