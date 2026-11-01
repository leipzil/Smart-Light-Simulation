# SID/Name : 13526036/Levina Nirwasita
# Date : 28/09/2026
# Description : count tax for each bracket

annual_income = int(input("Enter the annual income (rupiah): "))
first_bracket = (int(annual_income>60000000)*60000000*(5/100)) + (int(annual_income <= 60000000)*annual_income*(5/100))
second_bracket = (int(annual_income > 60000000 and annual_income <= 250000000))*(annual_income-60000000)*(15/100) + (int(annual_income > 250000000)*190000000*(15/100))
third_bracket = (int(annual_income > 250000000))*(annual_income-250000000)*(25/100)
print(f"The total tax Mr. Mik has to pay is Rp{int(first_bracket+second_bracket+third_bracket)}")