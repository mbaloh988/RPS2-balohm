import requests
import math

def trenutna_temperatura(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    podatki = odgovor.json()
    return podatki["current"]["temperature_2m"]

def vse_temperature(kraji):
    lat = []
    lon = []
    
    for ime, (l1, l2) in kraji.items():
        lat.append(l1)
        lon.append(l2)
    
    url = "https://api.open-meteo.com/v1/forecast"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    print(odgovor.url)
    podatki = odgovor.json()
    # return podatki["current"]["temperature_2m"]
    return podatki


def vrniKraj(vsi, iskana_koordinata: tuple[float,float]):
    najblizji_kraj = min(
        kraji.keys(),
        key=lambda k: math.dist(kraji[k], iskana_koordinata)
    )

    return najblizji_kraj

def najdi_na_spletu(lat: float, lon: float) -> str:
    url = "https://nominatim.openstreetmap.org/reverse"
    
    headers = {
        # Nominatim zahteva smiseln User-Agent z vašim kontaktom/imenom aplikacije
        "User-Agent": "MojaPythonAplikacija/1.0 (kontakt@primer.com)"
    }
    
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json",
        "zoom": 10  # 10 = Mesto/Kraj, 18 = Točen naslov z hišno številko
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        address = data.get("address", {})
        
        # Poišče mesto, naselje ali vas v odgovoru
        kraj = address.get("city") or address.get("town") or address.get("village") or address.get("municipality")
        return kraj or "Kraj ni najden"
    
    return "Napaka pri povezavi"

def main2():
    ime = najdi_na_spletu(46.0569, 14.5058)
    print(ime)

def main1():
    # Primer uporabe:
    print(poisci_najblizji_kraj(46.0569, 14.5058))  # Izpis: Ljubljana
     
    kraji = {
        "Ljubljana":  (46.0569, 14.5058),
        "Maribor":    (46.5547, 15.6459),
        "Kranj":      (46.2389, 14.3556),
        "Celje":      (46.2361, 15.2675),
        "Koper":      (45.5481, 13.7302),
        "Velenje":    (46.3592, 15.1103),
        "Novo mesto": (45.8040, 15.1689),
        "Ptuj":       (46.4200, 15.8700),
        "Trbovlje":   (46.1550, 15.0533),
        "Kamnik":     (46.2259, 14.6121),
        "Plava Laguna Umag": (45.445183, 13.513998),
    }

    print(kraji.items())

    temperature = {}
    vse = vse_temperature(kraji)
    # print(vse)

    for kraj in vse:
        koordinata = (kraj["latitude"],kraj["longitude"])
        ime = vrniKraj(kraji, koordinata)
        t = kraj["current"]["temperature_2m"]
        print(f"{ime}: {t} °C")
        temperature[ime] = t # f"{t} °C"

    print(temperature)
    najtoplejse = ""
    najvisja = 0
    vsota = 0
    for mesto, t in temperature.items():
        if t > najvisja:
            najvisja = t
            najtoplejse = mesto
        vsota = vsota + t

    print(f"Najtoplejše: {najtoplejse} ({najvisja} °C)")
    povprecje = vsota / len(temperature)
    print(f"Povprečje: {round(povprecje, 1)} °C")


if __name__ == "__main__":
    main2()