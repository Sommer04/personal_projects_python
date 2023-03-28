#1. Escribir un programa que pida al usuario n entradas. El usuario deberá introducir
# el nombre de n asignaturas y su respectiva calificación.  Almacenar esto en un diccionario y luego mostrar
# cuál fue la asignatura donde obtuvo mayor calificación.

#Ejemplo: {"python": 90, "C#": 84, "Java": 85}
#Salida del programa: La asignatura con mayor calificación fue Python: 90 puntos.

cantidad_materia = int(input('introduzca la cantidad de materias que desea guardar: '))
materia = {}
for i  in range(0,cantidad_materia) :
    asignatura = input('introduzca la asignatura: ')
    calificacion = int(input('introduzca la calificacion: '))
    materia[asignatura] = calificacion


print('Sus asignaturas son: ', materia,'\n')

max_calificacion = list(materia.values())
max_asignatura = list(materia.keys())
#if materia.values() > materia.values():
#print('su asignatura con mayor calificacion fue: ',max_asignatura[max_calificacion.index(max(max_calificacion))])
print('su asignatura con mayor calificacion fue: ',max_asignatura[max_calificacion.index(max(max_calificacion))],'=',max(max_calificacion))
