# CLASES Y OBJETOS

# CREANDO LA CLASE

class Alumno:
    def init (self, nombre):
        self.nombre = nombre

#CREANDO EL OBJETO

alumnoEmir = Alumno("Emir")
alumnoRoxel = Alumno("Roxel")
alumnoVictor = Alumno("Victor")

print(alumnoEmir.nombre)
print(alumnoRoxel.nombre)
print(alumnoVictor.nombre)

#ENTRADA DE DATOS

print("INGRESA TU NOMBRE")
nombre = input()
print(type(nombre))
palabras = nombre.split("")
nombre = nombre.capitalize()
nombre = nombre.replace(" ", "-")

for palabra in palabras:
    print(palabra.capitalize())
print("HOLA: " + nombre)

print("Ingresa nombre:")
nombre = input()
palabras = nombre.split(" ")
nombreCapitalizado= ""
for palabra in palabras:
    nombreCapitalizado += palabra.capitalize() + " "
print(nombreCapitalizado)