# algoritmo de lunth el cual te dice cual es el ultimo numero verificador que debe tener tu cedula para que sea valida. para eso toma
# los primeros 10 digitos de tu id y realiza una operacion para determinar cual debe de ser tu ultimo digito valido


# bucle para realizar la operacion que dara la verificacion de la cedula
def validador_cedula(cedula):
        try:
            while True:

                cedula.reverse()
                num_verificador = cedula.pop(0)
                for i in range(len(cedula)):
                    # se verifica que la posicion de la i
                    if i % 2 == 0:
                        x = cedula[i] * 2  # se realiza una multiplicacion * 2 al numero que se encuentre en la posicion [i] de la cedula
                    # Condicion para saber si el resultado de la operacion de arriba tiene una longitud de dos digitos para asi restarle 9
                    # que seria lo mismo si se  sumara ambos digitos de la longitud dada ejemplo: 18 (1+8) = 9: 18-9 = 9
                    if len(str(x)) == 2:
                        x -= 9
                    else:
                        cedula[i] = x  # en caso de que no se cumpla la condicion de arriba simplemente se almacena la operacion en la variable con posicion [i]
                total = sum(cedula) * 9
                total %= 10  # el resulado al dividir el total de la suma de cada numero de la cedula *9 entre 10 se utilizara para verificas el ultimo numero de la cedula
                # para saber si es el mismo numero
                if total == num_verificador:
                    print('cedula valida')
                    return
                else:
                    print('cedula invalida')
                    return ()
        except ValueError:
            print('no se acepta caracteres especiales, intetelo de nuevo')
