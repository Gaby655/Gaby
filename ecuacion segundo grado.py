import math 


print ("teniendo la ecuacion ax^2+bx+c: ")
print ("---------------------------------------------------")
a = int(input("introduce el valor de a: "))
b = int(input("introduce el valor de b: "))
c = int(input("introduce el valor de c: "))
# calculamos el discriminante
d =  (b*b)-4*a*c
# comprobamos y calculamos
if d>=0: 
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print ("----soluciones----: ")
    print ("solucion x1: ", x1)
    print ("solucion x2: ", x2)    
else:
    print ("No existen soluciones reales!!: ")
print ("Fin del programa: ")

