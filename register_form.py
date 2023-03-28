# 1. Escribir un programa que le pida a usuario los datos de una persona (nombre, apellido, cédula, correo)
# , el programa se debe mantener pidiéndole al usuario si quiere ingresar otra persona, hasta que el usuario decida salir.

# 2. Esas personas se deben guardar en un archivo de texto.
# 3. Escribir una función que reciba como parámetro la cédula de una persona y devuelva true si la cédula es valida y
# false si la cédula es invalida.Si es invalida se debe pedir la cédula nuevamente al usuario hasta
# que ingrese una cédula correcta.
# 4. Validar que el formato de correo sea un formato valido.
from Proyecto_Final.cedula_validador_proyectoFinal import validador_cedula
import re
id = 0
lista_persona = {}

while True:
    menu = {1: 'Registrar Persona', 2: 'Salir'}
    print(menu, '\n')
    try:
        opcion = int(input('Ingrese la opcion a escoger: '))
        verificar_opcion = list(menu.keys())
        if verificar_opcion[opcion - 1] == 1:
            nombre = input('Ingrese el nombre: ')
            apellido = input('Ingrese el apellido: ')
            while True:
                try:
                    cedula = list(map(int, (input('ingrese su Cedula: '))))
                    cedula_persona = tuple ((cedula)) # Esta variablee guardara la cedula intacta gracias a las tuplas ya que no cambian su valor
                                                    # guardar la cedula en el archivo .txt con essta variable
                    if len(cedula)==11:
                        validador_cedula(cedula)
                        #print(cedula_persona) para verificar que se este guardando la cedula si los calculos de la funcion
                        cedula_guardar = str(cedula_persona)  # write() argument must be str, not tuple
                        break
                    else:
                        print('cedula no cumple con la cantidad de digitos establecidas ')

                except ValueError:
                    print('no se acepta caracteres especiales, intetelo de nuevo')
            correo = input('Ingrese el correo: \n')
            validar_email= re.search(r'^[a-zA-Z0-9\W\-_]+\@\w+\.\w+',correo)
            while validar_email is None:
                correo = input('correo invalido, Ingrese de nuevo: \n')
                validar_email = re.search(r'^[a-zA-Z0-9\W\-_]+\@\w+\.\w+', correo)

        elif verificar_opcion[opcion - 1] == 2:
            break
    except ValueError:
        print('la opcion ingresada no es valida')
    except IndexError:
        print('La opcion a escoger no esta dentro del menu')
    id +=1
    lista_persona [(id)] = nombre,apellido,cedula_guardar,correo

    file = open('Registro_Personas.txt', 'a')
    file.writelines(str(lista_persona.get(id)))
    file.write('\n')
    file.close()
