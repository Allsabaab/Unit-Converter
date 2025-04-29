while True:
    print("""
Welcome to the Unit Converter """)

    x = int(input("""
What do you want to convert?
Type '1' if WEIGHT or type '2' if LENGTH : """))

    if x == 1:
        a = int(input("""
What unit do you want to convert from?
Type '1' if from KG, type '2' if from GRAMS or type '3' if from POUND : """))
        if a == 1:
            b = int(input("""
What unit do you want to convert to?
Type '1' if to GRAMS or type '2' if to POUND : """))
            if b == 1:
                c = float(input("     KG : "))
                d = c * 1000
                print(f"     GRAMS = {d:.2f}")
            elif b == 2:
                c = float(input("     KG : "))
                d = c * 2.20462
                print(f"     POUND = {d:.2f}")
            else:
                print("     INVALID CODE")
        elif a == 2:
            b = int(input("""
What unit do you want to convert to?
Type '1' if to KG or type '2' if to POUND : """))
            if b == 1:
                c = float(input("     GRAMS : "))
                d = c / 1000
                print(f"     KG = {d:.2f}")
            elif b == 2:
                c = float(input("     GRAMS : "))
                d = c * 0.00220462
                print(f"     POUND = {d:.2f}")
            else:
                print("     INVALID CODE")
        elif a == 3:
            b = int(input("""
What unit do you want to convert to?
Type '1' if to KG or type '2' if to GRAMS : """))
            if b == 1:
                c = float(input("     POUND : "))
                d = c * 0.453592
                print(f"     KG = {d:.2f}")
            elif b == 2:
                c = float(input("     POUND : "))
                d = c * 453.592
                print(f"     GRAMS = {d:.2f}")
            else:
                print("     INVALID CODE")
        else:
            print("     INVALID CODE")

    elif x == 2:
        a = int(input("""
What unit do you want to convert from?
Type '1' if from Foot, type '2' if from INCHES, type '3' if from METER or type '4' if from CENTIMETER : """))
        if a == 1:
            b = int(input("""
What unit do you want to convert to?
Type '1' if to INCHES, type '2' if to METER or type '3' if to CENTIMETER : """))
            if b == 1:
                c = int(input("     FOOT : "))
                d = float(input("     INCHES : "))
                e = (c * 12) + d
                print(f"     INCHES = {e:.2f}")
            elif b == 1:
                c = int(input("     FOOT : "))
                d = float(input("     INCHES : "))
                e = (c * 12) + d
                f = e * 0.0254
                print(f"   METER = {f:.2f}")
            elif b == 3:
                c = int(input("     FOOT : "))
                d = float(input("     INCHES : "))
                e = (c * 12) + d
                f = e * 2.54
                print(f"   CENTIMETER = {f:.2f}")
            else:
                print("     INVALID CODE")
        elif a == 2:
            b = int(input("""
What unit do you want to convert to?
Type '1' if to FOOT, type '2' if to METER or type '3' if to CENTIMETER : """))
            if b == 1:
                c = int(input("     INCHES : "))
                d = c / 12
                e = int(d)
                f = d - e
                g = f * 12
                print(f"     FOOT = {e}, INCHES = {g:.2f} or FOOT = {d:.2f}")
            elif b == 2:
                c = int(input("     INCHES : "))
                d = c * 0.0254
                print(f"     METER = {d:.2f}")
            elif b == 3:
                c = int(input("   INCHES : "))
                d = c * 2.54
                print(f"     CENTIMETER = {d:.2f}")
            else:
                print("     INVALID CODE")
        elif a == 3:
            b = int(input("""
What unit do you want to convert to?
Type '1' if to FOOT, type '2' if to INCHES or type '3' if to CENTIMETER : """))
            if b == 1:
                c = int(input("     METER : "))
                d = c * 3.28084
                e = int(d)
                f = d - e
                g = f * 12
                print(f"     FOOT = {e}, INCHES = {g:.2f} or FOOT = {d:.2f}")
            elif b == 2:
                c = int(input("     METER : "))
                d = c * 39.3701
                print(f"     INCHES = {d:.2f}")
            elif b == 3:
                c = int(input("     METER : "))
                d = c * 100
                print(f"     CENTIMETER = {d:.2f}")
            else:
                print("     INVALID CODE")
        elif a == 4:
            b = int(input("""
What unit do you want to convert to?
Type '1' if to FOOT, type '2' if to INCHES or type '3' if to METER : """))
            if b == 1:
                c = int(input("     CENTIMETER : "))
                d = c * 0.0328084
                e = int(d)
                f = d - e
                g = f * 12
                print(f"     FOOT = {e}, INCHES = {g:.2f} or FOOT = {d:.2f}")
            elif b == 2:
                c = int(input("     CENTIMETER : "))
                d = c * 0.393701
                print(f"     INCHES = {d:.2f}")
            elif b == 3:
                c = int(input("     CENTIMETER : "))
                d = c * 0.01
                print(f"     METER = {d:.2f}")
            else:
                print("     INVALID CODE")
        else:
            print("     INVALID CODE")
    else:
        print("     INVALID CODE")


    cont=int(input("""
Do you want to continue converting?
Press '1' if YES or press '2' if NO : """))
    if cont=="2":
        print("Goodbye!")

        break
