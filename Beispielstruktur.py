person = {
    "haustier": True,
    "mag_stadt": False,
    "arbeitet_online": True
}


# ort 1 = Lüdenscheid zum Beispiel
ort1 = {
    "name": "Luedenscheid",
    "parks": 10,
    "internet": "mittel",
    "tierärzte": 3,
    "einwohner": 500
}


# Score errechnen : Passt = 10, okay = 5 und gar nicht = 0 zum Beispiel
score = 0
if person["haustier"]:
    score += ort1["parks"] * 2
    score += ort1["tierärzte"] * 1.5

if person["arbeitet_online"] and ort1["internet"] == "mittel":
    score += 10

if not person["mag_stadt"] and ort1["einwohner"] < 10000:
    score += 5

###################
