#clave:valor
midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario["Francia"])

#Agregar elementos
midiccionario["Italia"]="Lisboa"
print(midiccionario)

#Redefinir valor nuevo a una clave
midiccionario["Italia"]="Roma"
print(midiccionario)

#Eliminar un elemento
del midiccionario["Reino Unido"]
print (midiccionario)

#
midiccionario={"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}
print(midiccionario)

#Crear diccionario a partir de lista
milista=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario={milista[0]:"Madrid", milista[1]:"París", milista[2]:"Londres", milista[3]:"Berlín"}
print(midiccionario)

#
print(midiccionario["Francia"])

#
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(midiccionario)
print(midiccionario["anillos"])
print(midiccionario["Equipo"])

#Guardar un diccionario dentro de un diccionario
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(midiccionario["anillos"])

#Imprimir solo las claves del diccionario
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(midiccionario.keys())

#Imprimir solo valores
print(midiccionario.values())

#Longitud del diccionario
print(len(midiccionario))