name = str(input("what is your name?"))
age = int(input("what is your age?"))
height = float(input("what is your height?"))
weight = float(input("what is your weight"))

bmi = (weight/height**2)

bmi = format(bmi,'.2f')

print(name,"you are",age,"years old","and your bmi is",bmi)