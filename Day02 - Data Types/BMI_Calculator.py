def BMI_Calculator():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    bmi = int(weight / (height ** 2))
    print(bmi)

BMI_Calculator()