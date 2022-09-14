import requests
import csv
import sys

url = "https://api.mercadopago.com/v1/card_tokens?public_key=APP_USR-e19a1836-a6ba-4cd7-97a6-2788e867578c"
body = {
	"card_number":"5031755734530604",
	"security_code": "123",
	"expiration_month":11,
	"expiration_year":2025,
	"site_id":"MLA",
	"cardholder": {
		"name":"apro",
		"identification": {
			"type":"DNI",
			"number":"11111111"
		}
	}
}
preData = [
    [5835176281570049,'https://www.mercadolibre.com.ar/',1167488254,783789745],
    [5835176281570049,'https://www.mercadolibre.com.ar/',1127473501,783789745],
    [5835176281570049,'https://www.mercadolibre.com.ar/',1168403283,783789745]]
preDataPointer = 0
tokens = []

print('se comienza con los request')

#el primero argumento que se recibe es la cantidad de tokens que se quiera
for x in range(int(sys.argv[1]) + 1):
    response = requests.post(url, json=body).json()
    if(preDataPointer < len(preData)):
        tokens.append([response["id"]] + preData[preDataPointer])
        preDataPointer += 1
    else:
        preDataPointer = 0

print('request finalizados, escribiendo en archivo')

with open("sellerwithcard.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(tokens)

print('proceso finalizado')