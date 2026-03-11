weight = float(input("Enter your Body Weight: "))
unit = input("Is this weight in (K)g or (L)bs? ").lower()

if unit == "k":
    print(f"Your weight in pounds is {weight * 2.205} lbs")
elif unit == "l":
    print(f"Your weight in kilograms is {weight / 2.205} kg")
else:
    print("Invalid unit entered!")