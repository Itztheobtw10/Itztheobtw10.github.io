def bmi_calc(weight,height):
    bmi = weight / height ** 2
    return bmi

weight = float(input("Please enter your weight in (KG)"))
height = float(input("please enter your heigh in (m)"))

result = bmi_calc(weight,height)
print("Your BMI is:", result)

