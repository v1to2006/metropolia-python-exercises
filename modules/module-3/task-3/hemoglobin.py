femaleMinHemoglobinRate = 117
femaleMaxHemoglobinRate = 175

maleMinHemoglobinRate = 134
maleMaxHemoglobinRate = 195

userGender = input("Enter your gender (male/female): ")
userHemoglobinLevel = float(input("Enter your hemoglobin rate: "))

if (userGender.lower() == "male"):
    if userHemoglobinLevel < maleMinHemoglobinRate:
        print("Your hemoglobin level is BELOW NORMAL")
    elif userHemoglobinLevel > maleMaxHemoglobinRate:
        print("Your hemoglobin level is ABOVE NORMAL")
    else:
        print("Your hemoglobin level is NORMAL")
elif (userGender.lower() == "female"):
    if (userHemoglobinLevel < femaleMinHemoglobinRate):
        print("Your hemoglobin level is BELOW NORMAL")
    elif (userHemoglobinLevel > femaleMaxHemoglobinRate):
        print("Your hemoglobin level is ABOVE NORMAL")
    else:
        print("Your hemoglobin level is NORMAL")
else:
    print("Invalid gender input.")