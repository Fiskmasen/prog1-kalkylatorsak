run = 0

while run != 5:
    print("[1] Räkna med +")
    print("[2] Räkna med -")
    print("[3] Räkna med *")
    print("[4] Räkna med /")
    print("[5] Avsluta")
    
    try:
        run = int(input("Gör ett val: "))
    except:
        print("Felaktig inmatning.\n")

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