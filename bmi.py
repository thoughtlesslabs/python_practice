# Take user input
height = int(input("Please enter your height in inches? "))
weight = int(input("Please enter your weight in pounds? "))

# Calculate BMI
user_bmi = (weight * 703) / (height * height)

if user_bmi < 16:
    bmi_status = "Severely Underweight"
elif user_bmi < 18.4:
    bmi_status = "Underweight"
elif user_bmi < 24.9:
    bmi_status = "Normal"
elif user_bmi < 29.9:
    bmi_status = "Overweight"
elif user_bmi < 34.9:
    bmi_status = "Moderately Obese"
elif user_bmi < 39.9:
    bmi_status = "Severely Obese"
else:
    bmi_status = "Morbidly Obese"

print(f"You have a BMI of {round(user_bmi,2)} and are considered {bmi_status}")
