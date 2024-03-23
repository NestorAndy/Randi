# Crear un diccionario con información personal
informacion_personal = {
    "Nombre": "Nestor",
    "Edad": 23,
    "Ciudad": "Archidona",
    "Profesion": "Ingeniero"
}

# Modificar el valor asociado con la clave "ciudad"
informacion_personal["Ciudad"] = "Archidona"

# Agregar una nueva clave-valor para la profesión
informacion_personal["Profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0988641946"

# Eliminar la clave "edad"
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)