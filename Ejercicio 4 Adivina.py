from random import randint #funcion a usar

def verificador(): #para asegurarse de que se ingresan numeros,  si no se hace, el bucle no terminara porque no retornara nada
    while(True):
        a = input("Ingrese un numero \n")
        if a.isnumeric(): #verificador
            return int(a)
        else:
            print("Se ingreso un caracter invalido \n")


inf = verificador() #ingreso de los limites inf y sup
sup = verificador()
if inf > sup: #Si se ingreso en el orden incorrecto se arreglara
    aux = inf
    inf = sup
    sup = aux    

numero = randint(inf,sup) #el numero aleatorio con semilla del reloj de la computadora
cont = 0 #contador
print("Adivine el numero ---- ")
while ( True ):
    guess = verificador()
    cont += 1
    if guess < numero:
        print ("Lo siento, ¡inténtalo de nuevo! Muy bajo. ") #Pista 1
    elif guess > numero:
        print ( "Lo siento, ¡inténtalo de nuevo! Muy alto. ") #Pista 2
    else:
        break #Cuando se adivina se felicita y se menciona cuantos intentos tomo
print('¡Felicidades! Lo has adivinado ')
print("Te tomo ", cont, " intentos.")            


