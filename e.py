num = int(input("Enter a number: "))

if num < 0 or num > 100:
    print("Invalid input")

elif num >= 91 and num <= 100:
    print("Super Smart")

elif num >= 81 and num <= 90:
    print("Smart")

elif num >= 71 and num <= 80:
    print("Smart enough")

elif num >= 61 and num <= 70:
    print("Just smart")

elif num >= 36 and num <= 60:
    print("No smart")

else:
    print("Dump")
