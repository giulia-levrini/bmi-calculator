#finestra opzioni
import tkinter as tk:
def scegli_lingua(lang)
    global lingua
    lingua = lang
    finestra.destroy() 
def apri_app()
    app = tk.Tk()
    app.title("BMI Calculator")
def scegli_lingua()
    finestra = tk.Tk()
    finestra.title("Choose the language/Scegli lingua")
    finestra.Label(finestra , text="Choose language/Scegli lingua").pack(pady=10)
    finestra.Button(finestra , text="Italiano" , command=lambda : scegli_lingua("IT")).pack(pady=10)
    finestra.Button(finestra , text="English" , command:lambda : scegli_lingua("EN")).pack(pady=5)
if lingua == "EN" : 
    print("Welcome on BMI Calculator!")
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
    if category == "underweight" : print("I know it could be hard to be the skinniest, don't be upset, your not alone<3. If then you have lost weight due to mental healt, you deserve help! It'll get better I promise <3")
    elif category == "normal" : print("Your weight is absoulutely perfect! Now just focus on beeing the healthiest version of you! You can do this<3")
    elif category == "overweight" : print("I know you could feel frustrated or copletely ok with yourself, just remember: Your pearson is not defined by a number<3")
    elif category == "obese" : print("The most important thing is that you love yourself! But I want you to keep in mind that beeing like this for a long time is not healthy for your body, wish you best<3")
    elif category == "overobese" : print("Mental health comes before everything else, but your body is facing a severe health condition I suggest you to look for help. You don't deserve to live like this. I know it'll be harsh but it's worth it")
    print("\n Your results have been saved in 'bmi-results.txt'")
    #save your results
    with open("bmi-results.txt", "a") as file:
        file.write("\n---RESULTS---")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Height: {height}\n")
    #bmi input 
if lingua == "IT" :
    print("Benvenut* su BMI Calculator")
    name = input("Come ti chiami?")
    age = input("Quanti anni hai?")
    height = float(input("Qual è la tua altezza in metri? es: 1.70m"))
    weight = float(input("Qual è il tuo peso in kg?"))
    #bmi index
    bmi = round(weight / height**2, 2)
    #results
    print("\n---Risultati---")
    print(f"Ciao {name} i tuoi risultati sono pronti!\n")
    #bmi categories
    if bmi < 18.5 : category = "sottopeso"
    elif 18.5<= bmi < 25 : category = "normale"
    elif 25<= bmi < 30 : category = "sovrappeso"
    elif 30 <= bmi < 35 : category = "obeso"
    else : category = "ultra obeso"
    print(f"Il tuo BMI è {round(bmi, 2)}. Quindi la tu categoria è {category} ")
#sentences based on result
if category == "sottopeso" : print("Vedo che sei sottopeso, non so se è perchè sei così di costituzione o lo sei diventat* in seguito a diete. Nel primo caso so come possa essere difficile essere sempre quell* più magr*, ma non preoccuparti, rimani sempre una bellissima persona. Se sui invece diventat* sottopeso, ti prego fatti aiutare<3 Tutti meritiamo una mano, ricordati che sei speciale<3")
elif category == "normale" : print("Il tuo peso è perfetto! Ora focalizzati sul rimanere in salute con uno stile di fita attivo e sano! Ti augoro il meglio<3")
elif category == "sovrappeso" : print("So quanto possa essere difficile essere quell* chepesa un pò di più ma ricordati che tu non sei un numero<3 Le tue azioni definiscono ciò che sei<3")
elif category == "obeso" : print("La cosa più importante è apprezzarsi per ciò che si è! Ricordati però che non è sano per il tuo corpo permanere in uno stato di obesità, col tempo portebbe portare a problemi di salute, ti augoro il meglio<3")
elif category == "ultra obeso" : print("La salute mentale viene prima di tutto, tu però ti trovi in una condizione che nel lungo termine non può essere sostenuta dal tuo organismo! Chiedi a figure esperte che ti aiutranno, so che sarà difficile ma credo in te<3")
print("\n I tuoi risultati sono stati salvati su 'bmi-risultati.txt'")
#save your results
with open("bmi-results.txt", "a") as file:
    file.write("\n---RISULTATI---")
    file.write(f"Nome: {name}\n")
    file.write(f"Età: {age}\n")
    file.write(f"Altezza: {height}\n")
    file.write(f"Peso: {weight}\n")
    file.write(f"BMI: {bmi}\n")
    file.write(f"Categoria: {category}\n")

