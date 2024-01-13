
print("\nWelcome to BMI calculator..!")
weight = float(input("\nEnter weight in Kilograms : "))
height = float(input("Enter height in Meters: "))
bmi = weight / height ** 2

if bmi < 18.5:
    print(' Your BMI is ' + str(bmi) + ', Your are underweight.')
elif bmi < 18.5:
    print(' Your BMI is ' + str(bmi) + ', Your are fit!')
elif 25.0 <= bmi <= 29.9:
    print(' Your BMI is ' + str(bmi) + ', Your are overweight.')
elif bmi >= 30:
    print(' Your BMI is ' + str(bmi) + ', Your are in obese range.')
else:
    print("Invalid credentials")

print("Thanks for using BMI calculator.")
