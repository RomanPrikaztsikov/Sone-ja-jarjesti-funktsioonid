while True:
    print("Men��:")
    print("1.�tletere")
    print("2.Teeliitmist")
    print("3.Teearitust")
    print("4.Teemitmist")
    print("5.Teedivideerimist")
    print("6.Teemoodul")
    print("7.Sisestaandmed")
    print("8.Kuvak�ik")
    print("9.V�ljumine")
    print("10.Lisa")
    
    valik=input("Valivalik(1,2v�i10):")
    
    if valik=='1':
        print("Tere!")
    elif valik=='2':
        num1=int(input("Sisestaesimennumber:"))
        num2=int(input("Sisestateinenumber:"))
        print(f"Liitmistulemus:{num1+num2}")
    elif valik=='3':
        num1=int(input("Sisestaesimennumber:"))
        num2=int(input("Sisestateinenumber:"))
        print(f"Arvutustulemus:{num1*num2}")
    elif valik=='4':
        num1=int(input("Sisestaesimennumber:"))
        num2=int(input("Sisestateinenumber:"))
        print(f"Miinustulemus:{num1-num2}")
    elif valik=='5':
        num1=int(input("Sisestaesimennumber:"))
        num2=int(input("Sisestateinenumber:"))
        print(f"Jagamistulemus:{num1/num2}")
    elif valik=='6':
        num1=int(input("Sisestaesimennumber:"))
        num2=int(input("Sisestateinenumber:"))
        print(f"Modulitulemus:{num1%num2}")
    elif valik=='7':
        andmed=input("Sisestageandmed:")
        print(f"Sisestatudandmed:{andmed}")
    elif valik=='8':
        print("Kuvak�ik!")
    elif valik=='9':
        print("Programmistv�ljumine...")
        break
    elif valik=='10':
        print("Lisa lisa!")
    else:
        print("Valevalik.Palunvalige1,2v�i10.")
