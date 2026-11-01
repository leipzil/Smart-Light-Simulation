# SID/Name : 13526036/Levina Nirwasita
# Date : 12/10/2026
# Description : determine if there are available time slots according to inputted duration
S1 = int(input("Enter S1: "))
E1 = int(input("Enter E1: "))
S2 = int(input("Enter S2: "))
E2 = int(input("Enter E2: "))
dur = int(input("Enter the event duration (D): "))
avail = False
if S2 <= E1 or S1 <= E2: #if events overlap/touch each other
    if S1 < S2:
        if S1 - dur >= 0:
            avail = True
            print("Yes, Mr. Vin can book the GSG.")
            print("Available time options:")
            print(f"- From {S1-dur} to {S1}") #before 1st event happens
            if E1 > E2 and 23 - E1 >= dur: #after 2nd event ends
                print(f"From {E1} to {E1 + dur}")
            elif E2 > E1 and 23 - E2 >= dur:
                print(f"From {E2} to {E2 + dur}")
            if S2 - E1 > 0: #if events don't overlap/touch
                if S2 - E1 >= dur:
                    print(f"- From {E1} - {S2-E1}")
        else:
            print("Yes, Mr. Vin can book the GSG.")
                print("Available time options:")
                print(f"- From {S1-dur} to {S1}") #before 1st event happens
                if E1 > E2 and 23 - E1 >= dur: #after 2nd event ends
                    print(f"From {E1} to {E1 + dur}")
                elif E2 > E1 and 23 - E2 >= dur:
                    print(f"From {E2} to {E2 + dur}")
                if S2 - E1 > 0: #if events don't overlap/touch
                    if S2 - E1 >= dur:
                        print(f"- From {E1} - {S2-E1}")
                else:

    else: #same but reversed
        if S2 - dur >= 0:
            avail = True
            print("Yes, Mr. Vin can book the GSG.")
            print("avail time opt s2 - {s2-dur}")
            if E1 > E2 and 23 - E1 >= dur:
                print("avail time opt e1 - {e1 + dur}")
            elif E2 > E1 and 23 - E2 >= dur:
                print("avail time opt e2 - {e2 + dur}")
else: #if events are completely separate from each other
    if S1 < S2:
        if S2 - E1 >= dur:
            print("avail time opt ")
if avail == False:
    print("No, try another day!")