while True:
    print("Menüü:")
    print("1.len()funktsiooni näide")
    print("2.append()funktsiooni näide")
    print("3.remove()funktsiooni näide")
    print("4.split()funktsiooni näide")
    print("5.join()funktsiooni näide")
    print("6.find()funktsiooni näide")
    print("7.sort()funktsiooni näide")
    print("8.reverse()funktsiooni näide")
    print("9.isdigit()funktsiooni näide")
    print("10.isalpha()funktsiooni näide")
    print("0.Väljumine")
    
    valik=input("Sisesta funktsiooni number:")
    
    if valik=="1":
        näidis_list=[1,2,3,4,5]
        print(f"Listi pikkus:{len(näidis_list)}")
    
    elif valik=="2":
        näidis_list=[1,2,3]
        näidis_list.append(4)
        print(f"List pärast append:{näidis_list}")
    
    elif valik=="3":
        näidis_list=[1,2,3,4,5]
        näidis_list.remove(3)
        print(f"List pärast remove:{näidis_list}")
    
    elif valik=="4":
        näidis_string="apple,orange,banana"
        tulemus=näidis_string.split(",")
        print(f"Tulemus split:{tulemus}")
    
    elif valik=="5":
        näidis_list=["apple","orange","banana"]
        tulemus=", ".join(näidis_list)
        print(f"Tulemus join:{tulemus}")
    
    elif valik=="6":
        näidis_string="Hello, world!"
        indeks=näidis_string.find("world")
        print(f"Alamstringi 'world' indeks:{indeks}")
    
    elif valik=="7":
        näidis_list=[5,1,4,3,2]
        näidis_list.sort()
        print(f"List pärast sort:{näidis_list}")
    
    elif valik=="8":
        näidis_list=[1,2,3,4,5]
        näidis_list.reverse()
        print(f"List pärast reverse:{näidis_list}")
    
    elif valik=="9":
        näidis_string="12345"
        tulemus=näidis_string.isdigit()
        print(f"Kas string on number?{tulemus}")
    
    elif valik=="10":
        näidis_string="Hello"
        tulemus=näidis_string.isalpha()
        print(f"Kas string koosneb ainult tähtedest?{tulemus}")
    
    elif valik=="0":
        print("Programmist väljumine.")
        break
    else:
        print("Vale valik.Proovi uuesti.")
