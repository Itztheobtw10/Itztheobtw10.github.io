def bmi_calc(weight,height):
    bmi = weight / height ** 2
    return bmi

weight = float(input("Please enter your weight in (KG)"))
height = float(input("please enter your heigh in (m)"))

result = bmi_calc(weight,height)

print("Your BMI is:",result)

response = input("Do you want any health advice (CLICK Y FOR YES AND N FOR NO )")

if response == "Y" and result < 18.5:
    print("Your BMI indicates you may be underweight. To support a healthier weight: \n -Consider adding nutrient-dense foods like lean proteins,whole grains,nuts,and healthier fats.\n -Aim to eat regular meald andf snacks throughout the day to graduslly increase your intake.\n -Include strength training in your routine to help muscle mass." )
elif response == "Y" and result >= 18.5 and  result < 25:
    print("Your BMI indicates you are at a normal weight keep doing what your doing buddy :)")
elif response == "Y" and result >= 25 and  result < 30:
    print("Your BMI indicates you are underweight")