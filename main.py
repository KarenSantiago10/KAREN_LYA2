#Mi primer programa
print("Hola Tec Mina")

#Variables
x=4
nombreMessi="MESSI"
nombreCristiano="CRISTIANO"
z=float(3)
y= int (3.2)
k= int ("10")
print(z)
print(y)
print(k)
print(type(z))
print(type(y))
print(type(k))


#condiciones
if x ==7:
    print(nombreCristiano)
elif x== 10:
    print(nombreMessi)
elif x==4:
    print("Rafa Marquez")
else:
    print("No existe")
# Strings
nombre= "LIZBETH"
print(nombre[0])

for letra in nombre:
    print(letra)


print(len(nombre))



# COMPROBAR SI EXISTE
texto=("alla en la fuente habia un chorrito")
print("chorrito" in texto)
if "chorrito" in texto:
    print("CHORRITO")


# DEL SIGUIENTE TEXTO
"""
'SON LAS 7 DE LA NOCHE Y YA ME QUIERO IR'
SI ENCUENTRA EL NUMERO 7 Y ES MENOR A 8
IMPRIMIR EL NUMERO 7 CONVERTIDO A INT 
Y EL TEXTO, 'ES HORA DE IRNOS SON LAS:'7'
"""
texto=("SON LAS 7 DE LA NOCHE Y YA ME QUIERO IR")
print("7" in texto)
if"7" in texto:
    print("ES HORA DE IRNOS SON LAS: 7")

b = "Hola Mundo"
#Slice por rango
print(b[5:10])
#Slice desde el inicio
print(b[:5])
#Slice desde una posicion hasta el final
print(b[5:])
#Slice con posiciones negativas
print(b[-5:-2])

#Boleanos

#Mayor que
print(10>9)
#Igual que
print(10==9)
#Menor que
print(10<9)
#Variables boleanas
enStock = True
isTiendaAbierta = True

if enStock and isTiendaAbierta:
    print("VENDER PRODUCTOS")

tieneEfectivo = False
tieneTarjeta = True
if tieneTarjeta or tieneEfectivo:
    print("PAGO ACEPTADO")

regresasteConEx= False
if not regresasteConEx:
    print("MENTIROSO!")

tienesNovie = False
if not tienesNovie:
    print("FALSO")

paseLenguajes = True
if not paseLenguajes:
    print("REPROBASTE")

isUploaded = False
if not isUploaded:
    print("REINTENTAR")

#OPERADORES ARITMETICOS

x=5
y=6

#SUMA
print(x + y)

#RESTA
print(x - y)

#MULTIPLICACION
print(x * y)

#DIVISION
print(x / y)

#MODULO
print(x % y)

#EXPONENTES
print(2 ** 2)
print(x ** 2)
print(x ** y)

#FLOOR DIVISION
print(4 // 2)
print(x // y)

#OPERADORES DE ASIGNACION
x=30
x +=32
x -=2
x *=2
x /=2
print(x)

#OPERADORES LOGICOS DE COMPARACION
a = 3
b = 2

#IGUAL
print(a == b)
#DIFERENTE
print(a != b)
#MAYOR
print(a > b)
#MENOR
print(a < b)
#MAYOR IGUAL
print(a >= b)
#MENOR IGUAL
print(a <= b)

#OPERADORES LOGICOS
promedio= 100
asistencias= True
aprobado = (promedio > 70) and asistencias
#and,or,not
print(aprobado)

#OPERADORES DE IDENTIDAD
j= "HOLA"
k = "HOLA"
print(j is k.replace(" ", ""))
print(j is not k)

#OPERADORES DE PERTENENCIA
print("A" in "HOLA")
print("A" not in "HOLA")

#LISTAS
frutas = ["Manzana","Banana","Mango"]
frutas2 =["🍎","🍌","🥭"]
print(frutas)
print(frutas2)
lista =[1, 2, 3, 4, 5, 6]
logico=[True, False, True]
lista1=["abc", 34, True, 'a', "🍑"]
print(type(lista))
print(lista1)

#LIST,TUPLE,SET,DICTIONARY
"""
List: es una colección la cual esta ordenada 
y mutable, la cual permite duplicados.
"""


"""
Tuple: Es una colección la cual es ordenada y 
no es modificable.Permite duplicados

Set: Es una colección la cual NO❌ esta ordenada y 
no es modificable ni indexada. NO❌ permite Duplicado.

Dictionary: Es una colección la cual esta ordenada 
es modificable. No permite duplicados.
"""
#LISTA
lista1 = ["🐕","🐒","🐷"]
lista1[1]="🐼"
lista1.insert(3,"🐮")
print(lista1)
#TUPLA
tupla1 = ("🐕","🐒","🐷")
print(tupla1)
#SET
set1 = {"🐕","🐒","🐷"}
set1.add("🐣")
set1.add("🦄")
set1.add("🐷")
print(set1)
#DICCIONARIO
diccionario1 = {
"perro": "🐕",
"monito": "🐒",
"cerdito": "🐷"
}
diccionario1["koala"] = "🐨"
diccionario1["mamut"] = "🦣"
print(diccionario1["monito"])
print(diccionario1)

"""
#0 CREAR UNA LISTA:1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
#1. CONVERTIR LA LISTA EN UN SET PARA ELEMINAR DUPLICADOS 
#2. CALCULAR LA SUMA DE LOS NUMEROS USANDO LISTA
#3. CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
#4. CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS 
NUMEROS UNICOS, SUMA TOTAL LISTA, SUMA TOTAL SET
MAXIMO VALOR, MINIMO VALOR
#5. IMPRIMIR LAS ESTADISTICAS
"""
numeros = [1, 2, 2, 3, 4, 4]
numerosSet = set(numeros)
sumaLista = sum(numeros)
sumaSet= sum(numerosSet)
len(numerosSet)
max(numeros)
min(numeros)

lista=[1,2,5,3,2,3,3,6,10,8,9]

listaSet= set(lista)

sumaLista = sum(lista)

sumaSet = sum(listaSet)


diccionario2 ={
    "NUMEROSUNICOS" : len(numerosSet),
    "SUMATOTAL" : sumaLista,
    "SUMASET" : sumaSet,
    "VALORMAX" : max(lista),
    "VALORMINIMO" : min(lista)
}
print(diccionario2)

#CONDICIONES
a = 200
b = 33
if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b ")


# CICLO WHILE-MIENTRAS

vecesRegresaron = 0
while vecesRegresaron < 3:
    vecesRegresaron += 1
    print("Han Vuelto" + str(vecesRegresaron) + "Veces")

#BREAK
i = 8
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("error")

# CONTINUE
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#CICLO FOR- FOR EACH
frutas =["🍎","🍌","🥭"]

#FOR- POR CADA
buscar = True
if buscar:
    for fruta in frutas:
        if fruta == "🍌":
            print("Se encontro: " + fruta)
        else:
            print("NO COINCIDE")
else:
    print(" NO SE ESTA BUSCANDO")





