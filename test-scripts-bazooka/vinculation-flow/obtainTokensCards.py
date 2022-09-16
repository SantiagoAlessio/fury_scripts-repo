import requests
import csv
import sys
import data

preDataIndex = 0
tokens = []
total_request = int(sys.argv[1])

print('se comienza con los request')

#el primero argumento que se recibe es la cantidad de tokens que se quiera
for x in range(total_request):
	#busco la public key del appid
	public_key = data.app_publickey[data.preData[preDataIndex][0]]

	#hago el request y parseo el json
	response = requests.post(data.url + public_key, json=data.body).json()

	#genero una linea del csv y verifico de apuntar el indice correctamente
	tokens.append([response["id"]] + data.preData[preDataIndex])

	print(f'obtenido {x + 1} de {total_request} tokens', end='\r')
	if(preDataIndex < len(data.preData) - 1):
		preDataIndex += 1
	else:
		preDataIndex = 0

print('request finalizados, escribiendo en archivo')

with open("sellerwithcard.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(tokens)

print('proceso finalizado')