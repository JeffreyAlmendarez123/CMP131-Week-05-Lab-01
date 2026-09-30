#Jeffrey Almendarez
#CMP131
#Week5_Lab01
print("---Temperature Catergory---")
temperature=float(input("Enter the Temperature:"))#Asking for the input
if temperature<50:
    print(f"{temperature}°F is Cold")
elif temperature<=80:
    print(f"{temperature}°F is Warm")
else:
    print(f"{temperature}°F is Hot")


