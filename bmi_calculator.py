def kg_to_pounds(kg):
        return kg * 2.20462
def meters_to_inches(meters):
        return meters * 39.3701
def pounds_to_kg(pounds):
        return pounds / 2.20462
def inches_to_meters(inches):
        return inches / 39.3701
#Getting user input for units
weight_unit = input("Enter weight unit (kg or pounds): ")
height_unit = input("Enter height unit (meters or inches): ")
# Unit conversion, using the if if because they are independent events
if weight_unit == "pounds":
        weight = pounds_to_kg
if height_unit == "inches":
        height = inches_to_meters
else:
        weight = kg_to_pounds
        height = meters_to_inches

def calculate_bmi(weight, height, weight_unit, height_unit, precision=1):
    # Convert to kg and meters if necessary
    if weight_unit == "pounds":
        weight = pounds_to_kg(weight)
    if height_unit == "inches":
        height = inches_to_meters(height)
    # Calculate BMI
    bmi = weight / (height ** 2)
     #this is to round the result in 1 precision
    return round (bmi, 1)
  #defining the category based on the bmi value, the elif are used because they are mutually exclusive
def bmi_category(bmi):
    if bmi < 18.5:
      return  f"underweight."
    elif 18.5 <= bmi and bmi < 24.9:
        return  f" normalweight."
    elif 25 <= bmi and bmi < 29.9:
         return  f"overweight."
    else:
         return  f"obese."

weight = float(input("Enter your weight: "))

height = float(input("Enter your height: "))


bmi = calculate_bmi(weight, height, weight_unit, height_unit)
category = bmi_category(bmi)
print(f"Your BMI is {bmi}. You are classified as {category}.")
