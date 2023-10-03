#ENTRADA DE DATOS
"""
print("INGRESA TU NOMBRE:")
nombre = input()
print(type(nombre))
palabras = nombre.split(" ")
nombre = nombre.capitalize()
nombre = nombre.replace(" ", " ")
for palabra in palabras:
    print(palabra.capitalize())
print("HOLA:" + nombre)
"""
print("Ingresa nombre:")
nombre = input()
palabras = nombre.split(" ")
nombrecapitalizado = ""
for palabra in palabras:
    nombrecapitalizado += palabra.capitalize() + " "
print(nombrecapitalizado)



