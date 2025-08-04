#bmi input
name = input("What's your name?")
age = input("How old are you")
height = input("What's your height in metres? es: 1.70m")
weight = input("What's your weight in kg?")
#bmi index
bmi = input(float(round("weight / heigh**2")))
#bmi categories
if bmi < 18.5 : category = "underweight"
elif 18.5<= bmi < 25 : category = "normal"
elif 25<= bmi < 30 : category = "overweight"
elif 30 <= bmi < 35 : category = "obese"
else : category = "overobese"
#results
print("\n---Results---")
print(f"Hi {name} your BMI results are ready!\n")
print(f"Your BMI is {round(bmi, 2)}. So your category is {category} ")
#save your results
with open("bmi-results.txt", "w") as file:
    file.write("\n---RESULTS---")
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Height: {height}\n")
    file.write(f"Weight: {weight}\n")
    file.write(f"BMI: {bmi}\n")
    file.write(f"Category: {category}\n")