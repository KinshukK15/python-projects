height = float(input("Enter your height here in meter"))
mass = float(input("Enter your mass here"))

heightfactor = height*height

BMI = mass / heightfactor
print(BMI)

if BMI >= 25:
    print("overweight")
elif BMI >= 18 and BMI <25:
    print("normal")
else:
    print("underweight")



