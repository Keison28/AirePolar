
from datetime import datetime
import os
from colorama import Fore
import random


from base import consultar_datos, consultar_datos2, consultar_datos3, insertar_registros, insertar_registros2, insertar_registros3


def principal():

    listaa2 = ["1","2","3","4","5"]
    listaa3 = ["1","2","3"]
    listaa4 = ["1","2","3"]
   
    eleccion_ipo = 0
    factura=  (0)
    aire_pieza = ""
    
  

    print (Fore.GREEN + "*****************************************************************************")
    print ("Bienvenido a Aire Polar")
    print()
    print ("Primero, elija una opcion: ")
    print()
    print ("1. Venta de aires acondicionados.")
    print()
    print ("2. Venta de piezas de aires acondicionados.")
    print()
    print ("3. Reparacion")
    print()
    print ("4. Consultar operaciones realizadas")
    print()
    print ("5. Salir")
    print()
    opcion_pro = (input("Opcion: "))
    print ("*****************************************************************************")

    while opcion_pro not in listaa2:
        os.system("cls")
        return principal()
        
    def venta_aire( factura, aire_pieza, eleccion_ipo):
    
 
        os.system("cls")
        print()
        print (Fore.CYAN +"Catalogos de aires acondicionados:")
        print()

        print ("1.Inverter  14,000$\n")
        print()
        print ("2.Samsung 40,000$\n")
        print()
        print ("3.Mitsubishi Electric 60,000$\n")

        

        print()
        aire_pieza = input(Fore.LIGHTYELLOW_EX + "Elija su Aire acondicionado: ")

        while aire_pieza not in listaa3:
            os.system("cls")
            return venta_aire(factura, aire_pieza, eleccion_ipo)

        if aire_pieza == "1":
            factura = factura + 14000
            aire_pieza = "Inverter"

        elif aire_pieza == "2":
             factura = factura + 40000
             aire_pieza = "Samsung"

        elif aire_pieza == "3":
            aire_pieza = "Mitsubishi Electric"
            factura = factura + 60000
        

        print()
        print ("Desea realizar instalacion")
        print()
        eleccion_ipo = (input("1.No O 2.Si: 250$: "))
        while eleccion_ipo > "2":
            print()
            print ("Opcion no valida")
            print()
            eleccion_ipo = input("Por favor elija una opcion valida: ")

        if eleccion_ipo == "2": 
            factura = factura + 250  

        if eleccion_ipo == "1":
            eleccion_ipo = "No"
        if eleccion_ipo == "2":
            eleccion_ipo = "Si"
        

        os.system("cls")
        print()
        usuario = (input(Fore.BLUE + " Ingrese su nombre y apellido: "))
        print()
        while(len(usuario) > 15):
            print("cantidad de caracteres demasiada")
            usuario = (input(" su nombre y apellido: "))
            print()


     
        
            
           

        fecha_renta = datetime.strptime(input("Ingrese la fecha de la venta: "), "%d/%M/%Y")



        iebis = factura * 0.20

        oal_factura = factura + iebis



        print(Fore.MAGENTA +"********************************************************")
        print()
        print(f"// Nombre: {usuario}")
        print()
        print(f"// fecha de la venta: {(fecha_renta.day)}/{fecha_renta.month}/{fecha_renta.year}")
        print()
        print(f"// El aire acondicionado elejido es: {aire_pieza}")
        print()
        print(f"// instalacion: {eleccion_ipo}")
        print()
        print(f"// El recibo sin itebis es: {factura}")
        print()
        print(f"// El itebis es: {iebis}")
        print()
        print(f"// El recibo con itebis es: {oal_factura}")
        print()
        print("********************************************************")


        arcivo = open("Aire.txt","a")
        arcivo.write  (f"""
        ********************************************************************

        // Nombre: {usuario}

        // fecha de la venta:  {(fecha_renta.day)}/{fecha_renta.month}/{fecha_renta.year}

        // El aire acondicionado elejido es: {aire_pieza}

        // instalacion: {eleccion_ipo}

        // El recibo sin itebis es: {factura}

        // El itebis es: {iebis}

        // El recibo con itebis es: {oal_factura}

        ********************************************************************
        """)

        arcivo.close()




        insertar_registros(usuario,aire_pieza,eleccion_ipo,oal_factura)
        os.system("pause")
        os.system("cls")
        return principal()



    canidad = (0)
    precio_canidad = (0)
    
    def venta_piezas(factura , aire_pieza, canidad, ):




        print (Fore.LIGHTRED_EX +"Catalogos de piezas de aires acondicionados: \n")

        print ("************** 1. Termostato 110$               ************** \n")
        print ("************** 2. Compresor 120$                **************\n")
        print ("************** 3. Condensador 110$              **************\n")
        print ("************** 4. Dispositivo de Expansion 130$ **************\n")
        print ("************** 5 Evaporador 150$                **************\n")
        print ("************** 6 Ventilador 130$                **************\n")
        print ("************** 7 Ductos 120$                    **************\n")

        aire_pieza = input(Fore.LIGHTBLUE_EX +"Elija su pieza: ")
        print()

        if aire_pieza == "1":
            
            print()
            canidad = int (input("Cantidad deseada: "))
            precio_canidad =  (canidad * 110)
            factura = factura + precio_canidad
            aire_pieza = "Termostato"

        elif aire_pieza == "2":

            canidad = float (input("Cantidad deseada: "))
            precio_canidad =  (canidad * 120)
            factura = factura + precio_canidad
            aire_pieza ="Compresor"
        elif aire_pieza == "3":

            canidad = int (input("Cantidad deseada: "))
            precio_canidad =  (canidad * 110)
            factura = factura + precio_canidad
            aire_pieza = "Condensador"
        elif aire_pieza == "4":


            canidad = int (input("Cantidad deseada: "))
            precio_canidad =  (canidad * 130)
            factura = factura + precio_canidad
            aire_pieza = "Dispositivo de Expansión"

        elif aire_pieza == "5":
            canidad = int (input("Cantidad deseada: "))
            aire_pieza = "Evaporador"
            precio_canidad =  (canidad * 150)
            factura = factura + precio_canidad
            factura = factura + canidad

        elif aire_pieza == "6":
            canidad = int (input("Cantidad deseada: "))
            aire_pieza ="Ventilador"
            precio_canidad =  (canidad * 130)
            factura = factura + precio_canidad
            factura = factura + canidad

        elif aire_pieza == "7":
            canidad = int (input("Cantidad deseada: "))
            aire_pieza = "Ductos"
            precio_canidad =  (canidad * 120)
            factura = factura + precio_canidad
            factura = factura + canidad
        else:
            return venta_piezas(factura , aire_pieza, canidad, )


           
                                
        

      
        print()    
        usuario = (input(Fore.CYAN +" Ingrese su nombre y apellido : "))
        print()
        while(len(usuario) > 15):
            print("cantidad de caracteres demasiada")
            usuario = (input(" su nombre: "))
            print()

        
     
        
            
           

        fecha_renta = datetime.strptime(input("Ingrese la fecha de la venta: "), "%d/%M/%Y")
        


        iebis = factura * 0.20

        oal_factura = factura + iebis

        
        print()
        print(Fore.LIGHTCYAN_EX + "********************************************************")
        print()
        print(f"// Nombre: {usuario}")
        print()
        print(f"// fecha de la venta: {(fecha_renta.day)}/{fecha_renta.month}/{fecha_renta.year}")
        print()
        print(f"// La pieza elejida es: {aire_pieza}")
        print()
        print(f"// El recibo sin itebis es: {factura}")
        print()
        print(f"// El itebis es: {iebis}")
        print()
        print(f"// El recibo con itebis es: {oal_factura}")
        print()
        print("********************************************************")
        insertar_registros2(usuario,aire_pieza,canidad,oal_factura)


        arcivo = open("Pieza.txt","a")
        arcivo.write  (f"""
        ********************************************************************

        // Nombre: {usuario}

        // fecha de la venta:  {(fecha_renta.day)}/{fecha_renta.month}/{fecha_renta.year}

        // La pieza elejida es: {aire_pieza}

        // El recibo sin itebis es: {factura}

        // El itebis es: {iebis}

        // El recibo con itebis es: {oal_factura}

        ********************************************************************
        """)

        arcivo.close()
        
        os.system("pause")
        os.system("cls")
        return principal()
      
        
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        
    def reparacion():
        precio = 250
        iteb = precio * 0.20
        precio_iteb = precio + iteb
        print()
        print(Fore.CYAN +"Bienvendido")
        print()
        print("Las reparaciones tienen un costo de 250$")
        print()    
        usuario = (input(Fore.BLUE +" Ingrese su nombre y apellido : "))
        print()
        while(len(usuario) > 15):
            print("cantidad de caracteres demasiada")
            usuario = (input(" su nombre y apellido: "))
            print()

        print("*************** Indique la region en donde vive: ***************")
        print()
        print("*************** 1. Cibao                         ***************")
        print()
        print("*************** 2. Oeste o Suroeste              ***************")
        print()
        print("*************** 3. Este o Sureste                ***************")
        print()
        region = (input("Region seleccionada: "))
        while region not in listaa4:
            os.system("cls")
            region = (input(Fore.RED + "La opcion selecionada no es valida, ingrese una opcion correcta: "))


        if region == "1":
            region = "Cibao"
        elif region =="2":
            region = "Oeste o Suroeste"

        elif region == "3":
            region = "Este o Sureste"
        
        


        print()
        fecha_renta = datetime.strptime(input(Fore.LIGHTBLUE_EX + "Ingrese la fecha de la solicitud: "), "%d/%M/%Y")
        lista = random.randint(2,7)

        print(Fore.GREEN + f"Bien enviaremos un tecnico para revisar su aire acondicionado. El tecnico prodia llegar aproximadamente en {lista} dias")

        print(Fore.LIGHTYELLOW_EX +"*Recibo:*")
        print()
        print(f"*Nombre: {usuario}*")
        print()
        print(f"*Region: {region}*")
        print()
        print(f"*Fecha de la solicitud: {(fecha_renta.day)}/{fecha_renta.month}/{fecha_renta.year}*")
        print()
        print(f"*Dias aproximados: {lista} dias*")
        print()
        print(f"*Precio: {precio}*")
        print()
        print(f"*Valor del Itebis: {iteb}*")
        print()
        print(f"*Precio con inpuestos: {precio_iteb}*")
        print()

        insertar_registros3(usuario,region,lista,precio_iteb)

        os.system("pause")
        os.system("cls")
        return principal()





#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def consultar():
        print(Fore.LIGHTMAGENTA_EX +"Bienvenido")
        print()
        print("************* Cual Consulta desea realizar *************")
        print()
        print("************* 1. Venta de aire             *************")
        print()
        print("************* 2. Venta de piezas           *************")
        print()
        print("************* 3. Reparacion                *************")
        print()
        elec_consulta = (input(Fore.RED +"Opcion: "))
        os.system("cls")
        
        
        if elec_consulta == "1":
            usuario = (input(Fore.LIGHTCYAN_EX +"Ingrese su nombre y apellido con el que se ha registrado anteriormente: "))
            print()
            consultar_datos(usuario)
        elif elec_consulta == "2":
            os.system("cls")
            usuario = (input(Fore.LIGHTCYAN_EX +"Ingrese su nombre y apellido con el que se ha registrado anteriormente: "))
            print()
            consultar_datos2(usuario)
        elif elec_consulta == "3":
            os.system("cls")
            usuario = (input(Fore.LIGHTCYAN_EX +"Ingrese su nombre y apellido con el que se ha registrado anteriormente: "))
            print()
            consultar_datos3(usuario)

        os.system("pause")
        os.system("cls")
        return principal()




    if opcion_pro == "1":
        
        venta_aire(factura ,eleccion_ipo, aire_pieza )
        
    elif opcion_pro == "2":

        venta_piezas(canidad, factura, aire_pieza )
    
    elif opcion_pro == "3":
        reparacion()

    elif opcion_pro == "4":
        consultar()
    
    elif opcion_pro == "5":
        os.system("pause")
principal()

    