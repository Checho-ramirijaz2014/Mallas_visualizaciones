import json
import os
print(os.getcwd())
with open("datos_mallas/ciencia_datos.json", "rt", encoding="utf-8") as file:
    diccionario = json.load(file)
    print(diccionario)