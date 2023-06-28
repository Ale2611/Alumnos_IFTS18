import os


alumno={}

    #Crea archivo txt
def crear_documento():
    with open("notas_alumno.txt", "a") as archivo:
        archivo.write("notas_alumnos")
        archivo.writelines(['\nDNI     ','Nombre     ','Apellido     ','Domicilio     ','Tec.Programación-Nota1     ','Tec.Programación-nota2     ','Administración BBDD-Nota1     ','Administración BBDD-Nota2     ','Tec.Programación-Promedio     ','Adminstración-Promedio     ''Situación - Tec.programación     ','Situación - Administración BBDD     \n'])


#valida dni ingresado
def validar_alumno(dni):
    if(dni in alumno):
        return True
    else:
        return False     


#Agregar alumnos al archivo. Si el archivo existe directamente lo abre y agrega informacion. Si no existe, llama a "crear_documento" y agrega info
def agregar_alumno(dni):
    archivo_path = "notas_alumno.txt"

    if os.path.exists(archivo_path): # import os activa la validacion verificando el path del archivo#
         with open("notas_alumno.txt", "a") as archivo:
            if validar_alumno(dni):
                print('El DNI ingresado ya está registrado')
            else:
                nombre=input("Indicar el nombre completo del alumno: ")
                apellido=input("Indicar el apellido del alumno: ")
                domicilio=input("Indicar la dirección del alumno: ")
                alumno[dni] = [nombre, apellido, domicilio,0,0,0,str,0,0,0,str]
                cadena_alumno= f"{dni} {nombre} {apellido} {domicilio}\n"
                archivo.write(cadena_alumno)
    else:
        crear_documento()
        with open("notas_alumno.txt", "a") as archivo:
            if validar_alumno(dni):
                print('El DNI ingresado ya está registrado')
            else:
                nombre=input("Indicar el nombre completo del alumno: ")
                apellido=input("Indicar el apellido del alumno: ")
                domicilio=input("Indicar la dirección del alumno: ")
                alumno[dni] = [nombre, apellido, domicilio]
                cadena_alumno = f"{dni} {nombre} {apellido} {domicilio}\n"
                archivo.write(cadena_alumno)


def modificar_alumno(dni):
    if not validar_alumno(dni):
        print('El DNI ingresado no está registrado')
    with open("notas_alumno.txt", "a") as archivo:

        if validar_alumno(dni):
            modif = input("Indicar que querés modificar: A-Para Nombre / B-Para Apellido / C-Para el domicilio: ")
            mayuscula = modif.upper()
            if mayuscula == 'A':
                nombre = input("Indicar el nuevo nombre: ")
                alumno[dni][0] = nombre
            elif mayuscula == 'B':
                apellido = input("Indicar el nuevo apellido: ")
                alumno[dni][1] = apellido
            elif mayuscula == 'C':
                domicilio = input("Indicar la nueva dirección: ")
                alumno[dni][2] = domicilio
            else:
                print('Opción invalida')
                return
            # Actualizar el archivo con los datos modificados
        with open("notas_alumno.txt", "r") as archivo:
            lineas = archivo.readlines()

        with open("notas_alumno.txt", "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split()
                if datos[0] == dni:
                    if mayuscula == 'A':
                        nombre = input("Indicar el nuevo nombre: ")
                        datos[1] = nombre
                    elif mayuscula == 'B':
                        apellido = input("Indicar el nuevo apellido: ")
                        datos[2] = apellido
                    elif mayuscula == 'C':
                        domicilio = input("Indicar la nueva dirección: ")
                        datos[3] = domicilio
                linea = " ".join(datos) + "\n"
                archivo.write(linea)

    print("Datos modificados exitosamente.")



def eliminar_alumno(dni):
    if validar_alumno(dni):
        with open("notas_alumno.txt", "r") as archivo:
            lineas = archivo.readlines()

        datos_actualizados = []
        for linea in lineas:
            datos = linea.strip().split()
            if len(datos) > 0 and datos[0] != dni:
                datos_actualizados.append(linea)

        with open("notas_alumno.txt", "w") as archivo:
            archivo.writelines(datos_actualizados)

        del alumno[dni]
        print('Alumno eliminado correctamente')
    else:
        print('El DNI ingresado no está registrado')




def nota_a_cargar(dni):
    if validar_alumno(dni):
        linea_nueva = ""
        nota_acargar = input("Querés cargar para A-Para Técnica de programación / B-Para Administración BBDD: ")
        nota_mayuscula = nota_acargar.upper()


        if nota_mayuscula == 'A':
            nota_tec = float(input("Cargar la Primera nota de la materia Técnica de programación: "))
            nota_tec2 = float(input("Cargar la Segunda nota de la materia Técnica de programación: "))
            linea_nueva = f" {nota_tec} {nota_tec2}\n"
            alumno[dni].insert(3, nota_tec)
            alumno[dni].insert(4, nota_tec2)
            alumno[dni][3]=nota_tec
            alumno[dni][4]=nota_tec2
            total_tec=nota_tec+nota_tec2
            alumno[dni].insert(5, total_tec)
            alumno[dni][5]=total_tec
            print("Carga completa")

        elif nota_mayuscula == 'B':
            nota_admin = float(input("Cargar la Primera nota de la materia Administración BBDD: "))
            nota_admin2 = float(input("Cargar la Segunda nota de la materia Administración BBDD: "))
            linea_nueva = f" {nota_admin} {nota_admin2}\n"
            total_adm=nota_admin+nota_admin2
            alumno[dni].insert(6, nota_admin)
            alumno[dni].insert(7, nota_admin2)
            alumno[dni].insert(8, total_adm)
            alumno[dni][6]=nota_admin
            alumno[dni][7]=nota_admin2
            alumno[dni][8]=total_adm
            print("Carga completa")

        else:
            print('Opción inválida. No se cargaron notas.')


        with open("notas_alumno.txt", "r+") as archivo:
            lineas = archivo.readlines()
            archivo.seek(0)

            for linea in lineas:
                datos = linea.strip().split()
                if datos[0] == dni:
                    linea = linea.strip() + " " + linea_nueva.strip() + "\n"
                archivo.write(linea)
    else:
        print('El DNI ingresado no está registrado')

def modificar_notas(dni):
    mat_amodif=input("Indicar la materia a modificar: A-Para Técnica de programación / B-Para Administración BBDD")
    mat_amodifmayuscul=mat_amodif.upper()
    if mat_amodifmayuscul=='A':
        eleccion_amodif=input("Que notas deseas modificar: A-la primera / B-la segunda / C-ambas")
        if eleccion_amodif=='A':
            nota_tec=float(input("Ingresa la nueva nota"))
            alumno[dni][3]=nota_tec
        elif eleccion_amodif=='B':
            nota_tec2=float(input("Ingresa la nueva nota"))
            alumno[dni][4]=nota_tec2
            total_tec=nota_tec+nota_tec2
            alumno[dni][5]=total_tec
        elif eleccion_amodif=='C':
            nota_tec=float(input("Actualiza la primera nota: "))
            alumno[dni][3]=nota_tec
            nota_tec2=float(input("Actualiza la segunda nota"))
            alumno[dni][4]=nota_tec2
            total_tec=nota_tec+nota_tec2
            alumno[dni][5]=total_tec
    elif mat_amodifmayuscul=='B':
               eleccion_amodif=input("Que notas deseas modificar: A-la primera / B-la segunda / C-ambas")
               if eleccion_amodif=='A':
                    nota_admin=float(input("Ingresa la nueva nota"))
                    alumno[dni][6]=nota_admin
               elif eleccion_amodif=='B':
                    nota_admin2=float(input("Ingresa la nueva nota"))
                    alumno[dni][7]=nota_admin2
               elif eleccion_amodif=='C':
                    nota_admin=float(input("Actualiza la primera nota: "))
                    alumno[dni][6]=nota_admin
                    nota_admin2=float(input("Actualiza la segunda nota"))
                    alumno[dni][7]=nota_admin2
                    total_adm=nota_admin+nota_admin2
                    alumno[dni][8]=total_adm
      # Actualizar el archivo TXT con los nuevos datos
    with open("notas_alumno.txt", "r+") as archivo:
        lineas = archivo.readlines()
        archivo.seek(0)

        for linea in lineas:
            datos = linea.strip().split()
            if datos[0] == dni:
                if mat_amodifmayuscul == 'A':
                    linea = linea.strip().split()[:5] + [str(alumno[dni][3]), str(alumno[dni][4])] + linea.strip().split()[7:]
                elif mat_amodifmayuscul == 'B':
                    linea = linea.strip().split()[:8] + [str(alumno[dni][6]), str(alumno[dni][7])] + linea.strip().split()[10:]
            linea = " ".join(linea) + "\n"
            archivo.write(linea)


def calcular_promedio(dni):
    if validar_alumno(dni):
        promedioprog=(alumno[dni][5])/2
        alumno[dni][10]=promedioprog
        print('El promedio de progrmacación es: ', promedioprog)
        promedioadm=(alumno[dni][8])/2
        alumno[dni][11]=promedioadm
        linea_nueva = f" {promedioprog} {promedioadm} \n"
        print('El promedio de administración BBDD es: ', promedioadm)

        with open("notas_alumno.txt", "r+") as archivo:
            lineas = archivo.readlines()
            archivo.seek(0)

            for linea in lineas:
                datos = linea.strip().split()
                if datos[0] == dni:
                    linea = linea.strip() + " " + linea_nueva.strip() + "\n"
                archivo.write(linea)

def estado_materia(dni):
    if validar_alumno(dni):
         estadoprog=alumno[dni][10]
         estadoadm=alumno[dni][11]
         if estadoprog>=7:
            print("La materia Técnica de programación está regular")
            estaescritoprog=('Regular')
         elif estadoprog<7:
            print("La materia Técnica de programación NO está regular")
            estaescritoprog=('NO Regular')
         if estadoadm>=7:
            print("La materia Administración BBDD está regular")
            estaescritoadm=('Regular')
         elif estadoadm<7:
            print("La materia Administración BBDD NO está regular")
            estaescritoadm=('NO Regular')
            
    linea_nueva = f" {estaescritoprog} {estaescritoadm} \n"
    
    with open("notas_alumno.txt", "r+") as archivo:
            lineas = archivo.readlines()
            archivo.seek(0)

            for linea in lineas:
                datos = linea.strip().split()
                if datos[0] == dni:
                    linea = linea.strip() + " " + linea_nueva.strip() + "\n"
                archivo.write(linea)
         
crear_documento()

texto="""Ingrese la operación a realizar"

1 Agregar Alumnos
2 Modificar Registro de un alumno
3 Eliminar Registro de un alumno
4 Trabajar con notas
5 Salir del menu
 
"""

opcion=int(input(texto))


while opcion != 5:
    dni = input('Ingrese el DNI de alumno: ')
    if opcion == 1:
        agregar_alumno(dni)
    elif opcion == 2:
        modificar_alumno(dni)
    elif opcion == 3:
        eliminar_alumno(dni)
    elif opcion == 4:
        texto_notas = """Ingrese la operación a realizar"
                    1 Cargar notas por materia
                    2 Modificar notas por materia
                    3 Calcular el promedio de notas por materia
                    4 Verificar situación del alumno
                    5 Salir del menú
                    """
        opcion2 = int(input(texto_notas))
        while opcion2 != 5:
            if opcion2 == 1:
                nota_a_cargar(dni)
            elif opcion2 == 2:
                modificar_notas(dni)
            elif opcion2 == 3:
                calcular_promedio(dni)
            elif opcion2 == 4:
                estado_materia(dni)
            else:
                print('Ingrese una opción correcta')
            opcion2 = int(input(texto_notas))
    else:
        print('Ingrese una opción correcta')
    opcion = int(input(texto))

'''print("Los nuevos valores son: {}".format(alumno))'''


