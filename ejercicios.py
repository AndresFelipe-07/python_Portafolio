def suma(a,b):
     return a+b

def resta(a,b):
     return a-b

def multiplicacion(a,b):
     return a*b

def division(a,b):
     # if b != 0:
     #      print("El resultado de la división es: ",str(division(a,b)))
     # else:
     #      print("ERROR")
     return a/b

def potencia(a):
     return a*a

def potenciaCubo(a):
     return a**a

print("** SUMA **")
i = 0
while True: # como hacer para que sea un bucle indefinido
     try:
          a = int(input("Escribe un número: "))
          b = int(input("Escribe un número: "))
          print("El resultado de la suma es: ",str(suma(a,b)))
     except:
          print("Por favor ingresa un entero.")
     i = i + 1
     break



print("** RESTA **")
i = 0
while True:
     try:
         a = int(input("Escribe un número: "))
         b = int(input("Escribe un número: "))
         print("El resultado de la resta es: ",str(resta(a,b))) 
     except:
          print("Por favor ingresa un entero.")
     i += 1
     break     

print("** MULTIPLICACIÓN **")
i = 0
while True:
     try:
          a = int(input("Escribe un número: "))
          b = int(input("Escribe un número: "))
          print("El resultado de la multiplicación es: ",str(multiplicacion(a,b)))
     except:
          print("Por favor escribe un entero.")
     i += 1
     break

print("** DIVISIÓN **")
i = 0
while True:
     try:
          a = int(input("Escribe un número: "))
          b = int(input("Escribe un número: "))
          a/b
          print("El resultado de la división es: ",str(division(a,b)))
     except ZeroDivisionError as e:
          print("ERROR, ingresa un numero valido diferente de 0",e)
     i += 1
     break
# if b != 0:
#      print("El resultado de la división es: ",str(division(a,b)))
# else:
#      print("ERROR")
# try:
#      a = a/b
#      print("El resultado de la división es: ",str(division(a,b)))
# except ZeroDivisionError as e:
#      print("ERROR",e)


print("** POTENCIA CUADRADA **")
i = 0
while True:
     try:
          a = int(input("Escribe un número: "))
          print("El resultado de la potencia es: ",str(potencia(a)))
     except:
          print("Por favor ingresa un número valido.")
     i += 1
     break

print("** POTENCIA CUBICA **")
i = 0
while True:
     try:
          a = int(input("Escribe un número: "))
          print("El resultado de la potencia cubica es: ",str(potenciaCubo(a)))
     except:
          print("Please type a number.")
     i = i + 1
     break
