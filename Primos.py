__author__ = 'aferreiradominguez'
#N?meros primos

def es_primo(num):
    if num < 2:
    #si es menos que 2 no es primo, por lo tanto devolver? Falso
        return False
    for i in range(2, num):
    #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:
        #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True
    #de lo contrario devuelve Verdadero

print es_primo(3)
#para probarlo llamamos a la funci?n



def primos(num1, num2):

    cont = 0

    for i in range(num1, num2):
        if es_primo(i) == True:
        #Llamamos a la primera funcion para ahorrar trabajo ;)
            cont += 1
            #Que va a determinar si es primo o no
                print i

    print ""
    print "Hay", cont, "numeros primos"
    #Total de numeros primos

print primos(487, 8976)