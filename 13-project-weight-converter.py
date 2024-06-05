weight = int(input("Weight: "))

units = input("(L)bs or (K)g ")

if units.upper() == "L":
    converted= weight//2.2
    print(f"You are {converted} kg")
elif units.upper() == "K":
    converted= weight * 2.2
    print(f"You are {converted} lbs")
else:
    print("please input weight in lbs or kg")