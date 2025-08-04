#bmi input 
name = input("What's your name?")
age = input("How old are you?")
height = float(input("What's your height in metres? es: 1.70m"))
weight = float(input("What's your weight in kg?"))
#bmi index
bmi = round(weight / height**2, 2)
#results
print("\n---Results---")
print(f"Hi {name} your BMI results are ready!\n")
#bmi categories
if bmi < 18.5 : category = "underweight"
elif 18.5<= bmi < 25 : category = "normal"
elif 25<= bmi < 30 : category = "overweight"
elif 30 <= bmi < 35 : category = "obese"
else : category = "overobese"
print(f"Your BMI is {round(bmi, 2)}. So your category is {category} ")
#sentences based on result
if category == "underweight" : print("I know it could be hard to be the skinniest, don't be upset, your not alone<3. If then you have lost weight due to mental healt, yuo deserve help! It'll get better I promise <3")
elif category == "normal" : print("Your weight is absoulutely perfect! Now just focus on beeing the healthiest version of you! You can do this<3")
elif category == "overweight" : print("I know you could feel frustrated or copletely ok with yourself, just remember: Your pearson is not defined by a number<3")
elif category == "obese" : print("The most important thing is that you love yourself! But I want you to keep in mind that beeing like this for a long time is not healthy for your body, wish you best<3")
elif category == "overobese" : print("Mental health comes before everything else, but your body is facing a severe health condition I suggest you to look for help. You don't deserve to live like this. I know it'll be harsh but it's worth it")
#save your results
with open("bmi-results.txt", "w") as file:
    file.write("\n---RESULTS---")
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Height: {height}\n")
    file.write(f"Weight: {weight}\n")
    file.write(f"BMI: {bmi}\n")
    file.write(f"Category: {category}\n")
