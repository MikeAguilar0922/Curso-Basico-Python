
# Declara Variable
calificacion = input("Introduce tu calificación de la AZ-900: ")

calificacion = int(calificacion)

#Preguntamos calificación
if calificacion < 700 :
    print("Ves, por no estudiar!")
elif calificacion > 1000 :
    print("Mientes! No puedes sacar mas de mil")
else :
    print("Felicidades pasa por tu Cetificado")


edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido")
elif edad > 100 :
    print("Si vienes acompañado de tus abbuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajer@ del tiempo")
else :
    print("No puedes llevarte esos cigarros")
