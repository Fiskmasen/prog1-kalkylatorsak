run = 0 
# "run" kan man säga är som själva huvud variablen och argumenterbart den viktigaste delen av koden, eftersom det är den som ska printas ut och ge användaren de olika valen man kan göra i kalkylatorn beroende på vilken siffra från 1 till 5 som användaren väljer

while run != 5: # "while" kommandot är också en väldigt viktig del av koden eftersom det är den som "loopar" koden fram tills användaren väljer valet "5".
    # "!=" kommandot står för "inte lika med" och är en viktig del av den här loopen. I det här fallet så är det den som ser till att både loopen och själva koden fungerar som de ska, och det är även den som ser till att loopen fortsätter så länge användaren väljer valet "5" som avlutar koden.
    print("[1] Räkna med +")
    print("[2] Räkna med -")
    print("[3] Räkna med *")
    print("[4] Räkna med /")
    print("[5] Avsluta")
    # "print" kommandot behövs för att printa ut själva koden i terminalen
    try: 
        run = int(input("Gör ett val: "))
    except:
        print("Felaktig inmatning.\n")
# "try" kommandot/blocket används till att testa koden eller ett kodblock för att söka efter möjliga fel/errors i koden eller kodblocket, och "except" används för att hantera dessa fel/errors. 
    if run == 1:
        print("\nRäkna med addition")
        try:
            tal1 = float(input("Skriv ett tal: "))
            tal2 = float(input("Skriv ett andra tal: "))
            summa = tal1 + tal2
            print(f"Summan av {tal1} + {tal2} är {summa}\n")
        except:
            print("Felaktig inmatning.\n")
    
    elif run == 2:
        print("\nRäkna med subtraktion")
        try:
            tal1 = float(input("Skriv ett tal: "))
            tal2 = float(input("Skriv ett andra tal: "))
            summa = tal1 - tal2
            print(f"Summan av {tal1} - {tal2} är {summa}\n")
        except:
            print("Felaktig inmatning.\n")
    
    elif run == 3:
        print("\nRäkna med multiplikation")
        try:
            tal1 = float(input("Skriv ett tal: "))
            tal2 = float(input("Skriv ett andra tal: "))
            summa = tal1 * tal2
            print(f"Summan av {tal1} * {tal2} är {summa}\n")
        except:
            print("Felaktig inmatning.\n")

    elif run == 4:
        print("\nRäkna med division")
        try:
            tal1 = float(input("Skriv ett tal: "))
            tal2 = float(input("Skriv ett andra tal: "))
            summa = tal1 / tal2
            print(f"Summan av {tal1} / {tal2} är {summa}\n")
        except:
            print("Felaktig inmatning.\n")

    else:
        if run == 5:
            (print("\nAvsluta"))

# "if", "elif", och "else" kommandona är också viktiga delar av koden och behövs delvis för att både loopen/looparna och själva koden ska fungera som de ska. Men dom behövs även för att programmet faktiskt ska kunna ge användaren de olika valen som hen har att välja på.
# "==" kommandot står för "lika med" och är också en väldigt viktig del av både loopen och själva koden och behövs för att koden och looparna ska fungera som de ska av i stort sett samma anledning(ar) som "!=" kommandot som jag (typ) beskrev tidigare.