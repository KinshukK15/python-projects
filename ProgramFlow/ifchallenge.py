name = input("Please enter your name: ")
age = int(input("Plese enter your age "))

if age >= 18 and age <=30:
    print("Welcome to the holiday, {0}".format(name))
else:
    print("Sorry! You are not eligible.")