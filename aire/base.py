from dis import Instruction
import sqlite3 as sql



def Crear_bd():
    cn = sql.connect("ProyectoAire.bd")
    cn.commit()
    cn.close()


def crear_tabla():
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    cursor.execute(
        """Create TABLE Aire(
            Nombre text,
            Marca text,
            Precio integer,
            Instalacion text
        )"""
    )
    cn.commit()
    cursor.execute(
        """CREATE TABLE piezas_aire(
            Nombre text,
            Pieza text,
            cantidad integer,
            precio integer
        )"""
    )
    cn.commit()
    cn.close()




def insertar_registros(usuario,aire_pieza,eleccion_ipo,oal_factura):
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    instruccion = f"INSERT INTO Aire VALUES ('{usuario}','El aire es: {aire_pieza}',{oal_factura},'Instalacion: {eleccion_ipo}')"
    cursor.execute(instruccion)
    
    cn.commit()
    cn.close()

def insertar_registros2(usuario,aire_pieza,canidad,oal_factura):
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    instruccion2 = f"INSERT INTO piezas_aire VALUES ('{usuario}','Pieza: {aire_pieza}','Cantidad: {canidad}',{oal_factura})"
    cursor.execute(instruccion2)
    
    cn.commit()
    cn.close()

def consultar_datos(usuario):
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    instruccion3 = f"SELECT * FROM Aire WHERE Nombre = '{usuario}'"
    cursor.execute(instruccion3)
    datos1 = cursor.fetchall()

    
    cn.commit()
    cn.close()
    print(datos1)



def consultar_datos2(usuario):
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    instruccion4 = f"SELECT Nombre, pieza, cantidad, precio FROM piezas_aire WHERE Nombre = '{usuario}'"
    cursor.execute(instruccion4)
    datos2 = cursor.fetchall()

    
    cn.commit()
    cn.close()
    print(datos2)

def consultar_datos3(usuario):
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    instruccion5 = f"SELECT * FROM Reparaciones WHERE Nombre = '{usuario}'"
    cursor.execute(instruccion5)
    datos3 = cursor.fetchall()

    
    cn.commit()
    cn.close()
    print(datos3)


def crear_tabla2():
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    cursor.execute(
        """Create TABLE Reparaciones(
            Nombre text,
            Region text,
            Precio integer,
            Dias integer
        )"""
    )
    cn.commit()
    cn.close()

def insertar_registros3(usuario,region,lista,precio_iteb):
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    instruccion3 = f"INSERT INTO Reparaciones VALUES ('{usuario}','Region: {region}',{precio_iteb}, {lista} )"
    cursor.execute(instruccion3)
    
    cn.commit()
    cn.close()

def borrar1():
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    cursor.execute(
        """DROP TABLE Aire"""
    )
    cn.commit()
    cn.close()

def eliminar_registros1():
    cn = sql.connect("ProyectoAire.bd")
    cursor = cn.cursor()
    cursor.execute(
        f"""DELETE FROM Aire WHERE Nombre = 'keison' """
    )
    cn.commit()
    cn.close()

if __name__ == "__main__":
    #Crear_bd()
    #crear_tabla()
    #insertar_registros("keison Cerda","s","Si", 48300)
    #consultar_datos()
    #crear_tabla2()
    #borrar1()
    #eliminar_registros1()
    pass  