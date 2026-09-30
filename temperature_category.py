#Jeffrey Almendarez
#CMP131
#Week5_Lab01
print("---Temperature Catergory---")
temperature=float(input("Enter the Temperature:"))#Asking for the input
if temperature<50:
    print(f"{temperature}°F is Cold") #Any number below 50 will print out it's cold
elif temperature<=80:
    print(f"{temperature}°F is Warm")#Any number within the range will display that the weather is warm.
else:
    print(f"{temperature}°F is Hot") #Any number greater than 50 or 80 will pop up as hot


