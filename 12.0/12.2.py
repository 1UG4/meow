import requests

paikkakunta = input("Anna paikkakunnan nimi: ")
api_key = "f2f60c0cdc20355629f116e23be67e20"

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric"
vastaus = requests.get(pyynto).json()

for saa in vastaus["weather"]:
    print(f"Sää: {saa['description']}")

print(f"Lämpötila: {vastaus['main']['temp']} °C")