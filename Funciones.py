#FUNCIONES
x = 1

#FUNCIONES CON PARAMETROS FINITOS Y KEYWORDS
def saludar(nombre, edad):
    print("Hola" + nombre + "EDAD:" + str(edad))

saludar("KAREN", 22)
saludar("LUIZ",20)
saludar("VICTOR",20)

# FUNCIONES CON N PARAMETROS
def asistencia(*alumnos):
    for alumno in alumnos:
        print("ASISTIO: " + alumno)

asistencia("LAURA", "ANGEL","OCTAVIO","EMIR")
asistencia("AXEL", "ROLEX")
asistencia("CJ")


