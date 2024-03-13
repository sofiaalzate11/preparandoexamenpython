bandas=[]  

#Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):
    print("1. Registrar banda")
    print("2. buscar informacion de una banda")
    print("3. Agenda del evento")
    print("4. modificar una banda")
    print("5. Salir")


    opcion=int(input("Digita una opcion: "))

    if opcion==1:
        banda={} #diccionario
        #Creando los datos del diccionario
        banda["id"]=int(input("Digita el id: "))
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Genero: ")
        banda["clasificacion"]=input("Clasificacion: ")
        banda["Tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Digita el costo de la banda: $"))

        #Agregando un diccionario a una lista
        bandas.append(banda)

    elif opcion==2:
        
        bandaBuscada=input("Digita el nombre de la banda que estas buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]==bandaBuscada:
                #como lo encontre muestro los datos de la bandAxiliar
                print(f"id: {bandAuxiliar["id"]}---nombre: {bandAuxiliar["nombre"]}") 


            else:
                print("siga buscando") 


    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass

    elif opcion==5:
        pass
    else:
        pass


