# introduzca un tiempo X en segundos 
# tiempo en realizarse una tarea Z en segundos minutos y horas
# con el tiempo X se puede realizar la tarea Z


tiempo_X = int(input("Escriba la cantidad de tiempo X en segundos: "))
tiempo_Z = int(input("Escriba la cantidad de tiempo Z en segundos: ")) 
if tiempo_X>=tiempo_Z:
    print ("tiempo_Z en min") 
    print (tiempo_Z / 60 ) 
    print ("tiempo_Z en hrs")
    print (tiempo_Z / 3600 ) 
    print ("el tiempo si alcanza para realizar la tarea Z: ")
else:
    print ("el tiempo de X no alcanza para realizar la tarea Z: ")
    
print ("fin del programa: ")