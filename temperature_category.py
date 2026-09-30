temperature=float(input("Enter the Temperature:"))
if temperature<50:
    print(f"{temperature}°F is Cold")
elif temperature<=80:
    print(f"{temperature}°F is Warm")
else:
    print(f"{temperature}°F is Hot")

