import dataclasses
menu= 4

while menu == 4:
    print("============eSports eShirlitos=====================")
    listajugador= []
    print("1.Registrar puntajes torneo")
    print("2.Listar los todos puntajes")
    print("3.Imprimir por Tipo")
    print("4.Salir del programa")
    menu = input("Seleccione un opcion:")
if menu == "1":
    try:
        with open ("puntaje.txt", "w") as archivo:
            id = input("Ingrese Nickname de juego:")
            nombre = input("Ingrese su nombre real:")
            valorant= input("Ingrese su puntaje de Valorant:")
            fornite = input("Ingrese su puntaje de Fornite:")
            fifa= input("Ingrese su puntaje de Fifa: ")
            dificultad = input("Ingrese su dificultad (Principiante, Avanzado, Experto)")
            archivo.write ("Nombre de usuario"+id+"Nombre real"+nombre+"Puntaje Valorant"+valorant+"Puntaje Fornite:"+fornite+"Puntaje Fifa:" + fifa +"Dificultad:"+dificultad)
    except:
        []
elif menu == "2":
    with open ("puntaje.txt", "r") as archivo:
        for puntaje in listajugador:
            print(puntaje)