def calculate_bmi(weight_kg, height_meters, precision=1):
  #formular for calculating
  bmi= weight_kg / (height_meters **2)
  #this is round the result in 1 precision
  return round (bmi, 1)
  #defining the category based on the bmi value
def bmi_category(bmi):
    if bmi < 18.5:
      return  f"underweight."
    elif 18.5 <= bmi and bmi < 24.9:
        return  f" normalweight."
    elif 25 <= bmi and bmi < 29.9:
         return  f"overweight."
    else:
         return  f"obese."
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)
print(f"Your BMI is {bmi}. You are classified as {category}.")