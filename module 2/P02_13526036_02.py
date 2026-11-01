# SID/Name : 13526036/Levina Nirwasita
# Date : 12/10/2026
# Description : determine if an ideal troop composition is possible based on available troops
wizard = int(input("Enter the number of wizards available: "))
archer = int(input("Enter the number of archers available: "))
witch = int(input("Enter the number of witches available: "))
healer = int(input("Enter the number of healers available: "))
hunter = int(input("Enter the number of hunters available: "))
bomber = int(input("Enter the number of bombers available: "))
total_troops = wizard + archer + witch + healer + hunter + bomber
print(archer//3 >= wizard//(archer/3))
print(healer//2 >= witch//(healer/2)) #if healer // 2 is 5, there must be less than/equal to 5 number of witches 
print(healer/2)
print(witch/(healer/2))
print(bomber//2>= (hunter*3)/(bomber/2))
if total_troops >= 30 and archer/3 >= wizard/(archer/3) and healer/2 >= witch/(healer/2) and bomber/2>= (hunter*3)/(bomber/2): #if archer // 3 = 5 then it should be more than/equal to wizard//5
    print(f"Mr. Ky can form an ideal troop composition with {int(wizard//(archer/3))} wizards, {int(archer//3)} archers, {int(witch//(healer/2))} witches, {int(healer//2)} healers, {int((hunter*3)//(bomber/2))} hunters, and {int(bomber//(2))} bombers.")
else:
    print("Mr. Ky cannot form an ideal troop composition.")